import MLAnalysis
fakeArticles =['http://abcnews.com.co/obama-executive-order-bans-pledge-of-allegiance-in-schools/',
            'http://abcnews.com.co/obama-signs-executive-order-banning-national-anthem/',
               'http://humansarefree.com/2016/10/why-flu-shots-are-greatest-medical.html',
               'http://conservativetribune.com/teacher-shot-trump-screamed-die/',
               'http://thedcgazette.com/2016/person-investigating-clintons-dead/',
               'http://www.infowars.com/swedish-police-overwhelmed-by-muslim-violence/'
    ]

data = []
for i in fakeArticles:
    data.append(MLAnalysis.calculate(i))

for i in data:
    print i['Total']
