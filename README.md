httpStatusBot
=============

Python command line application that checks the http status of a website.  Used to smoke test web apps on deploy.

Requirements
---------------
Need to be able to run .py files from the command line.

Use
------
httpStatusBot.py -h

usage: httpStatusBot.py [-h] -u URL [-t TIME]

URL to Ping

optional arguments:

  -h, --help            show this help message and exit
  
  -u URL, --url URL     Enter a full web address to check against goodStatus
                        list
                        
  -t TIME, --time TIME  Enter number of seconds to ping, default is 60
  

Testing
-------
Running test_httpStatusBot.py will run some basic unit tests.
