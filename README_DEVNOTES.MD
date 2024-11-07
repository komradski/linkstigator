# Development Notes

## Django Project Creation Steps

- Create Virtual Environment: `python -m virtualenv venv`
- Activate Virtual Environment
  - Windows/Powershell: `venv\Scripts\activate.ps1`
  - Linux/Bash: `. venv/bin/activate`
- Install Django: `python -m pip install Django`
- Create Project: `django-admin startproject config linkstigator`

### Run your Server

- `python manage.py runserver`

### Create the site-search app

- `python manage.py startapp sitesearch`

## Examples

### Django User Auth

- [Using the Django authentication system | djangoproject.com](https://docs.djangoproject.com/en/5.1/topics/auth/default/)
- [Login-Logout Tutorials](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

### Link-Tree Clones

- [Django | Pylos7 | linktree-clone](https://github.com/Pylos7/linktree-clone)
- [Complete Linktree Clone with Django and React JS (Full Tutorial) | Django | ReactJs | Tailwind CSS](https://www.youtube.com/watch?v=9eXf2X9LuyU)
  - [Github | DevDhira | Linktree Clone](https://github.com/DevDhira/linktree-clone)

- [Flask | Linktree-Clone](https://github.com/ruantmelo/linktree-clone)

<!-- 
The following paths are ignored by one of your .gitignore files:
account/__pycache__
account/migrations/__pycache__
config/__pycache__
sitesearch/__pycache__
sitesearch/migrations/__pycache__
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false" -->
