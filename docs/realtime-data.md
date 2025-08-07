# Real-time Data Streams API

This document details the API endpoints available for real-time data streams in the RexiAPI service.

## Endpoints

### WebSocket Live Calls Endpoint
- **Endpoint**: `WebSocket /solana/monitor/livecalls`
- **Description**: Real-time WebSocket endpoint for trading data, forwards live NEW_SCAN messages
- **Authentication**: WebSocket authentication handled at connection level
- **Response**: Real-time trading data stream

## Example Usage

```python
# Get WebSocket URL
ws_url = rexi.solana.realtime.get_websocket_url()

# Using WebSocket
import asyncio
import websockets

async def listen_to_livecalls():
    async with websockets.connect(ws_url) as websocket:
        while True:
            data = await websocket.recv()
            print(f"Received live call: {data}")
            
            # Process the live call data
            # ...

# Run the WebSocket listener
asyncio.run(listen_to_livecalls())
```

### WebSocket Authentication

The WebSocket connection requires authentication using your API key. The client handles this automatically when you use the provided `get_websocket_url()` method.

### Message Format

Messages received through the WebSocket connection are in JSON format and include the following fields:

```json
{
  "type": "NEW_SCAN",
  "data": {
    "token_address": "token_address_here",
    "token_name": "Token Name",
    "token_symbol": "TKN",
    "timestamp": 1628097600,
    "caller": {
      "id": "caller_id",
      "name": "Caller Name",
      "platform": "telegram"
    },
    "price_data": {
      "current_price": 0.00005,
      "market_cap": 500000
    }
  }
}
```

### Handling Connection Errors

It's recommended to implement reconnection logic to handle WebSocket disconnections:

```python
import asyncio
import websockets

async def connect_with_retry():
    while True:
        try:
            async with websockets.connect(ws_url) as websocket:
                while True:
                    data = await websocket.recv()
                    print(f"Received live call: {data}")
                    # Process data
        except websockets.ConnectionClosed:
            print("Connection lost, reconnecting...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Error: {e}, reconnecting...")
            await asyncio.sleep(5)

# Run the WebSocket listener with reconnection logic
asyncio.run(connect_with_retry())
```
