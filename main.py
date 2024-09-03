from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': 'thsdatabase',
    'password': 'verySecurePassword998877',
    'host': 'localhost',
    'database': 'assignments_db',
}

# Establish a connection to the MySQL database
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Custom API endpoint to fetch and return data as JSON
@app.route('/assignments', methods=['GET'])
def get_assignments():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # SQL query to fetch the required fields
    query = """
        SELECT id, title, description, imageUrl1, imageUrl2, imageUrl3, imageUrl4, 
               imageUrl5, imageUrl6, imageUrl7, imageUrl8, imageUrl9, imageUrl10, 
               videoUrl, fileUrl
        FROM assignments
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    # Return the fetched data as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
