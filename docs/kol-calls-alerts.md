# KOL Calls and Alerts API

This document details the API endpoints available for Key Opinion Leader (KOL) calls and alerts in the RexiAPI service.

## Endpoints

### Get New Calls and Alerts
- **Endpoint**: `GET /solana/radar/calls/new`
- **Description**: Get new token calls and alerts from monitoring systems
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `page`: Page number (≥1, default: 1)
  - `limit`: Number of results per page (1-100, default: 20)
- **Response**: Latest token calls and alerts

### Get Most Called Tokens by Timeframe
- **Endpoint**: `GET /solana/radar/calls/most/{timeframe}`
- **Description**: Get most called tokens by timeframe from monitoring systems
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `timeframe`: Valid timeframes (1h, 6h, 24h, 7d, 30d)
  - `page`: Page number (≥1, default: 1)
  - `limit`: Number of results per page (1-100, default: 20)
- **Response**: Most called tokens for the specified timeframe

### Get Latest Trading Calls
- **Endpoint**: `GET /solana/monitor/getlatestcalls`
- **Description**: Get latest Solana trading calls from the Scan API
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `page`: Page number (≥1, default: 1)
  - `limit`: Number of results per page (1-10000, default: 50)
- **Response**: Latest trading calls data

### Get Caller Profile
- **Endpoint**: `GET /solana/radar/caller/{caller_id}`
- **Description**: Get detailed profile information for a specific caller by their ID
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `caller_id`: Caller ID
- **Response**: Full caller profile including Telegram/Twitter info and performance metrics

### Get Caller Calls
- **Endpoint**: `GET /solana/radar/caller/{caller_id}/calls`
- **Description**: Get all calls made by a specific caller
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `caller_id`: Caller ID
  - `sort`: Sort order (newest, oldest, default: newest)
  - `page`: Page number (≥1, default: 1)
  - `limit`: Number of results per page (1-100, default: 20)
  - `q`: Optional search query to filter calls
- **Response**: Call history for the specified caller

### Get Caller Performance
- **Endpoint**: `GET /solana/radar/caller/{caller_id}/performance`
- **Description**: Get performance statistics for a specific caller by their ID
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `caller_id`: Caller ID
- **Response**: Caller stats including win rate, average gain, and analyzed calls

### Get Top Performing Callers
- **Endpoint**: `GET /solana/radar/callers/top`
- **Description**: Get top performing callers based on recent call data
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `limit`: Number of top callers to return (1-50, default: 20)
- **Response**: Callers ranked by performance score

## Example Usage

```python
# Get new calls
new_calls = await rexi.solana.radar.get_new_calls({
    'page': 1,
    'limit': 20
})

# Get most called tokens by timeframe
most_called = await rexi.solana.radar.get_most_called('24h', {
    'limit': 20
})

# Get latest trading calls
latest_calls = await rexi.solana.monitor.get_latest_trading_calls({
    'page': 1,
    'limit': 50
})

# Get caller profile
profile = await rexi.solana.radar.get_caller_profile('caller_id_here')

# Get caller calls
calls = await rexi.solana.radar.get_caller_calls('caller_id_here', {
    'page': 1,
    'limit': 20
})

# Get caller performance
performance = await rexi.solana.radar.get_caller_performance('caller_id_here')

# Get top callers
top_callers = await rexi.solana.radar.get_top_callers({
    'limit': 20
})
```
