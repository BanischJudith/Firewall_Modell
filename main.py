import ipaddress
import sqlite3
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder="templates")


def str_zu_int(str_ip):
    return int(ipaddress.ip_address(str_ip))


def check_firewall(eing_ip, eing_port):
    ip_dict = {
        (str_zu_int("1.0.0.0"), str_zu_int("9.255.255.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("11.0.0.0"), str_zu_int("126.255.255.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("129.0.0.0"), str_zu_int("169.253.255.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("169.255.0.0"), str_zu_int("172.15.255.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("172.32.0.5"), str_zu_int("191.0.1.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("192.0.3.0"), str_zu_int("192.88.98.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("192.88.100.0"), str_zu_int("192.167.255.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("192.169.0.0"), str_zu_int("198.17.255.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("198.20.0.0"), str_zu_int("198.168.0.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("198.168.1.0"), str_zu_int("198.168.1.255")): {"80", "443", "53", "67", "68"},
        (str_zu_int("172.16.0.3"), str_zu_int("172.16.0.225")): {"80", "443", "445", "139", "53", "67", "68"},
        (str_zu_int("172.16.0.0"), str_zu_int("172.16.0.3")): {"80", "443", "445", "139", "22", "3389", "53", "67", "68"},
        (str_zu_int("198.168.2.0"), str_zu_int("223.255.255.255")): {"80", "443", "53", "67", "68"},
    }

    ip = str_zu_int(eing_ip)

    for (start, ende), port_dict in ip_dict.items():
        if start <= ip <= ende:
            if eing_port in port_dict:
                return {
                    "allowed": True,
                    "port_open": True,
                    "message": f"Die Firewall hat die Verbindung mit deiner IP-Adresse {eing_ip} zugelassen. Port {eing_port} ist offen.",
                }
            return {
                "allowed": True,
                "port_open": False,
                "message": f"Die Firewall hat die Verbindung mit deiner IP-Adresse {eing_ip} zugelassen. Port {eing_port} ist geschlossen.",
            }

    return {
        "allowed": False,
        "port_open": False,
        "message": f"Die Firewall hat die Verbindung mit deiner IP-Adresse {eing_ip} verhindert.",
    }


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/database")
def index():
    conn = get_db()
    entries = conn.execute("SELECT * FROM entries ORDER BY id DESC").fetchall()
    conn.close()

    html = "<h1>Eintragsliste</h1>"
    html += "<p>Neuen Eintrag hinzufügen: /add?name=Beispiel</p><hr>"

    for entry in entries:
        html += (
            f"<p>#{entry['id']} – {entry['name']} "
            f"<a href='/delete?id={entry['id']}'>[löschen]</a></p>"
        )

    return html

@app.route("/add")
def add():
    name = request.args.get("name")

    if not name:
        return "Bitte einen Wert angeben, z. B. /add?name=Beispiel"

    conn = get_db()
    conn.execute("INSERT INTO entries(name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return "Eintrag hinzugefügt. Zurück zu: /"

@app.route("/delete")
def delete():
    entry_id = request.args.get("id")

    if not entry_id:
        return "Bitte eine id angeben, z. B. /delete?id=1"

    conn = get_db()
    conn.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

    return "Eintrag gelöscht. Zurück zu: /"

@app.route("/check")
def check():
    ip = request.args.get("ip")
    port = request.args.get("port")

    if not ip or not port:
        return jsonify({"error": "Bitte IP-Adresse und Port eingeben."}), 400

    try:
        result = check_firewall(ip, port)
    except ValueError:
        return jsonify({"error": "Ungültige IP-Adresse."}), 400

    return jsonify(result)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
