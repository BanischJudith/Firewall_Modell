"""docstring"""

def eingabe():
    ip = input("Gib eine IP-Adrsse ein: ")
    return ip

def main():
    erlaubte_ips = {
        "111.111.1.1": "erlaubt"
    }

    ip = eingabe()

    if ip in erlaubte_ips:
        print("Die Firewall von " + ip + " hat die Verbindung erlaubt")
    else:
        print("Die Firewall von " + ip + " hat die Verbindung geblockt")

main()
