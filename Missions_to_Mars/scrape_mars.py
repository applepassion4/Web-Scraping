import pymongo
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# DB Setup

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_db
collection = db.mars 


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    collection.drop()

    # Nasa Mars news
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")
    slide_element = news_soup.select_one("ul.item_list li.slide")
    slide_element.find("div", class_="content_title")
    latest_news = slide_element.find("div", class_="content_title").get_text()
    latest_paragraph = slide_element.find("div", class_="article_teaser_body").get_text()

    # JPL Mars Space Images - Featured Image
    space_images_url = 'https://spaceimages-mars.com/'
    html = browser.html
    soup = bs(html, 'html.parser')
    browser.visit(space_images_url)
    time.sleep(2)
    relative_image_path = soup.find_all('img')[1]["src"]
    feature_img = space_images_url + relative_image_path
    feature_img


    # Mars Facts
    mars_facts_url = 'https://galaxyfacts-mars.com/'
    mars_df = pd.read_html(mars_facts_url, header=0)[0]
    mars_df
    mars_html = mars_df.to_html()


    # Mars Hemispheres
    astrogeology_link ='https://marshemispheres.com/'
    html = browser.html
    soup = bs(html, 'html.parser')
    browser.visit(astrogeology_link)
    time.sleep(2)
    hemisphere_image_urls = []
    results = soup.find_all('div', class_='item')


    for result in results:
        hemisphere_url = 'https://marshemispheres.com/'
        title = result.find('h3').text
        img_url = result.find('img')[0]['src']
    
        hemisphere_data = {
        "title": title,
        "img_url": img_url
    }
    
    hemisphere_image_urls.append(hemisphere_data)
    
    print('-----------------')
    print(title)
    print(img_url)
    
    #Image URLS capture
    hemisphere_image_urls   

    for result in results:
        print(result)
    results

    # Return results
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]