# Flask School LMS

A comprehensive School Learning Management System (LMS) built with Python and Flask. This application facilitates interaction between teachers and students, allowing for group management, test creation, grading, and progress tracking.

## Features

* **Role-Based Access Control:** Distinct panels for **Teachers** and **Students**.
* **Student Panel:**
    * Take assigned tests and quizzes.
    * View grade history and calculate average scores.
    * Track progress across different subjects.
    * Review past test attempts and results.
* **Teacher Panel:**
    * Create, edit, and delete tests with custom questions.
    * Manage student groups (add/remove students).
    * View results and grade specific attempts.
    * Manually add grades for subjects.
* **Database Integration:** Uses SQLite with SQLAlchemy ORM for efficient data management.
* **Automatic Seeding:** Automatically initializes default subjects (Math, Physics, IT, etc.) upon first launch.

## Tech Stack

* **Language:** Python 3.x
* **Framework:** Flask
* **Database:** SQLite, SQLAlchemy (Flask-SQLAlchemy)
* **Templating:** Jinja2
* **Frontend:** HTML5, CSS3 (Bootstrap-ready structure)

## 📸 Interface Screenshots

### General
![Landing Page](screenshots/main_panel.png)
*Main landing page describing the platform features.*

### Student Zone
**Dashboard & Stats**
![Student Dashboard](screenshots/student_panel.png)
*Student view showing grade average, available tests, and recent history.*

**Taking a Test**
![Test Interface](screenshots/student_test_panel.png)
*Clean and distraction-free interface for solving quizzes.*

### Teacher Zone
**Teacher Dashboard**
![Teacher Panel](screenshots/teacher_panel.png)
*Central hub for managing tests, grades, and student groups.*

**Test Management**
![Test List](screenshots/teacher_test_panel.png)
*Overview of created tests with options to edit or view results.*

**Creating Tests**
![Edit Test](screenshots/teacher_test_creation_panel.png)
*Interface for configuring test details and assigning groups.*

**Question Editor**
![Add Questions](screenshots/teacher_question_panel.png)
*Tool for adding questions and defining correct answers.*

## Getting Started

Follow these instructions to set up and run the project locally on your machine.

### Prerequisites

* Python 3.8 or higher installed.
* Git (for cloning the repository).

## ⚡ Quick Start

```bash```
1. **Clone & Setup**
    git clone https://github.com/Jahgodka/flask-school-lms.git
    cd flask-school-lms
    python -m venv venv
    source venv/bin/activate  # Windows: .\venv\Scripts\activate
    pip install -r requirements.txt

2. **Run** (Database initializes automatically on first run)
    export FLASK_DEBUG=1      # Optional
    python app.py

### Running the Application

1.  **Start the server**
    Run the application using Python. This will automatically create the database file (`instance/database.db`) and seed default subjects if they don't exist.
    ```bash
    python app.py
    ```

2.  **Access the App**
    Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

3.  **First Steps**
    * Go to the **Register** page.
    * Create a **Teacher** account first to set up groups and tests.
    * Create a **Student** account to test the taking of quizzes.

## Project Structure

* `app.py`: Main application entry point and route definitions.
* `models.py`: Database models (User, Test, Question, Grade, etc.).
* `templates/`: HTML templates for the user interface.
* `instance/`: Contains the SQLite database (created after running the app).
* `requirements.txt`: List of Python dependencies.
