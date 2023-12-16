from fastapi import FastAPI
from google_auth import google_router
from github_auth import github_router

app = FastAPI()

app.include_router(google_router, prefix="/google")
app.include_router(github_router, prefix="/github")