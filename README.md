# Анализ освещения и контрастности изображения

Этот код представляет собой пример использования библиотек Pandas, NumPy, OpenCV (cv2) и Matplotlib для анализа освещения и контрастности изображения.
## Установка зависимостей
Для успешного выполнения кода необходимо установить следующие зависимости:

- pandas
- numpy
- opencv-python
- matplotlib

Вы можете установить их, используя pip, командой:
## *pip install pandas numpy opencv-python matplotlib*

## Использование
Убедитесь, что у вас есть изображение *"image.jpg"* в том же каталоге, где находится этот код. Или измените путь *image_path* на путь к вашему изображению.

**Установите все необходимые зависимости, как указано выше.**

Запустите код и оцените освещение и контрастность изображения. Результаты будут выведены в виде DataFrame, а также будет отображено оригинальное изображение и его гистограмма.

## Примечание
При возникновении ошибки *"cv2.error: ..."* проверьте правильность указанного пути к изображению и убедитесь, что изображение существует и доступно для чтения.

-------------------------------------------------------------------------------------------------------------
# Visual Data Metrics
This code performs an analysis of image lighting and contrast. It utilizes the Pandas, NumPy, OpenCV (cv2), and Matplotlib libraries to perform various operations.
First, the code loads the image using OpenCV and converts it to grayscale. Then, it computes the metrics for lighting and contrast based on the image pixels.
To calculate the lighting, the average brightness value of the grayscale pixels is used. The contrast is determined as the difference between the maximum and minimum pixel intensities, normalized within the range of 0 to 1.
After calculating the lighting and contrast metrics, a DataFrame is created using Pandas. The DataFrame is then displayed on the screen.
The code also visualizes the original image and its histogram using Matplotlib. The histogram shows the distribution of pixel intensities in the image.
By using this code, you can quickly assess the lighting and contrast of an image and visualize them for better understanding.

*Note: Make sure you have the "image.jpg" file in the same directory as the code, or modify the image path according to your requirements.*
