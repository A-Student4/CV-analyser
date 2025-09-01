from fastapi import FastAPI

app = FastAPI()

@app.get("/") # this is the root endpoint and it will be called when we access the root URL which is http://localhost:8000/ this root URL is also called the home page and this is the first page that will be displayed when we access the URL
def read_root():
    return {"Hello": "Prospero"} # this will return a JSON response with a key "Hello" and value "World" on accessing the root URL
