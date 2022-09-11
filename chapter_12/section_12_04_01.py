from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('sample.jpg')
print(img)
# => <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1280x853 at 0x10BB19D80>

plt.imshow(img)
plt.show()
