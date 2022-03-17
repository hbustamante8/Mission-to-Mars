


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
#Initiate headless driver for deployment
#set executable path and set up the URL
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_paragraph = mars_news(browser)
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }
    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
# Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

# Searching for elements with specific combination of tag "div" + Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


#C onvert the browser html to a soup object and then quit the browser 
    html = browser.html
    news_soup = soup(html, 'html.parser')
    #Add try and except for error handling
    try:
#assign the title and summary text to variables we'll reference later. In the next empty cell, let's begin our scraping.
        slide_elem = news_soup.select_one('div.list_text')

#just get the text from this scarpe, extra HTML is not necessary. Use the parent element to find the first tag and save it.
        news_title = slide_elem.find('div', class_='content_title').get_text()
    
    except AttributeError:
        return None, None
#Use the parent element to find the paragrpah text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    return news_title,news_p

# ### Featured Images
def featured_image(browser):
    
# Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

# Find and click the full image button 
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


#Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html,'html.parser')
#Add try/except for error handling 
    try:
# Find the relative image url

        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    except AttributeError:
        return None

#Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

def mars_facts():

# Add try/except for error handling
    try:
      # use 'read_html" to scrape the facts table into a dataframe telling pandas to to only pull the first table it encounters from the HTML Tables
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    #Assign columns and set index of the dataframe 
    df.columns=['description','Mars','Earth']
    df.set_index('description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":
    #If running script, print scraped data
    print(scrape_all())








