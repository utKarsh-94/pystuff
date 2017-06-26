
ReadFile.py:
              used to list the directory contents without using os.scandir, os.walk, glob.

SearchInsert.py :
            The list can grow to a maximum length of 10. Make this limit as a configurable at

            the instantiation part of the class.

            ○ The insert function should get a string as its argument, insert the string to

            the list and return the index in which it was inserted. If the length of the list

            reaches maximum length, the oldest item accessed with select should be

            deleted and the new item should be inserted in its place.

            ○ The select function should accept an integer as argument and return the

            value at that index in the list.

Scrape.py:
       Environment Setup for Scrapy to scrape dynamic website

      1) Installation for python3
        > sudo apt-get install python3.5

      2) Installation for pip
        > sudo apt-get install python3-pip

      3) Installaton for scrapy
        > sudo pip3 install scrapy

      4) Installation for mongodb:
        > sudo apt-get install mongodb

      5) Installation for pymongo
        > sudo pip3 install pymongo

      6) Installation for BeautifulSoup
        > sudo pip3 install bs4


      Deploy 	project:

        1) scrapy startproject scrapnykaa
        2) The folder constitue of files and folders
        3) Inside the main project there is directory for spider
          In scrapynykaa/scrapynykaa/spiders create file name called scrap_nykaa.py
        4) Copy the contents from file and paste it. It will parse all data with
          product-id, image-link, and product-title and store it in monogdb.
