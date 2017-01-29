from urlparse import urlparse

def is_fake(url):
        url = urlparse(url)
        base = url.netloc
        if base[0:3]=='www':
                base = base[4:len(base)]
        with open('fake_sites.csv') as f:
                lines = f.readlines()
                for line in lines:
                        if str(base.lower()) == str(line.strip().lower()):
                                return True
        return False

def is_valid(url):
        url = urlparse(url)
        base = url.netloc
        if base[0:3]=='www':
                base = base[4:len(base)]
        with open('valid_sites.csv') as f:
                lines = f.readlines()
                for line in lines:
                        if str(base.lower()) == str(line.strip().lower()):
                                return True
        return False