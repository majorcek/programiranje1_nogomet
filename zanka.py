from pobiranje_podatkov import *

for i in range(1,11):
    text = download_url_to_string('https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1&page={0})'.format(i))
    save_string_to_file(text, os.getcwd(), 'prestopi{0}.html'.format(i))
    ads = ads_from_file(os.getcwd(), 'prestopi{0}.html'.format(i))
    write_cat_ads_to_csv(ads, os.getcwd(), 'prestopi{0}.csv'.format(i))
    
import csv
koncni_file = open("koncna.csv","a")
for line in open("prestopi1.csv"):
    koncni_file.write(line)

for num in range(2,11):
    datoteka = "prestopi"+str(num)+".csv"
    with open(datoteka) as nova:
        f = nova
        next(f) # skip the header
        for line in f:
            koncni_file.write(line)
koncni_file.close()
for stevec in range(1,11):
    os.remove('prestopi{0}.csv'.format(stevec))
    os.remove('prestopi{0}.html'.format(stevec))
