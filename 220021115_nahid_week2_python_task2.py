import cv2
import os
import numpy as np
import requests
import os

def download_image(image_url, file_dir):
    response = requests.get(image_url)

    if response.status_code == 200:
        sdirectory = os.path.dirname(file_dir)
        if not os.path.exists(sdirectory):
            os.makedirs(sdirectory)

        with open(file_dir, "wb") as fp:
            fp.write(response.content)
        print("Image downloaded successfully.")
    else:
        print(f"Failed to download the image. Status code: {response.status_code}")

image_url = "https://raw.githubusercontent.com/sadiqueer/220021115/main/b.jpg"
file_dir = "C:/Users/User/Downloads/s.jpg"
download_image(image_url, file_dir)

image_path = r'C:/Users/User/Downloads/s.jpg'
img = cv2.imread(image_path)
directory = r'C:/Users/User/Downloads'


ksize= (10, 10)
bimg=cv2.blur(img, ksize)
cv2.imshow("image", bimg)
os.chdir(directory) 
filename = 's-blur.jpg'
cv2.imwrite(filename, bimg) 
cv2.waitKey(0)

bimg = cv2.imread(image_path, 0)
cv2.imshow("image1", bimg)
os.chdir(directory) 
filename = 's-gray.jpg'
cv2.imwrite(filename, bimg)
cv2.waitKey(0)

bimg = cv2.bitwise_not(img)
cv2.imshow("image2", bimg)
os.chdir(directory) 
filename = 's-inv.jpg'
cv2.imwrite(filename, bimg)
cv2.waitKey(0)

def add_random_noise(image, intensity=25):
    noisy_image = image.copy()
    noise = np.random.randint(-intensity, intensity + 1, noisy_image.shape)
    noisy_image = np.clip(noisy_image + noise, 0, 255).astype(np.uint8)
    return noisy_image
nimg = add_random_noise(img, intensity=25)
cv2.imshow("image3", nimg)
os.chdir(directory) 
filename = 's-noise.jpg'
cv2.imwrite(filename, nimg)
cv2.waitKey(0)

kernel = np.ones((6, 6), np.uint8) 
erimage = cv2.erode(img, kernel, cv2.BORDER_REFLECT)
cv2.imshow("image4", erimage)
os.chdir(directory) 
filename = 's-erode.jpg'
cv2.imwrite(filename, erimage)
cv2.waitKey(0)

dimage = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("image5", dimage)
os.chdir(directory) 
filename = 's-dilate.jpg'
cv2.imwrite(filename, dimage)
cv2.waitKey(0)

cv2.destroyAllWindows()



  
  

  
 
