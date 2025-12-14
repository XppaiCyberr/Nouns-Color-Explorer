import requests
from PIL import Image
from io import BytesIO
import json
import time

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def get_noun_colors(noun_id):
    url = f'https://noun.pics/{noun_id}.png'
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        
        colors = {}
        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                hex_color = rgb_to_hex((r, g, b))
                colors[hex_color] = colors.get(hex_color, 0) + 1
                
        return colors
    except Exception as e:
        print(f"Error processing noun {noun_id}: {e}")
        return None

def main():
    start_id = 1000
    end_id = 1747
    output_file = 'noun_colors_extracted.json'
    
    all_colors = {}
    
    print(f"Starting extraction for Nouns {start_id} to {end_id}...")
    
    for noun_id in range(start_id, end_id + 1):
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
