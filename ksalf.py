from flask import Flask, render_template, redirect

app = Flask(__name__)

# Root route, redirects to /flask or shows a welcome page
@app.route('/')
def home():
    return redirect('/flask')  # Or: return '<h2>Welcome! Go to <a href="/flask">/flask</a></h2>'

# /flask route, showing user dashboard
@app.route('/flask')
def dashboard():
    user = {
        'name': 'Abimereki',
        'is_admin': True,
        'tasks': ['Check logs', 'Review pull requests', 'Meet with design team']
    }
    return render_template('flask.html', user=user)

# /personnel route, showing a list of personnel
@app.route('/personnel')
def personnel():
    personnel_list = [
        {'person_id': 1, 'name': 'Alice', 'role': 'Engineer', 'department': 'R&D', 'access_level': 'High', 'salary': '$90,000'},
        {'person_id': 2, 'name': 'Bob', 'role': 'Manager', 'department': 'Sales', 'access_level': 'Medium', 'salary': '$85,000'},
        # Add more mock personnel here...
    ]
    return render_template('personnel.html', personnel=personnel_list)

if __name__ == '__main__':
    app.run(debug=True)

