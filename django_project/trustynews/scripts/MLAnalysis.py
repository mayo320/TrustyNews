import watson

url = 'http://www.cbc.ca/news/world/trump-putin-new-york-times-1.3956694'

def calculate(url):
    watson.analyze(url)
    returnList = {}
    keywords = watson.getKeyKeywords()
    returnList['Keywords'] = keywords
    
    emoA = watson.getEmotions()
    emoB = watson.getEmotionTone()
    emotion = {}
    emotion['Anger'] = (float(emoA['anger']) + float(emoB[0]['score']))/2
    emotion['Disgust'] = (float(emoA['disgust']) + float(emoB[1]['score']))/2
    emotion['Fear'] = (float(emoA['fear']) + float(emoB[2]['score']))/2
    emotion['Joy'] = (float(emoA['joy']) + float(emoB[3]['score']))/2
    emotion['Sadness'] = (float(emoA['sadness']) + float(emoB[4]['score']))/2
    emotion['Emotional Reliability'] = min(1,max(0.0,emotion['Sadness']*0.2+1-emotion['Anger']*0.5-emotion['Disgust']*0.5-emotion['Fear']*0.2)) #adjust these parameters
    returnList['Emotion'] = emotion
    
    language = watson.getLanguageTone()
    lang = {'Analytical':language[0]['score'], 'Confident':language[1]['score'], 'Tentative':language[2]['score']}
    lang['Language Reliability'] = min(1,max(0,1.5*lang['Analytical'] - lang['Tentative'] - 0.2*lang['Confident']))
    returnList['Language'] = lang

    social = watson.getSocialTone()
    soc = {'Openness':social[0]['score'],'Conscientiousness':social[1]['score'],'Extraversion':social[2]['score'],'Agreeableness':social[3]['score'],'Emotional Range':social[4]['score']}
    soc['Social Reliability'] = min(1,0.5*soc['Conscientiousness'] + 0.5*soc['Emotional Range'] + 0.5*soc['Agreeableness'])
    returnList['Social'] = soc

    totalScore = emotion['Emotional Reliability']*0.3+lang['Language Reliability']*0.3+0.4*soc['Social Reliability']
    returnList['Total'] = totalScore

    return returnList
    
    
