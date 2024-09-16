from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    result = None

    if request.method == 'POST':
        try:
            prelim_grade = float(request.form['prelim'])
            if prelim_grade < 0 or prelim_grade > 100:
                error = 'Please enter a valid grade between 0 and 100.'
            else:
                # Define the required passing grade
                passing_grade = 75

                # The remaining weight of the midterm and final grades
                remaining_weight = 0.30 + 0.50  # Midterm and Final weights

                # If it's impossible to pass based on the prelim grade alone
                max_possible_midterm_final = (prelim_grade * 0.20) + (100 * remaining_weight)
                if max_possible_midterm_final < passing_grade:
                    result = {
                        'prelim': prelim_grade,
                        'required_midterm': 'N/A',
                        'required_final': 'N/A',
                        'pass_possible': False
                    }
                else:
                    # Minimum grade required from Midterm and Final combined
                    required_combined = (passing_grade - (prelim_grade * 0.20)) / remaining_weight

                    # You could assume that both Midterm and Final are equally distributed
                    required_midterm = required_combined * (0.30 / remaining_weight)
                    required_final = required_combined * (0.50 / remaining_weight)

                    result = {
                        'prelim': prelim_grade,
                        'required_midterm': round(required_midterm, 2),
                        'required_final': round(required_final, 2),
                        'pass_possible': True
                    }
        except ValueError:
            error = 'Invalid input. Please enter a numerical grade.'

    return render_template('index.html', error=error, result=result)

if __name__ == '__main__':
    app.run(debug=True)
