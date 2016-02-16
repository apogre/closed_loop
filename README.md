#Installation Guide

* Install Python 2.7 and set up environment variable as given in :[set env vars on windows] (http://www.aaronstannard.com/how-to-setup-a-proper-python-environment-on-windows/)
* Download pip : [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and install using command `python get-pip.py`
* Install virtualenv `pip install virtualenv`
* Install git from [git](http://git-scm.com/download/win)
* open git-bash and activate virtualenv
* install cookiecutter using `pip install cookiecutter`
* create repo using `cookiecutter https://github.com/JackStouffer/cookiecutter-Flask-Foundation.git`
* install sqlite3 from here [Sqlite3 installation guide windows](http://www.codeproject.com/Articles/850834/Installing-and-Using-SQLite-on-Windows)
* change dir to repo and install requirements `pip install -r requirements.txt`
* In `manage.py`, replace `app = create_app('pixelracer.settings.%sConfig' % env.capitalize(), env=env())` with `app = create_app('pixelracer.settings.%sConfig' % env.capitalize())`, save and close
* Now run command `python manage.py createdb` to createdb
* Run `python manage.py runserver` to start the server

