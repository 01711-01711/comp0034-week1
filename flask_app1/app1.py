# Import the Flask class from the Flask library
from flask import Flask

# Create an instance of a Flask application
# The first argument is the name of the application’s module or package. __name__ is a convenient shortcut.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)


# Add a route for the 'home' page
# use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def hello_world():
    # The function returns the message we want to display in the user’s browser. The default content type is HTML,
    # so HTML in the string will be rendered by the browser.
    return 'Hello World!'


# Run the app
if __name__ == '__main__':
    app.run()
    # For any other port just put 'port=5001' inside brackets like app.run(port=5001) so the server would become 'http://127.0.0.1:5001'


# Running using Flask:
# (base) mateuszzawila@MacBook-Pro-3 tutorials python % source .venv/bin/activate
# (.venv) (base) mateuszzawila@MacBook-Pro-3 tutorials python % export FLASK_APP=comp0034-week1/flask_app1/app1
# (.venv) (base) mateuszzawila@MacBook-Pro-3 tutorials python % export FLASK_ENV=development
# (.venv) (base) mateuszzawila@MacBook-Pro-3 tutorials python % flask run
    # or flask --app comp0034-week1/flask_app1/app1.py run --debug
# ... will be running now ...
# after closing with CTRL+C: (.venv) (base) mateuszzawila@MacBook-Pro-3 tutorials python % deactivate

# Running using Python:
# (base) mateuszzawila@MacBook-Pro-3 tutorials python %  python comp0034-week1/flask_app1/app1.py

