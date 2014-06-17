#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import bottle

application = bottle.default_app()


@bottle.route('/')
def index_page():
    return 'Usage: <br/>\
        http://dyndns-py.server/update?host=HOST&ip=IP&password=PASS <br/>\
        http://dyndns-py.server/get?host=HOST&password=PASS'


@bottle.route('/update')
def update_page():

    hostname = bottle.request.query.host or 'null'
    ip = bottle.request.query.ip or '0.0.0.0'
    password = bottle.request.query.password or 'null'

    server = {'host': hostname, 'ip': ip, 'password': password}

    with open('hosts.csv', 'wb') as f:
        w = csv.DictWriter(f, server.keys())
        w.writeheader()
        w.writerow(server)

    return "update ok, ip=%s, hostname=%s" % (ip, hostname)


@bottle.route('/get')
def get_page():
    hostname = bottle.request.query.host or 'null'
    password = bottle.request.query.password or 'null'

    with open('hosts.csv', 'rb') as f:
        r = csv.DictReader(f, delimiter=',')
        resp = [line for line in r if line['host'] == hostname
                and line['password'] == password]

    return 'Not found' if len(resp) == 0 else resp[0]['ip']

# # debug
# def server():
#     """Starts bottle web framework"""
#     bottle.debug(True)
#     bottle.run(host='0.0.0.0', port=8082)
#
# server()
