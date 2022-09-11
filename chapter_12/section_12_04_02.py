from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('sample.jpg')
# img2 = img.rotate(45)
# plt.imshow(img2)
img_gray = img.convert('L')
img_gray.save('sample.gray.jpg')
plt.imshow(img_gray, cmap='gray')
plt.show()
