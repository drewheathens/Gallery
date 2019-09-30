# GALLERY
Photography keeps memories alive.

## DESCRIPTION
Gallery is an app that allows user(s) to upload photos, view them, search by category name, get their storage locations and if need be copy on clipboard.

## USAGE & INSTALLATION
- visit https://galerey.herokuapp.com/
- Clone the repository
- create virtual environment by running
1. python3.6 -m venv --without-pip virtual
2. source virtual/bin/activate
3. curl https://bootstrap.pypa.io/get-pip.py | python
- navigate to psql in terminal and create a database called galleryapp and set password by username# **\password**.
- exit by username# **\q**
- **python manage.py makemigrations photos**
- **python manage.py migrate** (to apply changes)
- in terminal run
**python3.6 manage.py runserver**

## BDD
|BEHAVIOUR|INPUT|OUTPUT|
|---------|-----|------|
|view large size|click on photo|larger version displayed|
|copy on clipboard|click on photo|click on copy button|
|search by category|category name|photos in that category| 
## TECHNOLOGIES USED
- Git
- Heroku
- Django
- Bootsrap
- postgresql
## PROJECT STATUS

The project is still under development

## CONTRIBUTION

When contributing to this repository, please first discuss the change you wish to make via issue.
contact me at mudavadie@gmail.com


## LICENSE

MIT License

Copyright (c) 2019 drewheathens

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.