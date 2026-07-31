---
name: xlsx-generation
description: Generate Excel spreadsheets (.xlsx) programmatically using Python. Use when creating data exports, reports, matrices, or any Excel file output.
license: MIT
compatibility: opencode
metadata:
  category: document-generation
---

# Excel Spreadsheet Generation

Generate professional Excel spreadsheets programmatically using Python.

## Installation

```bash
pip install openpyxl xlsxwriter pandas
```

## Basic Spreadsheet with openpyxl

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

def create_spreadsheet():
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    
    # Add headers
    headers = ["Name", "Value", "Date"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
        cell.alignment = Alignment(horizontal="center")
    
    # Add data
    data = [
        ["Item 1", 100, "2024-01-01"],
        ["Item 2", 200, "2024-01-02"],
    ]
    
    for row_idx, row_data in enumerate(data, 2):
        for col_idx, value in enumerate(row_data, 1):
            ws.cell(row=row_idx, column=col_idx, value=value)
    
    # Auto-adjust column widths
    for col in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(col)].width = 15
    
    wb.save('output.xlsx')
    return wb
```

## Using xlsxwriter (Better for Charts)

```python
import xlsxwriter

def create_with_charts():
    workbook = xlsxwriter.Workbook('chart.xlsx')
    worksheet = workbook.add_worksheet()
    
    # Add data
    data = [
        ['Month', 'Sales'],
        ['Jan', 100],
        ['Feb', 150],
        ['Mar', 200],
    ]
    
    for row_num, row_data in enumerate(data):
        for col_num, value in enumerate(row_data):
            worksheet.write(row_num, col_num, value)
    
    # Create chart
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'name': 'Sales',
        'categories': ['Sheet1', 1, 0, 3, 0],
        'values': ['Sheet1', 1, 1, 3, 1],
    })
    
    worksheet.insert_chart('D2', chart)
    workbook.close()
```

## Working with DataFrames

```python
import pandas as pd

def dataframe_to_excel(df, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Data', index=False)
        
        worksheet = writer.sheets['Data']
        for idx, col in enumerate(df.columns):
            worksheet.cell(1, idx + 1).font = Font(bold=True)
```

## Best Practices

1. **Use appropriate library** - openpyxl for formatting, xlsxwriter for charts
2. **Format headers** - Always format header rows for readability
3. **Auto-adjust columns** - Set column widths based on content
4. **Use formulas** - Let Excel calculate instead of hardcoded values
5. **Error handling** - Wrap file operations in try-except blocks

## When to Use

- Data exports and reports
- Inventory matrices
- Financial spreadsheets
- Data analysis outputs
- Batch report generation
