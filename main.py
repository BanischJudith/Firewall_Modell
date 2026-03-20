"""docstring"""

def eingabe():
    ip = input("Gib eine IP-Adrsse ein: ")
    print("Die Firewall hat " + ip + " abgelehnt")

def main():
    erlaubte_ips = {
        "111.111.1.1": "erlaubt"
    }

    if "111.111.1.1" in erlaubte_ips:
        print(erlaubte_ips.get('111.111.1.1'))
    else:
        print("verweigert")
        
eingabe()
main()