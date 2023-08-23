# Stock-Analysis-Web-Application

**Code Documentation: Stock Analysis Web Application**

This documentation provides an overview of the Python code that creates a web application for analyzing stock data using the Bokeh library. The web application allows users to input stock tickers, date ranges, and indicators to visualize and analyze stock data.

**Prerequisites:**
1. Python 3.x installed.
2. Required Python packages: numpy, yfinance, bokeh.

**How to Run:**
1. Open a terminal or command prompt.
2. Install required packages:
   ```bash
   pip install numpy yfinance bokeh
   ```
3. Save the code in a Python file (e.g., `stock_analysis_app.py`).
4. Navigate to the directory containing the Python file using the terminal.
5. Run the web application:
   ```bash
   bokeh serve --show stock_analysis_app.py
   ```
6. A browser window will open with the running web application.

**Code Overview:**
- The code creates a web application that uses the Bokeh library to visualize stock data.
- The application consists of interactive elements like text input, date picker, multi-choice selection, and a button.
- Users input main and comparison stock symbols, start and end dates, and select indicators to display on the plot.

**Code Structure:**

1. **Import Statements:**
   - Import necessary libraries and modules.

2. **Load Data Function:**
   - `load_data(ticker1, ticker2, start, end)` function downloads stock data for two tickers within the specified date range.

3. **Update Plot Function:**
   - `update_plot(data, indicators, sync_axis=None)` function creates and updates a Bokeh plot.
   - The function plots candlestick bars and additional technical indicators based on user selections.

4. **Button Click Handler:**
   - `on_button_click(main_stock, comparison_stock, start, end, indicators)` function handles the button click event.
   - It loads data, updates the plot, and synchronizes the x-axis of two plots.

5. **User Interface Elements:**
   - Define various Bokeh UI elements such as text input, date picker, multi-choice selector, and a button.
   - These elements allow users to input stock information and select indicators.

6. **Layout:**
   - `layout` organizes the UI elements vertically using the `column` layout manager.
   - The layout includes text inputs, date pickers, indicator choices, and the load button.

7. **Initialize the App:**
   - `curdoc().add_root(layout)` initializes and displays the Bokeh app using the specified layout.

**Running the Application:**
1. Open a web browser and navigate to `http://localhost:5006`.
2. Enter the main and comparison stock symbols.
3. Select start and end dates using the date pickers.
4. Choose indicators to display on the plot.
5. Click the "Load Data" button to generate the stock analysis plot.

**Note:** Ensure that you have an active internet connection to fetch stock data using the Yahoo Finance API.

The code provides a user-friendly interface for visualizing stock data with customizable indicators. Users can interact with the web application to gain insights into stock performance over a specified time frame.
