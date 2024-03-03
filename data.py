from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Configure database connection
server = 'unifidataserver.database.windows.net'
database = 'unifidata'
username = 'gavinsbrown@gmail.com'
password = 'Alph4num3r!cal'
driver = '{ODBC Driver 17 for SQL Server}'

# Establish database connection
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server +
                      ';PORT=1433;DATABASE=' + database +
                      ';UID=' + username + ';PWD=' + password)

@app.route('/api/data', methods=['GET'])
def get_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM YourTable')
    data = cursor.fetchall()
    cursor.close()
    return jsonify({'data': data})

if __name__ == '__data__':
    app.run(debug=True)
