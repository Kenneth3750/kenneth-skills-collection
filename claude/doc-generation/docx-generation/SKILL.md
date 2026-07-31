---
name: docx-generation
description: Generate Word documents (.docx) programmatically using Python. Use when creating reports, documents, or any Word file output.
---

# Word Document Generation

Generate professional Word documents programmatically using Python and python-docx.

## Installation

```bash
pip install python-docx
```

## Basic Document Structure

```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_document():
    doc = Document()
    
    # Add title
    title = doc.add_heading('Document Title', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Add sections
    doc.add_heading('Section 1', 1)
    doc.add_paragraph('Content for section 1')
    
    # Add table
    table = doc.add_table(rows=3, cols=3)
    table.style = 'Light Grid Accent 1'
    
    # Save document
    doc.save('output.docx')
    return doc
```

## Common Operations

### Working with Paragraphs

```python
def add_formatted_text(doc):
    p = doc.add_paragraph('Normal paragraph', style='Normal')
    
    # Add formatted runs
    p.add_run('Bold text').bold = True
    p.add_run(' and ')
    p.add_run('italic text').italic = True
    
    # Add colored text
    run = p.add_run(' Red text')
    run.font.color.rgb = RGBColor(255, 0, 0)
    run.font.size = Pt(12)
```

### Working with Tables

```python
def create_table(doc, data, headers):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Light Grid Accent 1'
    
    # Add headers
    header_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        header_cells[i].text = header
        header_cells[i].paragraphs[0].runs[0].font.bold = True
    
    # Add data rows
    for row_data in data:
        row = table.add_row().cells
        for i, cell_data in enumerate(row_data):
            row[i].text = str(cell_data)
    
    return table
```

### Working with Images

```python
def add_image(doc, image_path, width_inches=4):
    doc.add_picture(image_path, width=Inches(width_inches))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
```

## Best Practices

1. **Use styles consistently** - Define and reuse custom styles
2. **Modular functions** - Break document creation into reusable functions
3. **Error handling** - Wrap file operations in try-except blocks
4. **Template approach** - Use existing .docx files as templates when possible
5. **Test output** - Always verify generated documents open correctly

## When to Use

- Generating reports from data
- Creating document templates
- Automating document workflows
- Batch document generation
