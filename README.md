provinciasapp
=============

to install
----------

``` bash
$ git clone git@github.com:elpargo/provinciasapp.git
$ cd provinciasapp
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r deploy/requirements.txt
#wait for the dependencies to download and install
```

to run
------

``` bash
$ python run.py (uses some mac-only stuff)
```
or 
```bash
$ gunicorn provinciasapp:app
```
