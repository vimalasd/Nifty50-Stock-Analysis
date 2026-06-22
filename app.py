import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("analysis.db")

# Load Data 

@st.cache_data
def load_data():

    data = {
        "market_summary": pd.read_sql(
            "SELECT * FROM market_summary",
            conn
        ),

        "top_green": pd.read_sql(
            "SELECT * FROM top_green_stocks",
            conn
        ),

        "top_red": pd.read_sql(
            "SELECT * FROM top_red_stocks",
            conn
        ),

        "volatility": pd.read_sql(
            "SELECT * FROM volatility_analysis",
            conn
        ),
        "top10_volatility": pd.read_sql(
            "SELECT * FROM top10_volatility",
            conn
        ),
        "cumulative_return": pd.read_sql(
            "SELECT * FROM cumulative_return",
            conn
        ),

        "top5_cumulative_return": pd.read_sql(
            "SELECT * FROM top5_cumulative_return",
            conn
        ),

        "sector_performance": pd.read_sql(
            "SELECT * FROM sector_performance",
            conn
        ),

        "correlation_matrix": pd.read_sql(
            "SELECT * FROM correlation_matrix",
            conn
        ),

        "correlation_performance": pd.read_sql(
            "SELECT * FROM correlation_performance",
            conn
        ),

        "monthly_returns": pd.read_sql(
            "SELECT * FROM monthly_returns",
            conn
        )
    }

    return data


data = load_data()


# Market Overview Function

def market_overview():

    summary = data["market_summary"].iloc[0]

    top_green = data["top_green"]
    top_green.index += 1

    top_red = data["top_red"]
    top_red.index += 1

    st.header("Market Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📈 Green Stocks",
        summary["green_stocks"]
    )

    col2.metric(
        "📉Red Stocks",
        summary["red_stocks"]
    )

    col3.metric(
        "💰Average Price",
        round(summary["average_price"],2)
    )

    col4.metric(
        "📊Average Volume",
        round(summary["average_volume"],2)
    )

    st.subheader("Top 10 Green Stocks")
    st.dataframe(top_green)
    
    st.subheader("Top 10 Red Stocks")
    st.dataframe(top_red)


# Volatility Function

def volatility_analysis():
    st.title("📊Volatility Anaysis")
    Volatility = data["top10_volatility"]
    Volatility.index += 1

    st.subheader("Top 10 Volatile Stocks")
    st.dataframe(Volatility)

    plt.figure(figsize=(10,6))
    plt.bar(Volatility["ticker"],Volatility["volatility"])
    plt.title("Top 10 Most Volatile Stocks",color="r")
    plt.xlabel("Ticker",color="g")
    plt.ylabel("Volatility",color="g")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

# Cumulative Return Function

def cumulative_return_analysis():
    st.title("🚀Cumulative Return Analysis")
    cumulative_df = data["cumulative_return"]

    cumulative_df["date"] = pd.to_datetime(
        cumulative_df["date"]
    )

    top5 = data["top5_cumulative_return"]
    st.dataframe(top5)

    plt.figure(figsize=(12,6))
    for ticker in top5["ticker"]:

        stock_data = cumulative_df[cumulative_df["ticker"] == ticker]

        plt.plot(
            stock_data["date"],
            stock_data["cumulative_return"],
            label=ticker
        )
    plt.title("Top 5 Performing Stocks - Cumulative Return",size=15,color="r")
    plt.xlabel("Date",color="g")
    plt.ylabel("Cumulative Return",color="g")
    plt.legend()
    plt.grid()
    st.pyplot(plt.gcf())


# Sector Function

def sector_analysis():
    st.title("🏭Sector Performance Analysis")
    sector_df = data["sector_performance"]

    st.dataframe(sector_df)

    plt.figure(figsize=(12,6))
    plt.bar(
        sector_df["sector"],
        sector_df["Yearly_Return"],color=["g" if b >0 else "r" for b in sector_df["Yearly_Return"]]
    )
    plt.title("Average Yearly Return by Sector",color="r")
    plt.xlabel("Sector",color="g")
    plt.ylabel("Average Yearly Return",color="g")
    plt.xticks(rotation=45,ha="right")
    st.pyplot(plt.gcf())  

    
# Correlation Function

def correlation_analysis():
    st.title("🔗Stock Price Correlation")
    corr_matrix = data["correlation_matrix"]

    corr_matrix = corr_matrix.set_index(
        "ticker"
    )

    st.dataframe(corr_matrix)
    st.subheader("Heatmap")

    # Heatmap

    plt.figure(figsize=(14, 10))
    sns.heatmap(corr_matrix,cmap="coolwarm")
    plt.title("Stock Correlation Heatmap",color="g",size=15)
    st.pyplot(plt.gcf())

  
    top_corr = data["correlation_performance"]
    top_corr.index+=1
    st.header("Top 10 Correlated stocks")
    st.dataframe(top_corr)
    top_corr["pair"] = (top_corr["stock1"] + " - " + top_corr["stock2"])

    plt.figure(figsize=(10, 6))

    sns.barplot(data=top_corr,x="correlation",y="pair",palette="viridis")

    plt.title("Top 10 Correlated Stock Pairs",color="r")
    plt.xlabel("Correlation",color="g")
    plt.ylabel("Stocks Pair",color="g")
    st.pyplot(plt.gcf())

# Monthly Function

def monthly_analysis():
    st.title("📅Monthly gainers and losers")
    monthly = data["monthly_returns"]

    month = st.selectbox(
        "Select Month",
        sorted(
            monthly["month"].unique()
        )
    )

    month_data = monthly[
        monthly["month"] == month
    ]

    gainers = (
        month_data
        .sort_values(
            by="monthly_return",
            ascending=False
        )
        .head(5)
    )

    losers = (
        month_data
        .sort_values(
            by="monthly_return"
        )
        .head(5)
    )

    col1, col2 = st.columns(2)

    with col1:
            st.write(f"Top 5 Gainers -{month}")
            st.dataframe(gainers.reset_index(drop=True))

    with col2:
            st.write(f"Top 5 Losers -{month}")
            st.dataframe(losers.reset_index(drop=True))
    # Create figure
    plt.figure(figsize=(12,5))

    # Gainers chart
    plt.subplot(1,2,1)

    plt.bar(
        gainers["ticker"],
        gainers["monthly_return"],color="green"
        )

    plt.title(f"Top 5 Gainers - {month}")

    plt.xticks(rotation=45)

    plt.ylabel("Monthly Return")

    # Losers chart
    plt.subplot(1,2,2)

    plt.bar(
        losers["ticker"],
        losers["monthly_return"],color="red"
        )   

    plt.title(f"Top 5 Losers - {month}")
    plt.xticks(rotation=45)
    plt.ylabel("Monthly Return")
    plt.tight_layout()
    st.pyplot(plt.gcf())  

# Main App

st.set_page_config(
    page_title="Nifty 50 Dashboard",
    layout="wide"
)

st.title(
    "📈 Nifty 50 Stock Analysis Dashboard"
)

menu = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Market Overview",
        "Volatility Analysis",
        "Cumulative Return",
        "Sector Performance",
        "Stock Correlation",
        "Monthly Analysis"
    ]
)

if menu == "Market Overview":
    market_overview()

elif menu == "Volatility Analysis":
    volatility_analysis()

elif menu == "Cumulative Return":
    cumulative_return_analysis()

elif menu == "Sector Performance":
    sector_analysis()

elif menu == "Stock Correlation":
    correlation_analysis()

elif menu == "Monthly Analysis":
    monthly_analysis()

conn.close()