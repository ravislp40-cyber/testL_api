from flask import Flask, jsonify
import requests

app = Flask(__name__)

POSTS_API = "https://jsonplaceholder.typicode.com/posts"
COMMENTS_API = "https://jsonplaceholder.typicode.com/comments"
ALBUMS_API = "https://jsonplaceholder.typicode.com/albums"


# Posts JSON
@app.route('/posts')
def posts():
    data = requests.get(POSTS_API).json()
    return jsonify(data)


# Comments JSON
@app.route('/comments')
def comments():
    data = requests.get(COMMENTS_API).json()
    return jsonify(data)


# Albums JSON
@app.route('/albums')
def albums():
    data = requests.get(ALBUMS_API).json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
