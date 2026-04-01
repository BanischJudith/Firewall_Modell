<<<<<<< HEAD
"""docstring"""
=======
import ipaddress

def str_zu_int(str_ip):
    """Verwandelt Strings in Integers im IPv4-Format."""
    return int(ipaddress.ip_address(str_ip))

def eingabe():
    """Der User gibt die zu testende IP ein. Der eingegebene Input hat die Variable eing_ip."""
    eing_ip = input("Gib eine IP-Adresse ein: ")
    return eing_ip

def main():
    """Dictionary mit Integer-Zahlenumfängen im IPv4-Format. 
       User wird gefragt, eine IP einzugeben (Variable eing_ip).
       Eing_ip wird zu Integer (Variable ip).
       For-Loop: Schaut, ob ip im Umfang im Dictionary ist."""
    ip_dict = {
        (str_zu_int("192.168.1.0"), str_zu_int("192.168.1.100")): "placeholder",
        (str_zu_int("192.168.1.200"), str_zu_int("192.168.1.255")): "placeholder"
    }

    eing_ip = eingabe()

    ip = str_zu_int(eing_ip)

    for (start, ende), wert in ip_dict.items():
        if start <= ip <= ende:
            print(f"Die Firewall von {eing_ip} hat die Verbindung zugelassen")
            break
    else:
        print(f"Die Firewall von {eing_ip} hat die Verbindung geblockt")

main()
>>>>>>> test
