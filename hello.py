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
  pattern6 = re.compile("<b>")
  result6 = pattern6.sub("[b]",result5)
  pattern7 = re.compile("</b>")
  result7 = pattern7.sub("[/b]",result6)
  pattern8 = re.compile("<i>")
  result8 = pattern8.sub("[i]",result7)
  pattern9 = re.compile("</i>")
  result9 = pattern9.sub("[/i]",result8)
  pattern10 = re.compile("<h1>")
  result10 = pattern10.sub("[h1]",result9)
  pattern11 = re.compile("</h1>")
  result11 = pattern11.sub("[/h1]",result10)
  pattern12 = re.compile(r"<table style = |<table style =|<table style=")
  result12 = pattern12.sub("[table style=",result11)
  pattern13 = re.compile("</table>")
  result13 = pattern13.sub("[/table]",result12)
  pattern14 = re.compile("<table>")
  result14 = pattern14.sub("[table]",result13)
  pattern15 = re.compile("<tbody>")
  result15 = pattern15.sub("[tbody]",result14)
  pattern16 = re.compile("</tbody>")
  result16 = pattern16.sub("[tbody]",result15)
  pattern17 = re.compile("<tr>")
  result17 = pattern17.sub("[tr]",result16)
  pattern18 = re.compile("</tr>")
  result18 = pattern18.sub("[/tr]",result17)
  pattern19 = re.compile("<td>")
  result19 = pattern19.sub("[td]",result18)
  pattern20 = re.compile(r"<td style = |<td style =|<td style=")
  result20 = pattern20.sub("[td style=",result19)
  pattern21 = re.compile("</td>")
  result21 = pattern21.sub("[/td]",result20)

  processed_text = result21

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
    pp_result1 = []
    for val in result1:
        pp_result1.append(val[:-1].strip())

    # find the webkit-scrollbar divs and change them
    p_result1 = []
    for val in pp_result1:
      if "::-webkit-scrollbar" in val:
        pattern1=re.compile("::-webkit-scrollbar")
        result1=pattern1.sub(" div::-webkit-scrollbar",val)
        p_result1.append(result1)
      else:
        p_result1.append(val)

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
