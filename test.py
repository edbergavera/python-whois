import whois
from pprint import pprint


domains = '''
aipa.ca
split5.ca

'''

#domains = ''


for d in domains.split('\n'):
	if d:
		print('-'*80)
		print(d)
		w = whois.query(d, ignore_returncode=1)
		if w:
			wd = w.__dict__
			for k, v in wd.items():
				print('%20s\t"%s"' % (k, v))

