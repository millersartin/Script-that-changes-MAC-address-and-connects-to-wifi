import os

os.system('ifconfig wlp3s0 down')
print('\nwlp3s0 is down\n')
os.system('macchanger -m xx:xx:xx:xx:xx:xx wlp3s0')
print('\n')
os.system('warp-cli connect')
print('\n')
os.system('nmcli d wifi connect wifi_SSID_here')
