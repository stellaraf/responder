"""API Request & Response Models."""

# Third Party
from pydantic import BaseModel, StrictBool


class TestHttpResponse(BaseModel):
    """Response model for /test/http."""

    success: StrictBool
