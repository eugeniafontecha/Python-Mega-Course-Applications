from flask import Flask, render_template

from pandas_datareader import data
import datetime
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN #content delivery network

app = Flask(__name__)

@app.route('/plot/')
def plot():
    start=datetime.datetime(2020,12,15)
    end=datetime.datetime(2021,12,27)
    df=data.DataReader(name="GOOG", data_source="yahoo",start=start,end=end)
    #we generate a new column "Status"
    def inc_dec(c,o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value

    df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]

    #we generate a new column Middle with the avg between the open and close values
    df["Middle"] = (df.Open+df.Close)/2
    df["Height"] = abs(df.Open-df.Close)

    p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
    p.title="Candlestick Chart"
    p.grid.grid_line_alpha=0.3 #level of transparency of grid

    #rectangles parameters:
    # x_center
    # y_center
    # width in ms
    # height

    hours_12 = 12*60*60*1000

    #we first create the segments showing the highest and lowest values
    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    #we now create green rectangles corresponding to dates where
    #the Close values were higher than the Open values

    p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],hours_12,
        df.Height[df.Status=="Increase"],fill_color="#90EE90",line_color="black")

    #we then create red rectangles corresponding to dates where
    #the Close values were lower than the Open values

    p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours_12,
        df.Height[df.Status=="Decrease"],fill_color="#F08080",line_color="black")

    #script1 contains the javascript code
    #div1 contains the html

    script1, div1 = components(p)
    cdn_js=CDN.js_files[0]
    
    return render_template("plot.html",
    script1=script1,
    div1=div1,
    cdn_js=cdn_js)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

#Case 1 - Script Executed
#__name__ = '__main__'
#
#Case 2 - Script imported
#__name__ = 'script1' (en este caso no se ejecutaría esa linea.)