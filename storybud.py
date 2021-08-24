from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return jsonify('Story Bud?')


if __name__ == '__main__':
    app.run()
