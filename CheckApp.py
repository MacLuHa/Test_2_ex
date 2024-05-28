import pytesseract
import cv2
from PIL import Image
# from FindGM_NW import FindGM,FindGM2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def find_coordinates(text):
    num = [str(i) for i in range(10)]
    for number in text.split():
        if len(number) > 15 and len(number) <= 20:
            print(number)
            lst = list(number)
            if lst[0] in ['3','4','(']:
                for x in lst:
                    if x not in num:
                        lst.remove(x)
                if len(lst) < 17:
                    lst.insert(2,'.')
                    lst.insert(9,',')
                    lst.insert(12,'.')
                else:
                    lst.insert(2, '.')
                    lst.insert(10, ',')
                    lst.insert(13, '.')
    coordinates = ''.join(lst)
    print(coordinates)
    return coordinates
def search(img_path):
    # Подключение фото
    img = cv2.imread(img_path) #'D:\\Data\\Test\\maps\\sonya.jpg'
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Result', img)
    # cv2.waitKey(0)
    # Будет выведен весь текст с цифрами
    text = pytesseract.image_to_string(img, config='outputbase digits')
    return text

def ToGray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


