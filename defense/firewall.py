import os

def block_ip(ip):
    print(f"[DEFENSE] Blocking {ip}")
    cmd = f'netsh advfirewall firewall add rule name="Block_{ip}" dir=in action=block remoteip={ip}'
    os.system(cmd)