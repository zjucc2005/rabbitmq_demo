# encoding: utf-8
require 'bunny'

# 建立connection
connection = Bunny.new
connection.start

# 新建channel
channel = connection.create_channel

# 新建exchange, 类型topic
exchange = channel.topic('logger', :auto_delete => true)

# 根据routing_key新建queue
log_level = ARGV[0]
log_level = %w(info warning error).include?(log_level) ? log_level : '#'
queue = channel.queue("", :exclusive => true).bind(exchange, :routing_key => "logger.#{log_level}")

print " [*] Waiting for messages in #{queue.name}. To exit press CTRL+C\n"
# 设定block为true, 则会持续监听直到手动终止
# 默认是自动ack模式, 如果想切换到手动, 添加 :manual_ack => true
queue.subscribe(:block => true) do |delivery_info, metadata, payload|
  print " #{payload}\n"
end


