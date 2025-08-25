#!/usr/bin/env python3
import asyncio
from app.integrations.supabase_client import supabase_client

async def check_lead():
    lead = await supabase_client.get_lead_by_id('5fb4e389-7692-4eea-97c2-744d68d219d2')
    if lead:
        print(f"Lead atual:")
        print(f"  qualification_score: {lead.get('qualification_score')}")
        print(f"  updated_at: {lead.get('updated_at')}")
        print(f"  name: {lead.get('name')}")
    else:
        print("Lead não encontrado")

if __name__ == "__main__":
    asyncio.run(check_lead())