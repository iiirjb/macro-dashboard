import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="Service Industrialization Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 32px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("⚙️ Dashboard Controls")
st.sidebar.markdown("---")

# Simulation parameters
st.sidebar.subheader("📈 Data Parameters")
start_date = st.sidebar.date_input("Start Date", value=pd.Timestamp('2024-01-01'))
end_date = st.sidebar.date_input("End Date", value=pd.Timestamp('2026-02-01'))
volatility = st.sidebar.slider("Market Volatility", 0.1, 2.0, 1.0, step=0.1)

st.sidebar.markdown("---")
st.sidebar.subheader("💡 About This Dashboard")
st.sidebar.markdown("""
This is the **Sunday Night Protocol** - a macro dashboard monitoring:
- **PHYSICS**: Energy constraints (PJM Power)
- **VELOCITY**: AI token GDP growth
- **TRADE**: Hard vs Soft assets (Visser's Framework)
""")

# ============================================
# DATA GENERATION
# ============================================
@st.cache_data
def generate_data(start, end, vol):
    dates = pd.date_range(start=start, end=end, freq='W')
    n = len(dates)

    # --- MODULE 1: CONSTRAINTS ---
    base_power = 38 + np.random.normal(0, 5*vol, n)
    spike_start = int(n * 0.65)
    power_prices = base_power.copy()
    power_prices[spike_start:] += np.linspace(0, 300, n - spike_start)

    # Labor Arbitrage
    human_wage = np.linspace(42, 45, n)
    token_cost = 25 * np.exp(-0.03 * np.arange(n))
    arbitrage_ratio = human_wage / token_cost

    # --- MODULE 2: VELOCITY ---
    agent_traffic = np.linspace(1.5, 9.2, n) + np.random.normal(0, 0.2*vol, n)
    token_gdp = 12 * np.exp(0.025 * np.arange(n))

    # --- MODULE 3: THE TRADE ---
    scarcity_index = 100 * np.exp(0.02 * np.arange(n)) + np.random.normal(0, 3*vol, n)
    abundance_index = 100 + np.random.normal(0, 5*vol, n) - (0.05 * np.arange(n))
    scarcity_spread = scarcity_index / abundance_index

    # CapEx Velocity
    capex_growth = np.linspace(10, 45, n)
    opex_growth = np.linspace(10, 2, n)
    socket_seat_ratio = capex_growth / opex_growth

    return {
        'dates': dates,
        'power_prices': power_prices,
        'arbitrage_ratio': arbitrage_ratio,
        'agent_traffic': agent_traffic,
        'token_gdp': token_gdp,
        'scarcity_spread': scarcity_spread,
        'socket_seat_ratio': socket_seat_ratio
    }

data = generate_data(start_date, end_date, volatility)

# ============================================
# MAIN DASHBOARD
# ============================================
st.title("🚀 SERVICE INDUSTRIALIZATION MASTER DASHBOARD")
st.markdown("""
**The 2026 Macro Monitor**: Energy (Constraints) | AI Tokens (Velocity) | Hard Assets (Trade)
*Last updated: {}*
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
st.markdown("---")

# Key Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("💡 PJM Power Price", f"${data['power_prices'][-1]:.0f}/MWh",
              f"+{data['power_prices'][-1] - data['power_prices'][-5]:.0f}")
with col2:
    st.metric("🤖 Labor Arbitrage", f"{data['arbitrage_ratio'][-1]:.1f}x",
              f"+{data['arbitrage_ratio'][-1] - data['arbitrage_ratio'][-5]:.2f}x")
with col3:
    st.metric("🌐 Agent Traffic", f"{data['agent_traffic'][-1]:.1f}%",
              f"+{data['agent_traffic'][-1] - data['agent_traffic'][-5]:.1f}%")
with col4:
    st.metric("💰 Token GDP", f"${data['token_gdp'][-1]:.1f}T",
              f"+{(data['token_gdp'][-1] - data['token_gdp'][-5])/data['token_gdp'][-5]*100:.1f}%")

st.markdown("---")

# Create 6-pane dashboard
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=("1. PHYSICS: The Ashburn Gap (PJM Power Price)",
                    "2. ECONOMICS: Deflation Factor (Labor Arbitrage)",
                    "3. THROUGHPUT: The Headless Web (Agent Traffic)",
                    "4. GROWTH: Global Token GDP (Trillions)",
                    "5. THE TRADE: Scarcity (Hard) vs Abundance (Soft)",
                    "6. COMMITMENT: The Socket-to-Seat Ratio"),
    specs=[[{}, {}], [{}, {}], [{}, {}]],
    vertical_spacing=0.12,
    horizontal_spacing=0.15
)

# Chart 1: Power Prices
fig.add_trace(
    go.Scatter(x=data['dates'], y=data['power_prices'], name="PJM Power Price",
               fill='tozeroy', fillcolor='rgba(255, 245, 0, 0.2)',
               line=dict(color='#FFF500', width=2), hovertemplate='<b>Power Price</b><br>%{x|%Y-%m-%d}<br>$%{y:.2f}/MWh<extra></extra>'),
    row=1, col=1
)
fig.add_hline(y=38, line_dash="dash", line_color="red", row=1, col=1)

# Chart 2: Labor Arbitrage
fig.add_trace(
    go.Scatter(x=data['dates'], y=data['arbitrage_ratio'], name="Labor Arbitrage Ratio",
               line=dict(color='#00FF00', width=2), hovertemplate='<b>Arbitrage Ratio</b><br>%{x|%Y-%m-%d}<br>%{y:.2f}x<extra></extra>'),
    row=1, col=2
)

# Chart 3: Agent Traffic
fig.add_trace(
    go.Scatter(x=data['dates'], y=data['agent_traffic'], name="Agent Traffic %",
               line=dict(color='#00BFFF', width=2), hovertemplate='<b>Agent Traffic</b><br>%{x|%Y-%m-%d}<br>%{y:.1f}%<extra></extra>'),
    row=2, col=1
)
fig.add_hline(y=10, line_dash="--", line_color="red", row=2, col=1)

# Chart 4: Token GDP (Bar)
fig.add_trace(
    go.Bar(x=data['dates'][::4], y=data['token_gdp'][::4], name="Token GDP",
           marker=dict(color='#9370DB', opacity=0.8), hovertemplate='<b>Token GDP</b><br>%{x|%Y-%m-%d}<br>$%{y:.1f}T<extra></extra>'),
    row=2, col=2
)

# Chart 5: Visser Spread
fig.add_trace(
    go.Scatter(x=data['dates'], y=data['scarcity_spread'], name="Scarcity / Abundance",
               line=dict(color='#FFD700', width=3), fill='tozeroy', fillcolor='rgba(255, 215, 0, 0.1)',
               hovertemplate='<b>Visser Spread</b><br>%{x|%Y-%m-%d}<br>%{y:.2f}<extra></extra>'),
    row=3, col=1
)
fig.add_hline(y=1, line_dash="--", line_color="white", row=3, col=1)

# Chart 6: Socket-to-Seat
fig.add_trace(
    go.Scatter(x=data['dates'], y=data['socket_seat_ratio'], name="Socket-to-Seat Ratio",
               line=dict(color='#FF69B4', width=2),
               hovertemplate='<b>Socket-to-Seat</b><br>%{x|%Y-%m-%d}<br>%{y:.2f}<extra></extra>'),
    row=3, col=2
)
fig.add_hline(y=1, line_dash="--", line_color="white", row=3, col=2)

# Styling
fig.update_layout(
    title_text="",
    template='plotly_dark',
    height=1200,
    width=1600,
    showlegend=False,
    paper_bgcolor='#1a1a1a',
    plot_bgcolor='rgba(0,0,0,0.5)',
    font=dict(family="Courier New, monospace", size=11, color='white'),
    hovermode='x unified'
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)')
fig.for_each_annotation(lambda a: a.update(font=dict(size=11, color='white')))

st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
📊 Service Industrialization Dashboard | Built with Streamlit + Plotly<br>
Data refreshes weekly | Questions? Check the sidebar ⚙️
</div>
""", unsafe_allow_html=True)
