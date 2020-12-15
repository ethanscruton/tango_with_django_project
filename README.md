# Tango With Django Project
The main idea of the project is a website that allows users to register to the site, add/like categories, and add webpage links to each category.  
This project was put together with the help of the tutorial book [Tango With Django](https://www.tangowithdjango.com/).

# Motivation
I wanted to learn how to create both the backend and frontend aspect of a website. I chose Django as the framework because Python was my most familiar programming language.

# Screenshot examples
Index page:  
![Index](https://pasteboard.co/JEWR0xc.png)

Category page:
![Category](https://pasteboard.co/JEXlQNg.png)

Add category page:
![Add Category](https://pasteboard.co/JEXlCDx.png)

Add page:
![Add Page](https://pasteboard.co/JEXmwha.png)

Register:
![Register](https://pasteboard.co/JEXmRe8.png)

# Installation
The website is currently hosted at ethanscruton.pythonanywhere.com. However, the deployment site I am using requires me to log in every three months.  

If the website listed above is expired, you can run the site by using the instructions listed below.  

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ethanscruton/tango_with_django_project.git
$ cd tango_with_django_project
```

Install packages for creating a virtual environment:
```sh
$ pip install virtualenv
$ pip install virtualenvwrapper
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ mkvirtualenv rango
$ workon rango
```

Then install the dependencies:

```sh
(rango)$ pip install -r requirements.txt
```
Note the `(rango)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(rango)$ python populate_rango.py
(rango)$ python manage.py runserver
```

Enter [http://127.0.0.1:8000/](http://127.0.0.1:8000/) into your web browser to view the site.

# Built with
* Django
* HTML
* Bootstrap
* AJAX/JQuery
