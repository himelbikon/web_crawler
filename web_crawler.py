import requests, bs4, re, urllib.parse

target_url = input('Enter URL: ')
main_list = []

def response(url):
	try:
		return 'posetive', requests.get(url)
	except:
		return 'negative'

def link_filter(list_1):
	list_2 = []
	for x in list_1:
		x = re.findall('(?:href=")(.*?)"', str(x))
		x = urllib.parse.urljoin(target_url, str(*x))
		list_2.append(x)
	return list_2

def main(url):
	result = response(url)

	if result[0] == 'posetive':
		bs = bs4.BeautifulSoup(result[1].text, 'html.parser')
		a_list = bs.find_all('a')
		a_list = link_filter(a_list)
		for x in a_list:
			if target_url in x and not x in main_list:
				main_list.append(x)
				print('[%d]' % len(main_list), x)
				with open('links.txt', 'a') as f:
					f.write(x + '\n')
				main(x)

main(target_url)

print('Total %d links ganerated' % len(main_list))


