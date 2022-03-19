# Mission-to-Mars

## Purpose 

The purpose of this project is to use BeautifulSoup, Splinter, and Pandas to scrape webpages for data related to Mars. The results will display a webpage using MongoDB and Flask. 

## Breakdown of Process

* Scraping was done in Jupyter Notebook in the NASA Mars News website (https://redplanetscience.com/') for the title and text for most recent article. The results are stored in a variable to be referenced later in the results webpage. BeautifulSoup was used to parse through HTML and search for appropriate elements and classes.
* Secondly, the featured image from the Space Image-Mars website (https://spaceimages-mars.com) is scraped. BeautifulSoup was used as well again.  The result was stored in a variable again.
* Next, the images of all four Mars' hemispheres from GUSS website (https://marshemispheres.com) are scraped. This time, Find_by_CSS was used to find the relative elements and tags to scrape the image and their title to then display on the webpage.
*  A scraping function was created and the all of the results were stored as a dictionary and to be returned at the end of the function.
*  Another file. "app.py", is created to activate the scrape function and update the Mongo database with the results, and then return the results from the databases to the webpage. An instance of Flask was created and PyMongo was used to establish a connection to the MongoDB server. The flask page searches for records of data in the Mongo database with the index.html template to construct the layout.
* Finally, in the index.html, the /scrape route was linked to a button, which a user could click to initiate the scrape. The HTML also file also incorporates Bootstrap to format the results from the scrape.
