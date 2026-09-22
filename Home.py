import streamlit as st


st.set_page_config(
    page_title="World Cities Dashboard",
    page_icon="🌍",
    layout="wide",
)


st.title("Welcome to the World Cities Dashboard!")
st.write(
    "This application allows you to explore and visualize data about cities around "
    "the world. You can filter cities by population, capital status, and country to "
    "gain insights into global urbanization patterns."
)

st.header("Features:")
st.markdown(
    """
- 📊 Interactive population filtering
- 🏛️ Capital city selection
- 🌍 Map visualization
- 📈 Population analysis charts
- 📋 Detailed city information
"""
)

st.write(
    "Get started by navigating to the **World Cities** page to explore the data!"
)

st.divider()

st.header("🚀 Get Started")

# Center the navigation button and make it prominent, matching the welcoming layout.
_, button_column, _ = st.columns([1, 2, 1])
with button_column:
    if st.button(
        "🔑 Explore World Cities",
        type="primary",
        use_container_width=True,
    ):
        st.switch_page("pages/app.py")
