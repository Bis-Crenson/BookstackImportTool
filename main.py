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

#Function to find every single book, will be a limit of 500
def find_all_books():

    headers = {
      'Authorization': f'Token {cred["id"]}:{cred["secret"]}',
      'Content-Type': 'application/json'
    }

    book_name = []

    response = requests.request("GET", f"{cred['url']}/books", headers=headers, verify=False)  # Attempt creating the book
    book_dict = json.loads(response.text)  # Turns the response into a dictionary :D
   # print(response.text)
    for x in range(len(book_dict['data'])):  # Go through the entire dictionary
        book_name.append(book_dict['data'][x]['name'])  #Find every single book name
    return book_name


#Function to find every single book ID number, will be a limit of 500
def find_all_book_IDS():

    headers = {
      'Authorization': f'Token {cred["id"]}:{cred["secret"]}',
      'Content-Type': 'application/json'
    }

    book_IDS = []

    response = requests.request("GET", f"{cred['url']}/books", headers=headers, verify=False)  # Attempt creating the book
    book_dict = json.loads(response.text)  # Turns the response into a dictionary :D
   # print(response.text)
    for x in range(len(book_dict['data'])):  # Go through the entire dictionary
        book_IDS.append(book_dict['data'][x]['id']) #Get the ID of each book
    return book_IDS

#Function which will take in a book name and return its book ID
def find_specific_book_ID(book_name):

    headers = {
      'Authorization': f'Token {cred["id"]}:{cred["secret"]}',
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", f"{cred['url']}/books", headers=headers, verify=False)  # Attempt creating the book
    book_dict = json.loads(response.text)  # Turns the response into a dictionary :D
   # print(response.text)
    for x in range(len(book_dict['data'])):  # Go through the entire dictionary
        if book_dict['data'][x]['name'] == book_name: #Check to see if the book exists, if so, return its ID
            return book_dict['data'][x]['id'] #Break out of loop.
    return -1 #Error, no book ID find


#Function which will take in a book ID number and return its name
def find_specific_book(book_ID):

    headers = {
      'Authorization': f'Token {cred["id"]}:{cred["secret"]}',
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", f"{cred['url']}/books", headers=headers, verify=False)  # Attempt creating the book
    book_dict = json.loads(response.text)  # Turns the response into a dictionary :D
   # print(response.text)
    for x in range(len(book_dict['data'])):  # Go through the entire dictionary
        if book_dict['data'][x]['id'] == book_ID: #Check to see if the book exists, if so, return its ID
            return book_dict['data'][x]['name'] #Break out of loop.
    return "-1" #Error, no book ID find




#Testing purposes
print(find_all_books()) #List
print(find_all_book_IDS()) #List
print(find_specific_book_ID("Bob")) #100
print(find_specific_book_ID("Bobbbbb")) #-1
print(find_specific_book(100)) #Bob
print(find_specific_book(-1)) #"-1""

