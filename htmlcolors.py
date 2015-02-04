colors = {'white' : '#FFFFFF', 'silver' : '#C0C0C0', 'gray' : '#808080',
          'black' : '#000000', 'red' : '#FF0000', 'green' : '#008000', 'maroon' : '#800000',
          'blue' : '#0000FF', 'purple' : '#800080', 'gold' : '#FFD700', 'yellow' : '#FFFF00'}

def checkforcolor(string, index):
    for col, hex in colors.items():
        if index < string.__len__() + col.__len__():
            if string[index : index + col.__len__()] == col:
                return 1, hex, col.__len__()
    return 0, 0, 0