#required liberaries

Django==3.2.7 'pip install django'
django-import-export==2.6.1'pip install django-import-export'

The project uses default dbqlite as backend 
All the html files are in template folder
The startic folder contains all the images, css and js files
Urls are wrtten in Dashboard/urls.py
The basic structure of directory is:

-->dashboar_assignment📂<br />
|<br />
|->dashboard<br />
    &nbsp;&nbsp;|->migrations<br />
        |->0001_initial.py<br />
        |->0002_alter_datamodel.py<br />
    |->__init__.py
    |->admin.py
    |->apps.py
    |->models.py
    |->urls.py
    |->tests.py
    |->views.py
|->dashboar_assignment
    |->__init__.py
    |->asgi.py
    |->settings.py
    |->urls.py
    |->wsgi.py
|->static
    |->img
        |->contact_bg_1.jpg
        |->1635411046048.jpg
        |->d0.jpg       
    |->css
        |->home.css
    |->js
        |->home.js
|->templates
        |->home.html
        |->login.html
|->manage.py
|->db.sqlite3

