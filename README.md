uwsgicachetop
=============

A top like tool which shows statistics about uwsgi caches.
Inspired by uwsgitop (https://github.com/unbit/uwsgitop).

Run your uWSGI server with the stats server enabled, Ex.:

uwsgi --module myapp --socket :3030 --stats /tmp/stats.socket

Then connect uwsgitop to the stats socket

uwsgitop /tmp/stats.socket

To quit, press 'q'.

more info on http://projects.unbit.it/uwsgi/wiki/StatsServer