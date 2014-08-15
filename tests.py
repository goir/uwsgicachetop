# coding=utf-8
import imp
from mock import MagicMock
import os
import cStringIO

imp.load_source('uwsgicachetop', os.path.abspath(os.path.dirname(__file__) + '/uwsgicachetop'))

from uwsgicachetop import parse_hosts, merge_stats, add_header
import unittest

class TestParseHosts(unittest.TestCase):
    def test_parse_host_str(self):
        expected = {('localhost', 1234), }
        self.assertSetEqual(expected, parse_hosts('localhost:1234'))

    def test_parse_multiple_hosts(self):
        expected = {('localhost', 1234), 'localhost', ('localhost', 4567)}
        self.assertSetEqual(expected, parse_hosts(['localhost:1234', 'localhost', 'localhost:4567']))


class TestLoadStats(unittest.TestCase):
    pass

class TestMergeStats(unittest.TestCase):
    def test_merge(self):
        merge_stats()


class TestAddHeader(unittest.TestCase):
    def test_add_header(self):
        mocked_screen = MagicMock()
        stats = {('localhost', 1717): {u'load': 0, u'uid': 1000, u'workers': [{u'status': u'idle', u'last_spawn': 1408127646, u'respawn_count': 1, u'tx': 0, u'apps': [], u'delta_requests': 0, u'vsz': 0, u'pid': 17118, u'harakiri_count': 0, u'signals': 0, u'signal_queue': 0, u'cores': [{u'in_request': 0, u'vars': [], u'static_requests': 0, u'routed_requests': 0, u'offloaded_requests': 0, u'read_errors': 0, u'write_errors': 0, u'requests': 0, u'id': 0}], u'avg_rt': 0, u'exceptions': 0, u'accepting': 1, u'requests': 0, u'running_time': 0, u'id': 1, u'rss': 0}], u'pid': 17117, u'listen_queue': 0, u'sockets': [{u'can_offload': 0, u'name': u':3031', u'proto': u'uwsgi', u'queue': 0, u'shared': 0, u'max_queue': 100}], u'locks': [{u'user 0': 0}, {u'signal': 0}, {u'filemon': 0}, {u'timer': 0}, {u'rbtimer': 0}, {u'cron': 0}, {u'rpc': 0}, {u'snmp': 0}, {u'cache_mycache': 0}, {u'cache_mycache2': 0}], u'listen_queue_errors': 0, u'version': u'2.0.6', u'signal_queue': 0, u'gid': 1000, u'cwd': u'/home/goir/workspace/unister/ad-delivery-service', u'caches': [{u'hits': 0, u'full': 0, u'blocks': 100, u'name': u'mycache', u'blocksize': 65536, u'max_items': 100, u'last_modified_at': 0, u'hashsize': 65536, u'keysize': 2048, u'items': 0, u'hash': u'djb33x', u'miss': 0}, {u'hits': 0, u'full': 0, u'blocks': 100, u'name': u'mycache2', u'blocksize': 65536, u'max_items': 100, u'last_modified_at': 0, u'hashsize': 65536, u'keysize': 2048, u'items': 0, u'hash': u'djb33x', u'miss': 0}]}}
        add_header(mocked_screen, 1154, 3, stats)

        print mocked_screen.mock_calls