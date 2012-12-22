#!/usr/bin/env python
import yaml
import sys
from kazoo.client import KazooClient

if len(sys.argv) < 3:
	print "Usage: %s '<zookeeper server>' '<zookeeper root znode>(NO TRAILING SLASH!)' '<yaml file>'"
	sys.exit(1)

zk = KazooClient(hosts=sys.argv[1])
zk.start()

stream = open(sys.argv[3], 'r')
s = yaml.load(stream)

#http://stackoverflow.com/questions/11501090/iterate-over-nested-lists-and-dictionaries
string_types = (str, unicode)
iteritems = lambda mapping: getattr(mapping, 'iteritems', mapping.items)()

def objwalk(obj, path=(), memo=None):
    if memo is None:
        memo = set()
    iterator = None
    if isinstance(obj, dict):
        iterator = iteritems
    elif isinstance(obj, (list, set)) and not isinstance(obj, string_types):
        iterator = enumerate
    if iterator:
        if id(obj) not in memo:
            memo.add(id(obj))
            for path_component, value in iterator(obj):
                for result in objwalk(value, path + (path_component,), memo):
                    yield result
            memo.remove(id(obj))
    else:
        yield path, obj

for i in objwalk(s):
	x = ''
	for o in i[0]:
		x += '/%s' % (o)
	p = '%s%s' % (sys.argv[2], x)
	print 'Adding: %s, value: %s' % (p, str(i[1]))
	zk.create(p, value = str(i[1]), makepath=True)

zk.stop()
