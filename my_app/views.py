


def configure(app):
    @app.route("/")
    def hello():
        return "Hello World"

    
