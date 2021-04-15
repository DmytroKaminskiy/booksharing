from pydantic import BaseModel


class ZoomWebhookSchema(BaseModel):
    event_ts: int
    event: str
    payload: dict
