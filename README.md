# NCERT Chapter 13: Light - Data Extraction and Output Generation

This project extracts structured data Books PDF files and generates outputs such as knowledge graphs, formatted JSON, and Excel files.

## Project Structure

```
.
├── .env
├── .gitignore
├── data_extraction_prompt.pdf
├── extract_data.py
├── generate_outputs.py
├── Study_plan_prompt.pdf
├── Data-Extractor/
│   ├── .gitignore
│   ├── extract_data.py
│   ├── generate_outputs.py
│   ├── input_pdfs/
│   │   ├── chapter13.pdf
│   │   ├── chapter6.pdf
│   │   ├── chapter7.pdf
│   │   └── chapter8.pdf
│   └── outputs/
│       ├── chapter_graph.txt
│       ├── chapter_output.xlsx
│       └── format.json
├── input_pdfs/
│   ├── chapter13.pdf
│   ├── chapter6.pdf
│   ├── chapter7.pdf
│   └── chapter8.pdf
├── outputs/
│   ├── chapter_graph.txt
│   ├── chapter_output.xlsx
│   └── format.json
└── prompts/
```

## Main Scripts

- [`extract_data.py`](extract_data.py): Extracts structured data from input PDF files.
- [`generate_outputs.py`](generate_outputs.py): Generates outputs (knowledge graph, JSON, Excel) from extracted data.

## Usage

1. **Prepare Input PDFs**
   - Place chapter PDFs in `input_pdfs/` or `Data-Extractor/input_pdfs/`.

2. **Extract Data**
   - Run the extraction script:
     ```sh
     python extract_data.py
     ```
   - This will process the PDFs and generate intermediate data.

3. **Generate Outputs**
   - Run the output generation script:
     ```sh
     python generate_outputs.py
     ```
   - Outputs will be saved in the `outputs/` or `Data-Extractor/outputs/` directory:
     - `chapter_graph.txt`: Indented knowledge graph of the chapter.
     - `chapter_output.xlsx`: Excel file with structured data.
     - `format.json`: JSON file with the chapter's structure and content.

## Output Files

- [`outputs/chapter_graph.txt`](outputs/chapter_graph.txt): Text-based knowledge graph.
- [`outputs/chapter_output.xlsx`](outputs/chapter_output.xlsx): Excel spreadsheet of extracted data.
- [`outputs/format.json`](outputs/format.json): Structured JSON representation.

## Customization

- Modify the extraction or output generation logic in [`extract_data.py`](extract_data.py) and [`generate_outputs.py`](generate_outputs.py) as needed.
- Prompts for extraction can be found in the `prompts/` directory.

## Requirements

- Python 3.x
- Required packages (install via pip as needed, e.g., `PyPDF2`, `pandas`, etc.)

## License

This project is for educational and research purposes.

---

*For more details, see the code in [`Data-Extractor/extract_data.py`](Data-Extractor/extract_data.py) and [`Data-Extractor/generate_outputs.py`](Data-Extractor/generate_outputs.py).*
