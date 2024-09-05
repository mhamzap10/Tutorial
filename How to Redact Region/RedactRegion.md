# How to Redact Region in PDF Files

Redacting sensitive information in PDF documents is crucial for ensuring privacy and compliance with data protection regulations. The [POST] Redact Region API from IronSecure Doc offers an efficient way to hide sensitive text and information in specific regions of a PDF document using true redaction. This API ensures that the redacted data is completely removed and cannot be recovered, making it ideal for handling confidential information in legal, financial, or personal documents.

## The [POST] Redact Region API

The [POST] Redact Region API endpoint allows you to hide sensitive information within specific regions of a PDF document using true redaction. This feature is crucial for applications that manage confidential documents, such as legal contracts, medical records, or financial statements. By leveraging this API, you can ensure that sensitive text within defined areas of a PDF is permanently removed, offering both security and compliance.

## Getting Started

This guide assumes you already have a container instance running. If you are looking to get started, please [follow our guide](https://ironsoftware.com/enterprise/securedoc/docs/).

## Trying It Out in Swagger

Swagger is a powerful tool that allows developers to interact with RESTful APIs using a user-friendly web interface. If you are using languages like Python, Java, or others, Swagger provides a convenient way to test and implement this API.

To begin, you can interactively test the API using Swagger:

### Steps to Use the API with Swagger

1. **Access the Swagger UI:**
    If your API server is running locally, you can access Swagger by navigating to http://localhost:8080/swagger/index.html in your web browser.
   
   <img width="950" alt="image" src="https://github.com/user-attachments/assets/b2b7fce4-3a82-406a-a2dd-e86f83509e02">
   
2. **Locate the [POST] Redact Region API:**
    Within the Swagger UI, find the [POST] /v1/document-services/pdfs/redact-region endpoint.
   
  <img width="947" alt="image" src="https://github.com/user-attachments/assets/dff90d01-2d92-4872-9c9b-33c06957ae1d">
 
3. **Specify Redaction Coordinates:**
    In this example, we will remove a table from the PDF on Page Index 1 (i.e., Page #2). Use the following coordinates to define the redaction region:
   - X Coordinate (region_to_redact_x): 60
   - Y Coordinate (region_to_redact_y): 270
   - Width (region_to_redact_w): 470
   - Height (region_to_redact_h): 200
 4. **Set Optional Parameters:**
    Optionally, you can add a user or owner password, specify specific pages (if other than the entire document), or decide whether to draw a black box over the redacted area and save the document with PDF/A or PDF/UA compliance.

    <img width="549" alt="Input_Swagger" src="https://github.com/user-attachments/assets/745d174e-5085-4ecc-b341-0fbe668f1c63">
   
5. **Upload a Sample PDF:**
    In the request body, upload a sample PDF file where you want to apply the redaction. Ensure that the file is added as pdf_file.   
6. **Execute the Request:**
    Click "Execute" to run the request. The response will include the redacted PDF, with the table removed from Page Index 1 as specified.
    
    <img width="944" alt="image" src="https://github.com/user-attachments/assets/f243f657-fc5f-46b1-afa8-11bfab903123">

This Swagger UI interaction allows you to test the redaction process easily, giving you immediate feedback on how the coordinates affect the PDF content.

## Understanding Input Parameters

Before using this API, it's essential to understand the input parameters required and optional for redacting a region in your PDF. These parameters help define the specific area to redact.

### Key Parameters

- **pdf_file:** The PDF document you want to redact.
- **region_to_redact_x:** X coordinate of the region to redact (starting from the bottom-left of the page).
- **region_to_redact_y:** Y coordinate of the region to redact (starting from the bottom-left of the page).
- **region_to_redact_w:** Width of the region to redact.
- **region_to_redact_h:** Height of the region to redact.
### Optional Parameters

- **user_password:** If the PDF is password-protected, provide the user password.
- **owner_password:** Provide the owner password if modifications are restricted.
- **specific_pages:** Specify which pages to redact. If not provided, the redaction applies to all pages.
- **save_as_pdfa:** Save the PDF wit h PDF/A-3 compliance.
- **save_as_pdfua:** Save the PDF with PDF/UA compliance.

## API Integration: Python Example

Once you're familiar with the parameters, you can call this API using your preferred programming language. Below is an example of how to integrate this API using Python.
```
import requests

url = 'http://localhost:8080/v1/document-services/pdfs/redact-region'
headers = {
    'accept': '*/*',
    'author': 'Hamza | IRONSECUREDOC',
    'title': 'REDACT REGION DEMO 2024',
    'subject': 'DEMO EXAMPLE'
}

files = {
    'pdf_file': ('sample_file.pdf', open('sample_file.pdf', 'rb'), 'application/pdf')
}

data = {
    'region_to_redact_x': '60',
    'region_to_redact_y': '270',
    'region_to_redact_w': '470',
    'region_to_redact_h': '200',
    'specific_pages':[1]
}

response = requests.post(url, headers=headers, files=files, data=data)

# Save the redacted PDF
with open('redacted_output.pdf', 'wb') as f:
    f.write(response.content)

print('PDF redacted successfully.')
```
This Code performs the following steps:

- **Load the PDF:** The PDF file to be redacted is loaded from the local file system.
- **Set Redaction Parameters:** Specify the coordinates (X, Y), width, and height of the region to redact.
- **Specify Pages:** Specify the Page Index. Make sure to index the correct Page as it starts from 0.
- **Call the API:** The [POST] Redact Region API is called, passing in the necessary parameters.
- **Save the Result:** The redacted PDF is saved as a new file.

The given Region is redacted as shown below. 

<img width="708" alt="image" src="https://github.com/user-attachments/assets/6de1d9be-f049-4907-a849-c77c77f10906">

## .NET / C# Integration
For .NET / C# developers, there is a [client-side library](https://ironsoftware.com/enterprise/securedoc/tutorials/set-up-in-csharp-dotnet/) available for calling this API. In all cases, ensure that the Docker container is installed and running. For guidance on setting up Docker, please follow the [provided guide](https://ironsoftware.com/enterprise/securedoc/docs/).

## Common Errors and Troubleshooting

### Invalid credentials provided for PDF:
Ensure that the correct user and owner passwords are provided. If the PDF is not password-protected, these parameters should be omitted.
### Failed to redact the PDF: 400 Bad Request:
This error occurs when the user or owner password provided does not match the PDF's security settings. Double-check the passwords and try again.
### Region Coordinates Out of Bounds:
Ensure that the coordinates for the redaction regions are within the bounds of the document. If the coordinates are out of range, the API will return an error.

## Important Considerations

### :information_source: Ensure Docker Container Is Running
Ensure that the Docker container is installed and running. If you need guidance, please follow this guide.

### :warning: Warning
Be cautious when redacting sensitive information. Once a region is redacted, the content within that area cannot be recovered.

### :bulb: Tip
For better accuracy, make sure the PDF file is clear and that the region coordinates are specified correctly.

### :x: Error Handling
If you receive an error during the redaction process, double-check the coordinates and ensure the PDF file is accessible.

