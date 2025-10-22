# Database Project Starter

This is a starter project for you to use to start your Python database projects.

There are two videos to support:

* [A demonstration of setting up the project](https://www.youtube.com/watch?v=KMEt4GgWJXc)
* [A walkthrough of the project codebase](https://youtu.be/KMEt4GgWJXc?t=460)

## Setup

### 1. Clone the repository to your local machine
```
; git clone git@github.com:makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME
```

> Or, if you don't have SSH keys set up
```
; git clone https://github.com/makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME
```

### 2. Enter the directory
```
; cd YOUR_PROJECT_NAME
```

### 3. Set up the virtual environment
```
; python -m venv databases-starter-venv
```

### 4. Activate the virtual environment
```
; source databases-starter-venv/bin/activate 
```


### 5. Install dependencies
```
(databases-starter-venv); pip install -r requirements.txt
```

> Read below if you see an error with `python_full_version`

### 6. Create the database
```
(databases-starter-venv); createdb YOUR_PROJECT_NAME
```

> `YOUR_PROJECT_NAME` can be anything you want it to be

### 7. Change `DATABASE_NAME` to equal `YOUR_PROJECT_NAME`

On line 11 of `lib/database_connection.py` you'll find this...

```
DATABASE_NAME = "DEFAULT_MAKERS_PROJECT" # <-- CHANGE THIS!
```

Change `DEFAULT_MAKERS_PROJECT` to whatever you chose for `YOUR_PROJECT_NAME`

### 8. Run the tests - see below if you have any issues
```
(databases-starter-venv); pytest
```
> If the tests fail, see below

### 9. Run the app
```
(databases-starter-venv); python app.py
```

<br>
<details>
  <summary>I get a <code>ModuleNotFoundError: No module named 'psycopg'</code></summary>
  <br>
If, after activating your <code>venv</code> and installing dependencies, you see this error when running <code>pytest</code>, please deactivate and reactivate your <code>venv</code>. This should solve the problem - if not, contact your coach.
</details>
<br>
<details>
  <summary>The tests fails and I see <code>Exception: Couldn't connect to the database DEFAULT_MAKERS_PROJECT!</code></summary>
  <br>
This error most likely means you need to edit line 11 in <code>lib/database_connection.py</code>. Go there and change <code>"DEFAULT_MAKERS_PROJECT"</code> to the name of the database you created in step 6.
</details>
