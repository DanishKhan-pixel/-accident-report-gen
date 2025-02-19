# Django Violation Reporting System

This Django-based project allows users to report traffic violations using a web form. The form collects data such as date, time, location, license plate, speed, and an optional image. The submitted data is processed and converted into a downloadable PDF report.

## Features
- 📍 Automatic GPS location fetching
- 📷 Image upload for number plate
- 📄 PDF generation of the violation report
- 📝 Observations field for additional notes
- 🎨 Responsive Bootstrap-based UI

## Installation
### Prerequisites
- Python 3.x
- Django
- `pip install -r requirements.txt`



### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/DanishKhan-pixel/-accident-report-gen 
   cd bike_safety 
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the server:
   ```sh
   python manage.py runserver
   ```

## Usage
1. Open the web application in your browser at `http://127.0.0.1:8000/`
2. Fill in the form with the required details
3. Upload an image of the number plate (optional)
4. Click on `📄 PDF Generieren` to generate and download the violation report


## Contribution
Feel free to fork the repository, make enhancements, and submit a pull request.



🚀 Happy Coding!
    Muhammad Danish

