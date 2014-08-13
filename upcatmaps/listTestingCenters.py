import json
from pprint import pprint
txtfile =open('old.index.txt')

template = "                <li>%s</li>"

'''
for line in txtfile.readlines():
		if "h4" in line:
			print template % (line[26:-10])
'''
			
for line in txtfile.readlines():
		#if "h4" in line:
		#	print template % (line[26:-10])
		if "ul" in line:
			print line
		elif "<li><a" in line:
			print line
#		elif "menu-item" in line:
#			continue
#		elif "h4" in line:
#			continue
		elif "<div" in line:
			print "                <div>"
		elif "</div" in line:
			print "                </div>"			