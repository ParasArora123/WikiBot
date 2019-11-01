""" Project Primus!
	Implement a bot that will intelligently find a Wikipedia link ladder 
	between two given pages. You will be graded on both finding the shortest 
	path (or one of them, if there are several of equal length), and how fast 
	your code runs.
"""
__author__ = "Paras Arora" # put your name here!

import re
import requests

from urllib.request import urlopen
from urllib.request import Request
#from bs4 import BeautifulSoup

## The HIDEOUS beautiful soup way that takes years to get a result:

# def getGoodLinks(wikiPage):
# 	wikiURL = "https://en.wikipedia.org/wiki/" + wikiPage
# 	html = urlopen(wikiURL)
# 	bsObj = BeautifulSoup(html, "lxml") # lxml SO MUCH FASTER than html.parser (even though I am not using this way)
# 	linkList = bsObj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^\/wiki\/[^:]*$")})
# 	retList = []
# 	for link in linkList:
# 		retList.append(link.get("href").lstrip('\/wiki'))
# 	return retList


# Using regex (NO beautiful soup) making things much, much faster!! (main optimization strategy)
def getCleanLinksQuickly(wikiPage):
	""" This function takes a wiki page, gets all of the HTML content 
		and then uses regex to search through that content and return 
		a list of all of the titles of the pages that are links/clickable.
	"""
	wikiURL = "https://en.wikipedia.org/wiki/" + wikiPage
	html = urlopen(wikiURL).read() 
	strHtml = html.decode() #converting html to a string

	# a list of all the clean links using regex capture group so I can 
	# return it without having to strip off the wiki etc. :)))
	return re.findall(r'<a\shref="\/wiki\/([A-Za-z_0-9\(\)%]+?)"', strHtml) 


def wikiladder(startPage, endPage):
	""" This function returns a list of the wikipedia links (as page titles) 
		that one could follow to get from the startPage to the endPage using 
		Breadth First Search. The returned list includes both the start 
		and end pages.
	"""
	print("running!")
	queue = [[startPage]]

	while queue:
		path = queue.pop(0) # popping off the front 
		final_link = path[-1] # the link at the end of the path

		list_from_link = getCleanLinksQuickly(final_link)
		set_of_all_links = set() # Optimized!: So I don't check the same link twice 

		for link in list_from_link:
			if link != endPage and link not in set_of_all_links:
				new_path = list(path) # Can't assign new_path = path since it will change both 
				new_path.append(link)
				queue.append(new_path)
				set_of_all_links.add(link) # making sure to add link to the set so it is not checked twice

			elif link == endPage:
				path.append(link)
				return path

if __name__ == '__main__':
	# put your test code here
	ladder = wikiladder("Emu", "Duke_University") 
	print(ladder)

# NOTES: 
# Traversing trees:

# 1. Breadth-first search (look at every path that is one length away from you), once you look at every 1 hop away, then I look at every 2 hop
# 2. Depth-first search (go as far down as it can before it does anything)

# 1. Preorder (is an example of depth-first search)
# 2. Inorder 
# 3. Postorder

# Breadth first search --> use a queue (put them in the back take them out the front...first in first out)
# when you go to a page you add all the links to a queue

#                o
#		  1   2   3   4      5
#		 o 	  o    o   o 	 o 
#       /     /     \   \    |
#      6     7      8    9   10 
#	   o     o      o    o   o
# 
# With breadth first search I would add links (the numbers) using the following steps:
# Step 1: Add 1, 2, 3, 4, 5, onto the list (list = 1, 2, 3, 4, 5)
# Step 2: Take off 1 and add 6 (list = 2, 3, 4, 5, 6)
# Step 3: Take off 2 and add 7 (list = 3, 4, 5, 6, 7)
# Conitinue this process until you find the link 

#Queue:
	#.append()
	#.pop()

# put starter page in queue 
# while queue is not empty:
# 		pop the front of queue 
#		go to that page and get links
#		for each link:
#			if link is not the target:
#				append link to queue
#			else:
#				return the path to this link 

# Path to the link:
# in the queue append the list of the links to get to that link in a tuple 
# e.g: 
# my_queue = [(United_states, Michigan, Hawaii), (United_states, Michigan, Latin_language)]

# just put the path in and use the last thing in the list

