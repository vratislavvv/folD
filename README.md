# General

## What is folD?
Personal finance manager, that helps you understand your current financial situation. folD includes features such as adding your expenses & incomes, or viewing them in a chart!

## The idea
I wanted to create something that would actually help me, and I alway found banking apps kinda complicated + I wasn't able to see expenses from multiple account in one graph.

# Pages

## Authentification
Login- used for logging in

Register- used for registering new user

## Myapp
Dashboard- displays everything, incomes, expenses, data in chart, savings & investments, balance, etc. 

Add expense- used for adding expenses and flushing them

Add earnings and assets- used for adding incomes, savings & investments and flushing them

Settings- used for logging out of the application and reseting data in application.

# Desing

## Logo
Picture I use as a logo was not made by me, it is a canva template which I liked a lot and you can find the creator [here](https://www.canva.com/p/cincin-emas/).

## Colors
As you might noticed, the colors are matching the logo. The process of selecting them was simple, I just took the color codes from the logo and created a gradient that is displayed in the background. Later on, I picked color codes from the gradient, and added them to the script that is creating the graph.

# Technical documentation

## Technologies
Application is built using Python framework Django, which covers the whole backend side.

On the other side, for front end, I decided to use classic HTML & CSS. Besides these two, I also used free open-source JavaScript library called Charts.js, which covers the big chart on the dashboard.

Every piece of data is stored in sqlite3 database that is automatically created for you when you create django project.

## Backend structure
To start off, in the code, there are three main important folders. First one called folD which represents the project folder called as project *folD*, and then 2 application folders. First application folder called *myapp*, and second one called *accessing*.

Project folder includes files which connect other applications with each other(paths for example) and very important file that called *settings.py* which customizes and cofigures the whole application.

Let's start with the *accessing*. This app has only one and single purpose, and that is authentification. It is much safer to handle authentification this way than having everything in a single app. The authentification system is handled by Django user authentification system.

*Myapp* is basically for everything else. This app manages everything related to folD AFTER you log in, from dashboard, through adding pages, to settings tab.

## Frontend structure

For frontend, I have *templates* folder in both *myapp* and *accessing* applications. In these folders I store extended versions of layouts(there are two layouts, one for each application) which are saved inside *myapp* templates folder (for both apps). This might seem a little messy, it is due to the fact that I wasn't sure at the beginning if I want to create a separate application for authentification.

When it comes to static files, there is a static folder used for storing all static files (images, stylesheets). Again, I would like to apologize to everyone, for the brutally messy stylesheet, this is something I will definitely have to work on. 

# Database structure
My database tables are divided into 2 categories. One for the main *myapp* application and the second one for the *accessing* application.

## Accessing tables
For the accessing tables, there is not much I have done on my own. Because of the fact that I am using Django user authentification system, the framework covered all of this for me and therefore, there was no need of creating any models.

## Myapp tables
In *myapp* application, there is five models that I have implemented.

Bank- Storing username to which every table is connected

BankEvent- model that stores every expense

Income- model that stores incomes

Savings- model that stores savings

Investments- model that stores investments

My main thought was to store the nickname in accessing model, but although I tried, I wasn't able to connect these tables. It would be more effective, because of the fact that I could have only 4 tables in *myapp* instead of 5.

**If you find some lines that doesn't make sense, it could be due to two thing.First is, that it may be something that I wanted to implement in the future. Second is, that I forgot line of a feature that was in the application, but I've decided to remove it. Feel free to contact me about this if you want.*