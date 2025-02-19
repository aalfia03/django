# Import packages
from dash import Dash, html, dash_table
import pandas as pd
import requests

# Загрузка данных в формате JSON
response = requests.get('http://localhost:8000/Klients/')
data = response.json()

# Преобразование JSON-данных в DataFrame
df = pd.DataFrame(data)

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)