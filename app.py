from flask import Flask, render_template, request

# Initialize a Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize variables for error messages and results
    error = None
    result = None

    # Handle POST requests (form submissions)
    if request.method == 'POST':
        try:
            # Retrieve the prelim grade from the form input and convert it to a float
            prelim_grade = float(request.form['prelim'])
            
            # Check if the prelim grade is within the valid range (0 to 100)
            if prelim_grade < 0 or prelim_grade > 100:
                error = 'Please enter a valid grade between 0 and 100.'
            else:
                # Define the required passing grade
                passing_grade = 75

                # Define the weight of the prelim, midterm, and final grades
                prelim_weight = 0.20
                midterm_weight = 0.30
                final_weight = 0.50

                # Calculate the weighted contribution of the prelim grade
                weighted_prelim = prelim_grade * prelim_weight

                # Check if the weighted prelim grade alone is enough to pass
                if weighted_prelim >= passing_grade:
                    result = {
                        'prelim': prelim_grade,
                        'required_midterm': 0,
                        'required_final': 0,
                        'pass_possible': True
                    }
                else:
                    # Calculate the remaining grade needed from midterm and final to meet the passing grade
                    remaining_required = passing_grade - weighted_prelim

                    # Calculate the combined required grade from midterm and final
                    # We assume equal contributions from midterm and final for simplicity
                    required_midterm_final = remaining_required / (midterm_weight + final_weight)

                    # Split the combined required grade based on the weights of midterm and final
                    required_midterm = required_midterm_final
                    required_final = required_midterm_final

                    result = {
                        'prelim': prelim_grade,
                        'required_midterm': round(required_midterm, 2),
                        'required_final': round(required_final, 2),
                        'pass_possible': True
                    }
        except ValueError:
            # Handle cases where the input is not a valid number
            error = 'Invalid input. Please enter a numerical grade.'

    # Render the HTML template and pass the error message and results to it
    return render_template('index.html', error=error, result=result)

# Run the Flask application in debug mode if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
