from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'password'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/form_data', methods=['POST'])
def form_data():
    session['user_name'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_language'] = request.form['fav_lang']
    session['user_comment'] = request.form['comment']
    print(session['user_name'])
    print(session['user_location'])
    print(session['user_language'])
    print(session['user_comment'])
    return redirect('/results')

if __name__=="__main__":
    app.run(debug=True)