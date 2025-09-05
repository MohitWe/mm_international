from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    phone_number = "+9198******"  # Replace this with your desired phone number
    email = "mminter******@gmail.com"
    html = """
    <html>
      <head>
        <title>MM International Visa - Visa Experts</title>
        <style>
          .phone-right {
            position: absolute;
            right: 40px;
            top: 20px;
            font-size: 20px;
            color: #111;
          }
        </style>
      </head>
      <body>
        <div class="phone-right">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

        <i class="fa fa-phone"></i>{{ phone_number }}
        </div>
        <h1>MM International Visa agents</h1>
        <h1>Email : mminternatio***@gmail.com</h1>
      </body>
    </html>
    """
    return render_template_string(html, phone_number=phone_number)

if __name__ == '__main__':
    app.run(debug=True)
