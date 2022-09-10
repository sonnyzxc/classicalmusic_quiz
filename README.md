# classicalstream
test your knowledge on classical music through the bot :D

Setup Virtual Environment
```
python3 -m venv venv
```

Install Packages
```
pip install discord.py
pip install django
pip install djangorestframework
```

Add <b>'rest_framework'</b> to <b>INSTALLED_APPS</b> in <b>setting.py</b>
```
INSTALLED_APPS = [
   ...
   'rest_framework',
]

Run Server (cd to main folder)
```
python3 manage.py runserver
```
