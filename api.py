from flask import Flask
app = Flask(__name__)
 
@app.route("/search=<query>")
def hello(query):
    return "200"
 
if __name__ == "__main__":
    app.run()