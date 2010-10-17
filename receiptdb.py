#!/usr/bin/env python
# vim: set fileencoding=utf-8:

from __future__ import with_statement
import sys, re, datetime

def parse_db(name):
	year_match = re.compile("### (\d\d\d\d)")
	entry_match = re.compile("(\d+)\.(\d+)\.*\s+([A-Za-z]+)\s+(\d+,\d*)(.*)")
	entries = []
	with open(name) as f:
		for line in f:
			line = line.strip()
			if len(line) == 0:
				continue
			m1 = year_match.search(line)
			m2 = entry_match.search(line)
			if m1:
				year = m1.group(1)
				#print "Processing %d ..." % int(year)
			elif m2:
				day, month, category, price, info = m2.groups()
				date = datetime.date(int(year), int(month), int(day))
				cents = int(price.replace(",", ""))
				info = info.strip()
				entries.append((date,category,cents,info))
			else:
				print "OOPS: '%s'" % line
				sys.exit(1)
	return entries

def category_canonicalize(c):
	if c=="R" or c=="Ruoka": return "ruoka"
	if c=="V" or c=="Vaatteet": return "vaatteet"
	if c=="Matkustus" or c=="Matk": return "matkustus"
	if c=="M" or c=="Muut": return "muut"
	print "ERROR: unknown category: %s" % c
	sys.exit(1)

if __name__ == '__main__':
	print "ERROR: Dont execute this file"
	sys.exit(1)
