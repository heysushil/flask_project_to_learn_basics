# Flask First Basic project to learn basic

In this project I'm learning the basic concepts of Flask Framework and write down the basic things like:

1. how to create vartual env
1. How to insall flask?
1. How to run flask
1. how to activate development mode

## how to create vartual env

working with creating vertual enviornment is good practice beacuse for that have few important points:

1. all setup and package realted fils only ristrict to this repository
1. when every share this to others will work because all related files are available
1. if vritual environment not created then all the realated packages and setups will storn on the main system directory which slow down the system.

for creating the virtual environment run this common on the directory where you want this:

        py -3 -m venv venv

>>>Note: here first venv is keyword and second venv is the name of directory of virtual envionment in which all the related packeds will store

## How to insall flask?

we install the falsk using pip package

        pip install flask

## How to run flask

when create the first flask python file and want to run that follow this:

        set FLASK_APP=hello
        flask run

>>>Note: by defaut it rungs on http://127.0.0.1:5000/ also on 1st line hello is the name of the flask app

## how to activate development mode

its good practice to set the development mode when working on the project and when want to make it public don't forget to set the production mode. Because on development mode we get all the problems with details which we don't want to show users thats why on public domain make the mode production will help to hide the any problem if occure.

        set FLASK_ENV=development
        flask run

>>>Note: here on 1st line set the enviornmetna and on 2nd line run the flask.

## For learning I followed these documentations: 

1. [Flask Main Documenation](https://flask.palletsprojects.com/en/2.1.x/)
1. [Flask Quick Start Documentation](https://flask.palletsprojects.com/en/2.1.x/quickstart/)

## After completing this I'll start working on ChatGPT Api Intigration using Flask and Python:

1. [ChatGPT API](https://platform.openai.com/docs/quickstart/build-your-application)
1. [ChatGPT Examples](https://platform.openai.com/examples/default-qa)
