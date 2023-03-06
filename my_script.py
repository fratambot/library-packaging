from my_package import my_module as mod

print("Hello fellow mathematician ! Please insert your favourite number:")
x = input()
numeric = int(x) if x.isdigit() else float(x) 
print(f"If we add 1 to your number, we get: {mod.add_one(numeric)}")
print("Mind blowing, I know....")