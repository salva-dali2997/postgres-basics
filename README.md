# postgres-basics
To spin up this project, ensure that you have python3 installed by running -
```python3 --version```
Should return something like
```Python 3.12.2``` or whatever version you are running.
Then to spin up a virtual environment run -
```python3 -m venv .venv```
Which is running a command -m to make a venv (virtualenvironment) called .venv to run this code. To initialize the virtual environment run -
```source .venv/bin/activate```
Now to install the requirements -
```pip install -r requirements.txt```
Now that python has been initialized, let's spin up the containers. The `compose.yaml` is a Docker Compose file that will create multiple containers to run the Postgres database. To create this make sure you have Docker Desktop up and running, then run -
```docker compose up -d```
Which runs the containers in detached (-d) mode. You should now be able to visit 
[http://localhost:5050] to view the pgadmin console used to interact with the Postgres DB.

