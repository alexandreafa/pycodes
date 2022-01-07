import easyocr

reader = easyocr.Reader(['pt'])

results = reader.readtext('exemplo.png', paragraph=False)

for result in results:
    print(f"Posição: {result[0]}\n"
          f"Texto: {result[1]}\n")