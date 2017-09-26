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


def get_ques(count):
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
			if num==count:
				break


if __name__ == '__main__':

	print("Welcome to SPOJ PROBLEM SCRAPPER\n")
	while 1:
		print("To Agree press 1 or to disagree press 2\n")
		ans = int(input())
		if ans == 1:
			print("Getting Links From Server ,Please Wait :)\n")		
			get_links()
			while 1:
				print("How many question do you want to scrap ?the more you want the more time it will take :) max(1-634)\n")
				count = int(input("enter :"))
				if count<=634 and count>=1:
					print("Please Wait\n")	
					get_ques(count)
					print("Your task is completed, BYE BYE \n")
					exit()
				else :
					print("only 1 to 634 ques are available :) press again\n")
		elif ans == 2:
			exit()	
		else:
			print("you have entered wrongly , press again\n") 
		
