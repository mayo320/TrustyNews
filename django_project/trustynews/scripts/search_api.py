from pws import Google
import DatabaseSearch
import math
import json


def keyword_search(keyword):

	news = Google.search_news('keyword', 10, 0, True, 'h', "us")

	# Arguments:
	# search(query, num, start, sleep, recent)
	# query: Required. The keyword that will be searched.
	# num: Default 10. The number of results returnedself.
	# start: Default 0. The number of top results that are to be ignored.
	# sleep: Default True. If True, the program will wait for a second, when applicable, to avoid overwhelming the servers.
	# recent: Default None. The following values are allowed: 'h': hour, 'd': day, 'w': week, 'm': month and 'y': year.(Buggy)
	# country_code: For local results.

	total_results =  news["total_results"]
	print total_results
	scale = 1 - math.exp(- total_results / 80000)

	for result in news["results"]:
		link = result["link"]
		if DatabaseSearch.is_valid(link):
			return scale
	
	print "couldn't find valid source"
	return 0.0
			
	

def url_list(keyword):
	news = Google.search_news('keyword', 10, 0, True, 'h', "us")
	data = {}

	for result in news["results"]:
		link = result["link"]
		if DatabaseSearch.is_fake(link):
			data[link] = 0
		elif DatabaseSearch.is_valid(link):
			data[link] = 1
		else:
			# unknown
			data[link] = 2

	return json.dumps(data)
