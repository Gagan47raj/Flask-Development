from flask import Blueprint

department_bp = Blueprint("department", __name__)

@department_bp.route("/department")
def departmentHome():
    return "<h1>Department Page<h1>"