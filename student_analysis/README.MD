# Student Performance Analysis

## About
This Flask website is a dashboard for keeping track of personal progress on http://arena.siesgst.ac.in/  
This project gives a coder analysis on the submissions made by him and recommends Problems to him according to Topics solved/unsolved 
<br>
<br>
<b>For Unsolved Topics</b>
<br>
System provides problems in increasing difficulty 
<br>
<b>For Solved Topics</b>
<br>
System provides top 5 problems of Higher  difficulty which has not been solved yet


#### This project has been deployed on https://arena-siesgst-dashboard.herokuapp.com/

## Installation

### Install Dependencies
> <b>pip</b>: pip install -r requirements.txt
> <br>
<b>conda</b>:  conda install --yes --file requirements.txt

### Execute Code
>python main.py

### To view Dashboard (in Browser) goto following link once server starts
>http://localhost:5000/

#### Layouts are visible properly at 67% zoom in browser

## Dataset
The Data collected from Databases are stored inside Data folder in the following files
- users.json
- submissions.json
- problems.json

#### Get the Updated Dataset from <http://arena.siesgst.ac.in/labs> and place it 'data' folder

## Results
![](images/demo.gif)

## Meta

V.Karthikraj 
- karthikraj.v17@siesgst.ac.in
- [@LinkedIn](https://www.linkedin.com/in/naidukarthi2193/) 

## Contributing

1. Fork it (<https://github.com/naidukarthi2193/labs/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## TODOs
- Add Ratings Data and Graphs
- UI Improvements
- Responsive design
- Recommed Blogs according to submissions
- Add URLs for Recommended Problems
