from flask import Flask,render_template,request
from urllib.request import urlopen
import json

app=Flask(__name__)

@app.route('/movie',methods=['GET','POST'])  
def movie():
    if request.method=='POST':
        moviename=request.form['moviename']
        moviename=str(moviename)
        lst=moviename.split(" ")
        moviename="+"
        moviename=moviename.join(lst)
        url='http://www.omdbapi.com/?t='+moviename+'&y=&plot=short&r=json'
        response = urlopen(url).read().decode('utf8')
        obj = json.loads(response)
        if obj['Response']=='False':
            return render_template("not_found.htm")
        else:
            return render_template("moviedetails.html",obj=obj)

if __name__=="__main__": 
    app.run(debug=True)
    

    
