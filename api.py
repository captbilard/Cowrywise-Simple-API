import uuid
import datetime
from collections import OrderedDict

from flask import Flask, jsonify

app = Flask(__name__)

data = OrderedDict()

def timeStamp():
    """Return the timestamp in string format"""
    return str(datetime.datetime.now())


def uuidGenerator():
    """Generates random uuid"""
    return str(uuid.uuid4())


def updateData():
    """Updates the data dictionary
        with the timestamp & uuid"""
    key = timeStamp()
    value = uuidGenerator()
    data[key] = value
    return data


@app.route("/")
def index():
    data = updateData()
    new_data = [{key:data[key]} for key in reversed(data)]
    return jsonify(new_data)