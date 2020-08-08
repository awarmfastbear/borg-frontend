# ReactjsBrowserInputToAPythonBackEnd
This package contains all you need to stand up a simple nodejs web server and a Python backend server where you can submit input from a web browser and have the backend python server do something with it.

## Requirements

- Linux / Mac OSX
- An internet connection is required for installing the initial node dependencies but the app runs offline

## How to use

Prerequisites: 
- Have nodejs installed - https://nodejs.org/en/download/
- Have Python3.x installed - https://www.python.org/downloads/
- Have Flask installed. To install flask you can install it with pip: `pip install flask`
- Have the Python flask_cors module installed: `pip install flask_cors`

Instructions:

1) Open a terminal to this directory, e.g. next to the `package.json` file

2) Run `npm install` to install reactjs dependencies needed by the Reactjs package.

3) Run `npm start` to start the front end web server

4) Open another terminal from this same directory and run `export FLASK_DEBUG=1 && cd python_backend && flask run`

5) Visit http://localhost:3000/ and you should see a reactjs server you can visit and submit data with. You should see the data pop up in the Flask terminal as well as get saved to a file called `postdata.txt` in the `python_backend` folder.


## Notes

- Any changes you make to the source files should trigger the Flask and Nodejs server to be recompiled and automatically reloaded after you save changes.

Enjoy. Let me know what you think. Feel free to make pull requests or provide suggestions.
