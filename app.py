from flask import Flask, jsonify, request
from tool import get_html
app = Flask(__name__)







@app.route('/drh', methods=['GET'])
def get_data():
    re = get_html()
    if re == 'ok':
        print('runned Successfuly!')

    response = {
        'status': 'success',
        'message': 'Runned Successfuly'
    }
    return jsonify(response) 






if __name__ == '__main__':
    app.run(debug=True)