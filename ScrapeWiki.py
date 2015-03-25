import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
from create_Json import wikijson
from htmlcolors import *
from getimages import download_img
from remove_p import remove_p
from collegeContact import addLoc
import time
import team_link
from auxiliar_methods import *
from termcolor import *
############################################################
#########################################################
###   GET COLORS FORM WIKI TABLE
###
## pull the school colors from the schools wikipedia page
############################################################
def scrapeColors(table):

    table = str(table)#the table that contains the color information (as a string list)
    colors = []
    lines = 0
    ######################
    ##       looks for commands related to setting background color (if we have thr proper table this should return only what is needed)
    while lines < (table.__len__() - 12):
        color = ''

        #border-right is used for schools with 2 colors in a single colorbox
        if table[lines : (lines + 12)] == '"background:' or table[lines : lines + 12] == 'background-c' or table[lines : lines + 12] == 'border-right':
            blackorwhite = 0#if a black or white value is witten in text (common)

            textcolor = 0
            # get potential  color name string string
            while table[lines] != ':':
                lines += 1
            lines += 1
            temp = lines

            col = ''#potential color
            while table[temp] != ';':
                col += table[temp]
                temp += 1

            textcolor, col = checkforcolor3(col)

            if textcolor == 1:
                colors.append(col)
            else:
                linestart = lines
                while table[lines] != '#' and lines < table.__len__() - 5:#pulls all characters following the '#'

                   # checks for any 'english' color commands within the html, colors can be added to the dictionary within the functions corresponding script
                    #  bw = 1 or 0, col = the color code, ind = the position of the last character of the color within the html string
                    #bw, col, ind = checkforcolor2(table, lines)

                   # if bw == 1:# bw indicates the color was written in english within the html
                      #  blackorwhite = 1#this should probably just use the value bw now
                       # colors.append(col)
                      #  lines += ind
                       # break
                    lines += 1
                color += table[lines]
                lines += 1

                if blackorwhite == 0:
                    while table[lines].isalnum():
                        color += table[lines]
                        lines += 1


                    if colors.__len__() != 0:
                        if colors[- 1] != color:
                            colors.append(color)
                    else:
                        colors.append(color)
            lines += 1
        lines += 1
    del lines, table
    return colors# returns colors as an array, if no colors are found returns an empty array, its length will be checked to determine the existance of color data





def compileDiv1List():
    while 1:
        try:
            site = requests.get('http://en.wikipedia.org/wiki/List_of_NCAA_Division_I_institutions')
            break
        except:
            time.sleep(1)
            pass

    soup = BeautifulSoup(site.content)
    div1string = soup.table.text
    div1string = div1string.split('\n')

    loop = 0
    while loop < div1string.__len__():
        if div1string[loop].find('!') != -1:

            div1string[loop] = div1string[loop][div1string[loop].find('!') + 1 :]
        if div1string[loop].find('[') != -1:

            div1string[loop] = div1string[loop][: div1string[loop].find('[') - 1]
        loop += 1

    return div1string




def append_value(value, key, titles_list, values_list):
    if value != None:
        titles_list.append(key)
        values_list.append(value)


def scrapeD1Locations(div1List, schoolName):
    titles = []
    values = []

    loop = 10
    getname = 0
    while loop < div1List.__len__():
        if getname == 0:
            if div1List[loop] == schoolName:
                loop += 2
                if loop < div1List.__len__():
                    titles.append('city')
                    values.append(unidecode(div1List[loop]))
                loop += 1
                if loop < schoolName.__len__():
                    titles.append('region')
                    values.append(unidecode(div1List[loop]))
        getname += 1
        if getname == 7:
            getname = 0
        loop += 1
    return titles, values





def scrapeTable(school, div1List, university_contactlist):
    titles = []# the name of each element being pulled
    values = []# the value of each element beinh pulled
        #the two arrays correspond to each other (titles[0] is the name of the data at values[0])
    url = 'http://en.wikipedia.org/wiki/' + school
    #get html
    while 1:
        try:
            site = requests.get(url)
            break
        except:
            time.sleep(10)
            pass


    #get table
    soup = BeautifulSoup(site.content)

    try:
        stringtable = soup.table.text
        tab = soup.table
    except:

        return
    team_link_logo = ''
    for tables in soup.find_all('table'):
        if tables.text.find('Website') != -1:
            # The 'team_link_logo' variable will contain our logo link
            # Just plug it into the main code because i don't know where it is: Josue
            team_link_logo = team_link.find_team_img_link(tables)
            if team_link_logo is None:
                team_link_logo = ''         # Here it seems this variable is not use but you are going to
                                            # to use it later
            # Here the code ends#################################
            #print(team_link_logo)

            stringtable = tables.text
            tab = tables

            break

    ###########################################################################
    schoolname = soup.span.text#This is the name of the school at the top of the wiki page, this will be more consistent
    print colored(school, 'red')
    if schoolname == 'Main Page':
        return
    # Finds twitter and facebook's school
    twitter, facebook = get_facebook_and_twitter(school)
    img_125x = get_image_000x(school, 'imageIN125.txt')
    img_250x = get_image_000x(school, 'imageIN250.txt')
    #print('%%%%%%%%%%%%%%%%%%%%%%%%%%%', twitter, facebook)
    #colors = []#array that will store the school colors
    colors = scrapeColors(tab)#gets the school colors (from colorgrab2), the table is passed to this function
    print colors#check progress (delete this later)
        #############################################################################



    #############################################################################
    stringtable = stringtable.split('\n')#seperate each table entry


    titles.append('name')
    values.append(unidecode(schoolname))#add the name as it appears at the top of the wiki page

    ################################################################################

    i = 0
    for element in stringtable:
        stringtable[i] = unidecode(element)
        i += 1





    ################################################################################
    ####  This is the data being pulled from the wiki table, anything added here will be stored in the arrays
    #         if there is a matching 'name' value present within the table
    category = ['Established', 'Motto', 'Motto in English', 'Endowment', 'President', 'Postgraduates', 'Undergraduates',
                'Athletics', 'Nickname', 'Mascot', 'Website']

    #########################################################
    #### Find fields that match the specified category titles
    def findmatch(name):
        catcount = 0
        output = -1
        while catcount < category.__len__():
            if category[catcount] == name:
                output = catcount
                break
            catcount += 1
        return output

    #########################################################








    #########################################################
    #### builds the two arrays based on the data within the catagories array

    max = stringtable.__len__()
    current = 3
    while current < max:
        while stringtable[current] == '' or stringtable[current] == '\n':
            current += 1
            if current >= max:
                break
        if current >= max:
            break
        if findmatch(stringtable[current]) != -1:
            if stringtable[current] == 'Motto in English':
                stringtable[current] = 'english'
            elif stringtable[current] == 'Motto':
                stringtable[current] = 'latin'
            elif stringtable[current] == 'Nickname':
                stringtable[current] = 'nickname plural'
            elif stringtable[current] == 'Postgraduates':
                stringtable[current] = 'postgraduate'
            elif stringtable[current] == 'Undergraduates':
                stringtable[current] = 'undergraduate'
            elif stringtable[current] == 'Website':
                stringtable[current] = 'uni url'            # University url from wiki it will be changed after \
                # key_changer function
            elif stringtable[current] == 'Athletics':
                stringtable[current] = 'conference'
            else:
                stringtable[current] = stringtable[current].lower()
            titles.append(stringtable[current])
            current += 1#move to next line

            while stringtable[current] == '\n' or stringtable[current] == '':
                current += 1#skip blank lines between title and information


            firstentry = 1
            while stringtable[current] != '\n' and stringtable[current] != '':
                if firstentry == 1:
                    values.append(remove_p(stringtable[current]))
                    firstentry = 0
                else:
                    values[values.__len__() - 1] += ', ' + stringtable[current]

                current += 1#add all non blank lines until next blank
        else:
            current += 1

    ###############################################################################




    ###############################################################################
    ####   REMOVE NOTTAIONS
    notation = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]', '[10]', '[11]', '[12]', '[Note 1]', '[Note 2]', '[Note 3]', '[Note 4]', '[Note 5]']
    valuecount = 0
        #REMOVE NOTTAIONS
    while valuecount < values.__len__():
        notationcount = 0
        while notationcount < notation.__len__():
            values[valuecount] = values[valuecount].replace(notation[notationcount], '')
            notationcount += 1
        valuecount += 1

    ##############################################################################



        ##############################################################################
#### this adds the data pulled from the color finding script and the link to the wiki page of the school

    if colors.__len__() > 0:
        if colors[0] != 'able' and colors[0] != '#cite':
            titles.append('primary')
            values.append(colors[0])
            if colors.__len__() > 1:
                titles.append('secondary')
                values.append(colors[1])
                if colors.__len__() > 2:
                    titles.append('tertiary')
                    values.append(colors[2])







    t, v = scrapeD1Locations(div1List, schoolname)
    titles.append(t)
    values.append(v)
    del t, v




                #######################
    url = 'http://en.wikipedia.org/wiki/' + schoolname          # should avoid redirects
    url = url.replace(' ', '_')
    url = url.replace('&', '%26')
    if url != None:
        titles.append('wiki')
        values.append(unidecode(url))
    titles.append('id')
    idkey = str(time.time())
    values.append(idkey)
    image = download_img(tab, schoolname)
    #print image
    append_value(img_125x, 'tm png125', titles, values)
    append_value(img_250x, 'tm png250', titles, values)
    #print(img_125x, img_250x)
    append_value(image, 'raw_logo', titles, values)
    append_value(team_link_logo, 'tm small logo', titles, values)
    #print(team_link_logo)

    # small logo

    ########################
###############################################################################

    if schoolname == 'Main Page':
        return
    append_value(facebook, 'uni facebook', titles, values)

    append_value(twitter, 'uni twitter', titles, values)


    titles, values = addLoc(titles, values, schoolname, university_contactlist)

    jsonout = wikijson(titles, values, idkey)
    return jsonout