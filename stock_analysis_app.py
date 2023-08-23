import datetime as dt
import numpy as np
import yfinance as yf
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column, row
from bokeh.models import TextInput, Button, DatePicker, MultiChoice

# Load data function: Downloads stock data for two tickers within the specified date range
def load_data(ticker1, ticker2, start, end):
    df1 = yf.download(ticker1, start, end)
    df2 = yf.download(ticker2, start, end)
    return df1, df2

# Update plot function: Creates and updates a Bokeh plot with candlestick bars and technical indicators
def update_plot(data, indicators, sync_axis=None):
    df = data
    gain = df.Close > df.Open
    loss = df.Open > df.Close
    width = 12 * 60 * 60 * 1000  # half day in ms

    if sync_axis is not None:
        p = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000, x_range=sync_axis)
    else:
        p = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000)

    p.xaxis.major_label_orientation = "vertical"
    p.grid.grid_line_alpha = 0.3

    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.vbar(df.index[gain], width, df.Open[gain], df.Close[gain], fill_color="#00ff00", line_color="#00ff00")
    p.vbar(df.index[loss], width, df.Open[loss], df.Close[loss], fill_color="#ff0000", line_color="#ff0000")

    for indicator in indicators:
        if indicator == "30 Day SMA":
            df['SMA30'] = df['Close'].rolling(30).mean()
            p.line(df.index, df.SMA30, color="purple", legend_label="30 Day SMA")
        elif indicator == "100 Day SMA":
            df['SMA100'] = df['Close'].rolling(100).mean()
            p.line(df.index, df.SMA100, color="blue", legend_label="100 Day SMA")
        elif indicator == "Linear Regression Line":
            x_values = np.arange(len(df))
            par = np.polyfit(x_values, df.Close.values, 1)
            y_predicted = np.polyval(par, x_values)
            p.line(df.index, y_predicted, color="red", legend_label="Linear Regression")

        p.legend.location = "top_left"
        p.legend.click_policy = "hide"

    return p

# Button click handler: Handles the button click event, loads data, updates the plot, and synchronizes x-axis
def on_button_click(main_stock, comparison_stock, start, end, indicators):
    source1, source2 = load_data(main_stock, comparison_stock, start, end)
    p = update_plot(source1, indicators)
    p2 = update_plot(source2, indicators, sync_axis=p.x_range)
    layout.children[-1] = row(p, p2)

# User interface elements
stock1_text = TextInput(title="Main Stock")
stock2_text = TextInput(title="Comparison Stock")
date_picker_from = DatePicker(title='Start Date', value="2020-01-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))
date_picker_to = DatePicker(title='End Date', value="2020-02-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))
indicator_choice = MultiChoice(options=["100 Day SMA", "30 Day SMA", "Linear Regression Line"])

# Button for loading data
load_button = Button(label="Load Data", button_type="success")
load_button.on_click(lambda: on_button_click(stock1_text.value, stock2_text.value, date_picker_from.value, date_picker_to.value, indicator_choice.value))

# Organize UI elements using a column layout
layout = column(stock1_text, stock2_text, date_picker_from, date_picker_to, indicator_choice, load_button)

# Initialize the app if executed as the main module
if __name__ == "__main__":
    curdoc().add_root(layout)
