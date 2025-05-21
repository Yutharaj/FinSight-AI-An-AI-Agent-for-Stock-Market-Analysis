# 💹 FinSight-AI-An-AI-Agent-for-Stock-Market-Analysis

FinSight AI is a beginner-friendly stock market agent that fetches real-time stock data, visualizes recent performance, and uses OpenAI’s GPT to provide intelligent analysis.

## 🎯 Project Objective

This project was created as part of **Assignment II** for the **BSc in Applied Data Science Communication** program at **General Sir John Kotelawala Defence University**.

It demonstrates:
- Real-world AI application
- Reasoning and interaction via GPT-3.5
- Visualization and user-friendly interface

---

## 🛠 Features

- ✅ Real-time stock data from Yahoo Finance
- 📉 Closing price chart (last 5 days)
- 🤖 GPT-powered beginner-level financial analysis
- 🧠 Reasoning based on dynamic input context
- 🎨 Gradio-based clean UI for interaction

---

## 🧪 How to Run

### Requirements

```bash
pip install openai yfinance gradio matplotlib
```

### Setup

1. Replace your OpenAI API key in the script:

```python
OPENAI_API_KEY = "sk-..."
```

2. Run the script:

```bash
python stock_market_ai_agent.py
```

A browser tab will open with the Gradio app.

---

## 📹 YouTube Demo

[🔗 Link to Demo Video](https://youtube.com/shorts/CrVRKItMVL0?si=LtfpnKuOWeVAdPU8)

- Under 60 seconds
- Recorded in portrait (9:16)
- Clearly shows interaction, chart, and GPT output

---

## 📁 Files

- `stock_market_ai_agent.py`: Main Python agent script
- `README.md`: Documentation
- Generated price charts are saved dynamically per session

---

## 📚 Technologies Used

- [OpenAI API](https://platform.openai.com/)
- [Gradio](https://www.gradio.app/)
- [yFinance](https://pypi.org/project/yfinance/)
- [Matplotlib](https://matplotlib.org/)
