import urllib2
import urllib
import json

result = urllib2.urlopen("http://services.faa.gov/airport/status/DTW?format=json").read()
d = json.loads(result)
print d['city']
print d['weather']['temp']


