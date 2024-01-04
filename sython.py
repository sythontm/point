from fastapi import FastAPI
from telethon import TelegramClient
import uvicorn
from telethon.sessions import StringSession

app = FastAPI()

api_id = 23398930
api_hash = 'bd3e85a7aae40566f2fa8804d200d6d0'

@app.get("/api/{sess}")
async def send_message(sess: str):
    async with TelegramClient(StringSession(sess), api_id, api_hash) as client:
        receiver = await client.get_input_entity('me')
        await client.send_message(receiver, 'مرحبا')
    return {"message": "Message sent"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
