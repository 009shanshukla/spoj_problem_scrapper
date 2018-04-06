### The tool is built in multi-threaded python environment
### os library is used to create directory and sub-directory
### urllib is used to connect and get response from the specified website
### this is a main file which will be run for crawling 
### queue library is used to store and share the task amongst the spiders(workers)



import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'mysmallwebpage'
HOMEPAGE = 'http://spoj.com/problems/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

### class Spider is created in Spider library with given instances variable
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


### Create worker threads (will die when main exits)
def create_workers():

	###  Threads will be create to do work() job and will be destroyed when the main exits(t.daemon() = True)
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue, every thread will get a link(job) from the queue and will crawl the link 
def work():
	### a thread will take jobs(links), then crawl and repeat untill queue will not be empty 
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job(jobs are stored in queue)
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    ### job will be in the queue untill it is not done. (untill task_done() is not called)    
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
