from urlparse import urlparse

def is_fake(url):
	with open('fake_sites.csv') as f:
		lines = f.readlines()
		for line in lines:
			if url.lower() == line.strip().lower():
				return True


# replace with url input from search here
url = raw_input("URL: ")

url = urlparse(url)
base_domain = url.netloc

if is_fake(base_domain):
	print "FAKE"
