from flask import Flask, render_template, request, send_file
import pandas as pd
from werkzeug.utils import secure_filename
from geopy.geocoders import ArcGIS
from datetime import datetime

app=Flask(__name__)

def get_coordinates(row, geocoder):
    location = geocoder.geocode(row["Address"])
    if location:      
        row[["Latitude","Longitude"]] = [location.latitude, location.longitude]
    else:
        row[["Latitude","Longitude"]] = ["NaN", "NaN"]
    return row


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success_table', methods= ['POST'])
def success_table():
    global filename
    geocoder = ArcGIS()
    if request.method == 'POST':
        file=request.files["file"]
        try:        
            df = pd.read_csv(file)

            for col in df.columns:
                df.rename(columns={col: col.title()}, inplace=True)
            if "Address" in df.columns:
                df[["Latitude","Longitude"]] = None
                df = df.apply(get_coordinates,axis= 1, geocoder = geocoder)

                table = df.to_html()            
                with open(r"templates\table.html","w") as f:
                    f.write(table)
                
                filename = secure_filename(datetime.now().strftime("%d-%m-%Y--%H-%M-%S-%f")+" uploaded"+file.filename)        
                df.to_csv(filename, index=None)           
                
                return render_template("index.html", table = "table.html", btn = "download.html")
            else:
                return render_template("index.html", text = "Please make sure you have an address column in your CSV file!")
        except:
            return render_template("index.html", text = "The submitted CSV file is not valid. Please try with a different one.")

@app.route("/download")
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment = True)

if __name__ == '__main__':
    app.debug=True
    app.run()