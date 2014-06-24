#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import sqlite3

application = bottle.default_app()
db = sqlite3.connect(':memory:')


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

    cursor = db.cursor()
    count = cursor.execute(
        'SELECT COUNT(*) FROM data WHERE host=?',
        (hostname,))
    count = count.fetchone()[0]

    if count == 0:
        cursor.execute(
            'INSERT INTO data (ip, host, passw) VALUES (?, ?, ?)',
            (ip, hostname, password))
    else:
        cursor.execute(
            'UPDATE data SET ip=? WHERE host=? AND passw=?',
            (ip, hostname, password))

    return 'update ok, ip=%s, hostname=%s' % (ip, hostname)


@bottle.route('/get')
def get_page():
    hostname = bottle.request.query.host or 'null'
    password = bottle.request.query.password or 'null'

    cursor = db.cursor()
    cursor.execute("SELECT * from data WHERE host=? AND passw=?",
                   (hostname, password))

    output = ''
    for row in cursor:
        output += str(row) + "\n"

    return 'Not found' if len(output) == 0 else output


def init_db():
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data (ip CHAR(15) NOT NULL, \
                   host CHAR(50) NOT NULL, passw CHAR(50) NOT NULL); ')


init_db()

# # debug
# def server():
#     """Starts bottle web framework"""
#     bottle.debug(True)
#     bottle.run(host='0.0.0.0', port=8082)
#
# server()
