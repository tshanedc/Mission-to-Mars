#!/usr/bin/env python
# coding: utf-8


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)



# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()




df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# # Deliverable 1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres




# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'

browser.visit(url)



# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
list1 = []
list2 = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
img_soup = soup(html, 'html.parser')
links = []


print(img_soup.find_all('a', class_ ='itemLink'))

#hemisphere_image_urls = img_soup.find('img', class_='thumb').get('src')
for link_tag in img_soup.find_all('a', class_ ='itemLink'):
    links.append(link_tag.get('href'))
links = list(set(links))
links.remove('#')

for link in links:
    hemispheres = {}
    img_url = f'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/{link}'
    browser.visit(img_url)
    html = browser.html
    link_soup = soup(html, 'html.parser')
    #image_url = link_soup.find('img', class_ = 'wide-image').get('src')
    image_url = link_soup.find('a', href = True, text = 'Sample' ).get('href')
    full_image_url = f'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/{image_url}'
    page_title = link_soup.find('h2', class_ = 'title').text
    hemispheres['img_url'] = full_image_url
    hemispheres['title'] = page_title
    hemisphere_image_urls.append(hemispheres)


# 4. Print the list that holds the dictionary of each image url and title.
print(hemisphere_image_urls)


# 5. Quit the browser
browser.quit()

