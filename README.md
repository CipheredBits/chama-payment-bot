# 💸 Chama Payment Reminder Bot

This is a simple MVP WhatsApp bot for chama groups (savings groups) to help automate payment reminders.

---

## 📌 What it does

✅ Connects to a **Supabase** database with three tables:
- `members`: stores member names and phone numbers.
- `payments`: stores each member's payment status.

✅ Uses **Twilio’s WhatsApp API** to:
- Fetch all members with unpaid payments.
- Send each unpaid member a personalized WhatsApp reminder.

---

## ⚙️ How it works

1. **Supabase**  
   - Stores your members and payments.
   - Each payment has `is_paid = true/false`.

2. **Python script**  
   - Uses `supabase-py` to check who hasn’t paid.
   - Uses `twilio` to send WhatsApp messages via the Twilio Sandbox.

3. **Run locally**  
   ```bash
   python send_whatsapp_reminders.py

4. Member receives WhatsApp reminder
   - For example:
     Hi Test User! 👋 
This is your friendly ChamaBot.
Please remember to pay your contribution. Thank you!



