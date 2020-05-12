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
        sniffer = csv.Sniffer()
        fstring = package.read()
        dialect = sniffer.sniff(fstring)
        # reader = csv.reader(package)
        # for row in reader:
        #     nis=json.dumps(row)
        #     nothi = nothi +"\n"+ nis
        csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(fstring.splitlines(), skipinitialspace=True)]
        with open(name+'.json','w') as outfile:
            json.dump(csv_dicts,outfile)
    return "Succefully Uploaded" + "\n"+ "Delimiter: "+ str(dialect.delimiter)


if __name__=='__main__':
    app.run(debug=True)