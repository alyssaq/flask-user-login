# Flask user login on Heroku

A sample user login system with [Flask](http://flask.pocoo.org/) and deployed on [Heroku](https://www.heroku.com/)

## Prerequisites

Install `pip`, `virtualenv`, `virtualenvwrapper`, `foreman`, [`heroku client`](http://devcenter.heroku.com/articles/using-the-cli), `libevent` (for `gevent` web server.)

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ sudo pip install virtualenvwrapper
    $ sudo gem install foreman heroku
    $ brew install libevent

## Usage

1. Clone the repo
1. Install requirements `pip install -r requirements.txt`

## Running

You can run the Flask application locally with python:

    $ python app.py

Or, use foreman:

    $ foreman start

You can also specify what port you'd prefer to use.

    $ foreman start -p 5555

## Deploying on Heroku
Create an account at [Heroku](https://api.heroku.com/signup)and [add your SSH key to
Heroku](http://devcenter.heroku.com/articles/quickstart).

Now, login, create your application and push to Heroku:

    $ heroku login
    $ heroku create app_name -s cedar
    $ git push heroku master
    $ heroku scale web=1

Verify that the application is up and running:

    $ heroku ps

View the application in our web browser:

    $ heroku open

## Custom Domains

If your account is verified -- and your credit card is on file -- you
can also easily add a custom domain to your application.

    $ heroku addons:add custom_domains
    $ heroku domains:add www.mydomainname.com

You can add a [naked domain
name](http://devcenter.heroku.com/articles/custom-domains), too.

    $ heroku domains:add mydomainname.com

Lastly, add the following A records to your DNS management tool.

    75.101.163.44
    75.101.145.87
    174.129.212.2

## License
[MIT](http://alyssaq.github.io/mit-license/)