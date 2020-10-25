import easyocr
reader = easyocr.Reader(['en']) #specify the languages to read in the list
while True:
    img = input('Enter the image path or url: ')
    if len(img) == 0:
        break
    result = reader.readtext(img)
    print(result)
