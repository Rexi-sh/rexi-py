# Blockchain Data API

This document details the API endpoints available for blockchain data operations in the RexiAPI service.

## Endpoints

### Get Account Token Accounts
- **Endpoint**: `GET /solana/account/{address}/token-accounts`
- **Description**: Get token accounts for a wallet address with pagination support
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
  - `page`: Page number (≥1, default: 1)
  - `page_size`: Number of results per page (1-100, default: 100)
  - `token_type`: Type of tokens to return (default: "token")
  - `hide_zero`: Hide accounts with zero balance (default: true)
- **Response**: Detailed token account information

### Get Account Domains
- **Endpoint**: `GET /solana/account/{address}/domains`
- **Description**: Get domain information associated with an account address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
- **Response**: Domain names associated with the account address

### Get Account Transactions
- **Endpoint**: `GET /solana/account/{address}/transactions`
- **Description**: Get transactions for an account address with paging support
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
  - `page`: Page number (≥1, default: 1)
  - `page_size`: Number of results per page (1-100, default: 10)
  - `before`: Transaction signature to paginate before (optional)
- **Response**: Transaction history with detailed information

### Get Account Transfers
- **Endpoint**: `GET /solana/account/{address}/transfers`
- **Description**: Get token transfers for an account address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
  - `page`: Page number (≥1, default: 1)
  - `page_size`: Number of results per page (1-100, default: 10)
  - `remove_spam`: Filter out spam tokens (default: true)
  - `exclude_amount_zero`: Exclude zero amount transfers (default: true)
- **Response**: Transfer history with filtering options

### Get Account Transfers Total
- **Endpoint**: `GET /solana/account/{address}/transfers/total`
- **Description**: Get total count of token transfers for an account address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
  - `remove_spam`: Filter out spam tokens (default: true)
  - `exclude_amount_zero`: Exclude zero amount transfers (default: true)
- **Response**: Total number of transfers with filtering options

### Get Account DEX Trading Total
- **Endpoint**: `GET /solana/account/{address}/dex-trading/total`
- **Description**: Get total count of DEX trading activities for an account address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
- **Response**: Total number of DEX trading activities

### Get Account NFT Total
- **Endpoint**: `GET /solana/account/{address}/nft/total`
- **Description**: Get total count of NFT activities for an account address
- **Authentication**: X-API-Key header with valid Rexi subscription required
- **Parameters**:
  - `address`: Account address
- **Response**: Total number of NFT activities

## Example Usage

```python
# Get token accounts
token_accounts = await rexi.solana.account.get_token_accounts('address_here', {
    'page': 1,
    'page_size': 100
})

# Get account domains
domains = await rexi.solana.account.get_account_domains('address_here')

# Get account transactions
transactions = await rexi.solana.account.get_account_transactions('address_here', {
    'page': 1,
    'page_size': 10
})

# Get account transfers
transfers = await rexi.solana.account.get_account_transfers('address_here', {
    'page': 1,
    'page_size': 10
})

# Get account transfers total
transfers_total = await rexi.solana.account.get_account_transfers_total('address_here')

# Get account DEX trading total
dex_total = await rexi.solana.account.get_account_dex_trading_total('address_here')

# Get account NFT total
nft_total = await rexi.solana.account.get_account_nft_total('address_here')
```
