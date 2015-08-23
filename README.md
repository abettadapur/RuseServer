
#Ruse: A Central Music Server

This software allows collaborative playlist creation and playback. 
With the server running and plugged into a pair of speakers, anyone can choose what should be played next!

##Client Apps
[Windows](https://github.com/abettadapur/RuseClient)
[Android](https://github.com/abettadapur/RuseAndroid)

##Requirements

-   A Google Music All Access account

-   An Android or iOS device

##Features

-   Leverages a Google Music All Access pass to stream any content

-   Allows anyone with a client to search and queue music 

-   Song, Album, and Artist search

-   Google Music Radio Support

-   Rich track metadata

-   Easy to setup and use

##Using Ruse

###Installation


####Linux

You will need Python 2.7 and VLC to run Ruse. You can install them via the command-line on Linux.

Ubuntu/Debian

```bash
apt-get update
apt-get install python python-pip vlc
```

Fedora/RHEL

```bash
yum install python python-pip vlc
```

Once you have Python installed, clone the repository and cd into it

```bash

git clone https://github.com/abettadapur/RuseServer.git
cd RuseServer
```

Install the requirements by running 

```bash
   
pip install -r requirements.txt
```

Copy the example configuration file to a production version. Open in a text editor

```bash
cp ruse/etc/config/config.sample.py ruse/etc/config/config.py
gedit config.py
```

Fill in the information in the config file. If you use Google's two factor authentication, you will need to generate a one time password and use it here

Use the provided tool to get a stream key (More info later)

Once everything is configured, run the server 

```bash
crossbar start
python serve_wamp.py
```

####Windows


