# Technical Indicators and Candlestick Patterns

## Project Overview

This project aims to automate the detection and reporting of selected technical indicators and candlestick patterns in real time. The project is divided into three main parts:

1. **Detection of Indicator Divergences**
2. **Detection and Reporting of Candlestick Patterns**
3. **Training and Analysis of New Candlestick Patterns**

## Project Team

- **Project Leader/User**: Dr. S. B. Ghosh, Mumbai
- **Team Members**: Vaishnavi Katukollu, Krishna Chopra, Rohit Kamineni

## Features

### Part 1: Detection of Indicator Divergences

- **Indicators**: MACD, RSI, Stochastic
- **Time Frames**: 1 min, 5 min, 10 min, 15 min, 30 min, 1 hour, 2 hours, 1 day, 1 week
- **Charts**: Select up to 4 charts from a dropdown list of Nifty indices and F&O stocks
- **Functionality**:
  - Monitor selected charts in real-time during trading hours (9:15 AM - 3:30 PM)
  - Option to run in non-real-time mode for after-hours analysis
  - Report occurrence of indicator divergences
  - Clickable reports to verify events on charts

### Part 2: Detection and Reporting of Candlestick Patterns

- **Candlestick Patterns**:
  - **Bullish Reversal**: Hammer, Inverse Hammer, Doji, Bullish Harami, Bullish Engulfing, Bullish Piercing
  - **Bearish Reversal**: Hanging Man, Shooting Star, Doji, Bearish Harami, Bearish Engulfing, Dark Cloud Cover
  - **Bullish Continuation**: Three White Soldiers, Rising Three
  - **Bearish Continuation**: Three Black Crows, Falling Three
- **Time Frames**: Same as Part 1
- **Functionality**:
  - Monitor selected charts for candlestick patterns
  - Report historical occurrences and outcomes of patterns in the last 2 years

### Part 3: Training and Analysis of New Candlestick Patterns

- **Functionality**:
  - User-defined candlestick patterns
  - Backtest historical data for the last 2 years
  - Report pattern occurrences and outcomes in selected time frames
  - Run post-market hours or when not running Part 1 and Part 2 in real-time
