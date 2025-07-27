import google.generativeai as genai
import pypdf
import json
import os

# --- CONFIGURATION ---
# IMPORTANT: Replace "YOUR_API_KEY" with your actual Google API key.
API_KEY = "AIzaSyBkW0GEvss-yogwYRMSLQ-Kn4ePHGW_Aaw"

genai.configure(api_key=API_KEY)

def get_extraction_prompt():
    """Returns the master prompt for data extraction."""
    return """
# ROLE:
You are an expert data extraction AI specialized in processing educational content. Your task is to act as a structured data parser for NCERT science textbooks.

# CONTEXT:
I will provide you with the full text content of a single chapter from the Class 8 NCERT Science textbook.

# TASK:
Your mission is to meticulously read the provided chapter text and extract its content into a structured JSON format. You must follow these rules precisely:

1.  **Extract Verbatim:** Do NOT summarize, interpret, rephrase, or add any information that is not explicitly present in the text. Extract the content exactly as it appears.
2.  **Extraction Elements:** Identify and extract only the following elements from the chapter:
    * Chapter Number and Title
    * Topic names/headers
    * Sub-topic names/headers
    * Paragraphs of text
    * Tables (preserve the structure as best as possible in a string)
    * Activities (including their title, instructions, and any questions within them)
    * Content inside special boxes (e.g., "Boojho wants to know", "Paheli's Corner", or other boxed facts)
    * Figures/Images/Diagrams (extract their captions and figure numbers, e.g., "Figure 6.1: Combustion")
    * Keywords listed at the end of the chapter.
    * All questions from the "Exercises" section at the end of the chapter.

# OUTPUT FORMAT:
You MUST format the entire output as a single, clean JSON object. Do not wrap it in markdown (e.g., ```json ... ```). The JSON must adhere to the following structure:

{
  "chapter_number": "Integer (e.g., 6)",
  "chapter_title": "Title of the Chapter",
  "content_tree": [
    {
      "level": 1,
      "type": "TOPIC",
      "content": "The name of the main topic",
      "children": [
        {
          "level": 2,
          "type": "SUB_TOPIC",
          "content": "The name of the sub-topic",
          "children": [
            { "level": 3, "type": "PARAGRAPH", "content": "The full text of the paragraph." },
            { "level": 3, "type": "FIGURE", "content": "Figure 6.2: A diagram showing..." },
            { "level": 3, "type": "ACTIVITY", "content": "Activity 6.1: ..." },
            { "level": 3, "type": "BOXED_CONTENT", "content": "The text inside a special info box." },
            { "level": 3, "type": "TABLE", "content": "A string representation of the table." }
          ]
        }
      ]
    }
  ],
  "exercises": [
    { "question_number": 1, "question_text": "The text of the first question." }
  ],
  "keywords": [ "keyword1", "keyword2" ]
}

# START OF CHAPTER TEXT:
"""

def extract_text_from_pdf(pdf_path):
    """Opens a PDF file and extracts all text content."""
    print(f"Reading text from {pdf_path}...")
    try:
        reader = pypdf.PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() + "\n"
        print("Text extraction complete.")
        return full_text
    except FileNotFoundError:
        print(f"ERROR: PDF file not found at {pdf_path}")
        return None

def get_structured_data_from_gemini(chapter_text):
    """Sends the prompt and chapter text to the Gemini API and gets the response."""
    # Using the 'gemini-1.5-flash' model from your quickstart guide
    model = genai.GenerativeModel('gemini-1.5-flash') 
    
    prompt = get_extraction_prompt() + chapter_text
    
    print("Sending request to Gemini API... This may take a moment.")
    response = model.generate_content(prompt)
    
    cleaned_response = response.text.strip().replace("```json", "").replace("```", "")
    
    print("Received response from Gemini.")
    return json.loads(cleaned_response)

def main():
    """Main function to run the data extraction process."""
    # Assumes the PDF is in the 'input_pdfs' subfolder
    pdf_file_path = "input_pdfs/hesc106.pdf" 
    
    # Saves the output to the 'outputs' subfolder with your specified filename
    output_json_path = "outputs/format.json" 

    chapter_content = extract_text_from_pdf(pdf_path=pdf_file_path)
    
    if chapter_content:
        try:
            structured_data = get_structured_data_from_gemini(chapter_text=chapter_content)
            
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_json_path), exist_ok=True)

            with open(output_json_path, 'w', encoding='utf-8') as f:
                json.dump(structured_data, f, indent=4, ensure_ascii=False)
                
            print(f"SUCCESS: Structured data has been saved to '{output_json_path}'")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            print("This could be due to an API key issue, network problem, or an invalid response from the API.")

if __name__ == "__main__":
    main()