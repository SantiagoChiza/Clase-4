import re
RegularEx=r"\b\w\{4}\b"
num= r"\d{4}"
palabra=
resultado= re.findall(RegularEx,palabra)
años= re.findall(num, palabra)
print(años)
print(resultado)