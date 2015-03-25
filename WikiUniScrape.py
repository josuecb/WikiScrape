from ScrapeWiki import scrapeTable, compileDiv1List
import json
from collegeContact import getContactList
import os
from termcolor import *
##################################################################################
#  this is the list of schools whose state/city can be scraped from wikipedia

div1List = compileDiv1List()
#used to pull location information from wiki table
#################################################################################

#######################################################
##   BACKUP PREVIOUS OUTPUT FILE AND DELETE CURRENT BEFORE WIRITING
fileold = open('NCAA_json.json', 'r')
backup = open('NCAA_jsonBackup.json', 'w')
backup.write(fileold.read())
fileold.close()
backup.close()
os.remove('NCAA_json.json')
#########################################################



############################################################
##   reads the list of schools to be scraped
##  change the file being opened here to scrape more/other schools
file = open('NCAA_list.txt', 'r')
schoollist = file.read()
schoollist = schoollist.split('\n')
file.close()
############################################


#######################
type_dict = type({})## used to check if variable is a dictionary
jsonout = {}##  this dictionary will be used for the creation of the json file
file = open('NCAA_json.json', 'a')# the output file
##########################

#########################
##  this compiles a list of contact information from another website, the list it returns will be passed into other functions
contactlist = getContactList()
########################



########################
##  write to the output file
########################
counter = 0
first = 0

file.write('{')
for school in schoollist:
    result = scrapeTable(school, div1List, contactlist)
    if result != None:
        if first != 0:
            file.write(',')
        jsonout = result
        jsonout = json.dumps(jsonout)
        jsonout = str((jsonout[1:jsonout.__len__() - 1]))#probably already makes it a string but whatever
        print jsonout
        counter += 1
        print colored('Scraped Universities: ' + str(counter), 'green')


        file.write(jsonout)
        first = 1

file.write('}')
file.close()
###############################

