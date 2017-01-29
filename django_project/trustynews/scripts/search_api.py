from pws import Google
import DatabaseSearch


def keyword_search(keyword):

	news = Google.search_news('keyword', 10, 0, True, 'd', "es")

	# Arguments:
	# search(query, num, start, sleep, recent)
	# query: Required. The keyword that will be searched.
	# num: Default 10. The number of results returnedself.
	# start: Default 0. The number of top results that are to be ignored.
	# sleep: Default True. If True, the program will wait for a second, when applicable, to avoid overwhelming the servers.
	# recent: Default None. The following values are allowed: 'h': hour, 'd': day, 'w': week, 'm': month and 'y': year.(Buggy)
	# country_code: For local results.

	total_results =  news["total_results"]

	for result in news["results"]:
		link = result["link"]
		if DatabaseSearch.is_valid(link):
			print total_results
			if total_results > 10000:
				return True
			else:
				return False
	
	print "couldn't find valid source"
	return False
			
	

