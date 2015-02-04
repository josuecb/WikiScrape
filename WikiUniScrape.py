from ScrapeWiki import scrapeTable, compileDiv1List
import json
from collegeContact import getContactList
import os
#open the list of NCAA members and make it into a string array/list

div1List = compileDiv1List()#used to pull location information from wiki table

fileold = open('NCAA_json.json', 'r')
backup = open('NCAA_jsonBackup.json', 'w')
backup.write(fileold.read())
fileold.close()
backup.close()
os.remove('NCAA_json.json')



file = open('NCAA_list.txt', 'r')
schoollist = file.read()
schoollist = schoollist.split('\n')
file.close()


type_dict = type({})

jsonout = {}
file = open('NCAA_json.json', 'a')

contactlist = getContactList()


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
        print counter

        file.write(jsonout)
        first = 1
file.write('}')
file.close()