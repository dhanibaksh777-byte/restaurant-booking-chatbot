# The Coastal Grill — AI Restaurant Booking Chatbot

An AI-powered restaurant assistant that answers menu questions and books tables in natural conversation — no forms, no clicking through a calendar. Built as a portfolio demo with dummy restaurant data.

## Live Links

- **Website (frontend):** https://restaurant-booking-chatbot.vercel.app/
- **Backend API:** https://resturant-chatbot-597w.onrender.com/
- **Repo:** https://github.com/dhanibaksh777-byte/restaurant-booking-chatbot

> Backend is on Render's free tier — the first request after inactivity can take 20-30s to wake up.

## Screenshot

![Chatbot demo](https://github.com/dhanibaksh777-byte/restaurant-booking-chatbot/blob/0f244a31dedd1d9fe0d6953f5ac071696f67ac9c/Screenshot%202026-10-03%20223859.png)

## What it does

- **Menu Q&A** — ask about dishes, prices, or categories; answers come from a live database lookup, never guessed or invented
- **Table booking** — the bot collects name, phone, party size, and date/time through conversation, checks real table availability (accounting for party size and a 90-minute dining window), and confirms a booking
- **Conversation memory** — remembers context across messages in the same conversation (e.g. "tell me more about the salmon" works without re-stating the dish)

## How it works

The assistant runs on **Groq's `openai/gpt-oss-120b`** with function calling. Instead of hallucinating menu items or availability, the model calls two tools:

- `menu_lookup` — queries the database for dishes, filtered by category, keyword, or max price
- `book_table` — checks table availability for a given party size and time, then creates the booking if a table is free

Every user and assistant message is stored per conversation, so the bot has full context on follow-up questions.

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Alembic, PostgreSQL (Neon)
- **AI:** Groq (`openai/gpt-oss-120b`) with function calling
- **Frontend:** Plain HTML/CSS/JS, no framework
- **Deployment:** Backend on Render, frontend on Vercel

## Project Structure


restaurant-booking-chatbot/
├── main.py # FastAPI app, CORS middleware
├── database.py
├── models.py # Table, MenuItem, Booking, Conversation, Message
├── seed.py # Seeds dummy menu + table data
├── routers/
│ └── chat.py # POST /chat
├── services/
│ └── assistant.py # Core chat loop, tool-calling logic
├── tools/
│ ├── menu_lookup.py
│ └── booking.py # availability check + booking creation
└── alembic/


## Try it

Open the [live site](https://restaurant-booking-chatbot.vercel.app/), click the chat icon bottom-right, and try:
- "What mains do you have?"
- "Book a table for 2 at 8pm tomorrow, my name is [name], phone [number]"

---
*Demo project — all restaurant data (The Coastal Grill, San Diego) is fictional.*
