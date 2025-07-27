# NCERT Science Chapter Extractor & Planner

This project uses Python and the Google Gemini API to automatically extract structured content from NCERT Class 8 Science textbook chapters. It then processes this data into user-friendly formats like an Excel spreadsheet and a text-based knowledge graph.

---

## Features

* Automated Content Extraction: Pulls topics, sub-topics, paragraphs, activities, and exercises directly from PDF files.
* Structured JSON Output: Generates a clean, structured JSON file of the chapter's content.
* Excel & Knowledge Graph: Converts the JSON data into a well-formatted .xlsx file and a human-readable .txt knowledge graph.
* Secure API Key Handling: Uses a .env file to keep your Google API key safe and out of the repository.

---

## Setup & Installation

Follow these steps to set up the project on your local machine.

1.  Clone the Repository
    ```bash
    git clone [https://github.com/your-username/NCERT-Data-Extractor.git](https://github.com/your-username/NCERT-Data-Extractor.git)
    cd NCERT-Data-Extractor
    ```

2.  Create and Activate a Virtual Environment
    ```bash
    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Install Dependencies
    This project's dependencies are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  Set Up Your API Key
    * Create a file named `.env` in the main project folder.
    * Add your Google Gemini API key to this file:
        ```text
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```

---

## How to Use

1.  Add a PDF: Place the NCERT chapter PDF you want to process into the `input_pdfs/` folder.

2.  Run the Extraction Script: This script reads the PDF and creates the `format.json` file in the `outputs/` folder.
    ```bash
    python extract_data.py
    ```

3.  Run the Output Generation Script: This script reads `format.json` and creates the Excel and knowledge graph files.
    ```bash
    python generate_outputs.py
    ```

---

## Project Outputs

After running the scripts, you will find the following files in the `outputs/` folder:

* `format.json`: The raw, structured data extracted from the chapter.
* `chapter_data.xlsx`: An Excel spreadsheet containing the chapter content, organized by topics and sub-topics.
* `chapter_knowledge_graph.txt`: A text file showing the hierarchical relationship between all the content elements.