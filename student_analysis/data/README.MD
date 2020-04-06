## Data Structure for files

### Users

```json
[
    {
        "_id":{"$oid":"5b5c89298114180020d4bcb0"},
        "notifications":{
            "updates":true,
            "activities":true
            },
        "name":"User Name",
        "username":"username",
        "email":"email@siesgst.ac.in",
        "about":"about",
        "ratings":0.0,
        "createdAt":{"$date":"2018-07-28T15:18:01.849Z"},
        "updatedAt":{"$date":"2019-01-29T06:23:34.352Z"},
        "__v":0,
        "topics":["graphs","dp","geometry","webdev","ml","dl","android","opensource"]
    }
]
```


### Submissions

```json
[
    {
        "_id":{"$oid":"5b608157e228ec0020a1fcf5"},
        "userId":{"$oid":"5b5d756037392f89933e7514"},
        "problemId":{"$oid":"5b5c8cd7276e2200208fed62"},
        "contestId":{"$oid":"5b5c89ef30db8a0020962414"},
        "language":"C++14",
        "fileContent":"fileContentURL",
        "time":"0s",
        "memory":"3452KB",
        "output":"outputURL",
        "status":"Accepted",
        "points":0,
        "createdAt":{"$date":"2018-07-31T15:33:43.362Z"},
        "updatedAt":{"$date":"2018-11-11T11:51:18.721Z"},
        "__v":0,
        "duringContest":true
    }
]

```

### Problems

```json
[
    {
        "_id":{"$oid":"5b5c8cd7276e2200208fed62"},
        "code":"UNI01",
        "points":0,
        "name":"Problem Name",
        "description":"Problem Description",
        "explainInput":"Input Explain",
        "explainOutput":"Output Explain",
        "example":"Input Data Output Data",
        "explanation":"",
        "tags":["adhoc"],
        "outputFile":"outputFileURL",
        "inputFile":"inputFileURL",
        "contestCode":"UNIVERSE",
        "createdAt":{"$date":"2018-07-28T15:33:43.03Z"},
        "updatedAt":{"$date":"2018-11-11T14:18:53.641Z"},
        "__v":0,
        "constraints":"ConstraintData"
    }
]
```