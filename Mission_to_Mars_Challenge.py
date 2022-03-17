#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


#set executable path and set up the URL
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Searching for elements with specific combination of tag "div"Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


#set up html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


#assign the title and summary text to variables we'll reference later. In the next empty cell, let's begin our scraping.
slide_elem.find('div', class_='content_title')


# In[8]:


#just get the text from this scarpe, extra HTML is not necessary. Use t5he parent element to find the first tag and save it.
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[9]:


#Use the parent element to find the paragrpah text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


# Find and click the full image button 
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


#Parse the resulting html with soup
html = browser.html
img_soup = soup(html,'html.parser')


# In[13]:


# Find the relative image url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


#Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[15]:


#telling pandas to to only pull the first table it encounters from the HTML Tables
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description','Mars','Earth']
df.set_index('description', inplace=True)
df


# In[16]:


#convert our Dataframe back into HTML code to be used to add to a website or application
df.to_html()


# In[17]:


# shut down automated browser
browser.quit()


# In[18]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[21]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[22]:


slide_elem.find('div', class_='content_title')


# In[23]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[24]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[25]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[26]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[27]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[28]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[29]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# Mars Facts

# In[30]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[31]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[32]:


df.to_html()


# In[67]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[64]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.


# First, get a list of all of the hemispheres
links = browser.find_by_css('a.product-item img')
#Next, loop through those links, click the link, find the sample anchor, return the href
for i in range(len(links)):
    hemisphere = {}
       # We have to find the elements on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item img')[i].click()
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    # Get Hemisphere title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    
     # Finally, we navigate backwards
    browser.back()


# In[81]:


#using beautiful soup
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in range(4):
    
# First, get a list of all of the hemispheres
    browser.find_by_tag('h3')[i].click()

    # Empty dictionary
    hemisphere = {}

    # html browser 
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    hemi_soup


    # Get image link
    image_url = hemi_soup.find('div',class_="downloads").find('a').get("href")
    hemisphere["image_url"] = url + image_url

    # Get title text 
    title = hemi_soup.find('h2',class_="title").text
    hemisphere["title"] = title

    hemisphere_image_urls.append(hemisphere)

    browser.back()


# In[82]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:


# 5. Quit the browser
browser.quit()

