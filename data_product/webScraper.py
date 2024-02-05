from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.amazon.com.mx/s?k=pc&ref=nb_sb_noss_2')

htmldoc = BeautifulSoup (page.text, 'html.parsecs')
