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
        print("entra primer if")
        items_list = ["bread", "fish", "eggs", "milk"]
        await_body = await body
        await_body = json.loads(await_body)
        now = datetime.now()
        date = now.strftime("%d-%m-%Y-%H:%M:%S") + ".json"
        for key, value in await_body.items():
            if (key in items_list):
                id = id + 1
                item = '{"id"' + ":" + str(id) + "," + '"datetime"' + ':"' + str(datetime.now()) + '",' + '"value"' + ":" + str(
                    value) + ',' + '"devEUI"' + ':"' + await_body["devEUI"] + '"' + ',"item"' + ':"' + key + '"' + "},"
                jsonrecord = str(jsonrecord) + item
                with open("#path_to_save#" + date, 'w') as outfile:
                    outfile.write(jsonrecord[:-1] + ']')
        return {"message": "OK"}
    else:
        return {"message": "Not authorized"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0',
                ssl_certfile="/etc/letsencrypt/live/#domain_name#/fullchain.pem",
                ssl_keyfile="/etc/letsencrypt/live#domain_name#/privkey.pem")
