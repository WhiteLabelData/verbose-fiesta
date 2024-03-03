from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Configure database connection
server = 'unifidataserver.database.windows.net'
database = 'unifidata'
username = 'unifidata_admin'
password = 'Alph4num3r!cal'
driver = '{ODBC Driver 18 for SQL Server}'

# Establish database connection
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server +
                      ';PORT=1433;DATABASE=' + database +
                      ';UID=' + username + ';PWD=' + password)

@app.route('/api/data', methods=['GET'])
def get_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * from dbo.process')
    rows = cursor.fetchall()

    # Convert rows to a list of dictionaries
    data = []
    for row in rows:
        row_dict = {}
        for key, value in zip(cursor.description, row):
            if isinstance(value, bytes):
                value = value.decode('utf-8')  # Convert bytes to string
            row_dict[key[0]] = value
        data.append(row_dict)

    cursor.close()
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True)
