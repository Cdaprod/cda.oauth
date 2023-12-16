from fastapi import APIRouter, Depends, HTTPException, Response, Query
import os
import httpx

github_router = APIRouter()

# Replace with your GitHub OAuth credentials
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI")

@github_router.get("/login")
async def login_via_github():
    github_auth_url = "https://github.com/login/oauth/authorize"
    scope = "read:user"
    return Response(
        status_code=303,
        headers={"Location": f"{github_auth_url}?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope={scope}"}
    )

@github_router.get("/callback")
async def github_callback(code: str = Query(None)):
    if not code:
        raise HTTPException(status_code=400, detail="Missing code parameter")
    token_url = "https://github.com/login/oauth/access_token"
    payload = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
        "redirect_uri": GITHUB_REDIRECT_URI,
    }
    headers = {"Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=payload, headers=headers)
    response.raise_for_status()
    return response.json()