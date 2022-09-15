import os

os.system('ifconfig wlp3s0 down')
print('\nwlp3s0 is down\n')
os.system('macchanger -m 3C:58:C2:E5:41:F1 wlp3s0')
print('\n')
os.system('warp-cli connect')
print('\n')
os.system('nmcli d wifi connect WCS-DMD')
