# Service Industrialization Master Dashboard

A real-time macro monitoring dashboard tracking Energy (Constraints) | AI Tokens (Velocity) | Hard Assets (Trade).

## 🚀 Features

- **6-Pane Executive View** - Monitor all key macro indicators at once
- **Interactive Charts** - Hover, zoom, pan, and download visualizations
- **Live Data Simulation** - Parametric data generation with adjustable volatility
- **Professional Dark Theme** - Built with Plotly and Streamlit

## 📊 Dashboard Modules

1. **PHYSICS (Constraints)**: PJM Power Prices & Labor Arbitrage
2. **FACTORY (Velocity)**: Headless Web Traffic & Token GDP
3. **TRADE (Financials)**: Scarcity vs Abundance & CapEx Velocity

## 🛠️ Setup & Installation

### Local Development

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/service-industrialization-dashboard.git
cd service-industrialization-dashboard

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Deploy to Streamlit Cloud (FREE)

1. **Push your code to GitHub** (see below)
2. **Go to** [streamlit.io/cloud](https://streamlit.io/cloud)
3. **Click "New App"** and select your GitHub repository
4. **Select `app.py` as the main file**
5. **Click "Deploy"** - Your app is now live!

## 📤 GitHub Setup (First Time)

```bash
# Initialize git in your project directory
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Service Industrialization Dashboard"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/service-industrialization-dashboard.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 📝 File Structure

```
service-industrialization-dashboard/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # (Optional) Git ignore file
```

## 🎨 Customization

Edit the sidebar in `app.py` to adjust:
- **Date Range**: Change default start/end dates
- **Volatility**: Adjust market noise level
- **Colors**: Modify Plotly color scheme
- **Metrics**: Add your own KPIs

## 📞 Support

For issues or questions, open a GitHub issue or check Streamlit documentation.


## 📚 Indicator Glossary

### PHYSICS Module: Energy Constraints

**1. PJM Power Price** (The Ashburn Gap)

For detailed explanations and investment insights for each indicator, see [INDICATORS.md](INDICATORS.md).
- **What it measures:** Real-time electricity costs in the Pennsylvania-New Jersey-Maryland power grid, critical infrastructure serving major data center regions
- - **Why it matters:** Shows whether electricity—a hard constraint on AI and compute capacity—is becoming scarcer (rising prices) or more abundant (falling prices)
  - - **For investors:** This is the "ceiling on AI expansion." Rising power prices signal that energy infrastructure is a bottleneck; falling prices enable more computation
   
    - **2. Labor Arbitrage Ratio** (Deflation Factor)
    - - **What it measures:** The ratio of human worker wages to the cost of AI token computation
      - - **Why it matters:** Tracks whether AI compute is getting cheaper faster than human labor, driving automation decisions
        - - **For investors:** High and rising = AI becomes cost-effective vs hiring; falling = human labor regains competitiveness
         
          - ### FACTORY Module: Velocity & Growth
         
          - **3. Agent Traffic** (The Headless Web)
          - - **What it measures:** Percentage of web traffic driven by autonomous AI agents (bots) vs human users
            - - **Why it matters:** Captures the shift from human-driven to machine-driven economic activity; higher percentages mean AI systems taking autonomous actions at scale
              - - **For investors:** Leading indicator of AI adoption maturity; shows economy moving from "AI as tool" to "AI as economic actor"
               
                - **4. Token GDP** (Global Token Output)
                - - **What it measures:** Synthetic measure of total computational tokens (AI work units) generated across all systems, measured in trillions
                  - - **Why it matters:** Like GDP for the AI economy; grows as compute capacity and training data expand
                    - - **For investors:** Growing Token GDP = expanding AI productive capacity and economic activity
                     
                      - ### TRADE Module: Asset Allocation
                     
                      - **5. Scarcity vs Abundance Spread** (Visser Framework)
                      - - **What it measures:** Ratio of hard assets (scarce physical resources: power, chips, land) to soft assets (abundant digital resources: software, data, tokens)
                        - - **Why it matters:** Drives fundamental investment allocation; above 1 = hard assets winning, below 1 = soft assets winning
                          - - **For investors:** Choose between semiconductor/power companies (hard scarcity) or AI software/digital platforms (soft abundance)
                           
                            - **6. Socket-to-Seat Ratio** (Capital vs Operating Commitment)
                            - - **What it measures:** Capital expenditure growth (sockets = new infrastructure) divided by operating expenditure decline (seats = labor/offices)
                              - - **Why it matters:** Rising ratio = companies building expensive infrastructure (GPUs, data centers) while cutting operational costs (fewer employees)
                                - - **For investors:** Reflects structural shift from employment to capital-intensive economy
                                 
                                  - ---
## 📄 License

MIT License - Feel free to fork and modify!
