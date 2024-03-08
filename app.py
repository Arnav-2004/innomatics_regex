from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('result.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        is_valid = re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None
        return render_template('validate_email.html', email=email, is_valid=is_valid)
    else:
        return render_template('validate_email.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
