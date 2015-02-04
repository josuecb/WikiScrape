__author__ = 'Anonymous'


import requests
from unidecode import unidecode



def download_img(tables, titles):
    #info_box_file = open("box_file_code.txt", "w")      # Temp File to scrape
    #info_box_file.write(str(tables))
    file_box = tables
    image_code = file_box.find_all('img')

    #image_links = open("Images_links.txt", "a")
    for img in image_code:
        title = ''
        try:
            title_text = file_box.find_all('th')
            for title in title_text:
                title = unidecode(title.text)
                break
            # Fixed
            raw_title = title
            raw_title = raw_title.replace('\n', ' ')
            raw_title = raw_title.replace("'", '')
            raw_title = raw_title.replace("`", '')
            img_url = img.get("src").split()
            image_url = "http:" + img_url[0]

            return str((image_url))
            image_links.write(image_url)
        except:
            title_text = file_box.find_all('th')
            for title in title_text:
                title = unidecode(title.get_text())
                break
            # Fixed new_line
            raw_title = title
            raw_title = raw_title.replace('\n', ' ')
            raw_title = raw_title.replace("'", '')
            raw_title = raw_title.replace("`", '')
            img_url = img.get("src")
            image_url = "http:" + str(img_url)        # Converts into an url

            return str((image_url))
            image_links.write(image_url)
        break   # We want just ONE

    #info_box_file.close()
    return





