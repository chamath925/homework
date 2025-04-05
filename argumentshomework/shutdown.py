import time

confirm = int(input("Are you sure you want to shut down? ( yes / no): "))
confirm2 = int(input("Are you sure you want to shut down? Some programs should be closed. (yes = 1 / no = 0): "))

a = 10

if confirm == 1 and confirm2 == 1:
    while a > 0:
        print(f"Shutting down in {a}...")
        time.sleep(1)
        a -= 1
    print(" Shutting down...")
else:
    print("Shutdown cancelled.")
