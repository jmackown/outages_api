
### To Install
1. create a python 3.10 venv `python -m venv` and activate `source venv/bin/activate`
2. install dependencies `pip install -r requirements.txt`

### To Test
1. run with `python -m pytest tests`

### To Run (live)
1. update the values in the `.env` file to the live values
2. run with `python main.py`

### To Run (mock)
_(requires docker)_
1. start the mock api server with `docker-compose up`
2. run with `python main.py`
