import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://problemclassifier.appspot.com/').read()
soup = bs.BeautifulSoup(source, 'lxml')

def get_links():
	f = open('all_link.txt','w')
	fp = open('problem_tag','w')
	fpm = open('problem_tag_modified','w')
	count = 1
	count1=1
	for index in range(1,23):
		table = soup.find('div', attrs = {"class":"tab-pane", "id":"tab"+ str(index)})
		table_rows = table.find_all('a')

		for link in table_rows:
				f.write(str(count)+ ")\n"+ link.text + " :-\n"+ link.get("href")+ '\n')
				count = count+1
	  
		
		
		shan = table.find_all('tr')
		for tr in shan:
			td = tr.find_all('td')
			for i in td:
				if i!="\n":
					row =i.text	
			fp.write(str(count1)+" : "+row)
			count1 = count1+1

	with open("problem_tag","r") as fi:
		for line in fi:
			clean=line.strip()
			if clean:
				fpm.write(clean+"\n")
				
					
	
	print("Links Downloaded successfully\n")


def get_ques():
	f = open('all_link.txt','r')
	num = 0
	for line in f:
		num = num+1
		if num%3==0 and num<=100 :
			ques = urllib.request.urlopen(line).read()
			soup1 = bs.BeautifulSoup(ques, 'lxml')
			table1 = soup1.find('div', attrs = {"id":"problem-body"})
			print(table1.text)



if __name__ == '__main__':

	print("Welcome to SPOJ PROBLEM SCRAPPER\n")
	print("Getting Links From Server\n")		
	get_links()
#	get_ques()	

