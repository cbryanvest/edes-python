import configparser
import zmq
import zlib

from datetime import datetime
from elasticsearch import Elasticsearch

Config = configparser.ConfigParser()
Config.read("./edes-python.ini")

#print (Config.sections())

username = Config.get('Main', 'elastic.user')
password = Config.get('Main', 'elastic.pass')
hostname = Config.get('Main', 'elastic.host')

es = Elasticsearch(
	[hostname], 
	sniff_on_start=True,
	http_auth=(username,password)
)

__relayEDDN   = 'tcp://eddn.edcd.io:9500'
__timeoutEDDN = 600000
# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)


sock.setsockopt(zmq.SUBSCRIBE, b"")
sock.setsockopt(zmq.RCVTIMEO, __timeoutEDDN)
sock.connect(__relayEDDN)

while True:
    message= sock.recv()
    uncompressed = zlib.decompress(message)
    uncompressed = uncompressed.decode("utf-8")
    #print (str(uncompressed))
    #print ("")
    es.index(index='eddn-python', body=
    	uncompressed
    	)
