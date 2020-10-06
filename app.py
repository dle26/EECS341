from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import os

app = Flask(__name__)
CORS(app)




def send_email(results, email):
    
    results = pd.DataFrame(results).to_csv('CDSI_Data.csv')
    
    fromaddr = 'cdsi.datafiles@gmail.com'
    toaddr = email
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Your CDSI Data'
    
    body = 'Dear User, Attached is the data file for your CDSI query'
    msg.attach(MIMEText(body, 'plain'))
    
    attachment = open('CDSI_Data.csv', "rb")
    att = MIMEBase('application', 'octet-stream')
    att.set_payload((attachment).read())
    att.add_header('Content-Disposition', "attachment; filename= %s" % 'CDSI_Data.csv')
    msg.attach(att)
    email = smtplib.SMTP('smtp.gmail.com', 587)
    
    email.starttls()
    email.login(fromaddr, "12311997Jta")
    message = msg.as_string()
    
    email.sendmail(fromaddr, toaddr, message)
    os.remove('CDSI_Data.csv')
    email.quit()


@app.route('/search', methods=['GET'])
def searchByQueryString():
    queryString = request.args.get('query_string')
    email = request.args.get('email')
    if ("drop" in queryString.lower() \
         or "truncate" in queryString.lower() \
         or "delete" in queryString.lower() \
         or "create" in queryString.lower() \
         or "insert" in queryString.lower() \
         or "alter" in queryString.lower() \
         or ";" in queryString \
         or "/*" in queryString \
         or "--" in queryString
       ):
        resp = jsonify({'message': 'Invalid SQL query'})
        resp.status_code = 400
        return resp
    elif queryString:
        conn = sqlite3.connect('test.db')
        c = conn.cursor()

        result = c.execute(queryString.lower())
        rows = result.fetchall()

        if rows:
            rowsTemp = rows
            rows = list()
            column_names = list()
            for i in c.description:
                column_names.append(i[0])
            
            rows.append(column_names)
            for row in rowsTemp:
                rows.append(row)

        if email:
            send_email(rows, email)
        resp = jsonify(rows)
        resp.status_code = 200
        conn.close()
        return resp
    else: 
        resp = jsonify({'message': 'Query string is not included in query'})
        resp.status_code = 500
        return resp


if __name__ == '__main__':
    app.run()

