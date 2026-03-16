# Notes

## FastAPI

FastAPI framework, high performance, easy to learn, fast to code, ready for production

**FastAPI** app class, the main entrypoint to use FastAPI.

Example
```py
from fastapi import FastAPI

app = FastAPI()
```

### HTTP Methods

Add a path operation using an **HTTP GET** operation.

Example
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items():
    return [{"name": "Empanada"}, {"name": "Arepa"}]
```