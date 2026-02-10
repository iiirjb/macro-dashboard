import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="S&P 500 2029 Scenario Builder", layout="wide")

st.title("S&P 500: Feb 2029 Forward Projection")
st.markdown("""
This tool models the S&P 500 Index for **February 2029** (3-year horizon).
It assumes the **Annual EPS Growth Rate** you input compounds over the full 3-year window.
""")

# --- 1. BASELINE DATA (Feb 2026) ---
data = {
    'Sector': [
        'Info Tech', 'Financials', 'Health Care', 'Cons Discret', 
        'Comm Svcs', 'Industrials', 'Cons Staples', 'Energy', 
        'Utilities', 'Real Estate', 'Materials'
    ],
    'Weight': [0.315, 0.130, 0.120, 0.100, 0.090, 0.085, 0.060, 0.035, 0.025, 0.025, 0.020],
    'Current_PE': [31.0, 15.5, 19.0, 26.5, 21.5, 23.0, 20.5, 12.5, 19.0, 18.0, 20.0]
}

df_base = pd.DataFrame(data)
SP500_BASE_PRICE = 6858.47
# Calculate Base EPS based on the current price and a baseline P/E of 22
SP500_BASE_EPS = SP500_BASE_PRICE / 22.0 

# --- 2. SIDEBAR INPUTS ---
st.sidebar.header("Feb 2029 Assumptions")

apply_global = st.sidebar.checkbox("Apply Global Assumptions?", value=False)

if apply_global:
    st.sidebar.subheader("Global Settings")
    # Clarifying this is the annual rate that will compound
    global_growth = st.sidebar.slider("Annual Earnings Growth CAGR (%)", -10, 30, 7, 1)
    global_pe = st.sidebar.slider("Target Forward P/E", 10.0, 35.0, 22.0, 0.5)

    user_growth = {sect: global_growth/100 for sect in df_base['Sector']}
    user_pe = {sect: global_pe for sect in df_base['Sector']}

else:
    st.sidebar.subheader("Sector Specific Settings")
    user_growth = {}
    user_pe = {}
    
    for index, row in df_base.iterrows():
        with st.sidebar.expander(f"{row['Sector']} ({row['Weight']:.1%})"):
            g = st.slider(f"Annual Growth % (CAGR)", -10, 40, 8, key=f"g_{index}")
            user_growth[row['Sector']] = g / 100
            user_pe[row['Sector']] = st.slider(f"Feb 2029 Target P/E", 5.0, 50.0, float(row['Current_PE']), 0.5, key=f"p_{index}")

# --- 3. CALCULATIONS (3-YEAR COMPOUNDING) ---
df_scenario = df_base.copy()
df_scenario['Annual_Growth_Rate'] = df_scenario['Sector'].map(user_growth)
df_scenario['Target_PE'] = df_scenario['Sector'].map(user_pe)

# We derive sector earnings contribution based on the weights and current P/Es
total_weight_pe_ratio = sum(df_base['Weight'] / df_base['Current_PE'])
df_scenario['Base_EPS_Contribution'] = (df_scenario['Weight'] / df_scenario['Current_PE'] / total_weight_pe_ratio) * SP500_BASE_EPS

# KEY CHANGE: Compound the growth over 3 years: (1 + r)^3
df_scenario['Scenario_EPS_Contribution'] = df_scenario['Base_EPS_Contribution'] * ((1 + df_scenario['Annual_Growth_Rate']) ** 3)

# Apply the forecast PE to the new 2029 earnings to get the spot level contribution
df_scenario['Scenario_Price_Contribution'] = df_scenario['Scenario_EPS_Contribution'] * df_scenario['Target_PE']

scenario_eps = df_scenario['Scenario_EPS_Contribution'].sum()
scenario_price = df_scenario['Scenario_Price_Contribution'].sum()
scenario_pe = scenario_price / scenario_eps if scenario_eps != 0 else 0

# --- 4. DISPLAY RESULTS ---
st.header("Feb 2029 Forecast")
col1, col2, col3 = st.columns(3)
col1.metric("2029 Implied SPX Price", f"{scenario_price:,.0f}", f"{((scenario_price/SP500_BASE_PRICE)-1)*100:.1f}% Total")
col2.metric("2029 Implied EPS", f"${scenario_eps:.2f}", f"{((scenario_eps/SP500_BASE_EPS)-1)*100:.1f}% Total")
col3.metric("2029 Implied P/E", f"{scenario_pe:.1f}x")

st.divider()

# Visualization
st.subheader("2026 Spot vs. 2029 Forecast Contribution")
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df_base['Sector'],
    y=df_base['Weight'] * SP500_BASE_PRICE,
    name='Feb 2026 Price Contribution',
    marker_color='gray'
))
fig.add_trace(go.Bar(
    x=df_scenario['Sector'],
    y=df_scenario['Scenario_Price_Contribution'],
    name='Feb 2029 Forecast Contribution',
    marker_color='green'
))

fig.update_layout(barmode='group', height=500)
st.plotly_chart(fig, use_container_width=True)

st.caption("Note: Growth rates compound annually for 3 years (2026-2029).")
