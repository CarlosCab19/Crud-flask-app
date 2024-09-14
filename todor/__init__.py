from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    #Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolisto.db"
    )

    #Inicializamos nuestra conexion a nuestra bd
    db.init_app(app)

    #Registrar Bluprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app