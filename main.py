from ai_engine.rl_agent import get_action
from ai_engine.fake_data_generator import fake_file, fake_creds
from monitoring.analyzer import analyze
from defense.firewall import block_ip
import time

print("[*] Honey Network Started...")

while True:
    action = get_action()

    file = fake_file()
    creds = fake_creds()

    print("[AI] Generated:", file, creds)

    attackers = analyze()

    for ip in attackers:
        block_ip(ip)

    time.sleep(10)