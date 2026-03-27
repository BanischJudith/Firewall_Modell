"""docstring"""

def eingabe():
    ip = input("Gib eine IP-Adresse ein: ")
    return ip

def main():
    erlaubte_ips = {
        "111.111.1.1": "erlaubt"
    }

    ip = eingabe()

    status = erlaubte_ips.get(ip)

    if status:
        print(f"Die Firewall von {ip} hat die Verbindung erlaubt")
    else:
        print(f"Die Firewall von {ip} hat die Verbindung geblockt")

main()
