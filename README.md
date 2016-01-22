# WikiScrape
This Scripts were supposed to be unique all together to be automatized in any server and grap a huge JSON file so you can manage this data with just running it in your server.

This scripts, has many tools to scrape different kinds of universities in the US
This scripts, uses a predetermined text file where it says a list of all University in the US.

it'll scrape the information table that appears in the right side of the wikipedia page.
info scraped:

year created
team name
former names
mottos
type
endowment
president
academic staff
students
undergradruates
location
campus
colors
image logo
website

and more, 
# More Tools
This scrape has the ability to scrape the facebook and twitter from different resources as well.
It Has the ability to scrape the logo of each university and team of them in the US.

I will make another Version soon so you can have more capability to manage each field or grab only the field you need.

# Run WikiUniScrape.py

# Output
A Json File called 'NCAA_json.json':
output: 
`
{
    "1453503777.33": {
        "school": {
            "wiki": "http://en.wikipedia.org/wiki/[",
            "established": "1906",
            "contact": {
                "url": "www.acu.edu",
                "twitter": "http://www.twitter.com/acusports",
                "facebook": "http://www.facebook.com/ACUsports"
            },
            "names": {
                "nickname plural": "Wildcats"
            },
            "endowment": "$374 million",
            "mascot": "Willie the Wildcat"
        },
        "id:": "1453503777.33",
        "name": "[",
        "images": {
            "athletics": {
                "png125": "http://i.imgur.com/7m1brpq.png",
                "small logo": "http://upload.wikimedia.org/wikipedia/en/thumb/9/95/Abilene_Christian_Wildcats_Primary_Logo.png/200px-Abilene_Christian_Wildcats_Primary_Logo.png"
            },
            "university": {
                "raw_logo": "http://upload.wikimedia.org/wikipedia/en/thumb/3/36/AcuSeal.png/200px-AcuSeal.png"
            }
        },
        "colors": {
            "primary": "#461D7C",
            "secondary": "#FFFFFF"
        },
        "athletics": {
            "conference": "NCAA Division I - Southland"
        }
    }
`
