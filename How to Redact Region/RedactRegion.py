#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[ ]:




