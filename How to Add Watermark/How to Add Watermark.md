# How to Apply Custom PDF Watermarks
Watermarking is a popular technique for protecting PDF documents and asserting ownership or status, such as marking them as "Confidential" or branding them with a logo. 
IronPDF offers a simple yet powerful API for adding custom watermarks to PDF documents in Java. It provides a straightforward and highly customizable approach with parameters for opacity, rotation, and placement. Watermarks can include both text and images, styled using HTML and CSS for greater flexibility and customization.

This guide will demonstrate different types of watermarks—text, image, watermark location, opacity, and rotation adjustments, as well as advanced methods using [TextStamper](https://ironpdf.com/java/object-reference/api/com/ironsoftware/ironpdf/stamp/TextStamper.html) and [ImageStamper](https://ironpdf.com/java/object-reference/api/com/ironsoftware/ironpdf/stamp/ImageStamper.html).
## How to Apply Watermarks in Java
The steps to apply custom watermarks are as follows:
1. [Install IronPDF](https://central.sonatype.com/artifact/com.ironsoftware/ironpdf/2024.8.1) for Java.
2. Render a new PDF or load an existing one.
3. Configure the HTML string or image to be used as a watermark.
4. Apply the watermark using the appropriate method, adjusting parameters for opacity, rotation, and location as needed.

## Apply Text Watermark Example:
To apply a simple text watermark to a PDF document, use the applyWatermark() method. This allows you to input text using HTML and CSS for advanced styling.
```
package org.example;
import com.ironsoftware.ironpdf.*;

import java.io.IOException;
import java.nio.file.Paths;


PdfDocument pdf = PdfDocument.fromFile(Paths.get("sample.pdf"));
        // HTML text for watermark
        String watermarkHtml = "<h1 style='color:gray;'>Confidential</h1>";
        // Apply the watermark
        pdf.applyWatermark(watermarkHtml);
        // Save the PDF
        pdf.saveAs("text_watermark.pdf");
```

### Understanding the Code

1. **Loading the PDF**: The `PdfDocument.fromFile` method is used to load an existing PDF file from the specified path (`"sample.pdf"`). This initializes a `PdfDocument` object representing the loaded PDF.
2. **Defining the Watermark**: The watermark is defined as an HTML string (`"<h1 style='color:gray;'>Confidential</h1>"`). This allows for rich customization using HTML and CSS styling to define the appearance of the watermark.
3. **Applying the Watermark**: The `applyWatermark` method is used to apply the HTML-based watermark to all pages of the PDF. In this case, the text `"Confidential"` in gray is added as the watermark.
4. **Saving the File**: After the watermark is applied, the `saveAs` method saves the modified PDF to a new file named `"text_watermark.pdf"`. This step finalizes the changes made to the document.

### Output

The resulting PDF file, `"text_watermark.pdf"`, will have the specified watermark applied to all its pages, displaying the text `"Confidential"` in gray.
<iframe src="text_watermark.pdf" width="100%" height="600px" style="border: none;"></iframe>
