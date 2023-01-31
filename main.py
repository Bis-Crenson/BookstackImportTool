#Bookstack Importer Tool

import re
import time
import requests
import json
import os, glob

f = open('cred.json') #Open the JSON file which stores your credentials
cred = json.load(f) #Load the JSON data
#print(cred['url']) #Use url, id, and secret for future API calls

"""
Read and get functions of the importer tool
Things such as get book name, ID #, all books, all chapters.etc
There will be a limit of 500, this is a API issue
"""
def find_all_books():

    headers = {
      'Authorization': f'Token {cred["id"]}:{cred["secret"]}',
      'Content-Type': 'application/json'
    }

    book_name = []

    response = requests.request("GET", f"{cred['url']}/books", headers=headers, verify=False)  # Attempt creating the book
    book_dict = json.loads(response.text)  # Turns the response into a dictionary :D
   # print(response.text)
    for x in range(len(book_dict['data'])):  # Go through the entire dictionary and search for a name
        book_name.append(book_dict['data'][x]['name'])
    return book_name

print(find_all_books())

