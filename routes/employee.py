from flask import Blueprint, request, redirect, url_for

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/employee_home")
def employee_list():
    return "Employee List"

@employee_bp.route("/employee/add")
def add_employee():
    return "Add Employee"

@employee_bp.route("/employee/update")
def update_employee():
    return "Update Employee"

@employee_bp.route("/employee/delete")
def delete_employee():
    return "Delete Employee"

@employee_bp.route("/employee/<int:id>")
def getEmployeebyId(id):
    return f"Employee : {id}"

@employee_bp.route("/employee/<int:id>/<string:name>")
def searchByNameId(id, name):
    return f"ID : {id} Name : {name}"

# query parameter : filtering/ sorting  ?

@employee_bp.route("/employee")
def displaySpecific():
    department = request.args.get("department")
    page = request.args.get("page")

    return f"Department : {department} Page : {page}"

@employee_bp.route("/employeeDepartment")
def gotodept():
    return redirect(url_for("department.departmentHome"))