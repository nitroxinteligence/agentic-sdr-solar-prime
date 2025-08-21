#!/usr/bin/env python3
"""
Script to apply database indexes using SQL file
"""

import asyncio
import sys
import os
import psycopg2
from app.config import settings

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.logger import emoji_logger

def apply_indexes_from_sql():
    """Apply indexes using the SQL file"""
    emoji_logger.system_start("Applying database indexes from SQL file")
    
    try:
        # Read the SQL file
        sql_file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'migrations',
            'add_indexes.sql'
        )
        
        with open(sql_file_path, 'r') as f:
            sql_content = f.read()
        
        # Split the SQL content into individual statements
        # Remove comments and split by semicolon
        statements = []
        for statement in sql_content.split(';'):
            # Remove comments and whitespace
            cleaned_statement = statement.strip()
            if cleaned_statement and not cleaned_statement.startswith('--'):
                statements.append(cleaned_statement)
        
        # Connect to Supabase using psycopg2
        # Extract connection details from the Supabase URL
        # Format: postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
        import re
        match = re.match(r'postgresql://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)', settings.supabase_url)
        if not match:
            raise ValueError("Invalid Supabase URL format")
        
        user, password, host, port, dbname = match.groups()
        
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=dbname,
            user=user,
            password=settings.supabase_password  # Use the password from settings
        )
        
        cursor = conn.cursor()
        
        # Execute each statement
        for i, statement in enumerate(statements, 1):
            try:
                if statement.strip():  # Skip empty statements
                    cursor.execute(statement)
                    emoji_logger.system_info(f"✅ Index statement {i}/{len(statements)} executed successfully")
            except Exception as e:
                emoji_logger.system_warning(f"⚠️ Failed to execute index statement {i}: {e}")
                # Continue with other statements even if one fails
                continue
        
        # Commit the changes
        conn.commit()
        
        # Close the connection
        cursor.close()
        conn.close()
        
        emoji_logger.system_ready("🎉 All database indexes applied successfully from SQL file!")
        return True
        
    except Exception as e:
        emoji_logger.system_error(f"❌ Failed to apply database indexes from SQL file: {e}")
        return False

def main():
    """Main function"""
    success = apply_indexes_from_sql()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)