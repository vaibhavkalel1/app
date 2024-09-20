from flask import Flask, jsonify, request
from smart_contract.pencil_contract import PencilContract

app = Flask(__name__)
contract = PencilContract(channel_name='pencilchannel', chaincode_name='pencilCC')

@app.route('/api/list', methods=['POST'])
def list_pencil():
    data = request.json
    response = contract.list_pencil(data['id'], data['owner'], data['price'])
    return jsonify({'status': response})

@app.route('/api/buy', methods=['POST'])
def buy_pencil():
    data = request.json
    response = contract.buy_pencil(data['id'], data['buyer'])
    return jsonify({'status': response})

@app.route('/api/pencils', methods=['GET'])
def get_pencils():
    response = contract.get_pencils()
    return jsonify({'pencils': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
