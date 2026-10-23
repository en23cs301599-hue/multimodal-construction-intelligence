import json
import streamlit as st

from PIL import Image
from modules.gemini_client import analyze_ppe


st.set_page_config(
    page_title="Multimodal Construction Intelligence",
    page_icon="🏗️",
    layout="wide"
)


# =============================
# SIDEBAR
# =============================

st.sidebar.title("🏗️ Construction AI")

st.sidebar.subheader("🔐 Gemini Configuration")

api_key = st.sidebar.text_input(
    "Gemini API Key",
    type="password"
)

if api_key:
    st.sidebar.success("Gemini API key entered")
else:
    st.sidebar.info(
        "Enter your Gemini API key to enable AI analysis."
    )


st.sidebar.divider()

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


# =============================
# DASHBOARD
# =============================

if page == "🏠 Dashboard":

    st.title("🏗️ Multimodal Construction Intelligence Platform")

    st.markdown(
        """
        ### AI-Powered Construction Decision Support

        This platform provides AI-assisted tools for:

        - 🦺 PPE Safety Audit
        - 🧱 Concrete Crack Diagnostics
        - 💰 Project Planning & Real Estate Valuation
        - 🌦️ Weather-Aware Site Advisory
        - 🤖 Construction Engineering Assistant
        """
    )

    st.info(
        "This is an AI-assisted decision-support system. "
        "It does not replace qualified safety, structural, "
        "or engineering professionals."
    )

    st.divider()

    st.subheader("📊 Platform Modules")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("PPE Audit", "Ready")

    with col2:
        st.metric("Crack Diagnostics", "Ready")

    with col3:
        st.metric("Valuation", "Ready")

    with col4:
        st.metric("Weather Advisory", "Ready")


# =============================
# PPE SAFETY
# =============================

elif page == "🦺 Site Safety & PPE":

    st.header("🦺 Site Safety & PPE Audit")

    st.write(
        "Upload a construction-site image for "
        "AI-assisted PPE and hazard screening."
    )

    uploaded_file = st.file_uploader(
        "Upload construction site image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Construction Site",
            use_container_width=True
        )

        if st.button("🔍 Analyze PPE"):

            if not api_key:

                st.warning(
                    "Please enter your Gemini API key "
                    "in the sidebar."
                )

            else:

                with st.spinner(
                    "Analyzing construction site..."
                ):

                    result = analyze_ppe(
                        image,
                        api_key
                    )

                if "error" in result:

                    st.error(
                        f"Analysis failed: {result['error']}"
                    )

                else:

                    st.success(
                        "PPE analysis completed!"
                    )

                    st.subheader("📊 Safety Assessment")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Safety Score",
                            f"{result.get('safety_score', 0)}/100"
                        )

                    with col2:

                        st.metric(
                            "Overall Status",
                            result.get(
                                "overall_status",
                                "Unknown"
                            )
                        )

                    st.divider()

                    st.subheader("🦺 PPE Detection")

                    ppe = result.get(
                        "ppe_detection",
                        {}
                    )

                    for item, details in ppe.items():

                        status = details.get(
                            "status",
                            "Unknown"
                        )

                        compliance = details.get(
                            "compliance",
                            False
                        )

                        if compliance:

                            st.success(
                                f"✅ "
                                f"{item.replace('_', ' ').title()}: "
                                f"{status}"
                            )

                        else:

                            st.warning(
                                f"⚠️ "
                                f"{item.replace('_', ' ').title()}: "
                                f"{status}"
                            )

                    st.divider()

                    st.subheader("⚠️ Identified Hazards")

                    hazards = result.get(
                        "hazards",
                        []
                    )

                    if hazards:

                        for hazard in hazards:

                            st.warning(
                                f"""
**{hazard.get('hazard', 'Unknown hazard')}**

Severity: **{hazard.get('severity', 'Unknown')}**

Remedy: {hazard.get('remedy', 'No remedy provided')}
"""
                            )

                    else:

                        st.success(
                            "No obvious hazards were identified."
                        )

                    st.divider()

                    st.subheader("📄 JSON Report")

                    json_report = json.dumps(
                        result,
                        indent=4
                    )

                    st.download_button(
                        "⬇️ Download JSON Report",
                        data=json_report,
                        file_name="ppe_safety_report.json",
                        mime="application/json"
                    )


# =============================
# CRACK DIAGNOSTICS
# =============================

elif page == "🧱 Crack Diagnostics":

    st.header("🧱 Crack Diagnostics")

    uploaded_file = st.file_uploader(
        "Upload concrete/wall surface image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Concrete / Wall Surface",
            use_container_width=True
        )

        st.info(
            "AI crack classification will be connected "
            "in the next module."
        )


# =============================
# PLANNING & VALUATION
# =============================

elif page == "💰 Planning & Valuation":

    st.header(
        "💰 Project Planning & Real Estate Valuation"
    )

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
        [
            "Tier 1",
            "Tier 2",
            "Tier 3"
        ]
    )

    completion = st.slider(
        "Construction Completion (%)",
        0,
        100,
        25
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Structure",
            structure
        )

    with col2:
        st.metric(
            "Built-up Area",
            f"{sqft:,} sqft"
        )

    with col3:
        st.metric(
            "Completion",
            f"{completion}%"
        )


# =============================
# WEATHER ASSISTANT
# =============================

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


# =============================
# CHATBOT
# =============================

elif page == "🤖 Construction Chatbot":

    st.header(
        "🤖 Construction Engineering Assistant"
    )

    question = st.text_input(
        "Ask a construction-related question"
    )

    if question:

        st.info(
            "Gemini-powered chatbot will be connected "
            "in the next development step."
        )
