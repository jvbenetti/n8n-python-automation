import os
import re
from supabase import create_client, Client
from dotenv import load_dotenv

# --- 1. CONFIGURAÇÕES ---
load_dotenv()
SUPABASE_URL: str|None = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str|None = os.getenv("SUPABASE_KEY")

# Instancia o cliente do Supabase
supabase: Client = create_client(str(SUPABASE_URL), str(SUPABASE_KEY))
