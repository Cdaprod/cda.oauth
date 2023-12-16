from fastapi import APIRouter, Depends, HTTPException, Response, Query
import os
import httpx

google_router = APIRouter()

# Replace with your Google OAuth credentials
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

@google_router.get("/login")
async def login_via_google():
    google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth"
    scope = "openid email profile"
    return Response(
        status_code=303,
        headers={"Location": f"{google_auth_url}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={scope}&access_type=offline"}
    )

@google_router.get("/callback")
async def google_callback(code: str = Query(None)):
    if not code:
        raise HTTPException(status_code=400, detail="Missing code parameter")
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=payload)
    response.raise_for_status()
    return response.json()