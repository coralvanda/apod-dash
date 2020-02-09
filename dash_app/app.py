"""
Principal Author: Eric Linden
Description :

Notes :
February 08, 2020
"""

from datetime import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash_app.secrets import NASA_API_KEY


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
        html.Div(children=[
            html.P('Select an image date: '),
            dcc.DatePickerSingle(
                id='date-selection',
                date=datetime.now(),
            ),
        ]),
        html.Div(children=[
            html.P('Select the image quality: '),
            dcc.RadioItems(
                id='definition',
                options=[
                    dict(label='Standard definition', value='sd'),
                    dict(label='High Definition', value='hd'),
                ],
                value='sd',
            ),
        ]),
    ]),


    html.Img(id='apod-image', src=''),

    html.P(id='remaining-queries', children='Number of queries remaining: Unknown'),
])


if __name__ == '__main__':
    app.run_server(debug=True)
