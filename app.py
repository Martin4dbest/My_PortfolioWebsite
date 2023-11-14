from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project1')
def project1():
    return render_template('project1.html')

@app.route('/project2')
def project2():
    return render_template('project2.html')

# New route for a contact page with a simple form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Process form data (this is a simple example, you might save it to a database)
        # Here, let's just print it to the console
        print(f"Name: {name}, Email: {email}, Message: {message}")

        # You can add more logic here, like storing data to a database

        # Render a thank you page after form submission
        return render_template('thank_you.html', name=name)
    
    # If it's a GET request, render the contact form
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
