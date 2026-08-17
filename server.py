import asyncio
import websockets
import json

async def main():
    print("Conectando con TikFinity...")

    async with websockets.connect("ws://localhost:21213/") as ws:
        print("CONECTADO A TIKFINITY")
        print("Esperando regalos...")

        async for message in ws:
            event = json.loads(message)

            if event.get("event") == "gift":
                print("REGALO RECIBIDO:")
                print(event["data"])

asyncio.run(main())
