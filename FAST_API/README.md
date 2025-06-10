## FastAPI Hello World – Geetham's First FastAPI App

This is a simple FastAPI project I built to practice creating an API using FastAPI. It has one endpoint: /hello, which returns a greeting message.

## What this API does

When you visit GET /hello, it returns:
```
"Hello geetham"
```
## What I did — Step by Step

1. Installed FastAPI and Uvicorn
First, I created a virtual environment 
```
python -m venv Myenv
Myenv\Scripts\activate
```

Then I installed the required libraries:

```
pip install fastapi uvicorn
```

2. Created the FastAPI app in sample.py
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return "Hello geetham"
```

- @app.get("/hello"): Sets up a GET route at /hello

- async def hello(): Defines the function to run when that endpoint is accessed

- return "Hello geetham": Returns a simple greeting


3. Wrote a run script run.sh

```
uvicorn sample:app --reload
```

- sample is the filename (sample.py)

- app is the FastAPI instance

- --reload auto-restarts the server when code changes 

4. Ran the FastAPI server
```
sh run.sh
```

5. Tested the API
Once the server is running, I opened the browser and visited:

```
http://127.0.0.1:8000/hello
```

 It returned:

```
"Hello geetham"
```

