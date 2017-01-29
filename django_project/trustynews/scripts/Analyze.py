import MLAnalysis
import DatabaseSearch
import search_api
def analyze(url):
    returnList= {}
    returnList['MachineLearning'] =  MLAnalysis.calculate(url)
    
    if DatabaseSearch.is_valid(url):
        returnList['DomainCheck'] = 1
    elif DatabaseSearch.is_fake(url):
        returnList['DomainCheck'] = 0
    else:
        returnList['DomainCheck'] = 2

    stringList = []
    for i in range(0,3):
        stringList.append(returnList['MachineLearning']['Keywords'][i].encode('ascii','ignore'))

    returnList['SearchResults'] = " ".join(search_api.keyword_search(stringList))
    #returnList['TotalReliability'] = 
    return returnList
    
