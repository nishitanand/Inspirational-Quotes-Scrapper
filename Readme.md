<h1>Inspirational Quotes Scrapper</h1>

This Program is an Web Scrapper which is used to download and save inspirational quotes from the website [passiton.com](https://www.passiton.com/inspirational-quotes) . You can then use these qoutes to motivate yourself and send them to your family and friends also.

First user inputs what name he/she wants to give to the file where these quotes are saved. It then uses BeautifulSoup library and Requests library and does Web Scrapping on the website from the URL of the website.

It finds the top results from the website and then it writes the quotes to the file using file handling. 

To use it, first write this command in the command line

pip install -r requirements.txt

or (for Mac)

pip3 install -r requirements.txt

and then to run the file write

python Inspirational-Quotes-Scrapper.py

or (for Mac)

python3 Inspirational-Quotes-Scrapper.py


The downloaded quotes will be saved in the folder named "Inspirational_Quotes"
