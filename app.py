from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def show_time():
    now = datetime.now().strftime("%Y/%m/%d %H:%M")
    return f"""
    <html>
    <head>
        <meta charset='utf-8'>
        <title>即時時間</title>
        <style>
            body {{
                background-color: white;
                color: black;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-size: 60px;
                font-family: Arial, sans-serif;
            }}
        </style>
    </head>
    <body>
        台北時間：{now}
    </body>
    </html>
    """
