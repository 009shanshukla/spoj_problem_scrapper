import bs4 as bs  #BeautifulSoup library
import urllib.request   #to connect with url
import linecache    #to read specific line

source = urllib.request.urlopen('https://problemclassifier.appspot.com/').read()   #getting source page for given url
soup = bs.BeautifulSoup(source, 'lxml')    # parsing lxml parser by converting sourcepage in beautifulsoup object


def get_links():         # function to get links and tags and store them in hidden file (. is added before file)


	f = open('.garbage.txt','w')       #file that stores link and tag in inappropriate way
	fpm = open('.problem_tag_modified.txt','w')       #file that stores in good manner 



	count = 1             #to count total links
	

	for index in range(1,23):     #parsing all tag in links that are total 22
		table = soup.find('div', attrs = {"class":"tab-pane", "id":"tab"+ str(index)})     #for given tab getting div tag
		table_rows = table.find_all('a')                                                   #finding a tag to get url linked
		shan = table.find_all('tr')														#finding tr tag to get tag table data				
		for link,tr in zip(table_rows,shan):											#moving both loop together by zipping them
				f.write(str(count)+ ")\n"+ link.get("href")+ '\n')						# storing URL	
				td = tr.find_all('td')													#from tr tag getting td tag to stote tag name
				for i in td:
					if i!="\n":
						row =i.text	
						f.write(str(row))                                  #storing tag text
				count = count+1                                         
		
	with open(".garbage.txt","r") as fi:                              
		for line in fi:
			clean=line.strip()                                  # from above loop data is stored with garbage (eg. \n\n) ,here we are removing
			if clean:											
				fpm.write(clean+"\n")						#now good tag data is storing in new file
	
	print("Links Downloaded successfully\n")
	f.close()
	fpm.close()


def get_ques(count):                                      #question are parsed here along with tag from above stored file
	f = open('.problem_tag_modified.txt','r')
	#prob = open('problems.txt','w')
	num = 0                                           #to match total question that want to be downloaded (when num == count -> break) 
	for  i,line in enumerate(f):					#file is read in line by line with numbers from zero indexing				
		if "http:" in line :                       #as soon as http line detected
		
			lol = open('.problem_tag_modified.txt','r')      #file is again open in different object so that no overlapping happens 
			tagname = lol.readlines()[i+2]			#get next line of that http line to store tag  
			print("gettin problem with tag ->   "+tagname)    #console is printing tag name
			ques = urllib.request.urlopen(line).read()        #for that http link we are collecting source page
			soup1 = bs.BeautifulSoup(ques, 'lxml')          #doing same thing as above to get question
			table1 = soup1.find('div', attrs = {"id":"problem-body"})  #problem content is in problem-body
			#print(table1.text)
			with open(tagname,'a') as prob:     #for different tag storing in different file according to tagname
				prob.write(str(num+1)+":-\n"+table1.text)
				num = num+1
				prob.write("****************************************************************************************************************\n")
			
			if num==count:
				break
	f.close()
	lol.close()		
			
			
			#print(lines[line+1])


if __name__ == '__main__':        #giving look to main function to ask user wish

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
					print("Please Wait, file is distributing according to tag :)\n")	
					get_ques(count)
					print("Your task is completed, BYE BYE \n")
					exit()
				else :
					print("only 1 to 634 ques are available :) press again\n")
		elif ans == 2:
			exit()	
		else:
			print("you have entered wrongly , press again\n") 
		
