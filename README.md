# Academy #

###  Create new VENV for any new project ###

python3 -m venv venv

###  Switch terminal to the new Env ###

source venv/bin/activate

###  Switch OFF Env ###

deactivate

###  install packages ###

pip install -r requirements.txt 

### Run the local server ###

uvicorn main:app --reload
