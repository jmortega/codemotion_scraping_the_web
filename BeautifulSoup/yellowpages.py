# Web scraping exercise using BeautifulSoup in Python
'''
This is the example involved in the following YouTube tutorial:
    Scrape Websites with Python + Beautiful Soup 4 + Requests -- Coding with Python
    (https://www.youtube.com/watch?v=3xQTJi2tqgk&index=1&list=PLAT62XvLnSoUxedTIn5mydz3m6OnOq3X0)
'''
'''
- Data source: the first page of search result of "coffee" in "New York, NY"
  url: http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=New+York%2C+NY
- Objective: fetch the business name, address and phone number and display them
'''
import requests
from bs4 import BeautifulSoup

# connect the url
url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=New+York%2C+NY"
r = requests.get(url)
# get the content of the page using BeautifulSoup()
page = BeautifulSoup(r.content,"lxml")


# get the general data of the page
g_data = page.find_all("div", {"class": "info"})
counter = 0
for item in g_data:
    name = item.contents[0].find_all('a',{"class": "business-name"})[0].text
    try:
        street = item.contents[1].find_all('span',{"itemprop": "streetAddress"})[0].text
    except:
        pass

    try:
        city = item.contents[1].find_all('span',{"itemprop": "addressLocality"})[0].text.replace(",", "")
    except:
        pass
    try:
        region = item.contents[1].find_all('span',{"itemprop": "addressRegion"})[0].text
    except:
        pass

    try:
        postcode = item.contents[1].find_all('span',{"itemprop": "postalCode"})[0].text
    except:
       pass

    try:
       phone = item.contents[1].find_all("div", {"class": "primary"})[0].text
    except:
       pass
    counter += 1

    print("")# print an empty line to make the display look better
    print (counter)
    print ("Business Name: " + name)
    print ("Address: " + street + ", " + city +", " + region + " " + postcode)
    print ("Phone: " + phone)


# result display
# as we can see, the last one is not quite right(it is a copy of #30 without business name).
# the web scraping does not always work perfectly
'''
1
Business Name: Red Flame Coffee Shop
Address: 67 W 44th St, New York , NY 10036
Phone: (212) 869-3965

2
Business Name: Mon Petit Cafe
Address: 801 Lexington Ave # 1, New York , NY 10065
Phone: (212) 355-2233

3
Business Name: El Parador Cafe
Address: 325 E 34th St, New York , NY 10016
Phone: (212) 679-6812

4
Business Name: Cafe Boulud
Address: 20 E 76th St, New York , NY 10021
Phone: (212) 772-2600

5
Business Name: Podunk
Address: 231 E 5th St, New York , NY 10003
Phone: (212) 677-7722

6
Business Name: Local West
Address: 1 Penn Plz, New York , NY 10119
Phone: (212) 629-7070

7
Business Name: Macchiato Espresso Bar
Address: 141 E 44th St, New York , NY 10017
Phone: (212) 867-6772

8
Business Name: Champignon
Address: 200 7th Ave # 1, New York , NY 10011
Phone: (212) 929-3002

9
Business Name: Lugo Caffe
Address: 1 Penn Plz, New York , NY 10119
Phone: (212) 760-2700

10
Business Name: Aquavit
Address: 65 E 55th St, New York , NY 10022
Phone: (212) 307-7311

11
Business Name: Horus Kabab House
Address: 293 E 10th St, New York , NY 10009
Phone: (212) 228-4774

12
Business Name: Hurley's
Address: 232 W 48th St, New York , NY 10036
Phone: (212) 765-8981

13
Business Name: Ryan's Daughter
Address: 350 E 85th St, New York , NY 10028
Phone: (212) 628-2613

14
Business Name: Cafe Cluny
Address: 284 W 12th St, New York , NY 10014
Phone: (212) 255-6900

15
Business Name: Novecento
Address: 343 W Broadway, New York , NY 10013
Phone: (212) 925-4706

16
Business Name: Cafe Espanol On Carmine
Address: 78 Carmine St, New York , NY 10014
Phone: (212) 675-3312

17
Business Name: Raga
Address: 433 E 6th St, New York , NY 10009
Phone: (212) 388-0882

18
Business Name: Ground Support
Address: 399 W Broadway, New York , NY 10012
Phone: (212) 219-8722

19
Business Name: Ruby's Cafe & Bar
Address: 219 Mulberry St, New York , NY 10012
Phone: (212) 925-5755

20
Business Name: Cafe
Address: 496 9th Ave Frnt 1, New York , NY 10018
Phone: (212) 967-3892

21
Business Name: Luise
Address: 129 Rivington St, New York , NY 10002
Phone: (212) 673-5820

22
Business Name: Joe The Art Of Coffee
Address: 141 Waverly Pl, New York , NY 10014
Phone: (212) 924-6750

23
Business Name: Coffee Shop
Address: 29 Union Sq W, New York , NY 10003
Phone: (212) 243-7969

24
Business Name: Cafe Luxembourg
Address: 200 W 70th St, New York , NY 10023
Phone: (212) 873-7411

25
Business Name: 11th Street Cafe
Address: 327 W 11th St, New York , NY 10014
Phone: (212) 924-3804

26
Business Name: Cafe Evergreen
Address: 1288 1st Ave Frnt 1, New York , NY 10021
Phone: (212) 744-3266

27
Business Name: Cafe De Bruxelles
Address: 118 Greenwich Ave, New York , NY 10011
Phone: (212) 206-1830

28
Business Name: Shanghai Cafe
Address: 100 Mott St, New York , NY 10013
Phone: (212) 966-3988

29
Business Name: Starbucks Coffee
Address: 1460 Broadway, New York , NY 10036
Phone: (212) 869-0191

30
Business Name: Jack's Coffee
Address: 140 W 10th St, New York , NY 10014
Phone: (212) 929-0821

31
Business Name:
Address: 140 W 10th St, New York , NY 10014
Phone: (212) 929-0821
'''