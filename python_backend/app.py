from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import pty
import runServerSideCommands #import other pythonfile to access its function.

app = Flask(__name__)
CORS(app) #Take care of CORS issues.

#You'll need to restart the flask app if you make changes to it unless you enable debug mode.
 
 # Home page route.
@app.route('/')
def index():
	return "Hello World!"

#route designated for accepting data
@app.route('/receiveData', methods=["POST"])
def handle_request():
	data = request.json
	f = open("postdata.txt", "a")
	f.write(str(data))
	f.write("\n")
	f.close
	print("POST data submitted: " + str(data))
	runServerSideCommands.doSomething(data) #passing event data into the function from the runServerSideCommands.py file
	return jsonify(data)


@app.route('/getHostname', methods=["GET"])
def returnHostname():
	# hostname_var = os.system('hostname')
	hostname = subprocess.check_output(['hostname'])
	return hostname
