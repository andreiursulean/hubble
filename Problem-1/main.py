import requests
from bs4 import BeautifulSoup


vgm_url = 'https://www.formulastudent.de/academy/20200829-waymo/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
