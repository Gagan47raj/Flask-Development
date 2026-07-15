from flask import Blueprint #for declaring file as a routing 

home_bp = Blueprint("home", __name__)

@home_bp.route("/home")
def home():
    return "Welcome to first blueprint of flask"

@home_bp.route("/about")
def about():
    return "About Us"

# create employee.py 
# department.py
# auth.py

# make it as blueprint
# create api : viewEmployee : return list of user name in string