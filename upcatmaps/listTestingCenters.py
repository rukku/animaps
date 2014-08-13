import json
from pprint import pprint
txtfile =open('old.index.txt')

template = "                <li>%s</li>"

for line in txtfile.readlines():
		if "h4" in line:
			print template % (line[26:-10])