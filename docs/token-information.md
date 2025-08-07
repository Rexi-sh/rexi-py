# Token Information API

This document details the API endpoints available for token information operations in the RexiAPI service.

## Endpoints

### Get Token Information by Contract Address
- **Endpoint**: `GET /solana/token/info/{contract_address}`
- **Description**: Get comprehensive token information by pair address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `contract_address`: Token contract address
- **Response**: Token information

### Get Token Holder Data
- **Endpoint**: `GET /solana/token/holder-data/{contract_address}`
- **Description**: Get top 100 holders data for a token pair
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `contract_address`: Token contract address
  - `tracked_only`: Return only tracked wallets (optional, default: false)
- **Response**: Holder data for the token

### Get Top Token Traders
- **Endpoint**: `GET /solana/token/top-traders/{contract_address}`
- **Description**: Get top 100 traders for a token pair
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `contract_address`: Token contract address
- **Response**: Top traders data for the token

### Get Token Details by Mint Address
- **Endpoint**: `GET /solana/radar/token/{mint_address}`
- **Description**: Get detailed information about a specific token by mint address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `mint_address`: Token mint address
- **Response**: Detailed token information

### Get Account Tokens
- **Endpoint**: `GET /solana/account/{address}/tokens`
- **Description**: Get tokens held by an account address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
- **Response**: All tokens held by the specified account with balances and USD values

## Example Usage

```python
# Get token information
token_info = await rexi.solana.get_token_info({
    'address': 'token_address_here'
})

# Get token holders
holders = await rexi.solana.token.get_holder_data({
    'address': 'token_address_here'
})

# Get top traders
traders = await rexi.solana.token.get_top_traders({
    'address': 'token_address_here'
})

# Get token details by mint address
details = await rexi.solana.token.get_token_details({
    'address': 'mint_address_here'
})

# Get account tokens
tokens = await rexi.solana.account.get_account_tokens('address_here')
```
