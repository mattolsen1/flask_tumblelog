A Flask Tumblelog
=================

This Tumblelog uses the Flask web framework, Mongohq (hosted mongodb) for the backend and Heroku for application hosting.

Installation & Setup
----------------------
Setup Virtual Env:

      pip install virtualenv
      virtualenv myproject
      source myproject/bin/activate


Install needed items:
* pip install flask
* pip install flask-script
* pip install WTForms
* pip install mongoengine
* pip install flask_mongoengine



Run the tumblelog:
* python manage.py runserver
* Goto: [http://localhost:5000](http://localhost:5000)

Technology Used
----------------
* Heroku:  Web Hosting for Flask app https://www.devcenter.heroku.com/articles/python
* Mongohq:  Backend for the project http://www.mongohq.com/
* Flask:  Web Framework http://www.flask.pocoo.org/
* MongoEngine:  Document-Object Mapper http://mongoengine.org/

Running Version
-----------------
http://secure-mountain-3922.herokuapp.com/
