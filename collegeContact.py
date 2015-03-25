import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup

def addcontact(add, index, to):
    i = 0
    while i < 7:
        to.append(add[index])
        index += 1
        i += 1
    return to


def getContactList():
    site = requests.get('http://www.testprepreview.com/college_contactinfo.htm')
    soup = BeautifulSoup(site.content)

    contactlist = soup.text
    contactlist = contactlist.split('\n')

    def getEntryPoint():
        i = 0
        for lines in contactlist:
            if lines == 'Alabama':
                break
            else:
                i += 1
        i -= 1
        return i


    def buildList():
        i = getEntryPoint()
        newList = []

        while i < contactlist.__len__() - 1:
            if contactlist[i] == '':

                i += 3
            newList.append(contactlist[i])

            i += 1
            newList.append(contactlist[i])


            if contactlist[i].find('(307) 766-1121') != -1:
                break
            if contactlist[i].find(',') != -1:

                i += 2
            else:
                i += 1

            newList.append('')
        return newList


    def scrapeCommas():
        i = 0
        while i < contactlist.__len__():
            if (i + 2) % 3 == 0 and i < contactlist.__len__():
                contactlist[i] = contactlist[i].replace(',', '')
            i += 1
        return contactlist


    contactlist = buildList()
    contactlist = scrapeCommas()


    def pullAddress():
        i = 0
        newList = []
        while i < contactlist.__len__():
            address = []
            phone = ''
            address = contactlist[i]
            address = address.split(',')
            if address.__len__() == 4:
                newList.append(address[0].replace(',', ''))
                newList.append(address[1].replace(',', ''))
                newList.append(address[2].replace(',', ''))
                newList.append(address[3][1:3])
                newList.append(address[3][4:])


                i += 1
                num = ''

                for ch in contactlist[i]:
                    if ch.isdigit():
                        num += ch

                if num.__len__() == 10:
                    newList.append(num)
                else:
                    newList.append('NONE')

                newList.append('')
                i += 1
            i += 1
        return newList


    def removeSpace():
        i = 0
        while i < contactlist.__len__():
            if contactlist[i] != '':
                if contactlist[i][0] == ' ':
                    contactlist[i] = contactlist[i].replace(' ', '', 1)
            i += 1
        return contactlist


    contactlist = pullAddress()
    contactlist = removeSpace()


    ####
    ## integrate other list (built from google)
    ####
    contactfile = open('phone_address_list.txt', 'r')
    contact = contactfile.read()
    contactfile.close()
    contact = contact.split('\n')
    cl = 0
    combined = []
    while cl < contactlist.__len__():
        c = 0
        match = False
        while c < contact.__len__():
            if contactlist[cl] == contact[c]:
                match = True
                combined = addcontact(contact, c, combined)
                break
            c += 7

        if match == False and contactlist[cl] != '':
            combined = addcontact(contactlist, cl, combined)

        cl += 7


    c = 0
    while c < contact.__len__():
        com = 0
        match = False
        while com < combined.__len__():
            if contact[c] == combined[com]:
                match = True
            com += 7
        if match == False and contact[c] != '':
            combined = addcontact(contact, c, combined)

        c += 7

    return combined



def addLoc(titles, values, school, contactlist):
    i = 0
    while i < contactlist.__len__():
        if contactlist[i] == school:
            # University phone number, address 1, city, region, postal-code
            # These titles (keys) will be changed after key_changer method
            i += 1#go to address
            titles.append('uni address 1')
            values.append(contactlist[i])
            i += 1# go to city
            titles.append('uni city')
            values.append(contactlist[i])
            i += 1# go to state/region
            titles.append('uni region')
            values.append(contactlist[i])
            i += 1# postal
            titles.append('uni postalcode')
            values.append(contactlist[i])
            i += 1 #phone
            if contactlist[i] != 'NONE':
                titles.append('uni phone')
                values.append(contactlist[i])
            break
        i += 7
    return titles, values

def main():
    getContactList()

main()