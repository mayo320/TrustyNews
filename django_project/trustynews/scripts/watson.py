import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

api_key_alc='1983387b2fb355dca6bc2cf73437d3e4bbfa6dbf'

def analyze(url):
    alchemy_language = AlchemyLanguageV1(api_key=api_key_alc)
    combined_operations = [ 'entity', 'keyword', 'title', 'concept', 'doc-emotion']
    global data
    data = alchemy_language.combined(url=url, extract=combined_operations)
    

def getTitle():
    global data
    title = data['title']
    return title.encode('ascii','ignore')

def getKeywords():
    global data
    return data['keywords']    

def getKeyKeywords():
    words = []
    global data
    for i in range(0,7):
        words.append(data['keywords'][i]['text'])
    return words
    
def getEmotions():
    global data
    emotions= data['docEmotions']
    return emotions



