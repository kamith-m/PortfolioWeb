import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Log the request method
    logging.info(f"Request method: {req.method}")

    # Determine the type of request
    method = req.method
    if method == 'GET':
        # Render a simple HTML form for GET requests
        html_form = """
        <html>
            <body>
                <form action="/contactform" method="post">
                    Name: <input type="text" name="name"><br>
                    Email: <input type="text" name="email"><br>
                    Message: <textarea name="message"></textarea><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
        """
        return func.HttpResponse(html_form, mimetype="text/html")

    elif method == 'POST':
        # Log the form data received
        logging.info(f"Form data: {req.form}")

        # Process form data for POST requests
        name = req.form.get('name')
        email = req.form.get('email')
        message = req.form.get('message')

        if not name or not email or not message:
            return func.HttpResponse(
                "Please pass a name, email, and message in the request body",
                status_code=400
            )

        # Generate HTML to display the response
        response_html = f"""
        <html>
            <body>
                <h1>Thank you for your submission!</h1>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong.Message:</strong> {message}</p>
                <p><a href="/contactform">Submit another response</a></p>
            </body>
        </html>
        """
        return func.HttpResponse(response_html, mimetype="text/html")

    else:
        return func.HttpResponse(
            "Please send a GET or POST request.",
            status_code=400
        )
