#Jakub0101011;#0320

import speedtest
from time import sleep
from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED...")

# initializing the SpeedTest instance
st = speedtest.Speedtest()

st.get_best_server()  # Get the most optimal server available
for i in tqdm(range(10), colour="green", desc="Finding Optimal Server"):
    sleep(0.05)

st.download()  # Get downloading speed
for i in tqdm(range(10), colour="cyan", desc="Getting Download Speed"):
    sleep(0.20)

st.upload()  # Get uploading Speed
for i in tqdm(range(10), colour="magenta", desc="Getting Upload Speed"):
    sleep(0.20)

# Save all these elements in a dictionary
res_dict = st.results.dict()

# Assign to variables with an specific format
dwnl = round(st.download() / 1000 / 1000, 2)

upl = round(st.upload() / 1000 / 1000, 2)

# def bytes_to_mb(bytes):
#   KB = 1024 # One Kilobyte is 1024 bytes
#   MB = KB * 1024 # One MB is 1024 KB
#   return int(bytes/MB)


share = st.results.share()

# Display results in a nice looking table using colorama features
print("")

# divider - a line in the screen with a fixed width
print(Fore.MAGENTA + "="*80)
print(Fore.GREEN + """
░█▀▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀ ░█▀▀▄ 　 ▀▀█▀▀ ░█▀▀▀ ░█▀▀▀█ ▀▀█▀▀ 　 ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█─░█ ░█─── ▀▀█▀▀ ░█▀▀▀█ ▄ 
─▀▀▀▄▄ ░█▄▄█ ░█▀▀▀ ░█▀▀▀ ░█─░█ 　 ─░█── ░█▀▀▀ ─▀▀▀▄▄ ─░█── 　 ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ ░█─░█ ░█─── ─░█── ─▀▀▀▄▄ ─ 
░█▄▄▄█ ░█─── ░█▄▄▄ ░█▄▄▄ ░█▄▄▀ 　 ─░█── ░█▄▄▄ ░█▄▄▄█ ─░█── 　 ░█─░█ ░█▄▄▄ ░█▄▄▄█ ─▀▄▄▀ ░█▄▄█ ─░█── ░█▄▄▄█ ▀\n""".center(80))

print(Fore.MAGENTA + "="*80)
print(Fore.YELLOW +
      f"Download: {dwnl}mbps({float(dwnl)*0.125:.2f}MBs) | Upload: {upl}mbps ({float(upl)*0.125:.2f}MBs) | Ping: {res_dict['ping']:.2f}ms".center(80)) 
print(Fore.MAGENTA + "-"*80)
print(Fore.CYAN +
      f"HOST: {res_dict['server']['host']} | SPONSOR: {res_dict['server']['sponsor']} | LATENCY: {res_dict['server']['latency']:.2f}".center(80))
print(Fore.MAGENTA + "-"*80)
print(Fore.GREEN + 
      f"IP: {res_dict['client']['ip']} | Share: {share}".center(80))
print(Fore.MAGENTA + "-"*80)
print(Fore.RED + 
      "SPEEDTEST BY OOKLA / Speedtest.net in Python".center(80))
print(Fore.MAGENTA + "-"*80)
# print(res_dict)