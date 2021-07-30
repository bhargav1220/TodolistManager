
# System Requirements
You should install and setup PostgreSQL.

# Introduction

The repository contains a web app which is a todo list manager. The following
features are supported:

1. Adding a task.
1. Lists all the tasks.
1. Can be updated as complted or not completed.
1. View weekly scheduled tasks.
1. Can be deleted after completion.


# Setting up

1. Clone repository.
1. Open terminal and run command `createdb todolist` to create the database.
1. Run `psql todolist` then 
1. Run `ALTER USER postgres WITH PASSWORD 'password';` in the shell.
1. Create a virtualenv and activate it
1. Install dependencies using `pip install -r requirements.txt`
1. `python3 app.py` to run the application