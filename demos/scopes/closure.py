from flask import jsonify, Flask, Response

def main() -> None:
    app = Flask(__name__)


    @app.route("/")
    def hello_world() -> Response:
        return jsonify({"message": "hello, world!"})


    app.run(port=8080)

if __name__ == "__main__":
    main()