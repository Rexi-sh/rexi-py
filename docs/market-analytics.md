# Market Analytics API

This document details the API endpoints available for market analytics operations in the RexiAPI service.

## Endpoints

### Get Comprehensive Market Statistics
- **Endpoint**: `GET /solana/market-stats`
- **Description**: Get comprehensive market statistics including data for all trading platforms with timeframes (5m, 1h, 6h, 24h)
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Response**: Market statistics data

### Get SOL Market Data
- **Endpoint**: `GET /solana/sol/market-data`
- **Description**: Get SOL market data including price, market cap, and fee statistics
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Response**: Current SOL market information

### Get Activity Types
- **Endpoint**: `GET /solana/activity/types`
- **Description**: Get available activity types for Solana transactions
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `activity_type`: Activity type (transfer, nfttrading, dextrading, default: "transfer")
- **Response**: Mapping of activity type keys to descriptions

## Example Usage

```python
# Get market statistics
market_stats = await rexi.solana.get_market_stats()

# Get SOL market data
sol_market = await rexi.solana.market.get_sol_market_data()

# Get activity types
activity_types = await rexi.solana.market.get_activity_types()
```
