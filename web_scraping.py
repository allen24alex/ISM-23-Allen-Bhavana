#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:54:07 2023

@author: allen
"""

import re
import json
import requests
from bs4 import BeautifulSoup

#def get_the_page_request(url):
    #html = requests.get(url).content
    #soup = BeautifulSoup(html,"html.parser")
    #return soup

url = ['https://www.1mg.com/drugs/bandy-plus-12-tablet-63485',
       'https://www.1mg.com/drugs/zifi-200-tablet-51344',
       'https://1mg.com/drugs/augmentin-625-duo-tablet-138629']




def download_json(url):
    u = 0
    if len(url) > 1:
        for link in url:
            html = requests.get(link).content
            soup = BeautifulSoup(html,"html.parser")
        
            sub_script = soup.find_all("script")
        
            parts = []
            for part in sub_script:
                if '@' in part.get_text():
                    tmp_text = part.get_text().replace(u'\xa0', u' ').replace('<BR>', ' ')
                    parts.append(tmp_text)
                    print(part.get_text())
                    print('\n-------------------\n')
        
            start_ = '\n    window.__INITIAL_STATE__ = '
            end_ = ';\n    window.__STATUS_CODE__ = null;'
     
            j_parts = parts
            for i in range(len(parts)):
                if start_ in parts[i]:
                    j_parts[i] = json.loads(parts[i].replace(start_,'').replace(end_,'').rstrip())
                else:
                    j_parts[i] = json.loads(parts[i])
            f = str(u+1)
            
    
            json.dump(j_parts,open(f'data_{f}.json', "w+"))
            
            u = u + 1
            
        
        
            
    else:
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
    
        sub_script = soup.find_all("script")
    
        parts = []
        for part in sub_script:
            if '@' in part.get_text():
                tmp_text = part.get_text().replace(u'\xa0', u' ').replace('<BR>', ' ')
                parts.append(tmp_text)
                print(part.get_text())
                print('\n-------------------\n')
    
        start_ = '\n    window.__INITIAL_STATE__ = '
        end_ = ';\n    window.__STATUS_CODE__ = null;'
 
        j_parts = parts
        for i in range(len(parts)):
            if start_ in parts[i]:
                j_parts[i] = json.loads(parts[i].replace(start_,'').replace(end_,'').rstrip())
            else:
                j_parts[i] = json.loads(parts[i])
    
        json.dump(j_parts,open(f'data_{f}.json', "w+"))
    
    return j_parts
download_json(url)

import xlsxwriter 

workbook= xlsxwriter.Workbook('Info_on_medicine.xlsx')
worksheet= workbook.add_worksheet('firstsheet')
worksheet.write(0,0,'#')
worksheet.write(0,1,'Information')


for p in range(len(url)):

    # Opening JSON file
    f = open(f'data_{p+1}.json')
    # returns JSON object as a dictionary
    data = json.load(f)

    final_data = data[2]

    keys = list(final_data.keys())

    worksheet.write(0,p+2,final_data['name'])


    i = 1
    for index in keys:
        if index == 'manufacturer':
            worksheet.write(i,0,str(i))
            worksheet.write(i,1,index)
            worksheet.write(i,p+2,final_data[index]['legalName'])
            i+= 1
            
        elif (index == 'name') or (index == 'proprietaryName') or (index =='availableStrength') or (index == 'doseSchedule'):
            i = i
        else:
            worksheet.write(i,0,str(i))
            worksheet.write(i,1,index)
            worksheet.write(i,p+2,str(final_data[index]))
            i+= 1

        
workbook.close()
    
