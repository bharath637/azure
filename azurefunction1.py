import logging
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get the 'name' query parameter from the request
    name = req.params.get('name')

@app.route(route="my_http_trigger1")
def my_http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')   

    if not name:
        try:
            # If 'name' is not found in query, get from JSON body
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # If no 'name' found, set a default name
    if not name:
        name = "Friend"

    # Birthday HTML Message
    html_message = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Birthday Wishes</title>
        <style>
            body {{
                background-color: #f0e68c; /* Light yellow background */
                font-family: 'Arial', sans-serif;
                text-align: center;
                padding-top: 50px;
            }}

            .birthday-message {{
                font-size: 2.5em;
                font-weight: bold;
                color: #ff6347; /* Tomato color for the text */
                margin: 20px;
            }}

            .birthday-image {{
                width: 250px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }}

            .wish {{
                font-size: 1.5em;
                color: #4b0082; /* Indigo color */
                margin-top: 20px;
            }}

            .footer {{
                font-size: 1em;
                color: #555;
                margin-top: 40px;
            }}
        </style>
    </head>
    <body>

        <div class="birthday-message">
            Happy Birthday, {name}!
        </div>

        <img class="birthday-image" src="https://www.example.com/birthday-cake-image.jpg" alt="Birthday Cake">

        <div class="wish">
            Wishing you a wonderful day filled with love, joy, and laughter. May all your dreams come true!
        </div>

        <div class="footer">
            From all of us at Your Function App.
        </div>

    </body>
    </html>
    """

    # Return the HTML content as an HTTP response
    return func.HttpResponse(
        html_message,
        mimetype="text/html",
        status_code=200
    )
