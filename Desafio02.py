string = input("Digite uma palavra: ")
count = 0
for char in string:
    if char == 'a' or char == 'A':
        count += 1
print(f"A letra 'a' aparece {count} vez(es).")