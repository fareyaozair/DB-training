from flask import Flask
from routes import initiatise_routes

# create a flask object (micro web service framework) with name of module
app = Flask(__name__)

initiatise_routes(app)

if __name__ == "__main__":
    app.run(debug=True)