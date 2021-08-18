'''
Git Token
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
'''

import re
from flask import Flask, render_template,request
from werkzeug.utils import redirect
from werkzeug.wrappers import response
from surveys import Question, Survey,satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'



response = []
@app.route('/')
def homepage():
    response.clear()
    return  render_template('base.html',survey=satisfaction_survey,response=response);


@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html',survey=satisfaction_survey)


@app.route('/questions/<num>')
def next_quest(num):
    question = len(response)
    if question < len(satisfaction_survey.questions):
        return render_template('question.html',survey=satisfaction_survey,response = question)
    if question == len(satisfaction_survey.questions):
        return redirect('/goodbye')


@app.route("/answer", methods = ["GET","POST"])
def log_answer():
    
    response.append(request.args.get('choice'))
    return redirect(f'/questions/{len(response)+1}')
