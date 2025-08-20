#!/usr/bin/env python3
"""
Script to apply database indexes for improved performance
"""

import asyncio
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.integrations.supabase_client import SupabaseClient
from app.utils.logger import emoji_logger

async def main():
    """Main function to apply database indexes"""
    emoji_logger.system_event("🔍 Starting database index application...")
    
    try:
        # Initialize Supabase client
        db = SupabaseClient()
        
        # Test connection
        if await db.test_connection():
            emoji_logger.system_ready("✅ Connected to Supabase successfully")
        else:
            emoji_logger.system_error("❌ Failed to connect to Supabase")
            return 1
        
        # Apply database indexes
        success = await db.apply_database_indexes()
        
        if success:
            emoji_logger.system_ready("🎉 Database index recommendations generated successfully!")
            emoji_logger.system_info("📋 Please create these indexes manually in your Supabase dashboard:")
            emoji_logger.system_info("   1. Go to your Supabase project dashboard")
            emoji_logger.system_info("   2. Navigate to Table Editor")
            emoji_logger.system_info("   3. Open the SQL editor")
            emoji_logger.system_info("   4. Run each of the recommended CREATE INDEX statements")
            return 0
        else:
            emoji_logger.system_error("❌ Failed to generate database index recommendations")
            return 1
            
    except Exception as e:
        emoji_logger.system_error(f"❌ Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)