__author__ = 'Josue Carbonel'

import requests
from bs4 import BeautifulSoup


def finding_team_link_in(table_code):
    find_tr = (str(table_code).split('</tr>'))
    get_team_tr = []
    for index in range(0, len(find_tr)):
        if 'Nickname' in find_tr[index]:
            get_team_tr += [find_tr[index] + '\n']
            break
    if len(get_team_tr) > 0:
        get_team_in_tr = str(get_team_tr).split('\\n')
        team_name_code = get_team_in_tr[3]
        try:
            soup = BeautifulSoup(team_name_code)
            team_code = soup.find_all('a')
        except:
            pass
        for link in team_code:
            team_link = link.get('href')
            if 'wiki/' in team_link:
                return team_link
            else:
                team_link = ''
                return team_link


def find_team_img_link(table_code):
    team_link = finding_team_link_in(table_code)
    if team_link is None:
        team_link = ''
        return team_link
    else:
        link = 'http://en.wikipedia.org' + team_link
        html_content = requests.get(link).content
        soup = BeautifulSoup(html_content)
        table = soup.find_all('table', {'class': 'infobox vcard'})
        tm_table = ''
        for team_table in table:
            #print(team_table)
            tm_table = str(team_table)
            break
        #print(tm_table)
        find_my_image = BeautifulSoup(tm_table).find_all('img')
        for image_link in find_my_image:
            img_link = image_link.get('src')
            team_link = 'http:' + img_link
            return team_link