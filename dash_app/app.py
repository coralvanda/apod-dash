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
import requests


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

    # TODO add more info about the requested image
    #  title
    #  explanation
    html.Img(id='apod-image', src=''),

    # TODO pull this info from the response object and output it
    html.P(id='remaining-queries', children='Number of queries remaining: Unknown'),
])


@app.callback(
    dash.dependencies.Output('apod-image', 'src'),
    [
        dash.dependencies.Input('date-selection', 'date'),
        dash.dependencies.Input('definition', 'value'),
    ]
)
def get_image_callback(selected_date, image_quality):
    formated_date = datetime.strptime(selected_date.split('T')[0], '%Y-%m-%d')
    formated_date = datetime.strftime(formated_date, '%Y-%m-%d')
    api_response = make_request(date=formated_date, quality=image_quality)
    response_json = api_response.json()

    return response_json['url']


def make_request(date, quality):
    API_ADDRESS = 'https://api.nasa.gov/planetary/apod'

    response = requests.get(
        url=API_ADDRESS,
        params=dict(
            date=date,
            hd=quality == 'hd',
            api_key=NASA_API_KEY))

    if response.status_code != 200:
        return ''

    return response


if __name__ == '__main__':
    app.run_server(debug=True)
