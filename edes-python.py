import configparser
import zmq
import zlib

from datetime import datetime
from elasticsearch import Elasticsearch

Config = configparser.ConfigParser()
Config.read("./edes-python.ini")
username = Config.get('Main', 'elastic.user')
password = Config.get('Main', 'elastic.pass')
hostname = Config.get('Main', 'elastic.host')
debug = Config.get('Main', 'debug')
__relayEDDN   = 'tcp://eddn.edcd.io:9500'
__timeoutEDDN = 600000

es = Elasticsearch(
	[hostname], 
	sniff_on_start=True,
	http_auth=(username,password)
)

context = zmq.Context()
sock = context.socket(zmq.SUB)
sock.setsockopt(zmq.SUBSCRIBE, b"")
sock.setsockopt(zmq.RCVTIMEO, __timeoutEDDN)
sock.connect(__relayEDDN)

while True:
    message= sock.recv()
    uncompressed = zlib.decompress(message)
    uncompressed = uncompressed.decode("utf-8")
    if debug == '1':
        print (str(uncompressed))
    
    es.index(index='edes-python', body=
    	uncompressed
    	)
