import pandas as pd
import ta
from data.db import connect_db, fetch_raw_data, insert_cleaned_data, insert_feature_extraction
from data.preprocessing import preprocess_raw_value, extract_features
from data.analysis import analyze_data
from data.reporting import generate_report

# Function to load CSV data
def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df.rename(columns={'Adj Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Volume': 'volume'})
    df.dropna(inplace=True)
    return df

# Function to calculate indicators
def calculate_indicators(df):
    df['SMA_20'] = ta.trend.sma_indicator(df['close'], window=20)
    df['SMA_50'] = ta.trend.sma_indicator(df['close'], window=50)
    df['RSI'] = ta.momentum.rsi(df['close'], window=14)
    df['MACD'] = ta.trend.macd_diff(df['close'])
    return df

# Function to generate signals
def generate_signals(df):
    df['Buy_Signal'] = (df['SMA_20'] > df['SMA_50'])
    df['Sell_Signal'] = (df['SMA_20'] < df['SMA_50'])
    return df

# Function to preprocess data and calculate indicators and signals
def preprocess_data(file_path):
    df = load_csv_data(file_path)
    df = calculate_indicators(df)
    df = generate_signals(df)
    return df

# Function to simulate trades
def simulate_trades(df, initial_balance=10000):
    balance = initial_balance
    position = 0
    buy_price = 0

    for i in range(len(df)):
        if df['Buy_Signal'][i] and balance > 0:
            buy_price = df['close'][i]
            position = balance / buy_price
            balance = 0
            print(f"Buying at {buy_price} on {df.index[i]}")
        elif df['Sell_Signal'][i] and position > 0:
            sell_price = df['close'][i]
            balance = position * sell_price
            position = 0
            print(f"Selling at {sell_price} on {df.index[i]}")

    final_balance = balance + (position * df['close'].iloc[-1] if position > 0 else 0)
    print(f"Final balance: {final_balance}")

def fetch_and_process_data(start_date, end_date, file_path):
    # Fetch raw data
    raw_data = fetch_raw_data(start_date, end_date)

    for data in raw_data:
        data_id, source, timestamp, raw_value = data
        # Preprocess raw data
        cleaned_value = preprocess_raw_value(raw_value)
        insert_cleaned_data(data_id, cleaned_value, timestamp)

        # Extract features and insert into the database
        features = extract_features(cleaned_value)
        for feature_name, feature_value in features:
            insert_feature_extraction(data_id, feature_name, feature_value)

    # Analyze data
    df_analysis = analyze_data()

    # Generate report
    generate_report(df_analysis)

def main():
    # Process CSV data
    file_path = 'path/to/your/csvfile.csv'  # Update with actual path
    df = preprocess_data(file_path)
    simulate_trades(df)

    # Fetch and process data from the database
    fetch_and_process_data('2024-01-01', '2024-01-31', file_path)

if __name__ == "__main__":
    main()