import asyncio
import websockets
import json

TIKFINITY_URL = "ws://localhost:21213/"

async def main():
    print("🔌 Conectando con TikFinity...")

    async with websockets.connect(TIKFINITY_URL) as ws:
        print("✅ CONECTADO A TIKFINITY")
        print("🎁 Esperando regalos...\n")

        async for message in ws:
            try:
                event = json.loads(message)

                if event.get("event") == "gift":
                    data = event.get("data", {})

                    print("🎁 REGALO RECIBIDO")
                    print(json.dumps(data, indent=2, ensure_ascii=False))
                    print()

            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
