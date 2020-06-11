from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route('/')
def landing():
  return render_template('home.html')

@app.route('/attr')
def attr_form():
  return render_template('my-form.html')

@app.route('/attr',methods = ['POST'])
def attr_form_post():
  text = request.form['text']
  processed_text = ' '
  pattern = re.compile(r"<div class=|<div class = |<div class =")
  result = pattern.sub("[div][attr=\"class\",", text)
  pattern2 = re.compile(r"\">")
  result2 = pattern2.sub("\"]",result)
  pattern3 = re.compile(r"</div>")
  result3 = pattern3.sub("[/div]",result2)
  pattern4 = re.compile("<p>")
  result4 = pattern4.sub("[break][break]",result3)
  pattern5 = re.compile("</p>")
  result5 = pattern5.sub("",result4)

  processed_text = result5

  return render_template('my-form.html',processed_text=processed_text)

@app.route('/classes')
def my_form():
    return render_template('my-form.html')

@app.route('/classes', methods = ['POST'])
def my_form_post():
    text = request.form['text']
    # get rid of newlines.
    text = text.replace("\r","")
    split_text = text.split('\n')
    text = "".join(split_text)
    processed_text = ' '

    # get the names of your divs
    result1 = re.findall(r".[^.{]*{",text)
    p_result1 = []
    for val in result1:
        p_result1.append(val[:-1].strip())
        
    # get the values inside of the curly braces 
    result = re.findall(r"{[^{}]*}",text)
    p_result = []
    for val in result:
        p_result.append(val[1:-1])

    newclasses = []
    ncs = ""
    for x in range(0,len(p_result)):
        nc = "[newclass=" + p_result1[x] + "]" + p_result[x] +"[/newclass]"
        newclasses.append(nc)
        # whole string
        ncs += nc

    processed_text = ncs
    return render_template('my-form.html',processed_text=processed_text)

if __name__ == '__main__':
  app.run(threaded=True, port=5000)
