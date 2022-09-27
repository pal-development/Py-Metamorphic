import random
import string
print("Welcome to the metamorphic code changer!\n")
file_name = input("Script Name/Location: ")
content = open(file_name, "r")
val = content.read()
content.close()
with open(f"{file_name}", "w") as f:
    change = ""
    for i in range(random.randint(100, 350)):
        change = change + "\n" + f"time.sleep(0)\n'''{''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(350))}'''\ndef {''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(10))}():\n    pass"
    change_new = f"import time\n{change}\n\n{val}"
    f.write(change_new)
print("Successfully morphed the code!")
