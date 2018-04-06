# spoj_problem_scrapper
Self Mini Project on web scrapping and crawling

It is a multithreaded Python tool which is used to save problems onto text file from spoj.com. Basically it crawls the whole website (links are only visited once) and scrap the whole problem body using Beautiful Soup library and save them onto a text file.

Data searching, Data harvesting and data analytics are done as a seperate program. Multithreading makes program fast as it can crawl more links at a time and using set to store problem text and then save onto text, increases running time as it does not require to open text file each time.

### Requirements 

- Python3
- bs4
- requests
- urllib 
- os

### Specifications

- Multithreading

- No repetion of problems (As link is visited only once)

- Storing Onto file is fast (Sets are used so that file is not opened frequently)

![](https://github.com/009shanshukla/spoj_problem_scrapper/blob/master/1.png)  




