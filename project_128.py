from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Proper name","Distance", "Mass", "Radius"]
    star_data = []

    soup = BeautifulSoup(browser.page_source,"html.parser")
    
    star_table = soup.find_all('table')

    table_rows = star_table[7].find_all('tr')

    for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            if index == 0:
                temp_list.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(td_tag.contents[0])
                except:
                    temp_list.append("")
        star_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()   
     

scrape()

for index, data in enumerate(star_data):
    new_star_data_element = new_star_data[index]
    new_star_data_element = [elem.replace("\n", "") for elem in new_star_data_element]
    new_star_data_element = new_star_data_element[:7]
    final_star_data.append(data + new_star_data_element)
with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_star_data)