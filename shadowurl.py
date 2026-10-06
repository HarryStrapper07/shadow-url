import pyshorteners
import sys
import time

R  = '\033[31m'   # red
G  = '\033[32m'   # green
C  = '\033[36m'   # cyan
W  = '\033[0m'    # white
Y  = '\033[33m'   # yellow
P  = '\033[35m'   # purple
B  = '\033[34m'   # blue
BL = '\033[1m'    # bold

banner = r'''
_____________        _________               _____  _______________ 
__  ___/__  /_______ ______  /________      ___  / / /__  __ \__  / 
_____ \__  __ \  __ `/  __  /_  __ \_ | /| / /  / / /__  /_/ /_  /  
____/ /_  / / / /_/ // /_/ / / /_/ /_ |/ |/ // /_/ / _  _, _/_  /___
/____/ /_/ /_/\__,_/ \__,_/  \____/____/|__/ \____/  /_/ |_| /_____/
'''

def print_banner():
    print(f'\n{P}{"▓"*67}{W}')
    print(f'{C}{banner}{W}')
    print(f'{Y}{"          ══════════[ Made by harry_strapper ]══════════"}{W}\n')
    print(f'{P}{"▓"*67}{W}\n')
    print(f'  ║  {C}Description {G}:{W} Use only for ethical purpose  {G}║')

def show_loading():
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    for _ in range(10):
        for frame in frames:
            sys.stdout.write(f"\r  {C}[{Y}~{C}] Processing... {P}{frame}{W}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r\033[K")

print_banner()

print(f'{P}  {"─"*59}{W}')
print(f'{Y}  [ INPUT SECTION ]{W}')
print(f'{P}  {"─"*59}{W}\n')

original_url = input(f"  {G}[?]{W} Enter the original URL {C}(ex: https://google.com){W} : ")

# auto add https:// if missing
if not original_url.startswith("http://") and not original_url.startswith("https://"):
    original_url = "https://" + original_url
    print(f"\n  {Y}[!] Auto added https:// → {W}{original_url}")

custom_domain = input(f"\n  {G}[?]{W} Enter custom domain name {C}(ex: google.com){W} : ")
keyword       = input(f"\n  {G}[?]{W} Enter keyword {C}(ex: login){W}  : ")

print(f'\n{P}  {"─"*59}{W}')
print()
show_loading()

s = pyshorteners.Shortener(timeout=10)

shorteners = [
    s.tinyurl,
    s.dagd,
    s.clckru,
    s.osdb,
]

short_urls = []
for i, shortener in enumerate(shorteners):
    try:
        short_url = shortener.short(original_url)
        short_urls.append(short_url)
    except Exception as e:
        print(f"  {R}[✗] Shortener {i + 1} failed: {W}{str(e)}")
        continue

print(f'\n{P}  {"─"*59}{W}')
print(f'{Y}  [ RESULTS ]{W}')
print(f'{P}  {"─"*59}{W}\n')
print(f"  {R}[•]{W} Original URL  : {C}{original_url}{W}\n")
print(f"  {G}[~]{W} Masked URLs   :\n")

for i, short_url in enumerate(short_urls):
    final_url = f"https://{custom_domain}-{keyword}@{short_url.replace('https://','').replace('http://','')}"
    print(f"  {G}  ╰➤ {Y}Shortener {i+1} : {W}{final_url}")

print(f'\n{P}  {"─"*59}{W}')
print(f'{C}  {"        ✦ Stay in the Shadows — harry_strapper ✦"}{W}')
print(f'{P}  {"─"*59}{W}\n')
