from urlparse import urlparse
import os
def is_fake(url):
        url = urlparse(url)
        base = url.netloc
        fn = os.path.join(os.path.dirname(__file__),'fake_sites.csv')
        if base[0:3]=='www':
                base = base[4:len(base)]
        with open(fn) as f:
                lines = f.readlines()
                for line in lines:
                        if str(base.lower()) == str(line.strip().lower()):
                                return True
        return False

def is_valid(url):
        url = urlparse(url)
        base = url.netloc
        fn = os.path.join(os.path.dirname(__file__),'valid_sites.csv')
        if base[0:3]=='www':
                base = base[4:len(base)]
        with open(fn) as f:
                lines = f.readlines()
                for line in lines:
                        if str(base.lower()) == str(line.strip().lower()):
                                return True
        return False
