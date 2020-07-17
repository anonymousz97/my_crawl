import requests
from bs4 import BeautifulSoup



def get(number,gender='Nam',born_hours='20',date='13',month='2',year='1997',option='com_boi',view='simdep',itemid='37'):
	gio = [1,3,5,7,9,11,13,15,17,19,21,23,25]
	born_hours = int(born_hours)
	for i in range(len(gio)-1):
		if born_hours >= gio[i] and born_hours <= gio[i+1]:
			hour = '{} giờ đến {} giờ'.format((gio[i]%24),(gio[i+1]%24))
			break
	url = 'https://xemvanmenh.net/xem-boi-so-dien-thoai.html?utm_medium=namsinh{}'.format(year)
	myobj = {'sosim': number,
		'gioitinh': gender ,
		'giosinh': hour,
		'ngaysinh': date,
		'thangsinh': month,
		'namsinh': year,
		'option': option,
		'view': view,
		'Itemid': itemid
	}
	x = requests.post(url, data = myobj)
	text = x.text
	#soup = BeautifulSoup(,'html.parser')
	#print(text)
	#print('Số : '+number+' '+text[text.find('Tổng điểm'):text.find('Tổng điểm')+16])
	# with open('t.html','wb') as f:
	# 	f.write(text)
	# with open('t.html','r',encoding='utf-8') as f:
	# 	data = f.read()
	# soup = BeautifulSoup(data,'html.parser')
	#print(soup.find('td_diem'))
	r = text[text.find('Tổng điểm')+6:text.find('Tổng điểm')+20]
	score = r[r.find(' '):r.find('/')]
	return float(score)
# print(get('0867450854'))