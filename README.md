dyndns-py
=========

Self-hosted DynDNS (DDNS) service in Python

### About
The script gets local IP from client and stores on server with http get requests

### Install

1. Server

        sudo apt-get install python python-pip
        sudo pip install -r requirements-server.pip
    
        sudo add-apt-repository ppa:nginx/stable
        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C
        sudo apt-get update
        sudo apt-get install nginx
        sudo cp ./server/nginx.conf /etc/nginx/nginx.conf
        sudo cp -R ./server/ /var/www/dyndns-py/
        sudo chown -R www-data:www-data dyndns-py
    
        sudo apt-get install uwsgi
        sudo pip install uwsgi
        sudo mv /usr/bin/uwsgi /usr/bin/uwsgi.old
        sudo ln -s /usr/local/bin/uwsgi /usr/bin/uwsgi
        sudo cp ./server/dyndns-py.ini /etc/uwsgi/apps-available/
        sudo ln -s /etc/uwsgi/apps-available/dyndns-py.ini /etc/uwsgi/apps-enabled/dyndns-py.ini
    
        sudo service uwsgi restart
        sudo service nginx restart


2. Client

        sudo apt-get install python python-pip
        sudo pip install -r requirements-client.pip
    
        vi ./client/config.cfg  # edit server and password fields
    
        crontab -e
        
        @hourly
        python <full-path>/client/client.py


### License
GPL v2

Write me an email if you need other license.
