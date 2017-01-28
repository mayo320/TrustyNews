from pws import Google


search = Google.search(query='trump inauguration photo', num=10, start=0, country_code="es")
news = Google.search_news('github', 10, 0, True, 'd', "es")

# print search
# print news


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
for result in news["results"]:
	print result["link"]

# search = str(search).replace("'", '"') 
# news = str(news).replace("'", '"')

# f = open('search_output.txt', 'w')
# f.write('SEARCH RESULT\n') 
# f.write('=============\n')
# f.write(search)
# f.close()


# f = open('news_output.txt', 'w')
# f.write('NEWS RESULT\n')
# f.write('===========\n')
# f.write(news)
# f.close() 


