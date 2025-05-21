import openai
import yfinance as yf
import gradio as gr
import matplotlib.pyplot as plt

OPENAI_API_KEY = "sk-..."
client = openai.OpenAI(api_key=OPENAI_API_KEY)

#FUNCTION: Get 5-day Stock Summary and Plot
def get_stock_summary(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="5d")

        if data.empty:
            return "❌ No data found for this ticker.", None

        summary = f"📈 Stock data for {ticker.upper()} (last 5 days):\n\n"
        for date, row in data.iterrows():
            summary += f"{date.date()} | Open: ${row['Open']:.2f}, Close: ${row['Close']:.2f}, Volume: {int(row['Volume'])}\n"

        # Plotting
        plt.figure(figsize=(10, 4))
        data['Close'].plot(title=f"{ticker.upper()} Closing Prices", grid=True)
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plot_path = f"{ticker}_plot.png"
        plt.savefig(plot_path)
        plt.close()

        return summary, plot_path
    except Exception as e:
        return f"⚠️ Error fetching stock data: {str(e)}", None

#FUNCTION: AI Reasoning & Recommendation
def ask_gpt(stock_summary):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful financial assistant."},
                {"role": "user", "content": f"Please analyze this stock data and give an investor-friendly summary:\n\n{stock_summary}"}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content
    except openai.RateLimitError:
        return "❌ API quota exceeded or key is restricted."
    except Exception as e:
        return f"⚠️ OpenAI error: {str(e)}"

# FUNCTION: Full Agent Workflow
def run_agent(ticker):
    summary, plot = get_stock_summary(ticker)
    if summary.startswith("❌") or summary.startswith("⚠️"):
        return summary, None, ""
    analysis = ask_gpt(summary)
    return summary, plot, analysis

# GRADIO UI
def main():
    gr.Interface(
        fn=run_agent,
        inputs=gr.Textbox(label="Enter Stock Ticker (e.g., AAPL, TSLA)"),
        outputs=[
            gr.Textbox(label="📊 Stock Summary"),
            gr.Image(label="📉 Price Chart"),
            gr.Textbox(label="🤖 AI Analysis")
        ],
        title="💹 Stock Market AI Agent",
        description="Enter a stock ticker to get the latest 5-day summary, price chart, and GPT-powered AI analysis."
    ).launch()

if __name__ == "__main__":
    main()
