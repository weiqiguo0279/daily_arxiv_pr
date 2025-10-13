
# Daily arXiv – AI Research Tracker 📚🤖

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-cs.AI-b31b1b.svg)](https://arxiv.org/list/cs.AI/recent)

**English Document** | [中文文档](README_zh.md)

Automatically track the latest AI research papers on arXiv each day, use LLMs for intelligent summarization, and generate research trend analysis reports.

## ✨ Features

### Core Functions

- 🔍 **Intelligent Crawling**: Daily automatic fetching of the newest papers from arXiv in specified fields  
  - Supports multiple research areas (cs.AI, cs.LG, cs.CV, etc.)  
  - Keyword filtering  
  - TF‑IDF based smart selection  

- 🤖 **Multi‑Model Summarization**: Use LLMs to generate concise paper summaries  
  - Supports 5 LLM providers: OpenAI, Gemini, Claude, DeepSeek, vLLM  
  - Bilingual (Chinese & English) summaries  
  - Concurrent processing for higher efficiency  

- 📊 **Trend Analysis**: In‑depth analysis of research hot topics and technological trends  
  - TF‑IDF keyword extraction  
  - LDA topic modeling  
  - Word‑cloud visualization  
  - LLM deep analysis (research hotspots, technology trends, future directions)  

- 🌐 **Web Interface**: Modern responsive web UI  
  - Built with Bootstrap 5  
  - Real‑time data display  
  - Detailed paper view  
  - Pagination and filtering  

- ⏰ **Scheduled Execution**: Various scheduling options  
  - APScheduler (recommended)  
  - Linux cron jobs  
  - Systemd service  

- 📧 **Email Notifications**: Execution status via email  
  - Elegant HTML email templates  
  - Separate success/failure notices  
  - Detailed statistics  

## 📸 Interface Preview

```
┌─────────────────────────────────────────────────────────┐
│  📊 Statistics Overview                                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │ 📄 Papers│ │ 📝 Summaries│ │ 🏷️ Categories│ │ 🔑 Keywords│   │
│  │   20    │ │   20    │ │    2    │ │   50   │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │
├─────────────────────────────────────────────────────────┤
│  📊 Trend Analysis   │  📚 Paper List                     │
├─────────────────────────────────────────────────────────┤
│  🌐 Word Cloud                                          │
│  [WordCloud visualization]                              │
│                                                          │
│  🔥 Research Hotspots                                    │
│  • transformer (0.85)                                    │
│  • large language model (0.72)                           │
│                                                          │
│  📈 Technology Trends                                    │
│  [LLM‑generated analysis content]                        │
├─────────────────────────────────────────────────────────┤
│  Paper Card                                             │
│  ┌───────────────────────────────────────────────────┐ │
│  │ 📄 Attention Is All You Need                       │ │
│  │ 👥 Authors: Vaswani et al.                         │ │
│  │ 📅 2017‑06‑12                                      │ │
│  │ 📝 [Abstract preview …]                            │ │
│  │ [View Details] [arXiv Original]                   │ │
│  └───────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Conda (recommended) or virtualenv
- LLM API keys (OpenAI / Gemini / Claude / DeepSeek / vLLM)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/daily-arxiv.git
cd daily-arxiv
```

### 2. Create a virtual environment

```bash
# Using Conda (recommended)
conda create -n daily-arxiv python=3.12 -y
conda activate daily-arxiv

# Or using venv
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install uv
uv pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file
nano .env
```

Add your API keys:

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# Google Gemini
GEMINI_API_KEY=...

# Anthropic Claude
ANTHROPIC_API_KEY=...

# DeepSeek
DEEPSEEK_API_KEY=...

# vLLM (local deployment)
VLLM_API_KEY=EMPTY

# Email notifications (optional)
EMAIL_PASSWORD=your-app-password
```

### 5. Configure `config.yaml`

Edit `config/config.yaml`:

```yaml
# Research fields
arxiv:
  categories:
    - "cs.AI"  # Artificial Intelligence
    - "cs.LG"  # Machine Learning
  
  keywords:
    - "large language model"
    - "transformer"
  
  max_results: 20

# LLM provider
llm:
  provider: "vllm"  # openai, gemini, claude, deepseek, vllm

# Scheduler settings
scheduler:
  enabled: true
  run_time: "09:00"
  timezone: "Asia/Shanghai"
```

### 6. Run tests

```bash
# Test paper fetching
python test_fetcher.py

# Test LLM summarization
python test_summarizer.py

# Test trend analysis
python test_analyzer.py

# Test web service
python test_web.py

# Test scheduler
python test_scheduler.py
```

### 7. Execute the full workflow

```bash
# Manual single run
python main.py
```

### 8. Start the web service

```bash
# Development mode
python src/web/app.py

# Open http://localhost:5000
```

### 9. Launch scheduled execution

```bash
# Recommended: use the start script
./deploy/start.sh

# Or run directly
python scheduler.py
```

Visit http://localhost:5000 to view results.

## 📂 Project Structure

```
daily-arxiv/
├── config/
│   └── config.yaml              # Main configuration file
├── src/
│   ├── crawler/
│   │   └── arxiv_fetcher.py    # arXiv paper crawler
│   ├── summarizer/
│   │   ├── base_llm_client.py  # Base LLM class
│   │   ├── openai_client.py    # OpenAI client
│   │   ├── gemini_client.py    # Gemini client
│   │   ├── claude_client.py    # Claude client
│   │   ├── deepseek_client.py  # DeepSeek client
│   │   ├── vllm_client.py      # vLLM client
│   │   ├── llm_factory.py      # LLM factory
│   │   └── paper_summarizer.py # Paper summarizer
│   ├── analyzer/
│   │   └── trend_analyzer.py   # Trend analysis
│   ├── web/
│   │   ├── app.py             # Flask web app
│   │   └── templates/
│   │       └── index.html     # Web UI page
│   ├── notifier/
│   │   └── email_notifier.py  # Email notifier
│   └── utils.py               # Utility functions
├── static/
│   └── js/
│       └── main.js            # Front‑end JavaScript
├── data/                      # Data storage
│   ├── papers/               # Paper JSON files
│   ├── summaries/            # Summary JSON files
│  ──/ # word‑cloud images
├── logs/                     # Log files
├── deploy/                   # Deployment scripts
│   ├── start.sh             # Start script
│   ├── daily-arxiv.service  # Systemd service
│   └── crontab.example      # Cron example
├── docs/                     # Documentation
│   ├── arxiv_fetcher_guide.md
│   ├── trend_analyzer_guide.md
│   ├── web_interface_guide.md
│   └── scheduler_guide.md
├── main.py                   # Main entry point
├── scheduler.py              # APScheduler dispatcher
├── test_*.py                # Test scripts
├── requirements.txt         # Python dependencies
├── .env.example            # Example env file
└── README.md               # Project overview
```

## ⚙️ Configuration Details

### arXiv Category Codes

Common Computer Science categories:  
- `cs.AI` – Artificial Intelligence  
- `cs.LG` – Machine Learning  
- `cs.CV` – Computer Vision  
- `cs.CL` – Computation and Language (NLP)  
- `cs.NE` – Neural and Evolutionary Computing  
- `stat.ML` – Machine Learning (Statistics)  

See the full list at: https://arxiv.org/category_taxonomy

### LLM Providers

Supported providers:  
- **OpenAI**: GPT‑4, GPT‑3.5‑turbo  
- **Gemini**: Gemini models  
- **Anthropic**: Claude  
- **DeepSeek**: DeepSeek models  
- **vLLM**: Locally run open‑source models (OpenAI‑compatible API)

## 📝 Development Roadmap

- [x] Project scaffolding ✅  
- [x] arXiv crawling ✅  
- [x] LLM summarization ✅  
  - Support OpenAI, Gemini, Claude, DeepSeek, vLLM  
- [x] Trend analysis ✅  
  - Keyword extraction, topic modeling, word‑cloud generation  
  - LLM‑driven deep analysis (hotspots, trends, innovations)  
- [x] Web UI development  
- [x] Scheduling functionality  
- [x] Testing & optimization  
- [ ] UI beautification  
- [ ] Add WeChat public account integration  

## 🧪 Testing

```bash
# Test paper crawler
python test_fetcher.py

# Test summarizer
python test_summarizer.py

# Test trend analyzer
python test_analyzer.py

# Run full pipeline
python main.py
```

## 📊 Generated Files

```
data/
├── papers/
│   ├── papers_YYYY-MM-DD.json   # Daily paper data
│   └── latest.json              # Latest paper data
├── summaries/
│   ├── summaries_YYYY-MM-DD.json# Daily summaries
│   └── latest.json              # Latest summaries
└── analysis/
    ├── wordcloud_YYYY-MM-DD.png # Word‑cloud image
    ├── analysis_YYYY-MM-DD.json # Analysis results
    ├── report_YYYY-MM-DD.md     # Markdown report
    └── latest.json              # Latest analysis data
```

## 📖 Documentation

- [Paper Crawler Guide](docs/arxiv_fetcher_guide.md)  
- [LLM Summarizer Guide](docs/llm_guide.md)  
- [Configuration Guide](docs/config_guide.md)

## 🤝 Contributing

Feel free to open Issues and submit Pull Requests!

## 📄 License

MIT License