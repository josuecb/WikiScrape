def remove_p(strg):

    newstrg = ''
    inside = False
    for ch in strg:
        if ch == '(':
            inside = True
        if inside == False:
            newstrg += ch

        if ch == ')':
            inside = False



    return newstrg



