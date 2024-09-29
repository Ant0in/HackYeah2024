import websockets
import asyncio
import json

from test_main import MainPipelineHelper

import db


database = db.DB("dd.db")
main_pipeline = MainPipelineHelper()

async def handler(websocket, _path):
    try:
        async for message in websocket:
            data = json.loads(message)

            print("DATA", data)

            if data["type"] == "request_scan":
                url = data["url"]
                response_data = {"type": "scan_results", "url": url , "score": main_pipeline.run(url)}
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


async def start_server():
    server = await websockets.serve(handler, "0.0.0.0", 8080)
    print("WebSocket server started on 0.0.0.0:8080")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_server())
    asyncio.get_event_loop().run_forever()