char = input("Enter a character :")

def agreed():
    print("Agreed")

def not_agreed():
    print("Not agreed")


char = char.lower()
if char in ["y","yes"]:
    agreed()
if char in ["no", "n"]:
    not_agreed()

for i in range(1):
    print("hello")