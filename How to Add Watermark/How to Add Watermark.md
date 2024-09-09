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

**Loading the PDF**: The `PdfDocument.fromFile` method is used to load an existing PDF file from the specified path (`"sample.pdf"`). This initializes a `PdfDocument` object representing the loaded PDF.

**Defining the Watermark**: The watermark is defined as an HTML string (`"<h1 style='color:gray;'>Confidential</h1>"`). This allows for rich customization using HTML and CSS styling to define the appearance of the watermark.

**Applying the Watermark**: The `applyWatermark` method is used to apply the HTML-based watermark to all pages of the PDF. In this case, the text `"Confidential"` in gray is added as the watermark.

**Saving the File**: After the watermark is applied, the `saveAs` method saves the modified PDF to a new file named `"text_watermark.pdf"`. This step finalizes the changes made to the document.

### Output

The resulting PDF file, `"text_watermark.pdf"`, will have the specified watermark applied to all its pages, displaying the text `"Confidential"` in gray.
<iframe src="text_watermark.pdf" width="80%" height="400px" style="border: none;"></iframe>

## Image Watermark Example
IronPDF allows you to use images as watermarks, supporting various formats like PNG, JPEG, and SVG. The image can be styled and positioned using CSS within the HTML string.

```
package org.example;
import com.ironsoftware.ironpdf.*;

import java.io.IOException;
import java.nio.file.Paths;



PdfDocument pdf = PdfDocument.fromFile(Paths.get("sample.pdf"));
        // Image HTML watermark
        String watermarkHtml = "<img src='logo.png' style='width:100px;'/>";

        // Apply the image watermark
        pdf.applyWatermark(watermarkHtml);

        // Save the PDF
        pdf.saveAs("image_watermark.pdf");
```

### Understanding the Code

**Defining the Watermark**: The watermark is defined using an HTML string (`"<img src='logo.png' style='width:100px;'/>"`). This string specifies an image (`logo.png`) with a width of 100 pixels. The `src` attribute points to the image file, and the `style` attribute is used to adjust the image’s width.

**Applying the Watermark**: The `applyWatermark` method applies the HTML-based image watermark to all pages of the PDF. In this case, the image `logo.png` is added as a watermark.

### Output

The resulting PDF file, `"image_watermark.pdf"`, will have the specified image (`logo.png`) applied as a watermark to all its pages. The image will be displayed with a width of 100 pixels.

<iframe src="image_watermark.pdf" width="80%" height="400px" style="border: none;"></iframe>

## Watermark Opacity and Rotation Example
You can customize the watermark's appearance by adjusting its opacity and applying rotation. The applyWatermark() method allows you to specify both properties as parameters.

```
import com.ironsoftware.ironpdf.*;
import com.ironsoftware.ironpdf.stamp.HorizontalAlignment;
import com.ironsoftware.ironpdf.stamp.VerticalAlignment;


 PdfDocument pdf = PdfDocument.fromFile(Paths.get("sample.pdf"));
        // HTML for watermark
        String watermarkHtml = "<h1 style='color:blue;'>Confidential</h1>";

        // Apply the HTML watermark with 30% opacity, positioned at the top-left corner of each page
        pdf.applyWatermark(watermarkHtml, 30, VerticalAlignment.TOP, HorizontalAlignment.LEFT);

        // Save the PDF
        pdf.saveAs("watermark_opacity_rotation.pdf");
```


### Understanding the Code

**Loading the PDF**: The `PdfDocument.fromFile` method is used to load an existing PDF file from the specified path (`"sample.pdf"`). This initializes a `PdfDocument` object representing the loaded PDF.

**Defining the Watermark**: The watermark is defined using an HTML string (`"<h1 style='color:blue;'>Confidential</h1>"`). This string specifies text with the content `"Confidential"` styled in blue.

**Applying the Watermark**: The `applyWatermark` method applies the HTML-based watermark to all pages of the PDF with additional options:
- **Opacity**: The watermark is applied with `30%` opacity, making it partially transparent.
- **Vertical Alignment**: The watermark is aligned to the `TOP` of the page. Other vertical alignment options include:
  - **TOP**: Watermark appears at the top of the page.
  - **MIDDLE**: Watermark appears in the middle of the page.
  - **BOTTOM**: Watermark appears at the bottom of the page.
- **Horizontal Alignment**: The watermark is aligned to the `LEFT` of the page. Other horizontal alignment options include:
  - **LEFT**: Watermark appears on the left side of the page.
  - **CENTER**: Watermark appears at the center of the page.
  - **RIGHT**: Watermark appears on the right side of the page.

**Saving the File**: After the watermark is applied, the `saveAs` method saves the modified PDF to a new file named `"watermark_opacity_rotation.pdf"`. This step finalizes the changes made to the document.

### Output**

The resulting PDF file, `"watermark_opacity_rotation.pdf"`, will have the specified watermark applied to all its pages with 30% opacity. The watermark text `"Confidential"` in blue will be aligned to the top-left corner of each page.

<iframe src="watermark_opacity_rotation.pdf" width="80%" height="400px" style="border: none;"></iframe>

## Common Errors and Troubleshooting

- **Watermark Not Appearing**:
  - **Fix**: Verify the watermark is properly defined and applied. Check file paths and method usage.

- **Incorrect Watermark Placement**:
  - **Fix**: Adjust alignment parameters and ensure CSS properties do not interfere with positioning.

- **Opacity Issues**:
  - **Fix**: Ensure opacity values are correctly set between `0` and `100`.

- **Image Quality**:
  - **Fix**: Use high-resolution images and appropriate formats to prevent pixelation.

- **PDF Loading Errors**:
  - **Fix**: Confirm the file path is accurate and the PDF is not corrupted. Check for correct file permissions.

## Important Considerations
**Installation Note:** Ensure that the IronPDF library is correctly added to your project, either via Maven or manual import. Missing dependencies can lead to compilation errors.

**Image Quality:** When using image watermarks, ensure that the image has a high resolution and appropriate transparency. Low-quality images may appear pixelated or too prominent, detracting from the document's readability.


**Licensing:**
IronPDF offers different licensing options. Ensure you comply with their licensing terms, especially for commercial use. You can start with a free trial to evaluate the software before purchasing a license. For more details on licensing and the free trial, visit the IronPDF [Licensing page](https://ironpdf.com/java/licensing/).
