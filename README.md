# Image to ASCII Art Converter

![Sample ASCII Art](sample_ascii_art.png)

This Python script allows you to convert an image to ASCII art. It takes an input image, resizes it, and then converts it to ASCII characters based on the pixel darkness. The resulting ASCII art can be saved to a text file and also previewed in the console.

## Prerequisites

- Python 3.x
- Pillow library (Python Imaging Library fork)

You can install the Pillow library using the following command:

```bash
pip install pillow

How to Use

Clone this repository or download the png_to_ascii.py file.
Place the image you want to convert to ASCII art in the same directory as the script.
Open a terminal or command prompt and navigate to the directory containing the script and the image.
Run the script with the following command:

python png_to_ascii.py <image_path>


Replace <image_path> with the name of the image file you want to convert.

Optional arguments:

--width: Output width of the ASCII art (default: 100). You can adjust this value to control the width of the ASCII art.
--output_file: Path to save the ASCII art (default: 'ascii_art.txt'). You can specify a custom file name or path.
For example, to convert an image named my_image.png to ASCII art with an output width of 80 and save the result as my_ascii_art.txt, use the following command:

bash
Copy code
python png_to_ascii.py my_image.png --width 80 --output_file my_ascii_art.txt
The script will display the ASCII art in the console, along with the number of lines and characters per line. It will also save the ASCII art to a text file if the --output_file argument is provided.
Additionally, a preview of the ASCII art will be displayed in the console, showing the first few lines of the ASCII representation.
Sample Output

Here's a sample output of running the script:

yaml
Copy code
Result:
ASCII Art:
10 . 3 = 1 - 1 = 1 + 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1
10 . 1 - 9 = 1 * # * # 1 # 1 * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1
10 . 1 # 8 = 1 % = 2 % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = *
10 . 1 % 8 + 4 % + = 2 % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = % = * = %
10 . 1 = + 8 + # 9 # 8 % # 4 = 1 * # 1 # 1 * 1 # 1 # 1 * 1 # 1 # 1 * 1 # 1 # 1 * 1 # 1 # 1 * 1 # 1 # 1 * 1 # 1 # 1
10 . 1 # 4 * 1 # 8 * 1 * # 4 * 1 # 8 * 1 * # 4 * 1 # 8 * 1 * # 4 * 1 # 8 * 1 * # 4 * 1 # 8 * 1 * # 4 * 1 # 8 * 1 * 1
Number of Lines: 6
Number of Characters per Line: 80

ASCII Art Preview:
10 . 3 = 1 - 1 = 1 + 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1 - 1 = 1
10 . 1 - 9 = 1 * # * # 1 # 1 * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1 # * 1 # 1
Sample ASCII Art

The sample_ascii_art.png image above was converted using this script.

csharp
Copy code
[ASCII Art Here]
Enjoy creating ASCII art from your images!

typescript
Copy code

Replace `[ASCII Art Here]` with the actual ASCII art representation of your sample image or any other example you wish to showcase. Save this content in a file named `README.md` in your project directory.
