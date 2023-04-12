from datetime import datetime
from fastapi import FastAPI, Request
import json
import uvicorn

header_api_pass = '#token or password#'
app = FastAPI()


@app.post("/api/")
async def create_record(request: Request):
    id = 0
    jsonrecord = "["
    body = request.body()
    header = request.header
    if (header == header_api_pass):
        return {"message": "OK"}
    else:
        return {"message": "Not authorized"}

if __name__ == '__main__':
    uvicorn.run(app, port=443, host='0.0.0.0',
                ssl_certfile="/etc/letsencrypt/live/#domain_name#/fullchain.pem",
                ssl_keyfile="/etc/letsencrypt/live#domain_name#/privkey.pem")
