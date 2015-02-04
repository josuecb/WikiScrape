
def wikijson(wikititles, wikivalues, idkey):

    Location = {'city': '', 'region': '', 'address 1': '', 'address 2': '', 'postalcode': '',
                'country': '', 'lat': '', 'long': ''}
    LocationAlum = Location

    Contact = {'phone': '', 'url': '', 'facebook': '', 'twitter': '', 'linkedin': ''}
    ContactAlum = Contact

    ImagesAth = {'small logo': '', 'svg logo': '', 'png125': '', 'png250': ''}
    ImagesUni = {'raw_logo': '', 'small logo': '', 'svg logo': '', 'png125': '', 'png250': ''}
    Images = {'favicon': '', 'athletics': ImagesAth, 'university': ImagesUni, 'campus': ''}
    Motto = {'english': '', 'latin': ''}

    Names = {'nickname singular': '', 'nickname plural': ''}

    Colors = {'primary': '', 'secondary': '', 'tertiary': ''}

    Enrollment = {'undergraduate': '', 'postgraduate': ''}

    Alumni = {'contact': ContactAlum, 'location': LocationAlum}
    Athletics = {'conference': ''}

    School = {'wiki': '', 'mascot': '', 'established': '', 'names': Names, 'location': Location,
              'contact': Contact, 'motto': Motto}

    Schoolmain = {'name': '', 'id:': idkey, 'athletics': Athletics, 'enrollment': Enrollment,
                  'alumni': Alumni, 'school': School, 'colors': Colors, 'images': Images}

    Main = {idkey : Schoolmain}







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



    def addfromwiki(wikititles, wikivalues, dict):#ignores alumni related entries:
        i = 0

        for title in wikititles:
            for key, values in dict.items():
                if key.find('alumni') == -1:
                    if type(values) == type_dict:
                        dict[key] = addfromwiki(wikititles, wikivalues, dict[key])
                        return key

                    elif key == title:
                        dict[key] = wikivalues[i]


                else:
                    print 'yes'

        print dict
        i += 1



    def addfromwiki2(titles, values, dict):
        global totalElements
        for t,v in dict.items():
            if type(v) == type_dict and t.find('alumni') == -1:
                addfromwiki2(titles, values, dict[t])
            else:
                i = 0
                for title in titles:
                    if title == t:
                        totalElements += 1

                        dict[t] = values[i]
                    i += 1




















    addfromwiki2(wikititles, wikivalues, Main)

    removeunused(Main)#im going to fix this and make it a part of an actual loop
    removeunused(Main)
    removeunused(Main)
    removeunused(Main)
    removeunused(Main)
    removeunused(Main)
















    print totalElements
    if totalElements > 4:
        print Main
        return Main


    else:
        print Main
        return



