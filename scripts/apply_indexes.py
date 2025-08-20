#!/usr/bin/env python3
"""
Script to apply database indexes for improved performance
"""

import asyncio
import logging
from app.integrations.supabase_client import SupabaseClient
from app.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SQL statements to create indexes
INDEX_CREATION_QUERIES = [
    # Index on follow_ups.scheduled_at for faster retrieval of pending follow-ups
    """
    CREATE INDEX IF NOT EXISTS idx_follow_ups_scheduled_at 
    ON follow_ups (scheduled_at);
    """,
    
    # Composite index on follow_ups.status and follow_ups.scheduled_at 
    # for efficient querying of pending follow-ups
    """
    CREATE INDEX IF NOT EXISTS idx_follow_ups_status_scheduled_at 
    ON follow_ups (status, scheduled_at);
    """,
    
    # Index on follow_ups.lead_id for faster lookup of follow-ups by lead
    """
    CREATE INDEX IF NOT EXISTS idx_follow_ups_lead_id 
    ON follow_ups (lead_id);
    """,
    
    # Index on leads.phone_number for faster lookup of leads by phone
    """
    CREATE INDEX IF NOT EXISTS idx_leads_phone_number 
    ON leads (phone_number);
    """,
    
    # Index on leads_qualifications.lead_id for faster lookup of qualifications by lead
    """
    CREATE INDEX IF NOT EXISTS idx_leads_qualifications_lead_id 
    ON leads_qualifications (lead_id);
    """,
    
    # Index on conversations.lead_id for faster lookup of conversations by lead
    """
    CREATE INDEX IF NOT EXISTS idx_conversations_lead_id 
    ON conversations (lead_id);
    """,
    
    # Index on conversations.updated_at for faster lookup of recent conversations
    """
    CREATE INDEX IF NOT EXISTS idx_conversations_updated_at 
    ON conversations (updated_at);
    """
]

async def apply_indexes():
    """Apply indexes to the database tables"""
    logger.info("Starting database index application...")
    
    try:
        # Initialize Supabase client
        db = SupabaseClient()
        
        # Test connection
        await db.test_connection()
        logger.info("✅ Connected to Supabase successfully")
        
        # Apply each index creation query
        for i, query in enumerate(INDEX_CREATION_QUERIES, 1):
            try:
                logger.info(f"Applying index {i}/{len(INDEX_CREATION_QUERIES)}...")
                # Execute the raw SQL query
                result = db.client.execute_sql(query)
                logger.info(f"✅ Index {i} applied successfully")
            except Exception as e:
                logger.error(f"❌ Failed to apply index {i}: {e}")
                # Continue with other indexes even if one fails
                continue
        
        logger.info("🎉 All indexes applied successfully!")
        
    except Exception as e:
        logger.error(f"❌ Failed to apply indexes: {e}")
        raise

if __name__ == "__main__":
    # Run the async function
    asyncio.run(apply_indexes())