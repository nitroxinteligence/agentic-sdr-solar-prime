import asyncio
from app.integrations.supabase_client import supabase_client

async def check_lead():
    leads = await supabase_client.search_leads_by_name('Teste Busca Reversa')
    print(f'Leads encontrados: {len(leads)}')
    for lead in leads:
        print(f'- {lead["name"]} ({lead["phone_number"]})')

if __name__ == "__main__":
    asyncio.run(check_lead())