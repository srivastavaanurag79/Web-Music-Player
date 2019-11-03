# Music Player Web App
This website scrapes through different free music websites and allows users to listen to their favorite musics. I have used the URL provided in TASK 2.

Goal:
  * Scrape as many websites as possible and provide an ultimate API

Hardware Requirements:
  Ram: 4GB
  Processor: Core i5

Software Reqiurements:
- Operating System: Ubuntu
- Frontend: HTML, CSS, Javascript
- Backend: Python-Django
- Database: Sqlite

## Installation
Install requirements: `pip install -r requirement.txt`


## Run Server Locally
open terminal
Change directory to the project folder;
* `python manage.py import_from_json_file`(this command is used to add songs in database using JSON file)
or
* `python manage.py import_from_url`(this command is used to add songs in database using URL)
* `python manage.py runserver`
* Go to: `localhost:8000` or at http://127.0.0.1:8000/


1. The JSON file containing the song list and URL is stored inside the folder hplay/resources/import_from_json_file.
2. If yo want to change the URl of the song list Go to: hplay/management/commands/import_from_url, edit IMPORT_URL to the required URL.
