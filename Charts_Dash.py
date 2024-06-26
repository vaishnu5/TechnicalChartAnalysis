

#Libraries
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from datetime import datetime, timedelta

#Initilising the app
app = Dash(__name__)

#Tickers
indices = {
    'Nifty 50': '^NSEI',
    'Bank Nifty': '^NSEBANK',
    'Mid Cap Nifty': '^NSEMDCP50',
    'Fin Nifty': 'NIFTY_FIN_SERVICE.NS'
    
}

#Time frames
time_frames = {
    '1 Minute': '1m',
    '2 Minutes': '2m',
    '15 Minutes': '15m',
    '30 Minutes': '30m',
    '1 Hour': '60m',
}

#App Frontend
app.layout = html.Div([
    html.H1("Real-Time Nifty Index Candlestick Charts"),
    dcc.Dropdown(
        id='index-dropdown',
        options=[{'label': key, 'value': value} for key, value in indices.items()],
        value='^NSEI'
    ),
    dcc.Dropdown(
        id='timeframe-dropdown',
        options=[{'label': key, 'value': value} for key, value in time_frames.items()],
        value='1m'
    ),
    dcc.Graph(id='live-candlestick'),
    dcc.Interval(
        id='interval-component',
        interval=1*60*1000,  # in milliseconds (update every minute)
        n_intervals=0
    )
])

#Fetching data using YFinance
def fetch_data(ticker, interval):
    print(datetime.now())
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    data = yf.download(ticker, start=start_time, end=end_time, interval=interval)
    data.reset_index(inplace=True)
    return data


#App Callback
@app.callback(Output('live-candlestick', 'figure'),
              [Input('interval-component', 'n_intervals'),
               Input('index-dropdown', 'value'),
               Input('timeframe-dropdown', 'value')])
def update_graph_live(n, selected_index, selected_timeframe):
    df = fetch_data(selected_index, selected_timeframe)
    fig = go.Figure(data=[go.Candlestick(x=df['Datetime'],
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title=f'{selected_index} Live Candlestick Chart ({selected_timeframe})',
                      xaxis_title='Time',
                      yaxis_title='Price')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    


