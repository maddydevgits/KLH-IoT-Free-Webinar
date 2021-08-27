# Subscriber - client
import paho.mqtt.client as mqtt
import serial

# create a client object
client=mqtt.Client()

# create a serial object
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

# connect with broker
client.connect('broker.hivemq.com',1883)
print ('Broker Connected')

# subscriber
client.subscribe('klh/iot')

# create a notification service
def notification(client,userdata,msg):
 t=msg.payload.decode('utf-8') # bytes to string
 if(t=="on" or t=="ON"):
  print('Device On')
  ser.write('on'.encode('utf-8')) # string to bytes
 elif(t=="off" or t=="OFF"):
  print('Device Off')
  ser.write('off'.encode('utf-8'))
 

# configure this notification service
client.on_message=notification

# run this program forever
client.loop_forever()
