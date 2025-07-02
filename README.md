# Chama Payment Reminder Bot

A simple Supabase-powered backend for a WhatsApp bot that helps chama (group savings) members stay on top of their payments.  

---

## 📌 Project Overview

This project provides a lightweight, cloud-hosted database to manage:
- **Members** — people in the chama.
- **Payments** — payment records linked to each member.
- **Reminders** — automated reminder messages for upcoming or overdue payments.

The WhatsApp bot connects to this database to:
- Add new members when they join.
- Create payments with due dates.
- Send automated payment reminders.
- Mark payments as paid.

---

## 🗂️ Database Schema

**Tables:**

| Table     | Description                               |
|-----------|-------------------------------------------|
| `members` | Stores member details (name, phone number). |
| `payments`| Links payments to members with due amounts and status. |
| `reminders` | Stores reminder messages linked to payments. |

**Relationships:**

- `payments.member_id` → `members.id`
- `reminders.payment_id` → `payments.id`

---

## 🔑 Supabase Project

**Project URL:**

https://rscfkcduopypdfznxlrt.supabase.co

**Anon/Public API Key:**

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJzY2ZrY2R1b3B5cGRmem54bHJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE0NjQxNzUsImV4cCI6MjA2NzA0MDE3NX0.9kvWEmTGgrseB5h0VZqRNw32F1a5g1JukUBBrO116Qc

---

