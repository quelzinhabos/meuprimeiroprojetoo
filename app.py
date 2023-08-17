from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        
        return f"Dados recebidos: Nome - {nome}, Email - {email}"

if __name__ == '__main__':
    app.run(debug=True)
