# How to Encrypt/Add Password & Permissions to PDF Files
Securing PDF files with passwords and specific permissions is vital for protecting sensitive documents from unauthorized access and manipulation. The [POST] Encrypt/Add Password & Permissions API from IronSecure Doc provides an efficient way to encrypt PDF files with user and owner passwords while configuring permissions for printing, form filling, annotations, and more. This API ensures that the PDF is fully protected and access is controlled, making it ideal for legal, financial, or personal documents.
## The [POST] Encrypt/Add Password & Permissions API
The [POST] Encrypt/Add Password & Permissions API allows you to add security layers to PDF documents by encrypting them with passwords and setting specific permissions for various operations. Whether it's granting read access, allowing form filling, or disabling printing, this API gives you control over how your PDF files are accessed and modified.
## Getting Started
Before diving into the API, ensure you have the IronSecure Doc container running. Follow the [setup guide](https://ironsoftware.com/enterprise/securedoc/docs/) if needed.
## Trying It Out in Swagger
Swagger offers a user-friendly interface to test this API interactively. You can use it to send test requests and receive responses without writing code, making it a great tool for developers who are using Python, Java, C#, Javascript or other programming languages.
### Steps to Use the API with Swagger:
1.  **Access Swagger UI:** Navigate to the Swagger UI by opening http://localhost:8080/swagger/index.html in your browser.

<img width="954" alt="image" src="https://github.com/user-attachments/assets/0544ad1a-86ee-4901-bfe2-3af7f6b22970">

2. **Locate the [POST] /v1/document-services/pdfs/encrypt:** Find the Encrypt/Add Password & Permissions API under the Document Services section.

<img width="956" alt="image" src="https://github.com/user-attachments/assets/d1c541d0-dbe1-45ca-aca3-ac9f8bbdb6ea">

3.  **Input Parameters:** Provide the required parameters for the API request. You can upload a sample PDF file and specify permissions.

<img width="428" alt="Input Swagger" src="https://github.com/user-attachments/assets/23843db1-1055-4a8f-9266-850f531423bf">

4.  **Upload PDF File:** In the request body, upload a PDF file as pdf_file and define the necessary permissions, such as allowing or restricting printing, form filling, and content extraction.
5. **Execute the Request:** Once all parameters are set, click "Execute" to send the request. The response will return the encrypted PDF with the specified security settings.

<img width="934" alt="Swagger-Response" src="https://github.com/user-attachments/assets/a8acd346-ccf7-41ce-a6a3-5c91a1abe547">

## Understanding Input Parameters
The API requires specific parameters to encrypt the PDF and assign permissions. Below is a breakdown of both required and optional parameters:
### Required Parameters:
-  **pdf_file:** The PDF file you want to encrypt.
-  **allow_extracting_content:** Boolean indicating whether content extraction is allowed.
-  **allow_form_filling:** Boolean indicating whether form filling is allowed.
-  **allow_annotations:** Boolean indicating whether annotations are allowed.
-  **allow_printing:** Boolean indicating whether printing is allowed.
-  **allow_modifications:** Boolean indicating whether modifications are allowed.
-  **new_owner_password:** The new owner password for the PDF, which grants full access and the ability to change permissions.

### Optional Parameters:
-  **user_password:** The current user password, required if the PDF has a user password to grant read access.
-  **owner_password:** The current owner password, required if the PDF has an owner password to grant full access.
-  **new_user_password:** The new user password for read access.
-  **save_as_pdfa:** Save the PDF as PDF/A-3 compliant.
-  **save_as_pdfua:** Save the PDF as PDF/UA compliant.

### Optional Headers:
-  **author:** Set the PDF Metadata Author property.
-  **title:** Set the PDF Metadata Title property.
-  **subject:** Set the PDF Metadata Subject property.

## API Integration: Python Example
Once you're familiar with the input parameters, you can call the API using Python or any other preferred language. Below is an example of how to integrate this API using Python.

```
import requests

url = 'http://localhost:8080/v1/document-services/pdfs/encrypt'
headers = {
    'accept': '*/*',
    'author': 'Hamza | IRONSECUREDOC',
    'title': 'ENCRYPTION DEMO 2024',
    'subject': 'DEMO EXAMPLE'
}

files = {
    'pdf_file': ('sample.pdf', open('sample.pdf', 'rb'), 'application/pdf')
}

data = {
    'allow_extracting_content': 'false',
    'allow_form_filling': 'true',
    'allow_annotations': 'true',
    'allow_printing': 'false',
    'allow_modifications': 'false',
    'new_owner_password': 'p4ssw0rd',
    'new_user_password': 'p4ssw0rd',
    'save_as_pdfa': 'false',
    'save_as_pdfua': 'false'
}

response = requests.post(url, headers=headers, files=files, data=data)

# Save the encrypted PDF
with open('encrypted_output.pdf', 'wb') as f:
    f.write(response.content)

print('PDF encrypted successfully.')

```
### Steps Explained:

-  **Load the PDF:** The PDF file to be encrypted is loaded from the local file system.
-  **Set Encryption Parameters:** Define permissions like allowing printing, form filling, and content extraction, as well as setting new passwords.
-  **Call the API:** The [POST] Encrypt/Add Password & Permissions API is called, passing the necessary parameters.
-  **Save the Result:** The encrypted PDF is saved as a new file.

The PDF file is encrypted as shown below:

<img width="444" alt="Password - Output" src="https://github.com/user-attachments/assets/f6726cc5-cd07-4171-aaf1-dadf09db0b41">

### .NET / C# Integration
For .NET/C# developers, the API can be integrated similarly. Make sure Docker is running, and use the provided [client-side libraries](https://ironsoftware.com/enterprise/securedoc/tutorials/set-up-in-csharp-dotnet/) to call the API.

## Common Errors and Troubleshooting
### Invalid passwords:
Ensure that the correct user and owner passwords are provided. If the PDF is not password-protected, omit these parameters.
### 400 Bad Request:
This error occurs when the provided user or owner password doesn't match the PDF's current security settings. Verify the passwords.
### Incorrect file format:
The API only accepts PDF files. Ensure the file type is correct.

## Important Considerations
### ℹ️ Ensure Docker Container Is Running:
Make sure your Docker container is up and running before calling the API.
### ⚠️ Be Cautious with Passwords:
Once a PDF is encrypted with a password, access may be limited based on the permissions you’ve set. Double-check the passwords before applying them.
