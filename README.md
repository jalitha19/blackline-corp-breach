# Blackline Corp Breach

Blackline Corp Breach is an educational Capture The Flag (CTF) project created for **IE3132 – Penetration Testing**.

The box contains six connected challenges:

| Stage | Challenge | Domain |
|---|---|---|
| 1 | First Contact | OSINT / Reconnaissance |
| 2 | The Cipher Memo | Cryptography |
| 3 | Hidden in Plain Sight | Steganography |
| 4 | The Employee Portal | Web Security |
| 5 | Traces in the Logs | Digital Forensics |
| 6 | Full Disclosure | Capstone / Integration |

Flag format:

```text
BLK{...}
```

> This project is for authorized educational use only. Run it only inside the supplied Blackline Corp CTF environment.

---

## Requirements

Install:

- Git
- Docker Desktop / Docker Engine
- Docker Compose
- A web browser

Check:

```powershell
docker --version
docker compose version
git --version
```

---

## Clone the Project

```powershell
git clone <REPOSITORY_URL>
cd blackline-corp-breach
```

If `.env.example` is included:

```powershell
Copy-Item .env.example .env
```

---

## Start the CTF

### 1. Start CTFd

```powershell
docker compose -f ctfd/docker-compose.yml up -d --build
```

Open:

```text
http://localhost
```

### 2. Start Stage 1 Website

```powershell
docker compose -f challenges/stage1-first-contact/docker-compose.yml up -d
```

Open:

```text
http://localhost:8081
```

### 3. Start Stage 4 Employee Portal

```powershell
docker compose -f challenges/stage4-employee-portal/docker-compose.yml up -d --build
```

Open:

```text
http://localhost:8082
```

Check all running containers:

```powershell
docker ps
```

Expected main containers include:

```text
ctfd-nginx-1
ctfd-ctfd-1
ctfd-db-1
ctfd-cache-1
blackline-stage1-website
blackline-employee-portal
blackline-stage4-db
```

---

## Restore CTFd Challenges

If the repository includes:

```text
deployment/ctfd-backup.zip
```

start CTFd first, open the CTFd Admin panel, then use the backup/import option to restore the supplied backup.

After restoring, confirm that all six challenges, flags, hints, files and dependencies are available.

---

## Run for Players on the Same Network

Find the server computer IP:

```powershell
ipconfig
```

Use the current Wi-Fi IPv4 address as `SERVER_IP`.

Players can access:

```text
CTFd:
http://SERVER_IP

Stage 1:
http://SERVER_IP:8081

Stage 4:
http://SERVER_IP:8082
```

The IP may change after reconnecting to Wi-Fi, so check it before each session.

---

## Windows Firewall

If another laptop cannot connect, run PowerShell as Administrator on the server:

```powershell
New-NetFirewallRule -DisplayName "Allow ICMPv4 Ping" -Protocol ICMPv4 -IcmpType 8 -Direction Inbound -Action Allow
New-NetFirewallRule -DisplayName "Blackline CTF HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
New-NetFirewallRule -DisplayName "Blackline Stage1 Website" -Direction Inbound -Protocol TCP -LocalPort 8081 -Action Allow
New-NetFirewallRule -DisplayName "Blackline Stage4" -Direction Inbound -Protocol TCP -LocalPort 8082 -Action Allow
```

These rules normally only need to be added once.

---

## Stop the CTF

```powershell
docker compose -f challenges/stage1-first-contact/docker-compose.yml down
docker compose -f challenges/stage4-employee-portal/docker-compose.yml down
docker compose -f ctfd/docker-compose.yml down
```

---

## Reset

### Stage 1

Stage 1 is static. Restart it with:

```powershell
docker compose -f challenges/stage1-first-contact/docker-compose.yml restart
```

### Stage 4

Restart without deleting the database:

```powershell
docker compose -f challenges/stage4-employee-portal/docker-compose.yml restart
```

Full Stage 4 reset:

```powershell
docker compose -f challenges/stage4-employee-portal/docker-compose.yml down -v
docker compose -f challenges/stage4-employee-portal/docker-compose.yml up -d --build
```

### CTFd

Restart:

```powershell
docker compose -f ctfd/docker-compose.yml restart
```

Full CTFd reset:

```powershell
docker compose -f ctfd/docker-compose.yml down -v
docker compose -f ctfd/docker-compose.yml up -d --build
```

After a full CTFd reset, restore the supplied CTFd backup again.

Stages 2, 3 and 5 use static challenge files, so reset them by restoring/re-downloading the original supplied files.

Stage 6 should be reset using the supplied final archive/regeneration files included with the project.

---

## Quick Verification

After deployment, verify:

```text
http://localhost
http://localhost:8081
http://localhost:8082
```

Then check:

- CTFd opens
- all six challenges are visible
- Stage 1 website loads
- Stage 4 portal loads
- challenge files download correctly
- correct flags are accepted
- incorrect flags are rejected

---

## Troubleshooting

Check containers:

```powershell
docker ps -a
```

Check Stage 1 logs:

```powershell
docker logs blackline-stage1-website
```

Check Stage 4 logs:

```powershell
docker logs blackline-employee-portal
docker logs blackline-stage4-db
```

Test remote ports:

```powershell
Test-NetConnection SERVER_IP -Port 80
Test-NetConnection SERVER_IP -Port 8081
Test-NetConnection SERVER_IP -Port 8082
```

---

## Access Summary

```text
CTFd     : http://SERVER_IP
Stage 1  : http://SERVER_IP:8081
Stage 4  : http://SERVER_IP:8082
```

**Project:** Blackline Corp Breach  
**Module:** IE3132 – Penetration Testing  
**Platform:** CTFd + Docker + Nginx  
**Live Web Challenge:** PHP + MariaDB
