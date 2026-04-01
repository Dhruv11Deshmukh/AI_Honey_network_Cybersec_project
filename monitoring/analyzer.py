import os

def analyze():
    attackers = []

    if os.path.exists("logs/attacks.log"):
        with open("logs/attacks.log", "r") as f:
            for line in f:
                if "SSH" in line or "admin" in line:
                    ip = line.split("->")[0]
                    attackers.append(ip.strip())

    return list(set(attackers))