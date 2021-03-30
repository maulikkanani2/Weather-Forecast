# Weather Forecast App

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/maulikkanani2/Weather-Forecast.git 
$ cd Weather_report
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate(Ubuntu)
.\env\Scripts\activate(Windows)
```

Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd weather_report
(env)$ cd project
(env)$ python3 manage.py makemigrations
(env)$ python3 manage.py migrate
(env)$ python3 manage.py runserver
```
And navigate to `http://127.0.0.1:8000/data/api`.

