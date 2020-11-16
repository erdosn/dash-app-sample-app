# dash-app-sample-app

## Instructions
* Please install virtualenv by running `pip install virtualenv` in terminal
* Fork/Clone this directory and navigate to it in terminal
* Run the command `virtualenv venv` in the directory
* Open this entire directory in VSCode, PyCharm or your IDE of choice
* Make sure you set the environment of your IDE to the `venv/` folder


## Installing Dash Packages
* Activate venv in terminal by running `source venv/bin/activate`
* Install the necessary packages
    * `pip install dash`
    * `pip install dash-bootstrap-components`
    * `pip install pandas` (if you need pandas)
* Install any other packages you might need as you build your app

## Saving requirements.txt
* Activate venv in terminal by running `source venv/bin/activate`
* Save list of required packages using `pip freeze >> requirements.txt`


## What is Dash?
* It is a Python Framework for creating webapps


## Structure
- `components/` ← contains all of our components
    - `__init__.py` ← converts a folder to a python library
- `backend/` ← contains all functionality of our data 
    - `__init__.py`
- `data/` ← contains data
- `app.py` ← the file that will run to execute your dash app 


## Important Points in Dash
- use `@app.callback` to make a interactive dashboard
    - `Input` - triggers a callback
    - `State` - passes in current component state 
- create and use `assets/` to store `.css` files for styling
- track button clicks with `n_clicks` property
- create python library using a `__init__.py` file in the folder
- app organization
- write None conditionals in callbacks