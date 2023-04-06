import pytesseract
from PIL import Image

# Abra a imagem
imagem = Image.open('C:\Users\guilh\OneDrive\Documentos\SQL/zzzz.jpg')

# Converta a imagem em texto usando pytesseract
texto = pytesseract.image_to_string(imagem, lang='por')

# Imprima o texto
print(texto)
