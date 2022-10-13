# Academy #

###  Create new VENV for any new project ###

python3 -m venv venv

###  Switch terminal to the new Env ###

source venv/bin/activate

### Run the live server ###

uvicorn main:app --reload
