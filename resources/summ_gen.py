import re
import json

def extract_summaries(text_file):
    summaries = {}
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text using the pattern "Índice X:" as separators
    summary_sections = re.split(r'Índice \d+:', text)
    j=1
    
    for i, summary_section in enumerate(summary_sections):
        if i != 0 and summary_section.strip():  # Skip the first empty section
            # Remove leading and trailing whitespace
            summary_section = summary_section.strip()
            
            # Split the section into lines
            lines = summary_section.split('\n')
            
            # Remove any empty lines
            lines = [line.strip() for line in lines if line.strip()]
            
            # Join the lines to create the summary
            summary = ' '.join(lines)
            
            # Create a dictionary entry with the index and summary
            summaries[j] = summary
            j=j+1

    return summaries

if __name__ == "__main__":
    text_file = "text_summ.txt"
    summaries = extract_summaries(text_file)

    # Save the summaries in JSON file
    with open("spanish_summary.json", 'w', encoding='utf-8') as output_file:
        json.dump(summaries, output_file, ensure_ascii=False, indent=2)

    print("Summaries saved to 'spanish_summary.json'")
