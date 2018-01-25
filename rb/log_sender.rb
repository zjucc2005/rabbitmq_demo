# encoding: utf-8
require 'bunny'

# 从shell command获取参数
log_level = ARGV[0]
message = ARGV[1, ARGV.length-1].join(' ')
message = "[#{log_level}] #{message}"
print " [Send]#{message}\n"

# 建立connection
# 默认参数
# connection = Bunny.new(host: 'localhost', port: 5672, vhost: '/',username: 'guest', password: 'guest')
connection = Bunny.new
connection.start

# 新建channel
channel = connection.create_channel

# 新建exchange, 类型topic
exchange = channel.topic('logger', :auto_delete => true)

# 设定routing_key并把message发送到queue 
# exchange为topic类型时, 不用设定queue名称, queue名称随机生成, 并bind到设定的routing_key
if %w(warning error).include?(log_level)
  exchange.publish(message, :routing_key => "logger.#{log_level}")
else
  exchange.publish(message, :routing_key => 'logger.#')
end

# 关闭connection
connection.close
