# FastAPI-Swagger

Installation
First things first, make sure you have FastAPI installed. If not, you can install it using pip: 
```
pip install fastapi
```
Additionally, you’ll need an ASGI server to run your FastAPI application. For this example, we’ll use Uvicorn: 
```
pip install uvicorn
```
Now, let’s run our FastAPI application using Uvicorn: 
```
uvicorn main:app --reload
```

## Swagger Documentation

FastAPI uses Swagger UI to create an interactive documentation interface. To access the Swagger documentation, run your FastAPI application and navigate to

Swagger UI allows developers to explore and test API endpoints interactively. It displays detailed information about each endpoint, including parameters, request/response models, and example requests.
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```
