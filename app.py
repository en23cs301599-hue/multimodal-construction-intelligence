import streamlit as st

st.set_page_config(
    page_title="Multimodal Construction Intelligence",
    page_icon="🏗️",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------

st.title("🏗️ Multimodal Construction Intelligence Platform")

st.markdown(
    """
    **AI-powered construction decision-support system**

    Use this platform for:
    - 🦺 PPE Safety Audit
    - 🧱 Concrete Crack Diagnostics
    - 💰 Project Planning & Real Estate Valuation
    - 🌦️ Weather-Aware Site Advisory
    - 🤖 Construction Engineering Assistant
    """
)

st.info(
    "This platform provides AI-assisted decision support. "
    "It does not replace qualified safety, structural, or engineering professionals."
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🏗️ Construction AI")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "🦺 Site Safety & PPE",
        "🧱 Crack Diagnostics",
        "💰 Planning & Valuation",
        "🌦️ Daily Site Assistant",
        "🤖 Construction Chatbot"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------

if page == "🏠 Dashboard":

    st.header("Project Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("PPE Audit", "Ready")

    with col2:
        st.metric("Crack Diagnostics", "Ready")

    with col3:
        st.metric("Valuation", "Ready")

    with col4:
        st.metric("Weather Advisory", "Ready")

    st.divider()

    st.subheader("System Architecture")

    st.code(
        """
User
  │
  ▼
Streamlit Interface
  │
  ├── PPE Safety Audit
  │       └── Gemini Vision
  │
  ├── Crack Diagnostics
  │       └── Gemini Vision
  │
  ├── Planning & Valuation
  │       └── Calculation Engine
  │
  ├── Weather Advisory
  │       └── Safety Protocol Engine
  │
  └── Construction Chatbot
          └── Gemini AI
        """
    )

# -----------------------------
# PPE Safety
# -----------------------------

elif page == "🦺 Site Safety & PPE":

    st.header("🦺 Site Safety & PPE Audit")

    uploaded_file = st.file_uploader(
        "Upload a construction site image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Construction Site",
            use_container_width=True
        )

        st.success("Image uploaded successfully.")

        if st.button("🔍 Analyze PPE"):

            st.warning(
                "Gemini Vision integration will be added in the next development step."
            )

# -----------------------------
# Crack Diagnostics
# -----------------------------

elif page == "🧱 Crack Diagnostics":

    st.header("🧱 Crack Diagnostics & Structural Integrity")

    uploaded_file = st.file_uploader(
        "Upload concrete/wall surface image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Concrete / Wall Surface",
            use_container_width=True
        )

        if st.button("🔍 Analyze Crack"):

            st.warning(
                "AI crack diagnostics will be connected in the next development step."
            )

# -----------------------------
# Planning
# -----------------------------

elif page == "💰 Planning & Valuation":

    st.header("💰 Project Planning & Real Estate Valuation")

    structure = st.selectbox(
        "Structure Type",
        [
            "Residential Building",
            "Commercial Building",
            "Industrial Building",
            "Apartment",
            "Villa"
        ]
    )

    sqft = st.number_input(
        "Built-up Area (sqft)",
        min_value=100,
        value=1000,
        step=100
    )

    tier = st.selectbox(
        "Location Tier",
        ["Tier 1", "Tier 2", "Tier 3"]
    )

    completion = st.slider(
        "Construction Completion (%)",
        0,
        100,
        25
    )

    st.subheader("Project Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Structure", structure)

    with col2:
        st.metric("Built-up Area", f"{sqft:,} sqft")

    with col3:
        st.metric("Completion", f"{completion}%")

# -----------------------------
# Weather Assistant
# -----------------------------

elif page == "🌦️ Daily Site Assistant":

    st.header("🌦️ Daily Site Assistant")

    weather = st.selectbox(
        "Current Weather Condition",
        [
            "Normal",
            "High Wind",
            "Heavy Rain",
            "Extreme Heat"
        ]
    )

    if weather == "High Wind":

        st.warning(
            """
            ⚠️ HIGH WIND

            Recommended precautions:

            • Review crane operations  
            • Secure loose construction materials  
            • Restrict unsafe elevated work  
            • Inspect temporary structures
            """
        )

    elif weather == "Heavy Rain":

        st.warning(
            """
            🌧️ HEAVY RAIN

            Recommended precautions:

            • Protect electrical equipment  
            • Control water accumulation  
            • Inspect site access routes  
            • Protect concrete from excessive water exposure
            """
        )

    elif weather == "Extreme Heat":

        st.warning(
            """
            🌡️ EXTREME HEAT

            Recommended precautions:

            • Provide adequate drinking water  
            • Schedule suitable work/rest periods  
            • Monitor workers for heat-related illness  
            • Follow appropriate concrete curing procedures
            """
        )

    else:

        st.success(
            "Normal conditions. Continue standard site safety procedures."
        )

# -----------------------------
# Chatbot
# -----------------------------

elif page == "🤖 Construction Chatbot":

    st.header("🤖 Construction Engineering Assistant")

    question = st.text_input(
        "Ask a construction-related question"
    )

    if question:

        st.info(
            "Gemini-powered chatbot will be connected in the next development step."
        )
