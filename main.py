from fastapi import FastAPI
from routes import project, user

app = FastAPI()

app.include_router(user.router)
app.include_router(project.router)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}