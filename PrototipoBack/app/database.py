import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

supabaseUrl = os.environ.get("SUPABASE_URL", "")
supabaseKey = os.environ.get("SUPABASE_KEY", "")

supabaseClient: Client = create_client(supabaseUrl, supabaseKey)
