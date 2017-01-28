def getTopLevel(url):
    if url[0:4].lower()=='http':
        url = url[linSearch(url,'/',2)+1:len(url)]
    nextSlash = linSearch(url,'/',1)
    if nextSlash != 0:
        url = url[0:nextSlash]
    if url[0:3].lower()=='www':
        url = url[4:len(url)]
    return url

    
def linSearch (string, char, occ):
    temp = 0
    for i in range(0,len(string)):
        if string[i] == char:
            temp = temp +1
            if temp == occ:
                return i
    return 0
