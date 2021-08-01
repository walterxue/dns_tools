from flask_script import Manager,Server
from IncrteCloudAPI import create_app

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    # app.config['SECRET_KEY'] = "test"
    manager.run()

frist
second
