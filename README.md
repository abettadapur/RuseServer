.. Ruse documentation master file, created by
   sphinx-quickstart on Tue Aug  5 11:33:55 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ruse: A Central Music Server
================================
This software allows collaborative playlist creation and playback. 
With the server running and plugged into a pair of speakers, anyone can queue music to be played

Requirements
-------------
-   A Google Music All Access account

-   An Android or iOS device

Features
-----------
-   Leverages a Google Music All Access pass to stream any content

-   Allows anyone with a client to search and queue music 

-   Song, Album, and Artist search

-   Google Music Radio Support

-   Rich track metadata

-   Easy to setup and use

Using Ruse
-----------

.. toctree::
   :hidden:

   Installation
   Configuration

Installation
+++++++++++++++

**Linux**

You will need Python 2.7 and VLC to run Ruse. You can install them via the command-line on Linux.

Ubuntu/Debian

.. code-block:: none
   
   apt-get update
   apt-get install python python-pip vlc

Fedora/RHEL

.. code-block:: bash
   
   yum install python python-pip vlc

Once you have Python installed, clone the repository and cd into it

.. code-block:: bash

   git clone https://github.com/abettadapur/RuseServer.git
   cd RuseServer

Install the requirements by running 

.. code-block:: bash
   
   pip install -r requirements.txt

Copy the example configuration file to a production version. Open in a text editor

.. code-block:: bash
	
   cp ruse/etc/config/config.sample.py ruse/etc/config/config.py
   gedit config.py

Fill in the information in the config file. If you use Google's two factor authentication, you will need to generate a one time password and use it here

Use the provided tool to get a stream key (More info later)

Once everything is configured, run the server 

.. code-block:: bash

   python serve.py

Windows

Table of Contents
==================

* :ref:`genindex`
* :ref:`search`

