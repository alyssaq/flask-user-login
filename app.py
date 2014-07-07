"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',
                                          'this_should_be_configured')

@app.route('/')
def home():
  """Render website's home page."""
  return flask.render_template('home.html')


@app.route('/about/')
def about():
  """Render the website's about page."""
  return flask.render_template('about.html')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
  """Send your static text file."""
  file_dot_text = file_name + '.txt'
  return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
  """
  Add headers to both force latest IE rendering engine or Chrome Frame,
  and also to cache the rendered page for 10 minutes.
  """
  response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
  response.headers['Cache-Control'] = 'public, max-age=600'
  return response

@app.errorhandler(404)
def page_not_found(error):
  """Custom 404 page."""
  return flask.render_template('404.html'), 404

if __name__ == '__main__':
  app.run(debug=True)
