# from fpdf import FPDF
# import os

# # Function to generate the PDF
# def generate_pdf(data):
#     # Ensure the directory exists
#     directory = "static/reports"
#     if not os.path.exists(directory):
#         os.makedirs(directory)  # Create the directory if it doesn't exist

#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "", 12)

#     # Title
#     pdf.cell(0, 10, "Verstoßbericht - Fahrrad-Dashcam", ln=True, align="C")
#     pdf.ln(10)

#     # Date and Time
#     pdf.cell(0, 10, f"Datum und Uhrzeit: {data['date']} um {data['time']}", ln=True)
    
#     # Location
#     pdf.cell(0, 10, f"Ort: {data['location']}", ln=True)
    
#     # License Plate
#     pdf.cell(0, 10, f"Kennzeichen: {data['license_plate']}", ln=True)
    
#     # Distance and Speed
#     pdf.cell(0, 10, f"Abstand: {data['distance']} m", ln=True)
#     pdf.cell(0, 10, f"Geschwindigkeit: {data['speed']} km/h", ln=True)
    
#     # GPS Coordinates
#     pdf.cell(0, 10, f"GPS-Koordinaten: {data['gps']}", ln=True)

#     # Add Photo of Number Plate (if the photo exists)
#     if data.get('image_path'):
#         pdf.ln(10)
#         pdf.cell(0, 10, "Foto des Kennzeichens:", ln=True)
#         # Ensure the image is valid and within the size limits
#         try:
#             pdf.image(data['image_path'], x=10, w=100)  # Adjust width as needed
#         except Exception as e:
#             print(f"Error adding photo: {e}")
    
#     # Observations
#     pdf.ln(10)
#     pdf.cell(0, 10, "Beobachtungen:", ln=True)
#     pdf.multi_cell(0, 10, data['observations'])

#     # Save the PDF file in static/reports directory
#     file_path = f"static/reports/verstoßbericht_{data['date'].replace('.', '-')}.pdf"
#     pdf.output(file_path)
#     return file_path



from fpdf import FPDF
import os

# Function to generate the PDF
def generate_pdf(data):
    # Ensure the directory exists
    directory = "static/reports"
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it doesn't exist

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "", 12)

    # Title
    pdf.cell(0, 10, "Verstoßbericht - Fahrrad-Dashcam", ln=True, align="C")
    pdf.ln(10)

    # Date and Time
    pdf.cell(0, 10, f"Datum und Uhrzeit: {data['date']} um {data['time']}", ln=True)
    
    # Location
    pdf.cell(0, 10, f"Ort: {data['location']}", ln=True)
    
    # License Plate
    pdf.cell(0, 10, f"Kennzeichen: {data['license_plate']}", ln=True)
    
    # Distance and Speed
    pdf.cell(0, 10, f"Abstand: {data['distance']} m", ln=True)
    # pdf.cell(0, 10, f"Geschwindigkeit: {data['speed']} km/h", ln=True)
    
    # GPS Coordinates
    pdf.cell(0, 10, f"GPS-Koordinaten: {data['gps']}", ln=True)

    # Add a space between sections
    pdf.ln(10)

    # Add Photo of Number Plate (if the photo exists)
    if data.get('image_path'):
        pdf.cell(0, 10, "Foto des Kennzeichens:", ln=True)
        
        try:
            # Resize the image to fit the page
            pdf.image(data['image_path'], x=10, w=180)  # Adjust width to 180mm
        except Exception as e:
            print(f"Error adding photo: {e}")
    
    # Add a space between the image and the next section
    pdf.ln(10)

    # Observations
    pdf.cell(0, 10, "Beobachtungen:", ln=True)
    pdf.multi_cell(0, 10, data['observations'])

    # Save the PDF file in static/reports directory
    file_path = f"static/reports/verstoßbericht_{data['date'].replace('.', '-')}.pdf"
    pdf.output(file_path)
    return file_path
