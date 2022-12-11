from PIL import Image
import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/naminov/AppData/Local/Tesseract-OCR/tesseract.exe'

if __name__ == '__main__':
    image = '3.png'

    preprocess = "blur"

    # загрузить образ и преобразовать его в оттенки серого
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # проверьте, следует ли применять пороговое значение для предварительной обработки изображения

    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # если нужно медианное размытие, чтобы удалить шум
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    # сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
    # text = pytesseract.image_to_string(Image.open(filename))
    text = pytesseract.image_to_string(Image.open(filename), config="-c tessedit"
                                               "_char_whitelist=1234567890"
                                               " --psm 10"
                                               " --oem 3"
                                               " ")
    os.remove(filename)
    print(text)
    # показать выходные изображения
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    # input(‘pause…’)
