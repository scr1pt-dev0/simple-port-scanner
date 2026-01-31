# simple-port-scanner

Ein einfacher TCP‑Portscanner in Python.  
Dieses Projekt ist ein **reines Lernprojekt** und dient ausschließlich dazu,
die Grundlagen von Netzwerken besser zu verstehen und einen simplen Nmap‑ähnlichen Scanner nachzubauen.

Der Fokus liegt darauf, wie ein TCP‑Connect‑Scan funktioniert, wie man Sockets verwendet,
Timeouts setzt und Fehler sauber behandelt. Das Projekt ist bewusst minimal gehalten, um die technischen Grundlagen klar sichtbar zu machen.

---

## 🚀 Features

- TCP‑Connect‑Scan (klassische Methode)
- Scan eines festen Portbereichs (3000–3334)
- Fehlerbehandlung für ungültige Hosts
- Einfache CLI‑Nutzung: `python3 scan.py <IP>`
- Zeitstempel für Start und Ende
- Übersichtliche Ausgabe der offenen Ports

---

## 📦 Installation & Nutzung

Python 3 wird benötigt.

```bash
git clone https://github.com/scr1pt-dev0/simple-port-scanner
cd simple-port-scanner
python3 scan.py <IP>
