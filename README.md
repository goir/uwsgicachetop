uwsgicachetop
=============

A top like tool which shows statistics about uwsgi caches.
Inspired by uwsgitop (https://github.com/unbit/uwsgitop).

Install
-------
checkout the repository and run setup.py or simply use easy_install or pip

    pip install uwsgicachetop

Usage
-----
Run your uWSGI server with the stats server enabled, Ex.:
    
    uwsgi --module myapp --socket :3030 --stats /tmp/stats.socket

Then connect uwsgicachetop to the stats socket
    
    uwsgicachetop /tmp/stats.socket

To quit, press 'q'.

more info about the uwsgi Stats Server on http://projects.unbit.it/uwsgi/wiki/StatsServer
