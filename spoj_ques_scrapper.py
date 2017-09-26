import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://problemclassifier.appspot.com/').read()
soup = bs.BeautifulSoup(source, 'lxml')

def get_links():
	f = open('problem_tag.txt','w')
	fpm = open('problem_tag_modified.txt','w')
	count = 1
	count1=1
	for index in range(1,23):
		table = soup.find('div', attrs = {"class":"tab-pane", "id":"tab"+ str(index)})
		table_rows = table.find_all('a')
		shan = table.find_all('tr')
		for link,tr in zip(table_rows,shan):
				f.write(str(count)+ ")\n"+ link.get("href")+ '\n')
				td = tr.find_all('td')
				for i in td:
					if i!="\n":
						row =i.text	
						f.write(str(row))
				count = count+1
		
	with open("problem_tag.txt","r") as fi:
		for line in fi:
			clean=line.strip()
			if clean:
				fpm.write(clean+"\n")					
	
	print("Links Downloaded successfully\n")


def get_ques():
	f = open('problem_tag_modified.txt','r')
	prob = open('problems.txt','w')
	num = 1
	for line in f:
		if "http:" in line :
			ques = urllib.request.urlopen(line).read()
			soup1 = bs.BeautifulSoup(ques, 'lxml')
			table1 = soup1.find('div', attrs = {"id":"problem-body"})
			#print(table1.text)
			prob.write(str(num)+":-\n"+table1.text)
			num = num+1
			prob.write("****************************************************************************************************************\n")


if __name__ == '__main__':

	print("Welcome to SPOJ PROBLEM SCRAPPER\n")
	print("Getting Links From Server\n")		
	get_links()
	get_ques()	

