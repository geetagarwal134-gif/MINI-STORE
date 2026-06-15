import streamlit as st
from openai import OpenAI

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore Support Chatbot",
    page_icon="💬",
    layout="wide"
)

st.title("💬 MiniStore AI Support")

# ---------------------------------------------------
# OpenAI Client
# ---------------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ---------------------------------------------------
# Product Catalog
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": "$79.99",
        "category": "Electronics",
        "description": "Premium over-ear headphones with noise cancellation and 30-hour battery life."
    },
    {
        "name": "Smart Fitness Watch",
        "price": "$129.99",
        "category": "Wearables",
        "description": "Track workouts, sleep, heart rate, and notifications."
    },
    {
        "name": "Mechanical Keyboard",
        "price": "$89.99",
        "category": "Electronics",
        "description": "RGB mechanical keyboard with tactile switches."
    },
    {
        "name": "Minimalist Backpack",
        "price": "$54.99",
        "category": "Fashion",
        "description": "Stylish and durable backpack for work and travel."
    },
    {
        "name": "Portable Coffee Maker",
        "price": "$39.99",
        "category": "Home & Kitchen",
        "description": "Compact coffee maker for home and travel."
    },
    {
        "name": "LED Desk Lamp",
        "price": "$29.99",
        "category": "Home & Kitchen",
        "description": "Adjustable brightness with eye-care lighting."
    }
]

# ---------------------------------------------------
# Build Product Knowledge
# ---------------------------------------------------
catalog_text = ""

for p in products:
    catalog_text += f"""
Product: {p['name']}
Category: {p['category']}
Price: {p['price']}
Description: {p['description']}
"""

# ---------------------------------------------------
# System Prompt
# ---------------------------------------------------
SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support representative.

Your responsibilities:
- Help customers with products
- Order status
- Delivery and shipping
- Refunds
- Returns
- Payment methods
- Store policies

Store Catalog:
{catalog_text}

Rules:
1. Only answer questions related to MiniStore.
2. Use the catalog information when discussing products.
3. If a user asks unrelated questions
   (science, coding, history, politics, math, etc.),
   politely redirect them back to MiniStore support topics.
4. Be professional, concise, and friendly.
5. Never invent products not listed in the catalog.
"""

# ---------------------------------------------------
# Session State Chat History
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 Welcome to MiniStore Support.\n\n"
                "I can help with:\n"
                "• Products\n"
                "• Orders\n"
                "• Delivery\n"
                "• Refunds\n"
                "• Returns\n"
                "• Payments"
            )
        }
    ]

# ---------------------------------------------------
# Display Chat History
# ---------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------
# User Input
# ---------------------------------------------------
if prompt := st.chat_input("Ask about products, orders, delivery, refunds..."):

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Build conversation
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    # Generate response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.3
    )

    assistant_reply = response.choices[0].message.content

    # Save response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    # Display response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)