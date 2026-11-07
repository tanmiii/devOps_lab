from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    Class=request.form['Class']
    
    return render_template(
        'successful.html',
        name=name,
        Class=Class
    )

if __name__ == '__main__':
    app.run(debug=True)
