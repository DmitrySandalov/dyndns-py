#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
from sh import ifconfig, hostname
import ConfigParser

config = ConfigParser.RawConfigParser()
config_folder = os.path.dirname(os.path.realpath(__file__))
config.read(config_folder + '/config.cfg')
server = config.get('conf', 'server')
password = config.get('conf', 'password')

hostname = str(hostname())[:-1]
ip = str(ifconfig().split("\n")[1].split()[1][5:])

response = urllib2.urlopen(
    server + "/update?host=%s&ip=%s&password=%s" %
    (hostname, ip, password))

print response.read()
