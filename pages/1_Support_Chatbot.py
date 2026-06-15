import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬",
    layout="wide"
)

st.title("💬 MiniStore Support Chatbot")

# ---------------------------------------------------
# Product Knowledge Base
# ---------------------------------------------------
products = st.session_state.get(
    "products",
    [
        {"name": "Wireless Bluetooth Headphones", "price": 79.99},
        {"name": "Smart Fitness Watch", "price": 129.99},
        {"name": "Mechanical Keyboard", "price": 89.99},
        {"name": "Minimalist Backpack", "price": 54.99},
        {"name": "Portable Coffee Maker", "price": 39.99},
        {"name": "LED Desk Lamp", "price": 29.99},
    ]
)

# ---------------------------------------------------
# Chat History
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I'm MiniStore Support. "
                "Ask me about products, delivery, returns, refunds, payments, or orders."
            )
        }
    ]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------------------------
# Rule-Based Chatbot Logic
# ---------------------------------------------------
def chatbot_response(user_message):

    message = user_message.lower()

    # Product Queries
    for product in products:
        if product["name"].lower() in message:
            return (
                f"📦 {product['name']} is available "
                f"for ${product['price']}."
            )

    if "product" in message:
        product_names = "\n".join(
            [f"• {p['name']}" for p in products]
        )
        return f"We currently sell:\n\n{product_names}"

    # Delivery
    if any(word in message for word in [
        "delivery",
        "shipping",
        "ship"
    ]):
        return (
            "🚚 Standard delivery takes 3–5 business days. "
            "Express delivery takes 1–2 business days."
        )

    # Refunds
    if "refund" in message:
        return (
            "💰 Refunds are processed within "
            "5–7 business days after approval."
        )

    # Returns
    if "return" in message:
        return (
            "↩️ Returns are accepted within 30 days "
            "of receiving the product."
        )

    # Payment
    if any(word in message for word in [
        "payment",
        "pay",
        "card",
        "upi"
    ]):
        return (
            "💳 We accept Credit Cards, Debit Cards, "
            "UPI, Net Banking, and PayPal."
        )

    # Order Status
    if any(word in message for word in [
        "order",
        "status",
        "track"
    ]):
        return (
            "📍 To check order status, provide your "
            "Order ID. (Demo version)"
        )

    # Greeting
    if any(word in message for word in [
        "hello",
        "hi",
        "hey"
    ]):
        return (
            "👋 Hello! How can I help you today?"
        )

    return (
        "I'm sorry, I didn't understand that. "
        "Try asking about products, delivery, refunds, "
        "returns, payments, or orders."
    )

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
if prompt := st.chat_input("Ask a question..."):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = chatbot_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)