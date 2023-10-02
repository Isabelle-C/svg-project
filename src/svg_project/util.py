from PIL import Image
import cairosvg

class Util:
    def __init__(self):
        pass
    
    @staticmethod
    def read_file(self, file_path) -> str:
        with open(file_path, "r") as file:
            file_read= file.read()
        # Print the SVG content
        print('SVG Content:\n')
        print(file_read)
        return file_read
        

    @staticmethod
    def convert_svg_to_png(input_svg_file, output_png_file):

        # Convert SVG to PNG using cairosvg
        cairosvg.svg2png(url=input_svg_file, write_to=output_png_file)

        # Open the PNG image using Pillow
        image = Image.open(output_png_file)

        # Optionally, you can resize the image if needed
        # image = image.resize((width, height), Image.ANTIALIAS)

        # Save the resized image
        image.save(output_png_file)
