async function meldung() {
    const ip = document.getElementById("ip").value.trim();
    const port = document.getElementById("port").value.trim();
    const divErfolg = document.getElementById("erfolg");
    const divFehler = document.getElementById("fehler");
    const serverBox = document.querySelector(".server");

    divErfolg.style.display = "none";
    divFehler.style.display = "none";

    if (!ip || !port) {
        divFehler.innerHTML = `<span>Fehler!<br>Bitte gebe IP-Adresse und Port ein.</span>`;
        divFehler.style.display = "block";
        serverBox.style.backgroundColor = "var(--fehler)";
        return;
    }

    const response = await fetch(`/check?ip=${encodeURIComponent(ip)}&port=${encodeURIComponent(port)}`);
    const data = await response.json();

    if (!response.ok) {
        divFehler.innerHTML = `<span>Fehler!<br>${data.error || data.message}</span>`;
        divFehler.style.display = "block";
        serverBox.style.backgroundColor = "var(--fehler)";
        return;
    }

    if (data.allowed && data.port_open) {
        divErfolg.innerHTML = `<span>Erfolg!<br>${data.message}</span>`;
        divErfolg.style.display = "block";
        serverBox.style.backgroundColor = "var(--erfolg)";
    } else {
        divFehler.innerHTML = `<span>Fehler!<br>${data.message}</span>`;
        divFehler.style.display = "block";
        serverBox.style.backgroundColor = "var(--fehler)";
    }
}
