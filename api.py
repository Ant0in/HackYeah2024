import websockets
import asyncio
import json
from websockets.asyncio.server import serve
import concurrent.futures


from test_main import MainPipelineHelper

import db


database = db.DB("dd.db")
main_pipeline = MainPipelineHelper()

async def handler(websocket):
    try:
        async for message in websocket:
            data = json.loads(message)

            print("DATA", data)

            if data["type"] == "request_scan":
                url = data["url"]
                loop = asyncio.get_running_loop()
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    score = await loop.run_in_executor(pool, main_pipeline.run, url)

                response_data = {"type": "scan_results", "url": url , "score": score}
            elif data["type"] == "request_cache":
                url = data["url"]

                res = database.fetch_website(url)

                if res == None:
                    response_data = {"type": "cache_not_found", "url": url}
                else:
                    score, ts = res
                    response_data = {"type": "cache_found", "url": url, "score": score, "ts": ts.isoformat()}
            
            await websocket.send(json.dumps(response_data))

    except websockets.ConnectionClosed as e:
        print(f"Connection closed: {e}")


async def main():
    async with serve(handler, "0.0.0.0", 6969):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())
