# Taberystwyth
![alt text](https://codeship.com/projects/1084e7d0-7371-0133-b38a-7e06a486d05b/status?branch=master "Build Status")

Taberystwyth: Open source, testable tabbing program.

# Requirements
* Python 2.7.10
* Django 1.8.6
* Sqlite3 3.8.5

# Running
* Install the requirements
* Set up the database with `./manage.py migrate`
* From inside the project directory, run `./manage.py runserver`

# Testing
* From inside the project directory, run `./manage.py test`
* To run some manual tests, you can generate some fake data with `./manage.py seed_db`