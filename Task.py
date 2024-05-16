from selenium import webdriver # класс управления браузером
from selenium.webdriver.chrome.options import Options # Настройки
from selenium.webdriver.common.by import By # селекторы
from selenium.webdriver.support.ui import WebDriverWait # класс для ожидания
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import csv

driver = webdriver.Chrome()
driver.get("https://dzen.ru/")
news =[]
href = driver.find_element(By.XPATH, "//div[contains(@class, 'card-news-header-desktop__titleFloor-aO floor-title__titleWrapper-NF')]/a")
url = href.get_attribute("href")
driver.get(url)

'''rubric_names = []
rubric_names_list = driver.find_elements(By.XPATH, ".//h2/span[@aria-label]")
for rubric_name in rubric_names_list:
    rubric_names.append(rubric_name.text)
print(rubric_names)'''
data = []
n = 0
while True:
    try:
        rubric = driver.find_element(By.XPATH, f".//div[contains(@data-testid, 'rubric{n}')]")
        rubric_name0 = driver.find_element(By.XPATH, ".//*[@id='LayoutContentMicroRoot']/div[2]/div[2]/div/div[3]/h1")
        print(rubric_name0.text)
        rubric_name = driver.find_element(By.XPATH, f".//div[contains(@data-testid, 'rubric{n}')]/section/h2/span[@aria-label]")
        print(rubric_name.text)
        sources = driver.find_elements(By.XPATH, f".//div[contains(@data-testid, 'rubric{n}')]/section/article/div/div/article/div[2]/div/div/div[2]/div/span")
        links = driver.find_elements(By.XPATH, f".//div[contains(@data-testid, 'rubric{n}')]//section/article/div/div/article/div[2]/div[2]/a") # link
        titles = driver.find_elements(By.XPATH, f".//div[contains(@data-testid, 'rubric{n}')]//section/article/div/div/article/div[2]/div[2]/a/div") # title
        
        for i in range(len(sources)):
            rubric_dict = {}
            if i == 0:
                rubric_dict["rubric"] = rubric_name0.text
            else:    
                rubric_dict["rubric"] = rubric_name.text
            rubric_dict["source"] = sources[i].text
            rubric_dict["link"] = links[i].get_attribute("href")
            rubric_dict["title"] = titles[i].text
            print(rubric_dict.items())
            data.append(rubric_dict)
        
        other_links = driver.find_elements(By.XPATH, f".//div[contains(@data-testid, 'rubric{n}')]/section/article/div[2]/div/div[contains(@class, 'news-top-stories__other')]/div/a")
        other_titles = driver.find_elements(By.XPATH, f".//div[contains(@data-testid, 'rubric{n}')]/section/article/div[2]/div/div[contains(@class, 'news-top-stories__other')]/div/a/div/article/div/div/div[2]/div/span")
        for i in range(len(other_links)):
            rubric_dict = {}
            if i == 0:
                rubric_dict["rubric"] = rubric_name0.text
            else:    
                rubric_dict["rubric"] = rubric_name.text
            rubric_dict["source"] = 'other sorces'
            rubric_dict["link"] = f"https://dzen.ru{other_links[i].get_attribute('href')}"
            rubric_dict["title"] = other_titles[i].text
            data.append(rubric_dict)
        
        n += 1
    except:
        break

with open("news.csv", "w", newline='', encoding='utf-8')as f:
     writer = csv.DictWriter(f, fieldnames=["rubric", "source", "link", "title"])
     writer.writeheader()
     writer.writerows(data)

    

'''div_element = driver.find_element(By.XPATH, "//div [contains(@class, 'product-cards-layout__item without-border ng-star-inserted')]") # find the div element
print(div_element.text) # print the text of the div element
print(div_element.get_attribute("li")) # print the attribute "id" of the div element
'''

'''while True:
    products_list = driver.find_elements(By.XPATH, "//div[@class='quote']")
    for  quote_element in quote_elements:
        quote = quote_element.find_element(By.XPATH, ".//span[@class='text']").text
        author = quote_element.find_element(By.XPATH, ".//small[@class='author']").text
        quotes.append({"quote": quote, "author": author})

    next_button = driver.find_elements(By.XPATH, "//li[@class='next']/a")
    if not next_button:
        break
    else:
        next_button[0].click()

time.sleep(1)
driver.close()

for quote in quotes:
    print(quote['quote'], 'by', quote['author'])

with open("quotes.csv", "w", newline='', encoding='utf-8')as f:
     writer = csv.DictWriter(f, fieldnames=["quote", "author"])
     writer.writeheader()
     writer.writerows(quotes)'''