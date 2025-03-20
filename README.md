# Running Development Server

Follow the instructions below to set up and run the Django application on your local development environment.

## Prerequisites

Before you start, make sure you have the following installed on your machine:

- **Python 3.x**: [Download and install Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually comes with Python)
- **virtualenv**: For creating a virtual environment (optional but recommended)

You can check if Python and pip are installed by running:

```bash
python --version
pip --version
```
## Step 1: Clone the Repository

Clone the project repository to your local machine using git:

```bash
git clone https://github.com/your-username/your-django-app.git
cd your-django-app
```
## Step 2: Create and Activate a Virtual Environment
It is recommended to create a virtual environment to manage project dependencies. To create and activate a virtual environment:

#### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies
With the virtual environment activated, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Step 4: Set Up the Database
To set up the default SQLite database, run:
```bash
python manage.py migrate
```

## Step 5: Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
## Step 6: Run the Development Server
Start the Django development server with the following command:

```bash
python manage.py runserver
```
The development server will be running at http://127.0.0.1:8000/. Open this URL in your browser to see your Django application in action.

## Step 7: Access the Admin Interface (Optional)
If you created a superuser account earlier, you can access the Django admin interface by visiting:

```arduino
http://127.0.0.1:8000/admin/
```
