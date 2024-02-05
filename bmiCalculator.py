import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "BMI Calculator",
            style={
                "textAlign": "center",
                "backgroundColor": "#3498db",
                "color": "white",
                "padding": "10px",
            },
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label("Enter your weight (kg):"),
                        dcc.Input(
                            id="weight-input",
                            type="number",
                            value=70,
                            style={"marginBottom": 10},
                        ),
                    ],
                    style={"display": "inline-block", "marginRight": "20px"},
                ),
                html.Div(
                    [
                        html.Label("Enter your height (cm):"),
                        dcc.Input(
                            id="height-input",
                            type="number",
                            value=170,
                            style={"marginBottom": 10},
                        ),
                    ],
                    style={"display": "inline-block"},
                ),
            ],
            style={"marginBottom": 5},
        ),
        html.Button(
            "Calculate BMI",
            id="calculate-button",
            n_clicks=0,
            style={"marginTop": "10px"},
        ),  # Added spacing between the two input groups
        html.Div(id="bmi-result", style={"fontSize": 18, "marginTop": 20}),
    ]
)


@app.callback(
    Output("bmi-result", "children"),
    [Input("calculate-button", "n_clicks")],
    [State("weight-input", "value"), State("height-input", "value")],
)
def calculate_bmi(n_clicks, weight, height):
    if n_clicks == 0:
        return ""  # Initial state, no calculation

    if weight <= 0 or height <= 0:
        return "Please enter valid values for weight and height."

    # Convert height from cm to meters
    height_meters = height / 100.0

    # Calculate BMI
    bmi = round(weight / (height_meters**2), 2)

    # Provide BMI category
    category = get_bmi_category(bmi)

    result_text = f"Your BMI is {bmi}. Category: {category}"
    return result_text


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    app.run_server(debug=True)
