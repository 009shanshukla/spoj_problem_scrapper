from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
import requests
from bs4 import BeautifulSoup

### all methods and variables of a crawler will be defined in Spider class
class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    texting = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)


            ### opening crawling url and scrapping the problem-body
            res = requests.get(page_url)
            s = BeautifulSoup(res.text, 'html.parser')
            table1 = s.find('div', attrs = {"id":"problem-body"})
            #print(table1)
            if table1 != None:
                Spider.texting.add(table1.text)
                



            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))

            ### add all links from the current page
            Spider.add_links_to_queue(Spider.gather_links(page_url))

            ### remove the current page from queue set
            Spider.queue.remove(page_url)

            ### add current page  onto crawled set
            Spider.crawled.add(page_url)

            ### from both sets, update it onto file
            Spider.update_files()

            p = "problem.txt"
            with open(p, 'a') as file:

                for x in Spider.texting:
                    file.write('\n\n\n' +
                    	"............................ PROBLEM STATEMENT............................\n\n\n" + 	
                     x + '\n\n' + 
                        '###################################################################################################################################################################')


    # Converts raw response data into readable information and checks for proper html formatting(links are returned)
    @staticmethod
    def gather_links(page_url):
        html_string = ''    ### will store link string
        try:
            response = urlopen(page_url)       ### connect with the page

            ### check if a page is in html format if yes, continue
            if 'text/html' in response.getheader('Content-Type'):

            	### read() gives html page in bytes, then decode it into utf-8(readable english lang)
                html_bytes = response.read()                     
                html_string = html_bytes.decode("utf-8")

            ### create the object of LinkFinder class and send html for parsing    
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()

        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:

        	###  no -repeation of links
            if (url in Spider.queue) or (url in Spider.crawled):
                continue

            ### in case links is of another domain , reject it    
            if Spider.domain_name != get_domain_name(url):
                continue
                
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)







        		



        
