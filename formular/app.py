from flask import Flask, render_template, request, redirect, url_for
from cs50 import SQL
import random
from datetime import datetime
import sqlite3

app = Flask(__name__)

# SQL() ia ca argument drumul catre localizarea bazei de date in sistemul de operare. Trebuie indicat de utilizator
db = SQL('sqlite:///data.db')

class Period:
    def __init__(self) -> None:
        start_time = 0;
        end_time = 0;
        ai_time = 0;


# Initiate a period instance
user_session = Period()
user_session.ai_time = 0

# Number of images that will be presented to the user
FOTO_NUMBER = 10

# Allowed response values
ALLOWED_RESPONSES = ['1', '2', '3', '4']

# Legal countries to select from
COUNTRIES = ['germany', 'moldova', 'romania', 'switzerland']

# Legal positions to choose from
POSITIONS = ['student', 'resident', 'doctor']

# Legal years a user can be in
YEARS = ["1", "2", "3", "4", "5", "6"]

# Dictionary that will contain all the relevant info about the user
# Eventually it will be added into a database
user_data = {}

# Pagina initiala
@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'GET':
        return render_template('index.html', lang="eng")
    else:
        return render_template('index.html', lang=request.form.get('lang'))

# Pagina cu informatii despre clasificare
@app.route('/info')
def info():
    return render_template('info.html', lang = request.args.get('lang'))

# Pagina cu informatii personale
@app.route('/personal', methods=['get','post'])
def personal():
    if request.method == 'GET':
        # 50 percent chance to be in either group
        AI_group = random.choice(["True", "False"])

        user_session.start_time = datetime.now()
        return render_template('personal.html', lang = request.args.get('lang'), category = AI_group)
    else:
        # Should do user input check
        # Check existance of name
        if not request.form.get('name'):
            return render_template('personal.html', message='Name is a required field', lang = request.form.get('lang'), category = request.form.get('category'))
        # Save the values to the user dictionary
        user_data['name'] = request.form.get('name')

        # Check existance of surname
        if not request.form.get('surname'):
            return render_template('personal.html', message='Surname is a required field', lang = request.form.get('lang'), category = request.form.get('category'))
        user_data['surname'] = request.form.get('surname')

        # Check existance of position
        if not request.form.get('position'):
            return render_template('personal.html', message='Position is a required field', lang = request.form.get('lang'), category = request.form.get('category'))

        # Check position to be one of the legal options
        if request.form.get('position') not in POSITIONS:
            return render_template('personal.html', message='Should select only the available position options!', lang = request.form.get('lang'), category = request.form.get('category'))
        user_data['position'] = request.form.get('position')
        
        # If the position is not student make the year "0"
        if user_data['position'] == 'resident' or user_data['position'] == 'doctor':
            user_data['year'] = 0
        else: 
            if request.form.get('studentYear') not in YEARS:
                return render_template('personal.html', message= "Should select only the available year options!", lang = request.form.get('lang'), category = request.form.get('category'))
            user_data['year'] = request.form.get('studentYear')

        # Check existance of country
        if not request.form.get('country'):
            return render_template('personal.html', message='Country is a required field', lang = request.form.get('lang'), category = request.form.get('category'))

        # Check country to be one of the legal options
        if request.form.get('country') not in COUNTRIES:
            return render_template('personal.html', message='Should select only the available country options!', lang = request.form.get('lang'), category = request.form.get('category'))
        user_data['country'] = request.form.get('country')

        # Redirect user to questions form
        return redirect(url_for('form', lang = request.form.get('lang'), category = request.form.get('category')))

# Pagina pentru imagini
@app.route('/form', methods=['post','get'])
def form():
    # Page represented right at the beginning
    if request.method == 'GET':
        # 50 percent chance to be in either group
        AI_group = request.args.get('category')

        # Adding category info to user dict
        user_data["category"] = AI_group

        # Generate an integer from 3500 to 4500. It is the time in milliseconds for the animation to run
        aiWait = random.randint(3500, 4500)
        if AI_group == "True":
            # Add this time to total time
            user_session.ai_time += aiWait

        return render_template('form.html', number = 1, category = AI_group, lang=request.args.get('lang'), aiWait = aiWait)
    
    # Next pages
    else:
        # Get the value for the cateogry
        AI_group = request.form.get('category')

        # Generate an integer from 3500 to 4500. It is the time in milliseconds for the animation to run
        aiWait = random.randint(3500, 4500)
        if AI_group == "True":
            user_session.ai_time += aiWait

        # To do when we arrived at the last image
        if int(request.form.get('question')) >= FOTO_NUMBER:
            #Check for existence of user input
            if not request.form.get('q' + request.form.get('question')):
                return render_template('form.html', number = int(request.form.get('question')), message = "You should select an option!", category = AI_group, lang = request.form.get('lang'), aiWait = aiWait)
            
            #Check for valid user input
            if request.form.get('q' + request.form.get('question')) not in ALLOWED_RESPONSES:
                return render_template('form.html', number = int(request.form.get('question')), message = "Not an eligible option!", category = AI_group, lang = request.form.get('lang'), aiWait = aiWait)
            
            # Adding response to the dictionary containing all the user input
            user_data['q' + request.form.get('question')] = request.form.get('q' + request.form.get('question'))
            
            # Time when the user ended the survey
            user_session.end_time = datetime.now()

            # Total elapsed time since the start of the survey
            elapsed_time = int(user_session.end_time.timestamp() - user_session.start_time.timestamp()) - int(user_session.ai_time / 1000)
            # Add it to the user dict
            user_data['elapsed_time'] = str(elapsed_time)

            # Now request the goodbye page
            return redirect(url_for('goodbye', lang = request.form.get('lang')))
        
        # To do when we still haven't arrived at the last page
        else:
            # Checking user input as above
            if not request.form.get('q' + request.form.get('question')):
                return render_template('form.html', number = int(request.form.get('question')), message = "You should select an option!", category = AI_group, lang = request.form.get('lang'), aiWait = aiWait)
            if request.form.get('q' + request.form.get('question')) not in ALLOWED_RESPONSES:
                return render_template('form.html', number = int(request.form.get('question')), message = "Not an eligible option!", category = AI_group, lang = request.form.get('lang'), aiWait = aiWait)
            
            # Adding info to dict as above
            user_data['q' + request.form.get('question')] = request.form.get('q' + request.form.get('question'))
            return render_template('form.html', number = int(request.form.get('question')) + 1, category = AI_group, lang = request.form.get('lang'), aiWait = aiWait)

# Pagina cu multumirea pentru participant
@app.route('/goodbye', methods=['get'])
def goodbye():
    # Usage example
    conditions = {
        'name': user_data['name'],
        'surname': user_data['surname'],
        'position': user_data['position'],
        'year': user_data['year'],
        'country': user_data['country']
    }

    if not check_values_exist('answers', conditions):
        # Adding data to database
        db.execute('INSERT INTO answers (name, surname, position, year, country, category, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, elapsed_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user_data["name"], user_data["surname"], user_data["position"], user_data['year'], user_data["country"], user_data["category"], user_data['q1'], user_data['q2'], user_data['q3'], user_data['q4'], user_data['q5'], user_data['q6'], user_data['q7'], user_data['q8'], user_data['q9'], user_data['q10'], user_data['elapsed_time'])

    return render_template('goodbye.html', lang = request.args.get('lang'))

def check_values_exist(table_name, conditions):
    """
    Check if a row exists in a table that matches multiple conditions.
    
    Parameters:
        table_name (str): The name of the table.
        conditions (dict): A dictionary of column-value pairs to check.
        
    Returns:
        bool: True if a matching row exists, False otherwise.
    """
    # Connect to the database
    conn = sqlite3.connect('data.db')
    # For the webapp
    # conn = sqlite3.connect('sqlite:////home/availableusername/mysite/data.db')
    cursor = conn.cursor()
    
    # Dynamically build the WHERE clause
    where_clause = " AND ".join(f"{column} = ?" for column in conditions.keys())
    values = tuple(conditions.values())  # Values for parameterized query

    # Execute the SELECT query
    query = f"SELECT 1 FROM {table_name} WHERE {where_clause} LIMIT 1"
    cursor.execute(query, values)
    result = cursor.fetchone()  # Fetch one result
    
    # Close the connection
    conn.close()
    
    # Return True if a row is found, otherwise False
    return result is not None
