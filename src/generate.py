import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import json
import os

def generate_certificates():
    """
    Main function to generate certificates based on the config file.
    """
    # 1. LOAD CONFIGURATION
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("❌ Error: config.json not found! Make sure it's in the root directory.")
        return

    # 2. LOAD DATA
    try:
        data = pd.read_csv(config['data_path'])
    except FileNotFoundError:
        print(f"❌ Error: Data file not found at '{config['data_path']}'")
        return

    # 3. PREPARE OUTPUT DIRECTORY
    output_folder = config['output_folder']
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"📁 Created output directory: {output_folder}")

    print(f"\n🚀 Starting certificate generation for {len(data)} members...")

    # 4. CORE GENERATION LOOP
    for index, row in data.iterrows():
        try:
            # Open a fresh copy of the template for each certificate
            img = Image.open(config['template_path']).convert('RGB')
            draw = ImageDraw.Draw(img)

            # Draw each text element from the config file
            for element in config['elements']:
                column = element['column_name']
                text = str(row[column]) # Ensure data is string
                
                # Add prefix if it exists in config
                if 'prefix' in element:
                    text = element['prefix'] + text

                position = tuple(element['position'])
                font = ImageFont.truetype(config['font_path'], element['font_size'])
                
                # Use element-specific color, or fall back to default
                color = element.get("text_color", config.get("text_color", "black"))

                # Map alignment string to Pillow's anchor setting
                align_map = {'center': 'ms', 'left': 'ls', 'right': 'rs'}
                anchor = align_map.get(element['align'], 'ls') # Default to left-start

                draw.text(position, text, fill=color, font=font, anchor=anchor)

            # 5. SAVE THE CERTIFICATE
            output_filename = f"{row['FullName'].replace(' ', '_')}_certificate.pdf"
            output_path = os.path.join(output_folder, output_filename)
            img.save(output_path)
            
            print(f"✅ Generated: {output_filename}")

        except FileNotFoundError as e:
            print(f"❌ Error: A required file was not found. Check paths in config.json. Details: {e}")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred for {row['FullName']}: {e}")
            continue # Move to the next person

    print("\n🎉 All certificates generated successfully!")

# This makes the script runnable from the command line
if __name__ == "__main__":
    generate_certificates()