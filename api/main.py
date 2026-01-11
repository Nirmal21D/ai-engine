"""
Vercel entrypoint for FastAPI application.
This file is required by Vercel to locate the FastAPI app.
"""
from server.main import app

# Vercel requires the app to be named 'app' in this file
__all__ = ["app"]
