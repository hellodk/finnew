from flask import Flask, render_template, request
import requests
import json
import urllib2

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def startPage():
    return render_template('init.html')


@app.route('/redirect', methods=['GET', 'POST'])
def redirect():
    # pdb.set_trace()
    value = request.args.get('action')
    containerID = request.args.get('container_id')
    command = 'http://0.0.0.0:2375/containers/' + containerID + '/' + value
    print value, ' ', type(value), ' containerID ', containerID, ' ', command
    requests.post(command)
    return render_template('init.html')


@app.route('/getContainers', methods=['GET', 'POST'])
def getContainers():
    # getting the list of all containers
    containerList = json.load(
        urllib2.urlopen('http://0.0.0.0:2375/containers/json?all=1'))
    containerList = getList(containerList)
    return render_template('init.html', lists=containerList)


@app.route('/listStartedContainers', methods=['GET', 'POST'])
def getStartedContainers():
    startedContainers = []
    for dic in containerList:
        if(dic['Status'] != 'Exited'):
            stoartedContainers.append(dic['Id'])
    return render_template('startedContainers.html', lists=startedContainers)


def getList(containerList):
    listNames = []
    for dic in containerList:
        listNames.append(dic['Id'])  # making a list based on container ID
    return listNames

if __name__ == '__main__':
    app.run()

