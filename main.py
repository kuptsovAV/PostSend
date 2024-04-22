from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/submit_number', methods=['POST'])
def submit_number():
    number = request.form['number']
    # Здесь будет ваша логика обработки номера
    return f'Вы ввели номер: {number}'

if __name__ == '__main__':
    app.run(debug=True)