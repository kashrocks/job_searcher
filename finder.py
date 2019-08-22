import xlrd
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

cwd = os.getcwd()
in_lever = 0

workbook = xlrd.open_workbook(cwd + '/job_search.xlsx')
sheet = workbook.sheet_by_name('Sheet1') 

has_position = []
for i in range(1, 1280):
    company = sheet.cell(i, 0).value
    url = 'https://jobs.lever.co/' + company
    response = requests.get(url)
    if response.status_code != 200:
        continue

    in_lever += 1

    soup = BeautifulSoup(response.text, "html.parser")
    b = soup.findAll('h5')

    print('')
    print(company + ' ---------------------------' + str(i))
    has_position_flg = False
    for title in b:
        if title == 'source':
            continue
        if 'intern' in title.next_element.lower() and 'international' not in title.next_element.lower() and 'internal' not in title.next_element.lower(): 
            has_position_flg = True
            print(title.next_element)
    if has_position_flg:
        has_position.append(url)

for url in has_position:
    print(url)

print(len(has_position))

# -----------------------------------
# hits all companies and checks whether a lever plat form exists or not

# def good_comp(comp):
#     with open('good_comps.txt', 'a') as f:
#         f.write("%s\n" % comp)

# def bad_comp(comp):
#     with open('bad_comps.txt', 'a') as f:
#         f.write("\n" + comp)

# cols = ['name','domain','year founded','industry','size range','locality','country','linkedin url','current employee estimate','total employee estimate']
# data = pd.read_csv('free_pdl_company_dataset.csv', names=cols)
# names = data.name.tolist()
# print("")
# print('Finished retrieving names, finding one word companies:')
# print('')

# eligible = []
# for comp in names:
#     if isinstance(comp, str): 
#         if ' ' not in comp:
#             eligible.append(comp)

# print("")
# print('Finished retrieving one word names, starting tests:')
# print('')

# total = len(eligible)
# use_lever = []
# no_lever = []
# i = 0
# for comp in eligible:
#     i += 1

#     url = 'https://jobs.lever.co/' + comp
#     response = requests.get(url)
#     if response.status_code != 200:
#         print("Tested " + comp + " was not good. " + str(i) + '/ ' + str(total))
#         bad_comp(comp)
#         print(response.status_code)
#         continue
#     good_comp(comp)
#     print(" ")
#     print("Tested " + comp + " was GOOD. " + str(i) + '/ ' + str(total))
#     print(" ")
