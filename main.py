import ipaddress

def str_zu_int(str_ip):
    """Verwandelt Strings in Integers im IPv4-Format."""
    return int(ipaddress.ip_address(str_ip))

def eingabe():
    """Der User gibt die zu testende IP ein. Der eingegebene Input hat die Variable eing_ip."""
    eing_ip = input("Gib deine IP-Adresse ein: ")
    return eing_ip

def main():
    """Dictionary mit Integer-Zahlenumfängen im IPv4-Format. 
       User wird gefragt, eine IP einzugeben (Variable eing_ip).
       Eing_ip wird zu Integer (Variable ip).
       For-Loop: Schaut, ob ip im Umfang im Dictionary ist."""
    ip_dict = {
        (str_zu_int("1.0.0.0"), str_zu_int("9.255.255.255")): "placeholder",
        (str_zu_int("11.0.0.0"), str_zu_int("126.255.255.255")): "placeholder",
        (str_zu_int("129.0.0.0"), str_zu_int("169.253.255.255")): "placeholder",
        (str_zu_int("169.255.0.0"), str_zu_int("172.15.255.255")): "placeholder",
        (str_zu_int("172.32.0.0"), str_zu_int("191.0.1.255")): "placeholder",
        (str_zu_int("192.0.3.0"), str_zu_int("192.88.98.255")): "placeholder",
        (str_zu_int("192.88.100.0"), str_zu_int("192.167.255.255")): "placeholder",
        (str_zu_int("192.169.0.0"), str_zu_int("198.17.255.255")): "placeholder",
        (str_zu_int("198.20.0.0"), str_zu_int("223.255.255.255")): "placeholder"        
    }

    eing_ip = eingabe()

    ip = str_zu_int(eing_ip)

    for (start, ende), wert in ip_dict.items():
        if start <= ip <= ende:
            print(f"Die Firewall hat die Verbindung mit deiner IP-Adresse {eing_ip} zugelassen.")
            break
    else:
        print(f"Die Firewall hat die Verbindung mit deiner IP-Adresse {eing_ip} verhindert.")

main()
