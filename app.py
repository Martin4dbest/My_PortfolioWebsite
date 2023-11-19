from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize SQLite database connection
conn = sqlite3.connect('contact_data.db')
c = conn.cursor()

# Create a table for contact form data if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS contacts 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              name TEXT, email TEXT, message TEXT)''')
conn.commit()
conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/project1')
def project1():
    return render_template('project1.html')


@app.route('/project2')
def project2():
    return render_template('project2.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        conn = sqlite3.connect('contact_data.db')
        c = conn.cursor()

        # Insert form data into the database
        c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

        return render_template('thank_you.html', name=name)
    
    return render_template('contact.html')


@app.route('/view_contacts')
def view_contacts():
    conn = sqlite3.connect('contact_data.db')
    c = conn.cursor()

    # Fetch all contact records from the database
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()

    conn.close()

    return render_template('view_contacts.html', contacts=contacts)


if __name__ == '__main__':
    app.run(debug=True)
