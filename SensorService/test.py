import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("test", hostname="127.0.0.1")
print("%s %s" % (msg.topic, msg.payload))