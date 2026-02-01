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

## 📄 License

MIT License - Feel free to fork and modify!
