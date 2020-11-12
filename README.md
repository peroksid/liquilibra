
Development environment
---

Prerequisites:
Docker (Docker-Deskopt, brew install docker)
Python 3

What do I to:

... run dev-server locally?
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
FLASK_APP=librasrv.py flask run

... modify code?
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install -r development_requirements.txt
edit->
black ./ ->
pylint *.py tests/*.py ->
pytest ->
commit

... init db?
docker-compose up
  and in another console:
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
FLASK_APP=librasrv.py LIQUILIBRA_SETTINGS=test_environment.cfg flask init-db
