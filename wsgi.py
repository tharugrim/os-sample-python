from flask import Flask
import urllib
application = Flask(__name__)

@application.route("/")
def hello():
    return urllib.urlopen("http://www.stackoverflow.com").getcode()

if __name__ == "__main__":
    application.run()
