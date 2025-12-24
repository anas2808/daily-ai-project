from flask import Flask, request
import qrcode
import io
import base64

# Initialize the Flask application
app = Flask(__name__)

# This is a multi-line string containing all the HTML, CSS, and any minimal JS.
# The '{{' and '}}' syntax is used for literal curly braces in the HTML/CSS
# to avoid conflict with Python's f-string or .format() placeholders.
# The actual Python placeholders like '{initial_text}' and '{qr_image_html}'
# use single curly braces for dynamic content insertion.
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Generator (Fresher Project)</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            background-color: #e9ecef; /* Light gray background */
            color: #343a40; /* Darker text color */
        }}
        .container {{
            background-color: #ffffff;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 90%;
            max-width: 550px;
            animation: fadeIn 0.8s ease-out;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        h1 {{
            color: #007bff; /* Bootstrap primary blue */
            margin-bottom: 25px;
            font-size: 2.2em;
            font-weight: 600;
        }}
        form {{
            display: flex;
            flex-direction: column;
            gap: 18px;
            margin-bottom: 25px;
        }}
        input[type="text"] {{
            padding: 14px;
            border: 1px solid #ced4da; /* Light gray border */
            border-radius: 8px;
            font-size: 1.1em;
            width: 100%;
            box-sizing: border-box;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }}
        input[type="text"]:focus {{
            border-color: #80bdff; /* Blue on focus */
            box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
            outline: none;
        }}
        button {{
            padding: 14px 25px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1.1em;
            font-weight: 500;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }}
        button:hover {{
            background-color: #0056b3;
            transform: translateY(-2px);
        }}
        button:active {{
            transform: translateY(0);
        }}
        .qr-code-display {{
            min-height: 200px; /* Reserve space for QR code */
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .qr-code-display img {{
            max-width: 250px;
            height: auto;
            border: 5px solid #f8f9fa; /* Light border around QR */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            animation: popIn 0.5s ease-out forwards;
            opacity: 0;
        }}
        @keyframes popIn {{
            from {{ opacity: 0; transform: scale(0.8); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
        .message {{
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
            font-size: 0.95em;
        }}
        .message.error {{
            background-color: #f8d7da; /* Light red */
            color: #721c24; /* Dark red */
            border: 1px solid #f5c6cb;
        }}
        .footer {{
            margin-top: 40px;
            font-size: 0.9em;
            color: #6c757d; /* Muted gray */
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>QR Code Generator</h1>
        <form method="POST" action="/">
            <input type="text" name="text_data" placeholder="Enter text or URL here..." required value="{initial_text}">
            <button type="submit">Generate QR Code</button>
        </form>
        <div class="qr-code-display">
            {qr_image_html}
        </div>
    </div>
    <div class="footer">
        A simple project by a fresher student using Python Flask.
    </div>
</body>
</html>
"""

# Define the route for the home page, handling both GET and POST requests.
@app.route('/', methods=['GET', 'POST'])
def index():
    qr_image_html = ""  # This will hold the HTML for the QR code image, or an error message.
    initial_text = ""   # This will hold the text last entered by the user.

    if request.method == 'POST':
        # Get the text data from the form submission.
        text_data = request.form.get('text_data', '').strip()

        if text_data:
            initial_text = text_data  # Save the text to pre-fill the input field.
            try:
                # Create a QR code instance.
                # version: Controls the size of the QR Code. 1 is the smallest.
                # error_correction: How much error correction to use. L = ~7% errors.
                # box_size: How many pixels each "box" of the QR code is.
                # border: How many "boxes" thick the border around the QR code is.
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(text_data)
                qr.make(fit=True) # Ensure all data fits in the QR code matrix.

                # Generate the QR code image.
                # fill_color: Color of the QR code "modules".
                # back_color: Color of the background.
                img = qr.make_image(fill_color="black", back_color="white")

                # Save the image to an in-memory binary stream (BytesIO).
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                buffer.seek(0) # Rewind the buffer to the beginning.

                # Encode the image data to base64.
                # This allows embedding the image directly into the HTML without saving it to a file.
                img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

                # Create the HTML img tag with the base64 encoded image.
                qr_image_html = f'<img src="data:image/png;base64,{img_str}" alt="Generated QR Code">'
            except Exception as e:
                # Handle any errors during QR code generation.
                qr_image_html = f'<p class="message error">Error generating QR code: {e}</p>'
        else:
            # If no text was entered.
            qr_image_html = '<p class="message error">Please enter some text or a URL to generate a QR code.</p>'

    # Render the HTML template, inserting the initial text and the QR code image (or error message).
    return HTML_CONTENT.format(initial_text=initial_text, qr_image_html=qr_image_html)

# Run the Flask application if this script is executed directly.
# debug=True allows for automatic reloading on code changes and provides a debugger.
if __name__ == '__main__':
    # To run this application:
    # 1. Save this code as a Python file (e.g., `app.py`).
    # 2. Open your terminal or command prompt.
    # 3. Navigate to the directory where you saved the file.
    # 4. Install the required libraries: `pip install Flask qrcode Pillow`
    #    (Pillow is a dependency for qrcode image handling).
    # 5. Run the application: `python app.py`
    # 6. Open your web browser and go to `http://127.0.0.1:5000/`
    app.run(debug=True)