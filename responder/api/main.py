"""API Routes."""

# Standard Library
from typing import Dict

# Third Party
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Project
from responder.models.api import TestHttpResponse

api = FastAPI(redoc_url=None, docs_url=None)

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/test/http", response_model=TestHttpResponse)
async def test_http() -> Dict[str, bool]:
    """Simple response for HTTP test requests."""
    return {"success": True}
