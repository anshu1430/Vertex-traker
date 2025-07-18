
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vortex Spin Tracker", layout="centered")
st.title("🎯 Vortex Spin Pattern Tracker")

if "spins" not in st.session_state:
    st.session_state.spins = []

with st.form("spin_form"):
    spin_no = len(st.session_state.spins) + 1
    symbol = st.text_input("Enter Spin Symbol (e.g., Crown, Star, Heart)")
    submitted = st.form_submit_button("Add Spin")

    if submitted and symbol.strip():
        st.session_state.spins.append({"Spin No": spin_no, "Symbol": symbol.strip().title()})

if st.session_state.spins:
    df = pd.DataFrame(st.session_state.spins)
    st.subheader("📈 Spin History")
    st.dataframe(df, use_container_width=True)

    freq = df["Symbol"].value_counts().reset_index()
    freq.columns = ["Symbol", "Frequency"]
    st.subheader("🔍 Symbol Frequency")
    st.dataframe(freq, use_container_width=True)

    top_symbol = freq.iloc[0]
    if top_symbol[1] >= 3:
        st.success(f"🔥 '{top_symbol[0]}' is appearing frequently! Might be time to increase your bet.")
else:
    st.info("Enter your first spin result to begin tracking.")
