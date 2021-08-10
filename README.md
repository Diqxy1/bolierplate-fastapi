# bolierplate-fastapi

This is a project for studies, this project is done in python, SQLAlchemy, alembic. if there are any doubts in its development I hope this project helps!


## This is a simple API that performs the follwoing

**/USER**
- Create
- Update
- Delete
- Detail

## Requirements

install the virtual machine in the main folder
- Windowns
```
python -m venv .venv
```
- Linux
```
python3 -m venv venv
```
- Then install the dependencies
```
pip install -r requirements.txt
```

## Clone this repository

```
git clone https://github.com/Diqxy1/ts-restful.git
```

## Start the server

- Windowns
```
python runserver.py
```
- Linux
```
python3 runserver.py
```

## Some Commands

- Create Migration
-> alembic revision -m "create account table"
- Run Migration
-> alembic upgrade head

## Working Routes

https://bolierplate-fastapi.herokuapp.com/docs

## Documentation

https://bolierplate-fastapi.herokuapp.com/redoc
