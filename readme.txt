APPLICATION THAT SHOWS CURRENT BITCOIN VALUE
Python version 3.5.2+

HOW TO RUN

1) Create virtualenv
2) Install requirements using: 'pip install -r requirements.txt'
3) Run 'python manage.py migrate' to create db
4) Run application using 'python manage.py runserver'
5) Run 'python manage.py getbitcoin' in different console to start downloading data into db


1. Basic information
Simple Python application using Django framework and SQLite database. 

2. Functionality
Application:
1) Connects with https://www.gdax.com/ API usig GDAX library,
2) Saves necessary data in database,
3) Displays data using JS and AJAX technology.

3. Application structure
- application is developed using MVT design pattern.
- database model is defined in bitcoin_app/models.py
- views handles all the requests are defined in bitcoin_app/views.py
- static files are located in bitcoin_app/static
- html templates are located in bitcoin_app/templates
- configuration settings are located in bitcoin/settings.py
- migrations are located in bitcoin_app/migrations
- in bitcoinDataManager there is logic responsible for getting data from the internet and erasing old data from database
- getbitcoin command from bitcoin_app/management/commands is responsible for for getting data from the internet and erasing old data from database using bitcoinDataManager. It should be running simultaneously with app. 
