import sys
from time import sleep  
import Adafruit_DHT as dht
import urllib2

dhtPin = 4
delay = 15
writeKey = ''
writeUrl = 'https://api.thingspeak.com/update?api_key=%s' % writeKey

def getData():
    humidity, temperature = dht.read_retry(dht.DHT11, dhtPin)
    return humidity, temperature
    #return (str(humidity), str(temperature))
    #testing
while True:
    try:
        humidity, temperature = getData()
        
        if isinstance(humidity, float) and isinstance(temperature, float):

            conn = urllib2.urlopen(writeUrl + "&temperature=%s&humidity=%s" % (temperature, humidity))

            print(conn.read())
            print("Temperature: "+temperature)
            print("Humidity: "+humidity)
            conn.close()

            sleep(int(delay))
        
        else:
            print("Invalid data format on the return")
            
    except:
        print("Shuting down")
        break
