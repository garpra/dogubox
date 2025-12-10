import os
import subprocess

scripts_path = "scripts/"
scripts = os.listdir(scripts_path)

print("\nList Scripts:")
for i, script in enumerate(scripts, start=1):
    name = script[:-3].replace("-", " ").title()
    print(f"{i}. {name}")

choice = input("\nSelect script (number): ")

if not choice.isdigit():
    print("Input invalid, please enter a number")
    exit()

choice = int(choice)
if choice < 1 or choice > len(scripts):
    print("Script number not available")
    exit()

os.system("clear")
selected_script = scripts[choice - 1]
print(f"Run: {selected_script}")
subprocess.run(["bash", f"scripts/{selected_script}"])
