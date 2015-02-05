colors = {'white' : '#FFFFFF', 'silver' : '#C0C0C0', 'gray' : '#808080', 'crimson' : '#DC143C', 'orange' : '#FFA500',
          'black' : '#000000', 'red' : '#FF0000', 'green' : '#008000', 'maroon' : '#800000',
          'blue' : '#0000FF', 'purple' : '#800080', 'gold' : '#FFD700', 'yellow' : '#FFFF00', 'teal' : '#008080',
          'aqua' : '#00FFFF', 'lime' : '#00FF00', 'olive' : '#808000', 'navy' : '#000080', 'fuchsia' : '#FF00FF'}
from webcolors import name_to_hex






def checkforcolor3(string):
    try:
        hex = name_to_hex(string)
        return 1, hex
    except:
        return 0, 0






def checkforcolor2(string, index):

    colorname = ''
    if string[index] == ':':
        while string[index] != ';':
            if string[index].isalpha():
                colorname += string[index]
            index += 1
        try:
            hex = name_to_hex(colorname)
        except:
            return 0, 0, 0
        return 1, hex, index
    else:
        return 0, 0, 0




def checkforcolor(string, index):
    for col, hex in colors.items():
        if index < string.__len__() + col.__len__():
            if string[index : index + col.__len__()].lower() == col:
                return 1, hex, col.__len__()
    return 0, 0, 0


