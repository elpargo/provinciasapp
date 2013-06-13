provinciasapp
=============

to install
----------

$ git clone git@github.com:elpargo/provinciasapp.git
$ cd provinciasapp
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r deploy/requirements.txt
#wait a bit

to run
------

$ python run.py (uses some mac-only stuff)
or 
$ gunicorn provinciasapp:app
