---
name: office-document-extraction
description: Extract content from Office documents (.docx, .pptx, .xlsx) to traceable Markdown. Use when you need to read, search, or analyze content from Office files.
license: MIT
compatibility: opencode
metadata:
  category: document-generation
---

# Office Document Extraction

Extract content from `.docx`, `.pptx`, and `.xlsx` files to traceable Markdown format.

## Installation

```bash
pip install python-docx python-pptx openpyxl
```

## Word Documents (.docx)

```python
from docx import Document

def extract_docx(input_path, output_path=None):
    doc = Document(input_path)
    lines = []
    
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            level = int(para.style.name[-1])
            lines.append(f"{'#' * level} {para.text}")
        else:
            lines.append(para.text)
    
    for table in doc.tables:
        lines.append("\n| " + " | ".join(cell.text for cell in table.rows[0].cells) + " |")
        lines.append("|" + "|".join(["---"] * len(table.rows[0].cells)) + "|")
        for row in table.rows[1:]:
            lines.append("| " + " | ".join(cell.text for cell in row.cells) + " |")
    
    content = "\n\n".join(lines)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return content
```

## PowerPoint (.pptx)

```python
from pptx import Presentation

def extract_pptx(input_path, output_path=None):
    prs = Presentation(input_path)
    lines = []
    
    for slide_num, slide in enumerate(prs.slides, 1):
        lines.append(f"\n## Slide {slide_num}")
        
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    lines.append(paragraph.text)
            
            if shape.has_table:
                table = shape.table
                lines.append("\n| " + " | ".join(cell.text for cell in table.rows[0].cells) + " |")
                lines.append("|" + "|".join(["---"] * len(table.rows[0].cells)) + "|")
                for row in table.rows[1:]:
                    lines.append("| " + " | ".join(cell.text for cell in row.cells) + " |")
    
    content = "\n\n".join(lines)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return content
```

## Excel (.xlsx)

```python
from openpyxl import load_workbook

def extract_xlsx(input_path, output_path=None):
    wb = load_workbook(input_path, data_only=True)
    lines = []
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        lines.append(f"\n## Sheet: {sheet_name}\n")
        
        data = list(ws.iter_rows(values_only=True))
        
        if not data:
            lines.append("(empty sheet)")
            continue
        
        header = [str(cell) if cell is not None else "" for cell in data[0]]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("|" + "|".join(["---"] * len(header)) + "|")
        
        for row in data[1:]:
            cells = [str(cell) if cell is not None else "" for cell in row]
            lines.append("| " + " | ".join(cells) + " |")
    
    content = "\n\n".join(lines)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return content
```

## Batch Extraction

```python
import os, glob

def extract_all(source_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    extractors = {'.docx': extract_docx, '.pptx': extract_pptx, '.xlsx': extract_xlsx}
    results = []
    for ext, extractor in extractors.items():
        for file_path in glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True):
            basename = os.path.splitext(os.path.basename(file_path))[0]
            output_path = os.path.join(output_dir, f"{basename}.md")
            try:
                extractor(file_path, output_path)
                results.append({"source": file_path, "output": output_path, "status": "success"})
            except Exception as e:
                results.append({"source": file_path, "output": None, "status": f"error: {str(e)}"})
    return results
```

## Limitations

- Does not extract images, diagrams, embedded charts, SmartArt
- Screenshots, comments, and revision history are not extracted
- Complex formatting may be lost in Markdown conversion

## When to Use

- Reading content from Office files for analysis
- Converting documents to searchable Markdown
- Extracting data from Excel for processing
- Preparing documents for RAG systems
