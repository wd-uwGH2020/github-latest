import os
import json
import requests
from bs4 import BeautifulSoup

from flask import Flask

app = Flask(__name__)

    
@app.route("/current")
def get_time():
    response = requests.get("https://www.epochconverter.com/")
    soup = BeautifulSoup(response.content, "html.parser")
    time = soup.find_all("div", class_="ecclock")
    return time[0].getText()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6789))
    app.run(host="127.0.0.1", port=port)

    # response = requests.get("https://www.epochconverter.com/")
    # soup = BeautifulSoup(response.content, "html.parser")
    # time = soup.find_all("div", class_="ecclock")
    # other possible solution in below but return empty?  
    # time = soup.find_all("input", class_="epoch")
    # print(time)
    # print(time[0].getText())

    #question: why this is not dynamic, seems like the website has built-in delays