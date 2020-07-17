import requests
from bs4 import BeautifulSoup
import json
from check_sim import get

url = 'https://vietteltelecom.vn/api/get/sim'
#year = input('Nhap nam sinh : ')
i=1
with open('diem.txt','w+',encoding='utf-8') as f:
	while True:
		params = {'key_search': "", 'page': i, 'page_size': 10, 'total_record': 1}
		x = requests.post(url, data = params)
		#soup = BeautifulSoup(x.text,'html.parser')
		res = json.loads(x.text)
		i+=1
		if res['errorCode'] != 0:
			break
		for j in res['data']:
			r = get('0'+j['isdn'])
			s_r = "Số : "+'0'+j['isdn']+' điểm : '+str(r)
			f.write(s_r)
			f.write('\n')
			break





