from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Pipeline last check"

if __name__ == "__main__":
   server.run(host='0.0.0.0')
