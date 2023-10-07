from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is your local server!'

@app.route('/gps_data', methods=['POST'])
def receive_gps_data():
    data = request.get_json()  # Assuming the GPS data is sent as JSON
    # Process the GPS data (e.g., store it in a database)
    print("Received GPS data:", data)
    return jsonify({'message': 'GPS data received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
