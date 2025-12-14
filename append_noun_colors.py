import json
import time
import os
from extract_colors import get_noun_colors

def main():
    start_id = 1
    end_id = 999
    output_file = 'noun_colors_extracted.json'
    
    # Load existing data
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            try:
                all_colors = json.load(f)
            except json.JSONDecodeError:
                print(f"Error decoding {output_file}. Starting with empty dictionary.")
                all_colors = {}
    else:
        all_colors = {}
    
    print(f"Starting extraction for Nouns {start_id} to {end_id}...")
    
    for noun_id in range(start_id, end_id + 1):
        # Skip if already exists (optional, but good for resuming)
        if str(noun_id) in all_colors:
             print(f"Noun {noun_id} already exists. Skipping...", end='\r')
             continue

        print(f"Processing Noun {noun_id}...", end='\r')
        colors = get_noun_colors(noun_id)
        if colors:
            all_colors[str(noun_id)] = colors
        
        # Be nice to the server
        time.sleep(0.1)

    print(f"\nExtraction complete. Saving to {output_file}...")
    
    with open(output_file, 'w') as f:
        json.dump(all_colors, f, indent=2)
        
    print("Done!")

if __name__ == "__main__":
    main()
