from flask import Flask, jsonify
from flask_cors import CORS
import os

from back_api.pizzas_info import get_main_page_info


app = Flask(__name__)
CORS(app)


@app.route('/api/main_page', methods=['GET'])
def SendMainPageInfo():
    answer = jsonify(get_main_page_info())

    return answer


if __name__ == '__main__':
    app.run(port=5001, debug=True)
