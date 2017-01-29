from pws import Google
import DatabaseSearch
import math
import json


def keyword_search(keyword):
	news = Google.search_news(keyword, 10, 0, True, 'h', "us")

	# Arguments:
	# search(query, num, start, sleep, recent)
	# query: Required. The keyword that will be searched.
	# num: Default 10. The number of results returnedself.
	# start: Default 0. The number of top results that are to be ignored.
	# sleep: Default True. If True, the program will wait for a second, when applicable, to avoid overwhelming the servers.
	# recent: Default None. The following values are allowed: 'h': hour, 'd': day, 'w': week, 'm': month and 'y': year.(Buggy)
	# country_code: For local results.

	total_results =  news["total_results"]
	scale = 1 - math.exp(- total_results / 80000.0)

	dif = 0
	data = []
	for result in news["results"]:
		currentURL = {}
		link = result["link"]
		currentURL['url'] = link
		if DatabaseSearch.is_fake(link):
			dif = dif - 0.5
			currentURL['reliable'] = 0
		elif DatabaseSearch.is_valid(link):
			dif = dif + 1
			currentURL['reliable'] = 1
		else:
			# unknown
			currentURL['reliable'] = 2
		data.append(currentURL)

	if dif >=3.5:
		score = min(dif*scale/2.0,1)
	elif dif ==0:
		score = scale*0.75
	else:
		score = scale

	return {'SearchReliability':score, 'NumResults':total_results, 'URLs':data}
