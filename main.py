import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from PIL import Image

# opens tkinter window to select path!
def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path


def generate_palette_from_image(filepath, num_colors):
    img = Image.open(filepath)
    img = img.resize((150, 150))
    img = img.convert('RGB')
    img_array = np.array(img)
    img_array_reshaped = img_array.reshape(-1, 3)

    selected_indices = np.random.choice(len(img_array_reshaped), num_colors, replace=False)
    palette = img_array_reshaped[selected_indices]

    return palette



filepath = select_image()
palette = generate_palette_from_image(filepath,5)
print(palette)
plt.imshow([palette])
plt.axis("off")
plt.show()
