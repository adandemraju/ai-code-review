from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def get_health():
    return {
        "status" : "healthy"
    }

class WebhookEvent(BaseModel):
    action: str


valid_actions = {
    "opened": True,
    "synchronize": True,
    "reopened": True,
}

@app.post("/webhooks/github")
def post_webhook(event: WebhookEvent):
    return {
        "should_review": valid_actions.get(event.action, False)
    }



        



