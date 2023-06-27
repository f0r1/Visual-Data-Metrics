import pandas as pd
import numpy as np
import cv2 
import matplotlib.pyplot as plt

# Загрузка изображения с помощью OpenCV (cv2)
image_path = 'image.jpg'
image = cv2.imread(image_path)

# Преобразование изображения в оттенки серого с помощью OpenCV (cv2)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Оценка освещения и контрастности
brightness = np.mean(gray_image) # Оценка освещения
contrast = (np.max(gray_image) - np.min(gray_image) / 255.0 ) # Оценка контрастности


# Создание DataFrame с оценками
metrics = ['Brightness', 'Contrast']
values = [brightness, contrast]
data = {'Metric': metrics, 'Value': values}
df = pd.DataFrame(data)

# Вывод DataFrame
print(df.to_string(index=False))

# Отображение изображения и гистограммы с помощью Matplotlib
plt.figure(figsize=(12,6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.hist(gray_image.ravel(), bins=256, color='gray', alpha=0.7)
plt.title('Pixel Intensity Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.show()