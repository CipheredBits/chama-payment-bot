

from twilio.rest import Client as TwilioClient
from supabase import create_client, Client as SupabaseClient
from datetime import datetime


# --- Twilio setup ---
account_sid = "AC3deb3c62e27c6ba875a60027eecdbf07"
auth_token = "463869573238202e805dbb5f1c899cf1"
twilio_whatsapp_number = "whatsapp:+14155238886"  # sandbox number

twilio_client = TwilioClient(account_sid, auth_token)

# --- Supabase setup ---
supabase_url = "https://rscfkcduopypdfznxlrt.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJzY2ZrY2R1b3B5cGRmem54bHJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE0NjQxNzUsImV4cCI6MjA2NzA0MDE3NX0.9kvWEmTGgrseB5h0VZqRNw32F1a5g1JukUBBrO116Qc"
supabase: SupabaseClient = create_client(supabase_url, supabase_key)

# --- Get all members ---
members = supabase.from_("members").select("*").execute().data

unpaid_members = []

# --- Date info ---
today = datetime.today().date()
current_month = today.month
current_year = today.year

# --- Find unpaid members (ANY unpaid payment) ---
for member in members:
    payments = supabase.from_("payments").select("*").eq("member_id", member['id']).execute().data

    if not payments:
        unpaid_members.append(member)
    else:
        for payment in payments:
            if not payment['is_paid']:
                unpaid_members.append(member)
                break  # stop checking other payments for this member



print(f"Unpaid members: {[m['name'] for m in unpaid_members]}")

# --- Send WhatsApp messages ---
for member in unpaid_members:
    msg = f"Hi {member['name']}, this is your friendly Chama reminder! Please remember to pay your contribution for this month. Thank you!"
    
    message = twilio_client.messages.create(
        from_=twilio_whatsapp_number,
        body=msg,
        to=f"whatsapp:{member['phone_number']}"
    )
    print(f"✅ Sent to {member['phone_number']} | SID: {message.sid}")

print("🎉 All done!")
