from flask import Flask

from routes.home import home_bp
from routes.employee import employee_bp
from routes.department import department_bp

app = Flask(__name__) #to mention current file is the main file

app.register_blueprint(home_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(department_bp)

if __name__ == "__main__":
    app.run(debug=True)