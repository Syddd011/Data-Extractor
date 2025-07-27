import json
import pandas as pd

def parse_json_for_excel(data):
    """
    Flattens the nested JSON data from the content_tree into a list of rows 
    suitable for an Excel sheet.
    """
    rows = []
    chapter_num = data.get("chapter_number")
    chapter_title = data.get("chapter_title")

    # Process the main content tree
    for topic in data.get("content_tree", []):
        topic_content = topic.get("content", "")
        for sub_topic in topic.get("children", []):
            sub_topic_content = sub_topic.get("content", "")
            if not sub_topic.get("children"):
                rows.append([chapter_num, chapter_title, topic_content, sub_topic_content, "", ""])
            for item in sub_topic.get("children", []):
                rows.append([
                    chapter_num,
                    chapter_title,
                    topic_content,
                    sub_topic_content,
                    item.get("type", ""),
                    item.get("content", "")
                ])

    # Add a separator for exercises
    rows.append(["---", "---", "---", "---", "---", "---"])
    rows.append(["", "", "", "", "EXERCISES", ""])
    
    # Process exercises
    for exercise in data.get("exercises", []):
        rows.append([
            chapter_num, 
            chapter_title, 
            "Exercises", 
            "", 
            f"Question {exercise.get('question_number')}", 
            exercise.get('question_text')
        ])
    
    return rows

def generate_knowledge_graph(data):
    """
    Creates a simple text-based, indented representation of the chapter's structure.
    """
    graph_lines = []
    graph_lines.append(f"Chapter {data.get('chapter_number')}: {data.get('chapter_title')}\n")

    # Process content tree
    for topic in data.get("content_tree", []):
        graph_lines.append(f"|-- TOPIC: {topic.get('content')}")
        for sub_topic in topic.get("children", []):
            graph_lines.append(f"|   |-- SUB_TOPIC: {sub_topic.get('content')}")
            for item in sub_topic.get("children", []):
                graph_lines.append(f"|   |   |-- {item.get('type')}: {item.get('content', '')[:80]}...") 

    # Process exercises
    graph_lines.append("\n|-- EXERCISES")
    for exercise in data.get("exercises", []):
        graph_lines.append(f"|   |-- Question {exercise.get('question_number')}: {exercise.get('question_text')}")
        
    # Process keywords
    graph_lines.append("\n|-- KEYWORDS")
    for keyword in data.get("keywords", []):
        graph_lines.append(f"|   |-- {keyword}")
        
    return "\n".join(graph_lines)

def main():
    """Main function to load JSON and generate output files."""
    input_json_path = "outputs/format.json"
    output_excel_path = "outputs/chapter_data.xlsx"
    output_kg_path = "outputs/chapter_knowledge_graph.txt"

    print(f"--- Running Debugging Script ---")
    print(f"Loading data from {input_json_path}...")
    try:
        with open(input_json_path, 'r', encoding='utf-8') as f:
            structured_data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: The file was not found at {input_json_path}")
        return
    except json.JSONDecodeError:
        print(f"ERROR: The file at {input_json_path} is not valid JSON.")
        return

    # --- DEBUGGING PRINTS ---
    # Check if the main keys exist and how many items they have
    content_tree_items = structured_data.get('content_tree', [])
    exercises_items = structured_data.get('exercises', [])
    keywords_items = structured_data.get('keywords', [])

    print(f"DEBUG: Found {len(content_tree_items)} items in 'content_tree'.")
    print(f"DEBUG: Found {len(exercises_items)} items in 'exercises'.")
    print(f"DEBUG: Found {len(keywords_items)} items in 'keywords'.")
    # --- END DEBUGGING ---

    if not content_tree_items and not exercises_items:
        print("WARNING: The JSON file seems to be missing 'content_tree' and 'exercises' data. Output files will be empty.")

    # 1. Generate the Excel File
    print("Generating Excel file...")
    excel_rows = parse_json_for_excel(structured_data)
    df = pd.DataFrame(excel_rows, columns=[
        "Chapter Number", "Chapter Title", "Level 1: Topic", 
        "Level 2: Sub-Topic", "Content Type", "Content"
    ])
    df.to_excel(output_excel_path, index=False)
    print(f"SUCCESS: Excel file saved to {output_excel_path}")

    # 2. Generate the Knowledge Graph
    print("Generating knowledge graph...")
    kg_text = generate_knowledge_graph(structured_data)
    with open(output_kg_path, 'w', encoding='utf-8') as f:
        f.write(kg_text)
    print(f"SUCCESS: Knowledge graph saved to {output_kg_path}")
    print(f"--- Debugging Script Finished ---")

if __name__ == "__main__":
    main()