from flask import Flask, render_template,request, url_for, redirect
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import functions

with open('data/users.json', 'r', errors='ignore') as f:
        data = json.load(f)
users = pd.DataFrame(data)
with open('data/problems.json', 'r', errors='ignore') as f:
        data = json.load(f)
problems = pd.DataFrame(data)

with open('data/submissions.json', 'r', errors='ignore') as f:
        data = json.load(f)
submissions = pd.DataFrame(data)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('email.html')

@app.route('/email', methods = ['GET', 'POST'])
def email():
    email = str(request.form['email'])
    user_info = functions.get_user_details(users,email,problems,submissions)
    if user_info==0:
            status= "Not Found in DB"
            return render_template("email.html",status=status)
    personal = functions.get_submissions(email,users,problems,submissions)
    num_sub=len(personal)
    personal_merged,json_verdict,json_topics = functions.get_graphs(personal,users,problems,submissions)
    bad,good,best = functions.get_topic_ratings(personal,users,problems,submissions)
    nHighest,json_n_highest_submissions = functions.n_high_submission(personal,problems,users,submissions)

    unexplored_d,practice_d ,best_d= functions.get_recommendation(problems,bad,good,personal_merged,best) 

    return render_template("index.html",
        json_verdict=json_verdict,
        json_topics=json_topics,
        good=good,bad=bad,best=best,
        user_info=user_info,
        json_n_highest_submissions=json_n_highest_submissions,
        num_sub=num_sub,
        nHighest=nHighest,
        unexplored_d=unexplored_d,
        practice_d=practice_d,
        best_d=best_d
        )


if __name__ == '__main__':
    app.run(debug=True)