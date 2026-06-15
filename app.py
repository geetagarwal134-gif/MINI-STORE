import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# Product Data
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 79.99,
        "description": "Premium over-ear headphones with noise cancellation and 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "description": "Track your health, workouts, sleep, and notifications in real-time.",
        "category": "Wearables"
    },
    {
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "description": "RGB backlit keyboard with tactile switches.",
        "category": "Electronics"
    },
    {
        "name": "Minimalist Backpack",
        "price": 54.99,
        "description": "Stylish and durable backpack for work and travel.",
        "category": "Fashion"
    },
    {
        "name": "Portable Coffee Maker",
        "price": 39.99,
        "description": "Brew coffee anywhere with this compact coffee maker.",
        "category": "Home & Kitchen"
    },
    {
        "name": "LED Desk Lamp",
        "price": 29.99,
        "description": "Adjustable brightness and eye-care lighting.",
        "category": "Home & Kitchen"
    }
]

# Store products for chatbot access
st.session_state["products"] = products

# ---------------------------------------------------
# CSS Styling
# ---------------------------------------------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg,#4F46E5,#7C3AED);
    padding:40px;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.product-title{
    font-size:20px;
    font-weight:bold;
}

.product-price{
    color:green;
    font-weight:bold;
    margin-top:10px;
}

/* Floating Support Button */
.support-btn{
    position:fixed;
    bottom:25px;
    right:25px;
    background:#4F46E5;
    color:white;
    padding:15px 20px;
    border-radius:50px;
    text-decoration:none;
    font-weight:bold;
    box-shadow:0 4px 12px rgba(0,0,0,0.3);
    z-index:999;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Cart Summary")
st.sidebar.write("Items: 3")
st.sidebar.write("Total: $249.97")

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------
st.markdown("""
<div class="hero">
<h1>🛍️ MiniStore</h1>
<p>Your one-stop destination for quality products.</p>
</div>
""", unsafe_allow_html=True)

st.header("Welcome to MiniStore")

st.write(
    "Explore our featured collection of gadgets, fashion, and home essentials."
)

# ---------------------------------------------------
# Product Filter
# ---------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# ---------------------------------------------------
# Products Grid
# ---------------------------------------------------
st.header("Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered_products):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-title">{product['name']}</div>
            <div class="product-price">${product['price']}</div>
            <p>{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Add to Cart", key=i)

# ---------------------------------------------------
# Floating Support Button
# ---------------------------------------------------
st.markdown(
    """
    <a href="/Support_Chatbot" target="_self" class="support-btn">
        💬 Support
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.caption("© 2026 MiniStore")