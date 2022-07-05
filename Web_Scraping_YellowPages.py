import requests
from bs4 import BeautifulSoup
import pandas as pd
import Convert_to_Database as db


class scrapper():
    results = []

    def extract(self, url):

        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        r  = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        return soup.find_all('div', class_ = 'v-card')
    
    
    
    def transform(self, business_cards):

        business_cards = self.extract(f'https://www.yellowpages.com/search?search_terms=Real%20Estate%20Agents&geo_location_terms=Dallas%2C%20TX&page={page}')

        for item in business_cards:
            name = item.find('a', class_ = 'business-name').text
            
            try:
                address = item.find('div', class_ = 'adr').text
            except:
                address = ''
            

            try:
                ratings = item.find('a', class_ = 'rating').text
            except:
                ratings = ''
            
            try:
                website = item.find('a', class_ = 'track-visit-website')['href']
            except:
                website = ''
            
            try:
                telephone = item.find('div', class_ = 'phones phone primary').text
            except:
                telephone = ''
            
            try:
                YearsInBusiness = item.find('div', class_ = 'years-in-business').text
            except:
                YearsInBusiness = ''
            

            information = {
                'Name' : name,
                'Address' : address,
                'Ratings' : ratings,
                'Website' : website,
                'Telephone' : telephone,
                'YearsInBusiness' : YearsInBusiness
            }

            self.results.append(information)
        return

    def load(self):
            df = pd.DataFrame(self.results)
            df.to_csv('scrapped_data.csv')
            
            df.to_json(r'Scrapped_data.json', orient="index", indent=4)
            
            DB_creation = db.Create_DB()
            DB_creation.DB_Creation()


if __name__ == "__main__":
    scrape = scrapper()
    for page in range(1,10):
        try:
            soup = scrape.extract(f'https://www.yellowpages.com/search?search_terms=Real%20Estate%20Agents&geo_location_terms=Dallas%2C%20TX&page={page}')
            scrape.transform(soup)
            print(f'Scrapped Data From Page {page}')
        except:
            print(f'Error page {page}')

    scrape.load()

    print("Scrapped All Data")


