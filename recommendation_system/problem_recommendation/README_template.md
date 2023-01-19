## Performance based problem recommendation
<br>

## About
1) The recommendation is independent of the type of problem, it's completely dependent on the language in which the user has solved the previous problem.
2) The recommendation system (success score) is based on formula:- 1/(1+TS-PS);
where TS=successful submissions/total submissions,
PS=successful submissions for a particular language/total submissions for particular language
3) For training the model ,KNN algorithm is used.
4) Based on the calculated success score for a particular problem, the user will be recommended a problem having a similar success score. So the user will be recommended with problems having a similar success score to that of the previous problem solved based on language used, irrespective of type of problem.
5) The actual flask application is private which is using this methods to recommended problems. 
<br>

## Setup 

```
pip install -r requirements.txt
```
<br>


