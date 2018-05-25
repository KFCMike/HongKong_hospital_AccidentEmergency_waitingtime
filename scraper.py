import requests
#from bs4 import BeautifulSoup
import json
import scraperwiki
from datetime import datetime
#import pytz

req = requests.get('http://www.ha.org.hk/aedwt/data/aedWtData.json')
j = req.json()

names=[j['result']['hospData'][i]['hospNameB5'] for i in range(0,18)]
waitime=[j['result']['hospData'][i]['topWait'] for i in range(0,18)]
names[15]=names[15][0:5]

#hkt = pytz.timezone('Asia/Hong_Kong')
#dt = datetime.now().replace(tzinfo=hkt).date()
dt=j['result']['hospData'][0]['hospTimeEn']
data['date'] = dt
data = {names[i]: waitime[i] for i in range(0, 18)}

#print(data)
scraperwiki.sqlite.save(unique_keys=['date'], data=data)



