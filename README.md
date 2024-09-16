
# **Grade Requirement Calculator**

This project is a web-based grade requirement calculator built with Flask. It helps users determine if they can still pass their subject with a final grade of **75**, based on their Prelim score and the required Midterm and Final exam grades.

----------

## **Table of Contents**

1.  Requirements
2.  Setup Instructions
3.  Running the Application
4.  Using the Web Calculator
5.  Troubleshooting

----------

## **Requirements**

Before running this project, ensure you have the following installed:

-   **Python 3.8+**: You can download it from the [official website](https://www.python.org/downloads/).
-   **Flask**: The web framework used for this project.

----------

## **Setup Instructions**

1.  **Clone or Download the Project:**
    
    Clone this repository to your local machine using the following command: `git clone https://github.com/your-username/grade-requirement-calculator.git`
    
    Or download the ZIP file and extract it.
    
2.  **Navigate to the Project Directory:**
    
    Open a terminal or command prompt and navigate to the project folder: `cd grade-requirement-calculator`
    
3.  **Set Up a Virtual Environment (Optional but Recommended):**
    
    It's a good practice to use a virtual environment to manage dependencies. You can set it up with the following commands:
    
    On Windows: `python -m venv venv` `venv\Scripts\activate`
    
    On Mac/Linux: `python3 -m venv venv` `source venv/bin/activate`
    
4.  **Install Dependencies:**
    
    Once your virtual environment is activated, install the required packages by running: `pip install -r requirements.txt`
    
    If there’s no `requirements.txt` file, you can install Flask directly: `pip install Flask`
    

----------

## **Running the Application**

1.  **Run the Flask Application:**
    
    To start the Flask web server, run the following command in the terminal: `python app.py`
    
    If everything is set up correctly, you should see output similar to: `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
    
2.  **Open the Web Application:**
    
    Open your browser and go to: `http://127.0.0.1:5000/`
    
    The web calculator interface should now be displayed, and you can start entering your Prelim grade to calculate the required grades for Midterms and Finals.
    

----------

## **Using the Web Calculator**

1.  **Enter Your Prelim Grade:** Input a number between 0 and 100 into the Prelim grade field.
2.  **Click "Calculate":** Press the button to calculate the required Midterm and Final grades.
3.  **Review the Results:** Based on your input, the web calculator will display:
    -   The required Midterm and Final grades.
    -   Whether it's still possible to pass based on your Prelim score.
    -   An error message if the input is invalid.

----------

## **Troubleshooting**

1.  **Dependencies Not Installing:**
    
    -   Ensure you're using the correct Python version (3.8+).
    -   Double-check that the virtual environment is activated when installing Flask.
2.  **Application Not Launching:**
    
    -   Make sure you are running the `app.py` file within the project directory.
    -   Check that Flask is installed correctly by running `pip show Flask`.
3.  **Can't Access the Web Interface:**
    
    -   If the browser doesn't open the app at `http://127.0.0.1:5000/`, verify the terminal output to see if the server started properly.
    -   Ensure no other application is using port 5000.

----------

## **License**

This project is open source, and you are free to modify and share it under the terms of the MIT License.
