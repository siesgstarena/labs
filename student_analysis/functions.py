import json
import numpy as np
import pandas as pd
from math import ceil
from sklearn.preprocessing import MultiLabelBinarizer
from nltk.stem import WordNetLemmatizer 
from plotly.offline import plot
import plotly.offline as py
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from plotly.graph_objs import *
import plotly
from heapq import nlargest 
# init_notebook_mode(connected=True) 

lemmatizer = WordNetLemmatizer() 
mlb = MultiLabelBinarizer()

def preprocess_problem(problems):
    temp1 = list()
    for x in problems['tags']:
        temp = list()
        for a in x:
            for z in a.split(","):
                temp.append(lemmatizer.lemmatize(z.lower().strip()))
        temp1.append(temp)
    problems["tags"] = temp1
    problems = problems.join(pd.DataFrame(mlb.fit_transform(problems["tags"]),
                              columns=mlb.classes_,index=problems.index))
    problems=problems.drop(['description', 'explainInput',
           'explainOutput', 'example', 'explanation', 'tags', 'outputFile',
           'inputFile', 'contestCode', 'createdAt', 'updatedAt', '__v',
           'constraints', ],axis=1)
    problems.points = problems.points.apply(lambda x : ceil(x/100))
    temp = list()
    for x in problems['_id']:
        temp.append(x['$oid'])
    problems['_id']=temp
    return problems

def get_submissions(email,users,problems,submissions):
    user_id = users.loc[users['email'] ==  email]['_id']
    # print(user_id)
    personal = submissions.loc[submissions['userId'] ==  user_id.values[0]].reset_index(drop=True)
    personal = personal.drop(['fileContent','output','createdAt','updatedAt', '__v', 'duringContest'],axis=1)
    for x1 in ['_id','userId','problemId','contestId']:
        temp = list()
        for x in personal[x1]:
            temp.append(x['$oid'])
        personal[x1]=temp
    return personal 

def get_graphs(personal,users,problems,submissions):
    trace0 = go.Pie(values = list(personal.status.value_counts().to_dict().values()),
                    labels  = list(personal.status.value_counts().to_dict().keys()),
                   title="Verdicts"
                   )
    data_verdict = [trace0]
    json_verdict = json.dumps(data_verdict,cls=plotly.utils.PlotlyJSONEncoder)
    personal_accepted = personal.loc[personal['status']=='Accepted']
    personal_merged = pd.merge(personal_accepted,preprocess_problem(problems),
        left_on="problemId",
         right_on="_id",
         how="left",
         copy=True
        )
    a = personal_merged.drop(['_id_x', 'userId', 'problemId', 'contestId', 'language', 'time',
           'memory', 'status', 'points_x', '_id_y', 'code', 'name'],axis=1)
    te=list()
    for diff in set(a.points_y):
        new = a.loc[a['points_y']==diff]
        temp = list()  
        for x in list(new.drop(['points_y'],axis=1).columns):
            try:
                temp.append(len(new)-new[x].value_counts().to_dict()[0])
            except:
                temp.append(new[x].value_counts().to_dict()[1])
        d = str("Difficulty " + str(diff))
        trace0 = go.Bar(x =list( new.drop(['points_y'],axis=1).columns ),y =temp,name=d)
        te.append(trace0)
    json_topics = json.dumps(te,cls=plotly.utils.PlotlyJSONEncoder)
    
    return personal_merged,json_verdict,json_topics

def get_topic_ratings(personal,users,problems,submissions):
    personal_merged = pd.merge(personal,preprocess_problem(problems),
        left_on="problemId",
         right_on="_id",
         how="left",
         copy=True
        )
    personal_topics = personal_merged.drop(['_id_x', 'userId', 'problemId', 'contestId', 'language', 'time',
            'memory', 'status', 'points_x', '_id_y', 'code', 'points_y', 'name'],axis=1)
    l = dict()
    unexp=list()
    for x in personal_topics.columns:
        count = personal_topics[x].loc[personal_topics[x]==1].count()
        if count!=0:
            l[x]= count
        else:
            unexp.append(x)
    srt = sorted(l, key=l.get)
    b=np.array_split(np.asarray(srt) , 2)
    return unexp,list(b[0]),list(b[1])

def n_high_submission(personal,problems,users,submissions):
    personal_submissions = pd.merge(personal,preprocess_problem(problems),
        left_on="problemId",
         right_on="_id",
         how="left",
         copy=True
        )
    
    submit_types = ['Compilation Error','Time Limit Exceeded', 'Runtime Error', 'Wrong Answer',  'Accepted']
    nHighest = nlargest(10, personal_submissions.code.value_counts().to_dict(),
                            key = personal_submissions.code.value_counts().to_dict().get) 
    l= dict()
    figures = list()
    for sub in submit_types:
        for val in nHighest: 
            submit_personal = personal_submissions.loc[personal_submissions["status"]==sub]
            
            l[val] = submit_personal.code.value_counts().to_dict().get(val)
            trace0 = go.Bar( x = list(l.keys()),y=list(l.values()),name=sub)
        figures.append(trace0)
    json_n_highest_submissions = json.dumps(figures,cls=plotly.utils.PlotlyJSONEncoder)
    return nHighest,json_n_highest_submissions

def get_user_details(users,email,problems,submissions):
    try:
        user_id = users.loc[users['email'] ==  email]['_id']
        data=list()
        user_info=users.loc[users['email']==email].to_dict()
        data.append( users.loc[users['email'] ==  email]['_id'])
        data.append( list(user_info['name'].values())[0])
        data.append( list(user_info['username'].values())[0])
        data.append( list(user_info['email'].values())[0])
        data.append( list(user_info['topics'].values())[0])
        data.append( set(submissions.loc[submissions['userId'] ==  user_id.values[0]].reset_index(drop=True)['language']))
        data.append( list(user_info['ratings'].values())[0])
        return data
    except:
        return 0

def get_recommendation(problems,unexp,good,personal_merged,best):
    p = preprocess_problem(problems)
    unexp_d=dict()
    if len(unexp) > 0:
        for tops in unexp:
            sums =  list(p.loc[p[tops]==1]['code'].to_dict().values())
            l=dict()

            for su in sums:
                l[su] = list(p.loc[p['code']==su]['points'].to_dict().values())[0]
            srt = sorted(l, key=l.get)
            unexp_d[tops]=srt[0:5]
    prac_d=dict()
    if len(good)>0:
        for tops in good:
            # print(tops)
            sums =  list(p.loc[p[tops]==1]['code'].to_dict().values())
            l=dict()

            for su in sums:
                l[su] = list(p.loc[p['code']==su]['points'].to_dict().values())[0]
            srt = sorted(l, key=l.get,reverse=True)
            srt = set(srt) - set(personal_merged['code'])
            srt = list(srt)
            if len(srt)>0:
                prac_d[tops]=srt[0:5]


    best_d=dict()
    if len(good)>0:
        for tops in good:
            # print(tops)
            sums =  list(p.loc[p[tops]==1]['code'].to_dict().values())
            l=dict()

            for su in sums:
                l[su] = list(p.loc[p['code']==su]['points'].to_dict().values())[0]
            srt = sorted(l, key=l.get,reverse=True)
            srt = set(srt) - set(personal_merged['code'])
            srt = list(srt)
            if len(srt)>0:
                best_d[tops]=srt[0:5]

    return unexp_d,prac_d,best_d
        