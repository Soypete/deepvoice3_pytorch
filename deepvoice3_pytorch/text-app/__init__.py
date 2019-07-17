from flask import Flask, request, render_template

app = Flask(__name__)

try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text