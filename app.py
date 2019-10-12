from flask import Flask, render_template,request
import requests
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        saring = request.form['saring']
        namaProduk = request.form['namaProduk']
        r = requests.get("https://sites.google.com/macros/exec?service=AKfycbx_-gZbLP7Z2gGxehXhWMWDAAQsTp3e3bmpTBiaLuzSDQSbIFWD&menu={}&query={}".format(saring,namaProduk))
        data = r.json()
        return render_template('hasil.html',data=data)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 