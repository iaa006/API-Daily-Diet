from flask import Flask
from src.routes.meals_routes import meals_blueprint

app = Flask(__name__)
app.register_blueprint(meals_blueprint)

if __name__ == '__main__':
    app.run(debug=True)