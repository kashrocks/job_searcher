import xlrd
import requests
from bs4 import BeautifulSoup
import os

cwd = os.getcwd()
in_lever = 0

workbook = xlrd.open_workbook(cwd + '/job_search.xlsx')
sheet = workbook.sheet_by_name('Sheet1')

for i in range(1, 46):
    company = sheet.cell(i, 0).value
    url = 'https://jobs.lever.co/' + company
    response = requests.get(url)
    if response.status_code != 200:
        continue

    in_lever += 1

    soup = BeautifulSoup(response.text, "html.parser")
    b = soup.findAll('h5')

    print('')
    print(company + '---------------------------')

    for title in b:
        if title != 'source':
            continue
        if 'intern' in title.next_element.lower():
            print(title.next_element)

print('')
print('Total companies in lever: ' + str(in_lever))
