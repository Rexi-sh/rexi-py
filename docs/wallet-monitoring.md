# Wallet Monitoring API

This document details the API endpoints available for wallet monitoring operations in the RexiAPI service.

## Endpoints

### Get Wallet Trading Calls
- **Endpoint**: `GET /solana/monitor/getcalls`
- **Description**: Get Solana trading calls for a specific wallet address with monitoring capabilities
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Wallet address to monitor (required)
  - `timeout`: Maximum seconds to wait for calls (1-120, default: 30)
- **Response**: Trading calls data for the specified address

### Get Account Funding Source
- **Endpoint**: `GET /solana/account/{address}/funded-by`
- **Description**: Get the funding source for an account address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
- **Response**: Information about which address funded this account

## Example Usage

```python
# Monitor wallet
wallet_calls = await rexi.solana.monitor_wallet({
    'address': 'wallet_address_here',
    'timeout': 30
})

# Get funding source
funding = await rexi.solana.account.get_account_funding_source('address_here')
```
