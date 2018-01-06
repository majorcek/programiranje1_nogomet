import requests
import re
import os
import csv


########################################################################
# First, let's write some functions to get the data from the web.
########################################################################

# define the URL of the main page of the bolha cats listing
prestopi_frontpage_url1 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=1'
prestopi_frontpage_url2 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=2'
prestopi_frontpage_url3 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=3'
prestopi_frontpage_url4 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=4'
prestopi_frontpage_url5 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=5'
prestopi_frontpage_url6 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=6'
prestopi_frontpage_url7 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=7'
prestopi_frontpage_url8 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=8'
prestopi_frontpage_url9 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=9'
prestopi_frontpage_url10 = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page=10'

# the directory to which we save our data
prestopi_directory1 = 'prestopi'

# the filename we use to save the frontpage
frontpage_filename1 = 'prestopi1.html'
frontpage_filename2 = 'prestopi2.html'
frontpage_filename3 = 'prestopi3.html'
frontpage_filename4 = 'prestopi4.html'
frontpage_filename5 = 'prestopi5.html'
frontpage_filename6 = 'prestopi6.html'
frontpage_filename7 = 'prestopi7.html'
frontpage_filename8 = 'prestopi8.html'
frontpage_filename9 = 'prestopi9.html'
frontpage_filename10 = 'prestopi10.html'

# the filename for the CSV file for the extracted data
csv_filename1 = 'prestopi1.csv'
csv_filename2 = 'prestopi2.csv'
csv_filename3 = 'prestopi3.csv'
csv_filename4 = 'prestopi4.csv'
csv_filename5 = 'prestopi5.csv'
csv_filename6 = 'prestopi6.csv'
csv_filename7 = 'prestopi7.csv'
csv_filename8 = 'prestopi8.csv'
csv_filename9 = 'prestopi9.csv'
csv_filename10 = 'prestopi10.csv'

def download_url_to_string(url):
    '''This function takes a URL as argument and tries to download it
    using requests. Upon success, it returns the page contents as string.'''
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36'
    url = url
    try:
        # some code here that may raise an exception
        r = s.get(url)
        # some more code that won't be run if the exception occured
    except requests.exceptions.ConnectionError:
        # some error handling / recovery code here
        # we may just display an informative message and quit
        print("failed to connect to url " + url)
        return
    # continue with the non-exceptional code
    if r.status_code == requests.codes.ok:
        return r.text
    print("failed to download url " + url)
    return


def save_string_to_file(text, directory, filename):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    print(os.getcwd())
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding = 'utf-8') as file_out:
        file_out.write(text)
    return None

def save_frontpage():
    '''Save "cats_frontpage_url" to the file "cat_directory"/"frontpage_filename"'''
    text = download_url_to_string(prestopi_frontpage_url2)
    #print(text)
    save_string_to_file(text, os.getcwd(), frontpage_filename2)
    return None

def read_file_to_string(directory, filename):
    '''Return the contents of the file "directory"/"filename" as a string.
    '''
    path = os.path.join(directory, filename)
    print(path)
    #file = open(filename, encoding="utf8")
    with open(path, 'r', encoding="utf8") as file_in:
        return file_in.read()

def page_to_ads(page):
    '''Split "page" to a list of advertisement blocks.'''
    rx = re.compile(r'<tr class(.*?)</td></tr>',
                    re.DOTALL)
    players = re.findall(rx, page)
    #print(players)
    return players

def vrni(players):
    stevec = 0
    while stevec <= 24:
        print(stevec + 1)
        print(get_dict_from_ad_block(players[stevec]))
        stevec += 1
        
def get_dict_from_ad_block(block):
    '''Build a dictionary containing the name, description and price of an ad block.'''
    rx = re.compile(r'title="(?P<ime>.*?)"'
                    r'.*?<td>(?P<pozicija>.*?)</td>'
                    r'.*?class="zentriert">(?P<starost>.*?)<'
                    r'.*?;plus=1">(?P<sezona>.*?)</'
                    r'.*? title="(?P<Država>.*?)"'
                    r'.*?class="vereinprofil_tooltip".*?" alt="(?P<klub1>.*?)"'
                    r'.*?title="(?P<liga1>.*?)"'
                    r'.*?img src=.*?" alt="(?P<klub2>.*?)"'
                    r'.*?title="(?P<liga2>.*?)"'
                    r'.*?transfers/spieler.*?>(?P<cena>.*?)<',
                    re.DOTALL)
    data = re.search(rx, block)
    ad_dict = data.groupdict()
    return ad_dict

def ads_from_file(directory, filename):
    '''Parse the ads in filename/directory into a dictionary list.'''
    page = read_file_to_string(directory, filename)
    blocks = page_to_ads(page)
    ads = [get_dict_from_ad_block(block) for block in blocks]
    return ads

def ads_frontpage():
    return ads_from_file(os.getcwd(), frontpage_filename2)

########################################################################
# We processed the data, now let's save it for later.
########################################################################

def write_csv(fieldnames, rows, directory, filename):
    '''Write a csv file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.
    '''
    #fieldnames = ['ime','pozicija', 'starost', 'sezona', 'Država', 'klub1', 'liga1', 'klub2', 'liga2', 'cena']
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w',encoding = 'cp1252') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None


# Write a function that takes a non-empty list of cat advertisement
# dictionaries and writes it to a csv file. The fieldnames can be read off the
# dictionary.
def write_cat_ads_to_csv(ads, directory, filename):
    #'''Write a csv file containing one ad from "ads" on each row.'''
    write_csv(ads[0].keys(), ads, directory, filename)

def write_cat_csv(ads):
    #'''Save "ads" to "cat_directory"/"csv_filename"'''
    #write_cat_ads_to_csv(ads, prestopi_directory1, csv_filename)
    write_cat_ads_to_csv(ads, os.getcwd(), csv_filename3)



#save_frontpage()
#ts = read_file_to_string(os.getcwd(), frontpage_filename1)
#ads = page_to_ads(ts)
