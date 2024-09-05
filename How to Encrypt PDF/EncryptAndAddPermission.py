#!/usr/bin/env python
# coding: utf-8

# In[6]:


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


# In[ ]:





# In[ ]:




