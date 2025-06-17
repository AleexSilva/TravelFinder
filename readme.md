# TravelFinder Pro - Deployment Guide

This guide covers various deployment options for TravelFinder Pro, from local development to cloud production.

## Prerequisites

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 1GB free disk space
- Internet connection for scraping

### Required Packages
```bash
pip install streamlit>=1.28.0 pandas>=1.5.0 plotly>=5.15.0 requests>=2.31.0 beautifulsoup4>=4.12.0 selenium>=4.15.0
```

## Local Development Setup

### 1. Quick Start
```bash
# Clone/download the project
cd travel-scraper

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### 2. Development Environment
```bash
# Create virtual environment
python -m venv travel_scraper_env
source travel_scraper_env/bin/activate  # On Windows: travel_scraper_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_scraper.py

# Start development server
streamlit run app.py --server.runOnSave true
```

## Cloud Deployment Options

### 1. Streamlit Community Cloud (Recommended)

**Steps:**
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy your repository
5. Your app will be available at `https://username-travel-scraper-app-xyz.streamlit.app`

**Benefits:**
- Free hosting
- Automatic deployments
- SSL certificates
- Easy sharing

### 2. Heroku Deployment

**Create additional files:**

`Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```