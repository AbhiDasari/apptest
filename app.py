from flask import Flask

# initialize our Flask application
app= Flask(__name__)

@app.route("/hello", methods=["GET"])


def hello():
    return "Hello World!"

@app.route("/class/name", methods=["GET"])
def name():
    return "This is CS446! This is Dasari's server!"

#  main thread of execution to start the server
if __name__=='__main__':
    app.run( host="54.215.216.213",port="8888")
