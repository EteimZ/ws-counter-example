import asyncio
import json
import logging
import websockets

logging.basicConfig()

# set of users
USERS = set()

# counter value
VALUE = 0

def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

def value_event():
    return json.dumps({"type": "value", "value": VALUE})

async def counter(websocket):
    global USERS, VALUE
    try:
        # Register user
        USERS.add(websocket)
        websockets.broadcast(USERS, users_event())
        # Send current state to user
        await websocket.send(value_event())
        # Manage state changes
        async for message in websocket:
            event = json.loads(message)
            if event["action"] == "minus":
                VALUE -= 1
                websockets.broadcast(USERS, value_event())
            elif event["action"] == "plus":
                VALUE += 1
                websockets.broadcast(USERS, value_event())
            else:
                logging.error("unsupported event: %s", event)
    finally:
        # Unregister user
        USERS.remove(websocket)
        websockets.broadcast(USERS, users_event())

async def main():
    async with websockets.serve(counter, "localhost", 6789):
        await asyncio.Future() # run forever

if __name__ == "__main__":
    try:
        print("Serving WS on localhost port 6789 (http://localhost:6789/) ...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down server...")
