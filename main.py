from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

    <html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form method="post">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0">
        <br>            
        <textarea name="text"></textarea>
        <br>
        <input type="submit" value="Submit Form">
    </form>
    </body>
    </html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form.get("rot"))
    text = request.form.get("text")
    text = rotate_string(text, rot)
    return "<h1>{}</h1>".format(text)

app.run()