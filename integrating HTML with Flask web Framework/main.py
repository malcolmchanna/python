### Integrate HTML with Flask
### HTTP verb GET and Post
from flask import Flask ,redirect,url_for,render_template, request
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=" "
    if score>= 50:
         res= "PASS"
    else:
         res="FAIL"
    return render_template('result.html',result=res)


@app.route('/fail/<int:score>')
def fail(score):
   return'the student is fail and mark is '+ str(score)


@app.route('/results/<int:marks>')
def results(marks):
        result = ""
        if marks<50:
            result='fail'
        else:
            result='success'
        return  redirect(url_for(result,score=marks))      

##Result Checker
@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score= 0
    if request.method == 'POST':
        science= float(request.form['science'])
        math=float(request.form['maths'])
        c =float(request.form['c'])
        data_science= float(request.form['datascience'])
        total_score=(science+math+c+data_science)/4 
    res= "" 
    #if total_score>=50:
    #  res = "success"
    #else:
    #   res = "fail"
    return redirect(url_for('success',score=total_score))    

if __name__=='__main__':
 app.run(debug=True)



