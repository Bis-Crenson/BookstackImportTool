#Bookstack Importer Tool

# import re
import time
import requests
import json
import os, glob
from bs4 import BeautifulSoup #For parsing through img tags and just HTML
import base64 #Used for encoding images
# import aspose.words as aw #Used for converting txt to html

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
      'Content-Type': 'application/json',
    }

    response = requests.request("GET", f"{cred['url']}/books?count=500", headers=headers, verify=False)  # Attempt creating the book
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



"""
Import Scripts
"""
#This code will import a specific HTML file into a bookstack book of your choosing
def import_html_into_book(html_file_path, name_of_page, book_name):
    payload = json.dumps({
        "name": name_of_page, #Name of your lovely file
        "book_id": int(find_specific_book_ID(book_name)),  #Convert to an int
        "html": HTML_SRC_parse(open(html_file_path, 'r', encoding='utf-8').read())  # Insert HTML here
    })
    headers = {
        'Authorization': f'Token {cred["id"]}:{cred["secret"]}',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", f'{cred["url"]}/pages', headers=headers, data=payload, verify=False) #Attempt creation of the page

#For multiple uploads, you can use this function with a for loop and a directory loop.
# os.chdir(rf'C:PATH')
# for file in glob.glob("*.html"): #Traverse files in directory, file will be the name of every file.
# For multiple uploads, you can use this function with a directory loop.
def import_html_directory_into_book(directory_path, book_name):
    os.chdir(directory_path) #Change the current directory path
    for filename in glob.glob("*.html"): #Go through each file in a given directory that has a HTML tag
        payload = json.dumps({
            "name": filename.replace(".html", ""),  # Name of your lovely file, remove the html tag from the name
            "book_id": int(find_specific_book_ID(book_name)),  # Convert to an int
            "html": HTML_SRC_parse(open(rf"{directory_path}\{filename}", 'r', encoding='utf-8').read())  # Insert HTML here
        })
        headers = {
            'Authorization': f'Token {cred["id"]}:{cred["secret"]}',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", f'{cred["url"]}/pages', headers=headers, data=payload,
                                    verify=False)  # Attempt creation of the page

#This is a function which will parse through a given HTML file for each src tag and replace the image with BASE64
#This will return a new HTML file/
def HTML_SRC_parse(html_file):
    soup = BeautifulSoup(html_file, features="html.parser") #Insert the HTML here
    for img in soup.findAll('img'): #Go through each img tag
        if "http" not in img['src'] and "data:image" not in img['src']: #If this isn't a website link or base64, go ahead
            with open(img['src'], 'rb') as rb_image: #Open image as binary image
                img['src'] = f"data:image/png;base64,{base64.b64encode(rb_image.read()).decode('utf-8')}" #Convert!
    new_html = str(soup) #New file
    print(new_html)
    return new_html


#Testing purposes
# print(find_all_books()) #List
# print(find_all_book_IDS()) #List
# print(find_specific_book_ID("Chris Playground")) #100
# print(find_specific_book_ID("Bobbbbb")) #-1
# print(find_specific_book(100)) #Bob
# print(find_specific_book(-1)) #"-1""
#import_html_into_book(r"C:\Users\chris\Documents\BookstackTesting\test3image.html", "test page", "Chris Playground") #Page uploaded
#import_html_directory_into_book(r"C:\Users\chris\Documents\BookstackTesting", "Chris Playground") #Page uploaded
#HTML_SRC_parse(open(r"C:\Users\chris\Documents\BookstackTesting\test3image.html", 'r', encoding='utf-8').read())

