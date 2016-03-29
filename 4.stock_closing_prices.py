import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook

AAPL = pd.read_csv(
        "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2016",
        parse_dates=['Date']
    )
IBM = pd.read_csv(
        "http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2016",
        parse_dates=['Date']
    )
    
GOOG = pd.read_csv(
        "http://ichart.yahoo.com/table.csv?s=GOOG&a=0&b=1&c=2000&d=0&e=1&f=2016",
        parse_dates=['Date']
    )    
MSFT = pd.read_csv(
        "http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2016",
        parse_dates=['Date']
    )    
output_notebook()

# create a new plot with a datetime axis type
p = figure(width=800, height=350, x_axis_type="datetime")

p.title = "Stock Closing Prices"
p.grid.grid_line_alpha=0.3
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'

p.line(AAPL['Date'], AAPL['Close'], color='navy', alpha=0.5, legend="Apple")
p.line(IBM['Date'], IBM['Close'], color='green', alpha=0.5, legend="IBM")
p.line(MSFT['Date'], MSFT['Close'], color='orange', alpha=0.5, legend="Microsoft")
p.line(GOOG['Date'], GOOG['Close'], color='red', alpha=0.5, legend="Google")

show(p)