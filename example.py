"""
Rexi Python API Client - Usage Example

This script demonstrates how to use the Rexi Python API client with all its capabilities.
"""

import os
import asyncio
from rexi import RexiAPI
import dotenv

dotenv.load_dotenv()

async def main():
    # Initialize Rexi API client
    rexi = RexiAPI({
        'api_key': os.environ.get('REXI_API_KEY')
    })
    
    # =====================
    # Market Analytics APIs
    # =====================
    print("\n=== Market Analytics ===\n")
    
    # Get market statistics
    market_stats = await rexi.solana.get_market_stats()
    print(f"Market Stats: {market_stats}\n")
    
    # Get SOL market data
    sol_market = await rexi.solana.market.get_sol_market_data()
    print(f"SOL Market Data: {sol_market}\n")
    
    # Get activity types
    activity_types = await rexi.solana.market.get_activity_types()
    print(f"Activity Types: {activity_types}\n")
    
    # =====================
    # Token Information APIs
    # =====================
    print("\n=== Token Information ===\n")
    
    # Get token information
    token_info = await rexi.solana.get_token_info({
        'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
    })
    print(f"Token Info: {token_info}\n")
    
    # Get token holders
    token_holders = await rexi.solana.token.get_holder_data({
        'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
    })
    print(f"Token Holders: {token_holders}\n")
    
    # Get top traders for a token
    top_traders = await rexi.solana.token.get_top_traders({
        'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
    })
    print(f"Top Traders: {top_traders}\n")
    
    # =====================
    # KOL Calls and Alerts APIs
    # =====================
    print("\n=== KOL Calls and Alerts ===\n")
    
    # Get new calls
    new_calls = await rexi.solana.radar.get_new_calls({
        'page': 1,
        'limit': 5
    })
    print(f"New Calls: {new_calls}\n")
    
    # Get most called tokens in last 24h
    most_called = await rexi.solana.radar.get_most_called('24h', {
        'limit': 5
    })
    print(f"Most Called Tokens (24h): {most_called}\n")
    
    # Get top callers
    top_callers = await rexi.solana.radar.get_top_callers({
        'limit': 5
    })
    print(f"Top Callers: {top_callers}\n")
    
    # =====================
    # Wallet Monitoring APIs
    # =====================
    print("\n=== Wallet Monitoring ===\n")
    
    # Monitor wallet activity
    wallet_calls = await rexi.solana.monitor_wallet({
        'address': 'So11111111111111111111111111111111111111112',
        'timeout': 10
    })
    print(f"Wallet Calls: {wallet_calls}\n")
    
    # Get latest trading calls
    latest_calls = await rexi.solana.monitor.get_latest_trading_calls({
        'limit': 5
    })
    print(f"Latest Trading Calls: {latest_calls}\n")
    
    # =====================
    # Blockchain Data APIs
    # =====================
    print("\n=== Blockchain Data ===\n")
    
    wallet_address = "So11111111111111111111111111111111111111112"
    
    # Get account tokens
    account_tokens = await rexi.solana.account.get_account_tokens(wallet_address)
    print(f"Account Tokens: {account_tokens}\n")
    
    # Get account funding source
    funding_source = await rexi.solana.account.get_account_funding_source(wallet_address)
    print(f"Funding Source: {funding_source}\n")
    
    # Get account domains
    domains = await rexi.solana.account.get_account_domains(wallet_address)
    print(f"Account Domains: {domains}\n")
    
    # Get account transactions
    transactions = await rexi.solana.account.get_account_transactions(wallet_address, {
        'page': 1,
        'page_size': 5
    })
    print(f"Transactions: {transactions}\n")
    
    # =====================
    # Real-time Data APIs
    # =====================
    print("\n=== Real-time Data ===\n")
    
    # Get WebSocket URL for live calls
    ws_url = rexi.solana.realtime.get_websocket_url()
    print(f"WebSocket URL: {ws_url}\n")
    
    print("\nAPI Demonstration Complete!")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
