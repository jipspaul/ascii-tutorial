from PIL import Image
import argparse

# ASCII characters in increasing order of darkness
ASCII_CHARS = '@%#*+=-:. '

# Function to resize the image
def resize_image(image, new_width):
    width, height = image.size
    ratio = height / float(width)
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Function to convert grayscale pixel to ASCII character
def pixel_to_ascii(pixel_value):
    if pixel_value >= 256:
        return ASCII_CHARS[-1]
    index = int(pixel_value / 256 * len(ASCII_CHARS))
    return ASCII_CHARS[index]

# Function to convert the image to ASCII art
def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Error:", e)
        return

    image = resize_image(image, new_width)
    grayscale_image = image.convert('L')
    pixels = grayscale_image.getdata()
    ascii_characters = [pixel_to_ascii(pixel) for pixel in pixels]
    ascii_art = "".join(ascii_characters)

    # Split the string into lines of the same width as the resized image
    lines = [ascii_art[i:i + new_width] for i in range(0, len(ascii_art), new_width)]

    # Convert consecutive occurrences of each character to a readable format
    counted_lines = []
    for line in lines:
        char_count = 1
        counted_line = ""
        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                char_count += 1
            else:
                counted_line += f"{char_count} {line[i - 1]} "
                char_count = 1
        counted_line += f"{char_count} {line[-1]} "
        counted_lines.append(counted_line)

    ascii_art = "\n".join(counted_lines)

    return ascii_art, lines, new_width

def save_ascii_art_to_file(ascii_art, output_file):
    with open(output_file, "w") as f:
        f.write(ascii_art)

def print_ascii_art_preview(lines):
    num_preview_lines = len(lines)
    preview_lines = lines[:num_preview_lines]
    print("ASCII Art Preview:")
    for line in preview_lines:
        print(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert an image to ASCII art.')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--width', type=int, default=100, help='Output width of the ASCII art')
    parser.add_argument('--output_file', type=str, default='ascii_art.txt', help='Path to save the ASCII art')
    args = parser.parse_args()

    input_image_path = args.image_path
    output_width = args.width
    output_file = args.output_file

    ascii_art, lines, num_characters = image_to_ascii(input_image_path, output_width)

    print("Result:")
    print("ASCII Art:")
    print(ascii_art)
    print("\nNumber of Lines:", len(lines))
    print("Number of Characters per Line:", num_characters)

    # Print ASCII art preview
    print_ascii_art_preview(lines)

    # Save the ASCII art to a text file
    save_ascii_art_to_file(ascii_art, output_file)
    print(f"\nASCII art saved to '{output_file}'.")

