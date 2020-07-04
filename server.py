from flask import Flask, request, redirect, url_for, flash, render_template

app = Flask(__name__)
app.secret_key = 'nv'



@app.route('/')
def index():
    return render_template('bot.html')


@app.route('/start')
def start():
    return redirect('/')

@app.route('/stop')
def stop():
    return redirect('/')

app.run(host='0.0.0.0', port=4000 , debug=True)
