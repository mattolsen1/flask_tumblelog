from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
"""
app.config["MONGODB_DB"] = "my_tumble_log"
app.config["MONGODB_USERNAME"] = "molsen"
app.config["MONGODB_PASSWORD"] = "shauna"
app.config["MONGODB_HOST"] = "linus.mongohq.com"
app.config["MONGODB_PORT"] = "10038"
#app.config["MONGODB_SETTINGS"] = {"DB": "my_tumble_log"}
#app.config["MONGODB_SETTINGS"] = {'DB': "mongodb://molsen:shauna@linus.mongohq.com:10038/my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
"""
app.config["MONGODB_DB"] = "app12893270"
app.config["MONGODB_USERNAME"] = "molsen"
app.config["MONGODB_PASSWORD"] = "shauna"
app.config["MONGODB_HOST"] = "linus.mongohq.com"
app.config["MONGODB_PORT"] = "10056"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
