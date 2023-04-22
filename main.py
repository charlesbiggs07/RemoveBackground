from rembg import remove
from PIL import Image
import easygui as eg

input_path = eg.fileopenbox(title="open")
output_path = eg.filesavebox(title="save")
input = Image.open(input_path)
output = remove(input)
output.save(output_path)