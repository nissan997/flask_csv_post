from flask import Flask, request, jsonify
import json
# from flask_sqlalchemy import SQLAlchemy 
import csv


app = Flask(__name__)

@app.route('/file',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        package = request.files["package"]
        nothi = str(package.filename)
        name = nothi.split('.')[0]
        reader = csv.reader(package)
        for row in reader:
            nis=json.dumps(row)
            nothi = nothi +"\n"+ nis
        with open(name+'.json','w') as outfile:
            json.dump(nothi,outfile)
    return nothi + "\n" + "Succefully Uploaded"


if __name__=='__main__':
    app.run(debug=True)