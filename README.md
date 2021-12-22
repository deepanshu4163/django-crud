=====
CRUD
=====

A simple crud (Django based) application where user can add a data to the database, select a particular data
from the database, update the selected data and delete that particular data from the database.

Quick start
-----------

1. Add "myapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'myapp',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('myapp.urls')),

3. Run ``python manage.py migrate`` to create the Person models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/myapp/ to start creating, updating and deleting data.