# Welcome to What's up, Doc? (Bugs, Bugs, Bugs!)

Django is the most popular Python web framework for making user-facing applications. This is an a new application using django that helps track bugs and manage tickets. It requires logging in, and you can't create an account if your not logged in, you'll have to figure it out. It shows tickets sorted by status, lets you create, edit, assign and do all sorts of things. Check it out!


### Created BY
Kash Farhadi

## Running the Application

Fork, Clone, Navigate to directory
Create and start a a virtual environment

for pipenv:
`pipenv install`

`pipenv shell`

`python manage.py makemigrations {foldername}` 
(where foldername is the top level folder for this project)

`python manage.py migrate`

Create an admin account (superuser) if you would like to test admin features and access the admin page. Easily create users and objects from the built in django visual interface

`python manage.py createsuperuser`

Finally start the django server using: 
`python manage.py runserver`

Access the homepage at 
`http://127.0.0.1:8000/` 
`http://localhost:8000/`

Admin page
`http://127.0.0.1:8000/admin` 
`http://localhost:8000/admin`


##### Built using Python 3.8 and the latest version of Django (2.1.2 as of this writing)
