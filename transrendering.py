#!/usr/bin/env python3

import re

file = open('in.txt', 'r')
out = open('out.txt', 'w')
for text in file:
	dict = open('dict.txt', 'r')
	for new in dict:
		x = new.split(':')
		x[1] = x[1].strip()
		if x[0] in text:
			text = re.sub(r'\b' + x[0] + r'\b', x[1], text)
	dict.close()
	out.write(text)
out.close()
file.close()
