# Mission-to-Mars

## Purpose 

The purpose of this project is to use BeautifulSoup,Splinter, and Pandst to scrape webpages for data related to Mars. The result will display a webpage using MongoDB and Flask. 

## Breakdown of Process

* Scraping was done in Jupyter Notebok in the NASA Mars News websute for the title and text for most recent article. The results are stored in a variable to be referenced later on the results webpage. BeautifulSoup was used to parse through HTML and search for appropriate elements and classes.
* Secondly,another function is used to scrape the featured image from the Space Image-Mars website (https://spaceimages-mars.com) 
* The images of all four hemispheres of all fours Mars' hemispheres from GUSS website  (https://marshemispheres.com). Find_by_CSS was used to find the relative elements and tags to scapare the image and their title to then display on the webpage.
*  A scraping fucnction was created  and the all of the results were stored as a dictionary and to be returned at the end of the function.
*  Another file "app.py" is created to activate the scrape function and update the Mongo database with the results, and then return the results on the datasbase of on the webpage. An instance of Flask was created and PyMongo was used to establish a connection to the MongoDB server. The flask page searches for records of data in the Mongodatabase with the index.html template on the webpage 
* Finally, in the index.html, the /scrape route was linked to a button, which a user could click to initiate the scrape. The HTML also file also incoporates Bootstrap to format the results from the scrape.
