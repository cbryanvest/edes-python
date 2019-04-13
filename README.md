# Elite Dangerous EDDN Data to Elasticsearch Client

This is a simple client that subscribes to the EDDN data feed and indexes this data into an Elasticsearch cluster. EDDN uses ZeroMQ to push data from the game Elite Dangerous to subscribers. This client takes that data in its raw form and indexes it into an Elasticsearch cluster for research.

## Getting Started

This is a simple python3 script. There are only a few requirements outside of the stock libraries that come with python3. 

### Prerequisites

```
Python3
pyzmq
elasticsearch
ConfigParser
```

### Installing

Download, copy or clone the code. Don't forget the ini file, this is needed to tell the script which elasticsearch cluster to connect to.

```
Downlaod code
pip install pyzmq
pip install elasticsearch
pip install ConfigParser
```

Edit the ini file with your host information. If you do not have an elasticsearch host see the section below entitied Running Local. If your host does not require authentication leave the username and password settings as they are.

Start the client. 


This should create a new index on your Elasticsearch cluster called edes-python.

If you have your own cluster you can go to Management -> Index Patterns and create the new index pattern for edes-python now and start browsing the data.


If you do not have a cluster follow to the next section for building a local cluster from the Elasticsearch binary packages.

### Running Local
 To setup a local elasticsearch instance or a larger cluster to work with this data you should always follow the current documentation here [https://www.elastic.co/downloads/elasticsearch](https://www.elastic.co/downloads/elasticsearch) for Elasticsearch and here [https://www.elastic.co/downloads/kibana](https://www.elastic.co/downloads/kibana) for Kibana.
 
 No setup is required to run this in basic mode on any machine. It is simply download the two pieces of software and run them. The default settings will setup a 1 node elastic cluster and Kibana to view the data in the cluster. The python client by default will connect to localhost so to get going fast no real setup is required besides the requred python libraries and following the documentation for installing elasticsearch and kibana.
 
 I tested all of these components together on a 2018 Macbook Pro without problems. If you let it run for a long time and the data set gets large you will start to see lag but for small tests a laptop works fine. Large in this case being millions of documents. This feed provides about 1,000 documents per minute average but can peak to 5k+ documents per minute when new patches for the game come out or there are big events going on.
 
 
### EDDN Data

The EEDN data stream is provided by players of the game who decided to install clients on their computers that read data from the commander log file generated by the game. The clients all feed into the same data center at EDDN who then graciously provides the data for research using a ZeroMQ message broker.

The data by default is in JSON format and resembles this


```
{
      "Atmosphere": "",
      "AtmosphereType": "None",
      "AxialTilt": 2.398546,
      "BodyID": 49,
      "BodyName": "Pru Aub TY-H c23-7 7 d",
      "Composition": {
        "Ice": 0,
        "Metal": 0.090722,
        "Rock": 0.909278
      },
      "DistanceFromArrivalLS": 2950.692383,
      "Eccentricity": 0.16041,
      "Landable": true,
      "MassEM": 0.007369,
      "Materials": [
        {
          "Name": "iron",
          "Percent": 19.709469
        },
        {
          "Name": "sulphur",
          "Percent": 19.355995
        },
        {
          "Name": "carbon",
          "Percent": 16.276388
        },
        {
          "Name": "nickel",
          "Percent": 14.907418
        },
        {
          "Name": "phosphorus",
          "Percent": 10.420423
        },
        {
          "Name": "manganese",
          "Percent": 8.13981
        },
        {
          "Name": "germanium",
          "Percent": 5.682408
        },
        {
          "Name": "zirconium",
          "Percent": 2.288676
        },
        {
          "Name": "tin",
          "Percent": 1.181506
        },
        {
          "Name": "yttrium",
          "Percent": 1.177223
        },
        {
          "Name": "mercury",
          "Percent": 0.86068
        }
      ],
      "OrbitalInclination": -0.361544,
      "OrbitalPeriod": 85866.804688,
      "Parents": [
        {
          "Null": 48
        },
        {
          "Planet": 42
        },
        {
          "Null": 41
        },
        {
          "Star": 0
        }
      ],
      "Periapsis": 222.695053,
      "PlanetClass": "Rocky body",
      "Radius": 1359745,
      "RotationPeriod": -132086.71875,
      "ScanType": "Detailed",
      "SemiMajorAxis": 4154460,
      "StarPos": [
        -410.5625,
        6.28125,
        42180.3125
      ],
      "StarSystem": "Pru Aub TY-H c23-7",
      "SurfaceGravity": 1.58857,
      "SurfacePressure": 0,
      "SurfaceTemperature": 132.884903,
      "SystemAddress": 2007326798794,
      "TerraformState": "",
      "TidalLock": false,
      "Volcanism": "minor silicate vapour geysers volcanism",
      "event": "Scan",
      "timestamp": "2019-04-12T02:54:58Z"
    }
  }
```

There are a few different data sets that come from thie EDDN data. Baically these are identified by the event key, since this is a raw zmq inserter it tags everything going to elastic with message so what we would see in Elastic is message.event. 

One interesting thing about the EDDN data is that planet exporation data seen as Scan and FSSDiscovery are astronomical bodies created by the Elite Dangerous Stellar Forge. The systems are generated based on real phycics and can create some really interesting and unique solar systems.

According to Frontier Development < 1% of the galaxy has been explored. There is much analysis that could be done with this data to see how the virtual world is growing compared to what we know about our own galaxy.

Another interesting aspect of game data is commodity trading in the virtual world. Also the political state of the systems which are computer controlled but affected by player actions.

There is much data here to do a lot of analysius on. This data is real and ever changing especially as more players head out to explore the whole galaxy in their ships.

Install you cluster, get the script and start exploring this sweet stream of data as world after world are explored and generated.

