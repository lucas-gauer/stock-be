from datetime import datetime

from fastapi import FastAPI

from source.controllers.auth import router as auth_router
from source.controllers.product import router as product_router
from source.controllers.user import router as user_router

app = FastAPI(title="Products Stock Manager")


@app.get("/")
async def home():
    return {"server_utc_time": datetime.utcnow()}


app.include_router(product_router)
app.include_router(user_router)
app.include_router(auth_router)
