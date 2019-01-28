from flask import Flask
import urllib.request
application = Flask(__name__)

@application.route("/")
def hello():
    return (urllib.request.urlopen("http://www.stackoverflow.com").getcode()

if __name__ == "__main__":
    application.run()
