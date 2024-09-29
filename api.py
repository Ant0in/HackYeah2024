import websockets
import asyncio
import json

from modules.legal_keywords_checker import LegalKeywordsChecker
from modules.trustpilot_checker import TrustPilotReviews
from modules.whois import WhoisLookupModule
from modules.update_date import UpdateDateModule
from modules.media import MediaModule
from modules.html_parser import HTMLParserModule
from modules.html_text import HTMLTextModule
from modules.type_checker import ThemeChecker

from pipeline import Pipeline
from executor import Executor


def run_pipeline(url):
    # pipeline = Pipeline()
    # pipeline.add_module('HTMLParser', [])
    # pipeline.add_module('HTMLTextModule', ['HTMLParser'])
    # pipeline.add_module("LegalChecker", [])
    # pipeline.add_module("MediaModule", ["HTMLParser"])
    # # rev image
    # #pipeline.add_module("TrustPilotChecker", ["HTMLTextModule"])
    # pipeline.add_module('ThemeChecker', ["HTMLTextModule"])
    # pipeline.add_module("UpdateDate", ["WhoIS"])
    # pipeline.add_module("WhoIS", [])


    # module_list = {
    #     "HTMLParser": HTMLParserModule(url),
    #     "HTMLTextModule": HTMLTextModule(url),
    #     "LegalChecker": LegalKeywordsChecker(url),
    #     "MediaModule": MediaModule(url),
    #     # rev image
    #     #"TrustPilotChecker": TrustPilotReviews(url),
    #     "ThemeChecker": ThemeChecker(url, 'polish'),
    #     "UpdateDate": UpdateDateModule(),
    #     "WhoIS": WhoisLookupModule(url),
    # }


    # executor = Executor()
    # executor.run_pipeline(pipeline, module_list)
    return 42


async def handler(websocket, path):
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"Received data: {data}")

            url = data["url"]

            response_data = {"type": "scan_results", "url": url , "score": run_pipeline(url)}

            await websocket.send(json.dumps(response_data))
            print(f"Sent response data.")
    except websockets.ConnectionClosed as e:
        print(f"Connection closed: {e}")


async def start_server():
    server = await websockets.serve(handler, "0.0.0.0", 8080)
    print("WebSocket server started on 0.0.0.0:8080")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_server())
    asyncio.get_event_loop().run_forever()