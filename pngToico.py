from PIL import Image

def png_to_ico(input_file, output_file):
    try:
        # Open the PNG image using Pillow
        with Image.open(input_file) as img:
            # Convert and save the image as an ICO file
            img.save(output_file, format="ICO", sizes=[(32, 32)])
            print(f"Conversion successful. {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = "wp2601082-4k-desktop-kali-linux-wallpapers.jpg"  # Replace with the path to your PNG file
    output_file = "output.ico"  # Replace with the desired output ICO file path
    png_to_ico(input_file, output_file)
