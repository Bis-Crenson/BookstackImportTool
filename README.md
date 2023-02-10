# BookstackImportTool
A tool used to interface with the Bookstack API which will allow users to import HTML files along with other Bookstack features. 
You'll need an account on Bookstacks which will be able to access to API. 
Once you have an account with API access, you'll want your client ID and Secret since this will be used with your API. You'll also need 
your bookstack website link. Such as https://bookstack.NAMEHERE.internal/api/
All 3 of these will be used in a JSON file. <br>
If you need help, watch this Youtube chapter(https://youtu.be/nEaRvJNLI7M?t=332) about setting up the API token, the JSON file is located in the respository 

**REQUIREMENTS** <br>
Python 3.6+ <br>
pip install json  <br>


**Current Features:**<br>
Return all book names in your Bookstack Collection<br>
Return all book IDs in your Bookstack Collection<br>
Return a specific book ID with a given book name in your Bookstack Collection<br>
Return a specific book name with a given book ID in your Bookstack Collection<br>
Import a html page with a given import path<br>
import all HTML pages within a directory to a specific book<br>
Every import will have their local images carry over<br>

Just use any of the functions included once you get the credentials needed for the tool to work. I'll add more over time! <br>
