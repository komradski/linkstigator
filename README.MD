# README.MD

A project of tools for open source media analysis and research.

## How To's

## Initial Setup

- clone repository
- create virtualenv: `python3 -m virtualenv venv`
- activate virtualenv: `. venv/bin/activate`
- install requirements: `pip install -r requirements.txt`
- launch/preview the django project: `python manage.py runserver`

### Django Migrations

After data model changes in models.py, you must run the three step migration process for them to become active.

- makemigrations:
  - `python manage.py makemigrations sitesearch`
  - take note of the migration number (ex. 0001, 0002, 0003, etc.)
- sqlmigrate:
  - using the migration number you took note of above
  - `python manage.py sqlmigrate sitesearch 0001`  
- migrate:
  - `python manage.py migrate`

### Reset App Database

- `python manage.py reset appname`

### Admin Page Customization

- [realpython.com | Customize the Django Admin With Python](https://realpython.com/customize-django-admin-python/)

## Python Libraries Utilized or Planned

- [Neo4j for Django Developers](https://neo4j.com/developer-blog/neo4j-for-django-developers/)

- [Requests for Humans](https://docs.python-requests.org/en/latest/index.html)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup)
  - [soup cheatsheet](https://proxiesapi.com/articles/the-complete-beautifulsoup-cheatsheet-with-examples)
- [ua-generator | User-Agent Generator](https://pypi.org/project/ua-generator/)
- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Djoser Documentation | Web Token Authenticatin](https://djoser.readthedocs.io/en/latest/getting_started.html)
- [Django Bootstrap5](https://django-bootstrap5.readthedocs.io/en/latest/quickstart.html)
- [Django Packages](https://djangopackages.org)
  - [Django-Countries](https://pypi.org/project/django-countries/)
  - [Django-Cities](https://github.com/coderholic/django-cities)
  - [Django-Cities-Light](https://github.com/yourlabs/django-cities-light)

## Graph DB

### Reading Graph Meta Data
- [Open Graph Protocol](https://ogp.me/)
- [PyOpenGraph | Github](https://github.com/minichiello/PyOpenGraph)

### Graph DB engines
- [Neo4j](https://neo4j.com/)
  - [Neo4j Python Tutorial](https://www.datacamp.com/tutorial/neo4j-tutorial)
  - [Neo4j for Django Developers](https://neo4j.com/developer-blog/neo4j-for-django-developers/)
- [CogDB](https://cogdb.io/)


## Apps

## News Site & Additional Link Directory

### Model

- Organization
- Links organized by type:
  - Choices: website, youtube, rumble, odysee, socials, etc.

#### Meta (Models)

- [Model field reference](https://docs.djangoproject.com/en/5.1/ref/models/fields/)
- [Meta: unique_together](https://docs.djangoproject.com/en/dev/ref/models/options/#unique-together)

## News Site Search

- search multiple news sites simultaneously for the same search terms
- limits:
  - captcha protected search

### Model

- Links from News site search
- Search will add
  - additional search string
  - keyword search terms

## Dork Search

- Search Engine Advanced Search / User Interface for Dork Searches

- Search Candidates:
  - Google
  - Yandex
  - Bing

### Article Meta Unroller

- Input: Paste a news link
- Extract
- Store:
- Display:
- Process & Output: Extract meta information
  - Title
  - Meta
  - Citation links from main body of article
- Parent > Child Relationships between article and citation links
  - Article and Citation Links
- [text](https://www.aljazeera.com/news/2020/12/5/case-173-egypt-closes-decade-old-ngo-foreign-funding-case)
