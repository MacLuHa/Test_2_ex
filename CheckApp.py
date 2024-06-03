import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#Далее функция просто преобразует найденные Tesseract координаты в нормальный вид
def find_coordinates(text):
    #Массив цифр от 0 до 10
    num = [str(i) for i in range(10)]
    #разделяем поэлементно строку
    for number in text.split():
        #Находим нужной длины элемент
        if len(number) > 15 and len(number) <= 20:
            print(number)
            #Преобразуем в список
            lst = list(number)
            if lst[0] in ['3','4','(']:
                for x in lst:
                    #Удаляем все символы, не являющиеся цифрами
                    if x not in num:
                        lst.remove(x)
                # В зависимости от длины координаты подставляем точки и запятую на нужные места
                if len(lst) < 17:
                    lst.insert(2,'.')
                    lst.insert(9,',')
                    lst.insert(12,'.')
                else:
                    lst.insert(2,  '.')
                    lst.insert(10, ',')
                    lst.insert(13, '.')
    #Преобразуем список в строку
    coordinates = ''.join(lst)
    print(coordinates)
    return coordinates
def search(img_path):
    # Подключение фото
    img = cv2.imread(img_path)
    #Преобразуем в серый
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Result', img)
    # cv2.waitKey(0)
    # Будет выведен только текст с цифрами
    text = pytesseract.image_to_string(img, config='outputbase digits')
    return text


