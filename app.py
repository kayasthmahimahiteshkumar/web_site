from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # needed for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Here you can process the form, e.g., send email or store in DB
    # For now, just flash a success message and redirect home
    
    flash("Thank you for contacting us, we will get back to you soon!")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
