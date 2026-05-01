from fastapi import FastAPI
from routes.project import router as router_project
from routes.user import router as router_user
import models


app = FastAPI()

app.include_router(router_user)
app.include_router(router_project)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}