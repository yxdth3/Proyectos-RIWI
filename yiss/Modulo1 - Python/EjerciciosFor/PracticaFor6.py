
#Explicación For
coders = ["isa","Nando","Juan","Andres","Will"]

for index,coder in enumerate(coders):
    print(f"coder {coder} esta en el index {index}")
    
#2.0
coders = ["isa","Nando","Juan","Andres","Will"]
final = ""
for index,coder in enumerate(coders):
    final += f"{coder} "
    
print(final)