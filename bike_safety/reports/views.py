# from django.shortcuts import render, redirect
# from django.http import HttpResponse, FileResponse
# from .utils import generate_pdf
# import requests
# import os

# # Function to get location (simulating GPS)
# def get_location():
#     try:
#         response = requests.get("https://ipinfo.io/json", timeout=5)
#         data = response.json()
#         return data.get("loc", "0,0")  # Returns latitude, longitude
#     except Exception as e:
#         print(f"Error fetching location: {e}")
#         return "0,0"

# # View to handle form submission and PDF generation
# def report_violation(request):
#     if request.method == "POST":
#         uploaded_image = request.FILES.get("photo")  # Get uploaded image
        
#         image_path = None
#         if uploaded_image:
#             image_dir = "static/uploads"
#             os.makedirs(image_dir, exist_ok=True)  # Ensure directory exists
#             image_path = f"{image_dir}/{uploaded_image.name}"
#             with open(image_path, "wb") as f:
#                 for chunk in uploaded_image.chunks():
#                     f.write(chunk)

#         # Collect Data
#         data = {
#             "date": request.POST.get("date"),
#             "time": request.POST.get("time"),
#             "location": request.POST.get("location"),
#             "license_plate": request.POST.get("license_plate"),
#             "distance": request.POST.get("distance"),
#             "speed": request.POST.get("speed"),
#             "gps": get_location(),  # Get location dynamically
#             "observations": request.POST.get("observations"),
#             "image_path": image_path,  # Pass Image Path
#         }

#         pdf_path = generate_pdf(data)  # Generate PDF
        
#         # Serve the PDF as a downloadable file
#         return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")

#     return render(request, "index.html", {"gps": get_location()})




from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .utils import generate_pdf
import requests
import os

# Function to get location (simulating GPS)
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        data = response.json()
        return data.get("loc", "0,0")  # Returns latitude, longitude
    except Exception as e:
        print(f"Error fetching location: {e}")
        return "0,0"

# View to handle form submission and PDF generation
def report_violation(request):
    if request.method == "POST":
        uploaded_image = request.FILES.get("photo")  # Get uploaded image
        
        image_path = None
        if uploaded_image:
            image_dir = "static/uploads"
            os.makedirs(image_dir, exist_ok=True)  # Ensure directory exists
            image_path = f"{image_dir}/{uploaded_image.name}"
            with open(image_path, "wb") as f:
                for chunk in uploaded_image.chunks():
                    f.write(chunk)

        # Collect Data
        data = {
            "date": request.POST.get("date"),
            "time": request.POST.get("time"),
            "location": request.POST.get("location"),
            "license_plate": request.POST.get("license_plate"),
            "distance": request.POST.get("distance"),
            "speed": request.POST.get("speed"),
            "gps": get_location(),  # Get location dynamically
            "observations": request.POST.get("observations"),
            "image_path": image_path,  # Pass Image Path
        }

        pdf_path = generate_pdf(data)  # Generate PDF
        
        # Serve the PDF as a downloadable file
        return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")

    return render(request, "index.html", {"gps": get_location()})
