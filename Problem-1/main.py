import requests
from bs4 import BeautifulSoup


print('Program starting...')
# get html text and parse it in BeautifulSoup object
fsg_url = 'https://www.formulastudent.de/academy/20200829-waymo/'
html_text = requests.get(fsg_url).text
soup = BeautifulSoup(html_text, 'html.parser')

# find our table in the document
team_table = soup.find('table', class_="overview")
# print(team_table) # For debugging
# get all table rows with teams
team_rows = team_table.tbody.find_all('tr')
# print(team_rows) # For debugging

# open file
f = open("teams.csv", 'w', encoding="utf-8")
# iterate over the rows set and get required info
for row in team_rows:
    # print(row)
    team_data = row.find_all('td')
    # print(team_data)
    team_name = team_data[0].a.string
    category = team_data[5].string
    country = team_data[3].string
    city = team_data[2].string
    university = team_data[1].string
    # get homepage
    team_link = 'https://www.formulastudent.de/{}'.format(team_data[0].a.get('href'))
    team_page_htext = requests.get(team_link).text
    team_bs = BeautifulSoup(team_page_htext, 'html.parser')    
    homepage = team_bs.tbody.find_all('tr')[1].td.string

    # write to file    
    f.write('{},{},{},{},{},{}\n'.format(team_name, category, \
    country, city, university, homepage))
    
# close file
f.close()

print('Done')