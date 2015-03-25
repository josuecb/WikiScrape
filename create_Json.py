from auxiliar_methods import *
from termcolor import *

def wikijson(wiki_titles, wiki_values, id_key):

    ImagesAth = {'tm small logo': '', 'tm svg logo': '', 'tm png125': '', 'tm png250': ''}
    ImagesUni = {'raw_logo': '', 'small logo': '', 'svg logo': '', 'png125': '', 'png250': ''}
    Images = {'favicon': '', 'athletics': ImagesAth, 'university': ImagesUni, 'campus': ''}

    Location = {'uni city': '', 'uni region': '', 'uni address 1': '', 'uni address 2': '', 'uni postalcode': '',
                'uni country': '', 'uni lat': '', 'uni long': ''}
    Names = {'nickname singular': '', 'nickname plural': ''}
    Contact  = {'uni phone': '', 'uni url': '', 'uni facebook': '', 'uni twitter': '', 'uni linkedin': ''}
    Motto = {'english': '', 'latin': ''}
    School = {'wiki': '', 'mascot': '', 'established': '', 'names': Names, 'location': Location, 'endowment': '',
              'contact': Contact, 'motto': Motto}

    Enrollment = {'undergraduate': '', 'postgraduate': ''}
    Athletics = {'conference': ''}
    ContactAlum = {'phone': '', 'url': '', 'facebook': '', 'twitter': '', 'linkedin': ''}
    LocationAlum = {'city': '', 'region': '', 'address 1': '', 'address 2': '', 'postalcode': '',
                    'country': '', 'lat': '', 'long': ''}
    Alumni = {'contact': ContactAlum, 'location': LocationAlum}
    Colors = {'primary': '', 'secondary': '', 'tertiary': ''}
    Schoolmain = {'name': '', 'id:': id_key, 'athletics': Athletics, 'enrollment': Enrollment,
                  'alumni': Alumni, 'school': School, 'colors': Colors, 'images': Images}

    Main = {id_key: Schoolmain}


    type_dict = type({})
    type_list = type([])

    global totalElements
    global depth
    totalElements = 0

    depth = 0

    def removeunused(dict):
        for name,value in dict.items():
            if type(value) != type_dict:
                if value == '':
                    del dict[name]
                elif type(value) == type_list:
                    if value.__len__() == 0:
                        del dict[name]
            else:
                if value.__len__() == 0:
                    del dict[name]
                else:
                    removeunused(dict[name])




    def removeempty(dict):
        for name,value in dict.items():
            if type(value) == type_dict:
                if value.__len__() == 0:
                    del dict[name]
                    return dict
                else:
                    dict[name] = removeempty(value)


    """
    def addfromwiki(wiki_titles, wiki_values, dict):#ignores alumni related entries:
        i = 0

        for title in wiki_titles:
            for key, values in dict.items():
                if key.find('alumni') == -1:
                    if type(values) == type_dict:
                        dict[key] = addfromwiki(wiki_titles, wiki_values, dict[key])
                        return key

                    elif key == title:
                        dict[key] = wiki_values[i]


                else:
                    print 'yes'

        print dict
        i += 1
    """


    def addfromwiki2(titles, values, dict):
        global totalElements
        global website
        for t, v in dict.items():
            if type(v) == type_dict:
                addfromwiki2(titles, values, dict[t])
            else:
                i = 0
                for title in titles:
                    if title == t:
                        totalElements += 1
                        dict[t] = values[i]
                    i += 1





    addfromwiki2(wiki_titles, wiki_values, Main)

    removeunused(Main)#im going to fix this and make it a part of an actual loop
    removeunused(Main)
    removeunused(Main)
    removeunused(Main)
    removeunused(Main)
    removeunused(Main)

    #old_key_list = ['tm small logo', 'tm svg logo', 'tm png125', 'tm png250']
    key_changer(ImagesAth, 'tm ')
    #print(ImagesAth)
    key_changer(Contact, 'uni ')
    #print(Contact)
    key_changer(Location, 'uni ')
    #print(Location)


    print colored('Total elements: ' + str(totalElements), 'cyan')
    if totalElements > 3:
        print Main
        return Main


    else:
        print Main
        return



