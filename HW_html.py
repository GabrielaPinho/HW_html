#! usr/bin/python

# we downloaded the files in shell with curl -L https://www.dropbox.com/s/u70dtrdr35p5tgk/seminars.tar.gz | tar zxv

from bs4 import BeautifulSoup
import os
import re

#the os. let the for iteract different files
files = os.listdir(".")

for i in files:
#organize the html file in hierarchies
    soup = BeautifulSoup(open(i))
#find the most specific section for my objectives
    main = soup.find(class_="clear-fix right-wide-column")
#find the section where it shows if the talk is from EcoEvoPub or not
    Eco = main.find_all("strong")
#this one didnt work, I was trying to exclude the webpages where there is no talk
    if main.find_all(class_="section")[0].string.split("\t")[4].split("                  ")[0] == u'no speakers scheduled at this time :-(':
        print("no talk")
#this worked partially, it stopped in the webpages with no talk
    elif Eco[0].string != "EcoEvoPub Series" or Eco[0].string == 0 or Eco[0].string == None:
        print("not EcoEvoPub")
#this worked fine to parse the date and names in the EcoEvoPub talks
    elif Eco[0].string == "EcoEvoPub Series":
        name = re.search("\<p\>(\w+\s\w+)\<br", str(main), re.I)
        date = re.search("\<h4\>\s*(\w+\s+\d+\s+\d+)\s*\<\/h4\>", str(main), re.I)
        print (name.group(1)+ " "+ date.group(1))
    else:
        break

#file used to test 
soup = BeautifulSoup(open("797.html"))

# the files are not consistent, sorry, I couldn't write a code to account for all websites
