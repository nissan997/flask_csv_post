from flask import Flask,request,jsonify
import json
import csv
nothi = 'nissan'
name = ''
app = Flask(__name__)

@app.route('/file', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        package = request.files["package"]
        fname = package.filename
        nam = nothi.split('.')[0]
        print("nisan")
    return "koci"

if __name__=='__main__':
    app.run(debug=True)