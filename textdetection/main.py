import easyocr
reader = easyocr.Reader(['en'])
while True:
    img = input('Enter the image path or url: ')
    if len(img) == 0:
        break
    result = reader.readtext(img)
    print(result)