import os
import psycopg2
from urllib.parse import urlparse
from dotenv import load_dotenv  # Correct import for loading .env files

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../..', '.env'))

SUPABASE_HOST = os.getenv("SUPABASE_HOST")
SUPABASE_PASSWORD = os.getenv("SUPABASE_PASSWORD")
SUPABASE_DATABASE = os.getenv("SUPABASE_DATABASE")
SUPABASE_USER = os.getenv("SUPABASE_USER")
SUPABASE_PORT = os.getenv("SUPABASE_PORT")

# Parse the SUPABASE_URL to extract connection parameters
# Example: postgres://user:password@host:port/dbname

USERFINANCIALS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS "UserFinancials" (
    session_id UUID PRIMARY KEY,
    gross_salary NUMERIC(15, 2),
    basic_salary NUMERIC(15, 2),
    hra_received NUMERIC(15, 2),
    rent_paid NUMERIC(15, 2),
    deduction_80c NUMERIC(15, 2),
    deduction_80d NUMERIC(15, 2),
    standard_deduction NUMERIC(15, 2),
    professional_tax NUMERIC(15, 2),
    tds NUMERIC(15, 2),
    created_at TIMESTAMPTZ DEFAULT NOW()
);
"""

def ensure_userfinancials_table():
    try:
        conn = psycopg2.connect(
            host=SUPABASE_HOST,
            dbname=SUPABASE_DATABASE,
            user=SUPABASE_USER,
            password=SUPABASE_PASSWORD,
            port=SUPABASE_PORT
        )
        cur = conn.cursor()
        cur.execute(USERFINANCIALS_TABLE_SQL)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error creating UserFinancials table: {e}") 