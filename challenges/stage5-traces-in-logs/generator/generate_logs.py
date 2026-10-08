from pathlib import Path
from datetime import datetime, timedelta
import random
import base64


# =========================================================
# Blackline Corp Breach
# Stage 5 - Traces in the Logs
# Fictional educational CTF log generator
# =========================================================


# ---------------------------------------------------------
# Directory configuration
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
PLAYER_DIR = BASE_DIR / "player"

PLAYER_DIR.mkdir(parents=True, exist_ok=True)

ACCESS_LOG = PLAYER_DIR / "access.log"
AUTH_LOG = PLAYER_DIR / "auth.log"


# ---------------------------------------------------------
# Stage 5 / Stage 6 values
# ---------------------------------------------------------

STAGE5_FLAG = "BLK{logs_reveal_the_path}"

# This is carried forward into Stage 6
STAGE6_FRAGMENT = "ECHO"

ATTACKER_IP = "198.51.100.77"


# ---------------------------------------------------------
# Convert important evidence to Base64
# ---------------------------------------------------------

stage5_flag_b64 = base64.b64encode(
    STAGE5_FLAG.encode("utf-8")
).decode("utf-8")

stage6_fragment_b64 = base64.b64encode(
    f"Case Fragment: {STAGE6_FRAGMENT}".encode("utf-8")
).decode("utf-8")


# ---------------------------------------------------------
# Random seed
#
# This keeps the generated logs reproducible.
# Running this script again produces the same normal traffic.
# ---------------------------------------------------------

random.seed(3132)


# ---------------------------------------------------------
# Normal fictional internal users/IP addresses
# ---------------------------------------------------------

normal_ips = [
    "10.20.0.21",
    "10.20.0.32",
    "10.20.0.44",
    "10.20.0.51",
    "10.20.0.63",
    "10.20.0.75",
]


# ---------------------------------------------------------
# Normal website requests
# ---------------------------------------------------------

pages = [
    "/",
    "/index.php",
    "/login.php",
    "/employee.php",
    "/dashboard.php",
    "/assets/style.css",
    "/assets/logo.png",
    "/assets/app.js",
    "/favicon.ico",
]


# ---------------------------------------------------------
# Example browser user agents
# ---------------------------------------------------------

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
]


# ---------------------------------------------------------
# Start time for generated normal traffic
# ---------------------------------------------------------

start = datetime(
    2026,
    9,
    18,
    21,
    45,
    0
)


# ---------------------------------------------------------
# Generate normal Apache-style access log traffic
# ---------------------------------------------------------

lines = []

for _ in range(90):

    timestamp = start + timedelta(
        seconds=random.randint(0, 3500)
    )

    ip = random.choice(normal_ips)

    page = random.choice(pages)

    agent = random.choice(user_agents)

    status = random.choice([
        200,
        200,
        200,
        200,
        302,
        404,
    ])

    size = random.randint(
        300,
        6000
    )

    line = (
        f'{ip} - - '
        f'[{timestamp.strftime("%d/%b/%Y:%H:%M:%S +0530")}] '
        f'"GET {page} HTTP/1.1" '
        f'{status} '
        f'{size} '
        f'"-" '
        f'"{agent}"'
    )

    lines.append(
        (
            timestamp,
            line
        )
    )


# =========================================================
# ATTACK TIMELINE
# =========================================================


# ---------------------------------------------------------
# 22:13:58
# Attacker first visits the employee login page
# ---------------------------------------------------------

attack_time_1 = datetime(
    2026,
    9,
    18,
    22,
    13,
    58
)

lines.append(
    (
        attack_time_1,

        f'{ATTACKER_IP} - - '
        '[18/Sep/2026:22:13:58 +0530] '
        '"GET /login.php HTTP/1.1" '
        '200 '
        '4210 '
        '"-" '
        '"Mozilla/5.0 (X11; Linux x86_64)"'
    )
)


# ---------------------------------------------------------
# 22:14:37
# Authentication bypass occurs against Stage 4 portal
#
# We deliberately do not include the exact SQL injection
# payload in the player logs.
# ---------------------------------------------------------

attack_time_2 = datetime(
    2026,
    9,
    18,
    22,
    14,
    37
)

lines.append(
    (
        attack_time_2,

        f'{ATTACKER_IP} - - '
        '[18/Sep/2026:22:14:37 +0530] '
        '"POST /login.php HTTP/1.1" '
        '302 '
        '512 '
        '"-" '
        '"Mozilla/5.0 (X11; Linux x86_64)"'
    )
)


# ---------------------------------------------------------
# 22:14:42
# Attacker successfully reaches the admin panel
# ---------------------------------------------------------

attack_time_3 = datetime(
    2026,
    9,
    18,
    22,
    14,
    42
)

lines.append(
    (
        attack_time_3,

        f'{ATTACKER_IP} - - '
        '[18/Sep/2026:22:14:42 +0530] '
        '"GET /admin.php HTTP/1.1" '
        '200 '
        '4872 '
        '"-" '
        '"Mozilla/5.0 (X11; Linux x86_64)"'
    )
)


# ---------------------------------------------------------
# 22:15:11
# Suspicious request containing the Stage 5 flag
#
# Flag is hidden as Base64 inside cmd=
# ---------------------------------------------------------

attack_time_4 = datetime(
    2026,
    9,
    18,
    22,
    15,
    11
)

lines.append(
    (
        attack_time_4,

        f'{ATTACKER_IP} - - '
        '[18/Sep/2026:22:15:11 +0530] '
        f'"GET /admin.php?action=audit&cmd={stage5_flag_b64} HTTP/1.1" '
        '200 '
        '5031 '
        '"-" '
        '"Mozilla/5.0 (X11; Linux x86_64)"'
    )
)


# ---------------------------------------------------------
# 22:16:03
# Attacker leaves another encoded artefact.
#
# This contains the Stage 6 clue.
# ---------------------------------------------------------

attack_time_5 = datetime(
    2026,
    9,
    18,
    22,
    16,
    3
)

lines.append(
    (
        attack_time_5,

        f'{ATTACKER_IP} - - '
        '[18/Sep/2026:22:16:03 +0530] '
        f'"GET /admin.php?action=case_note&ref={stage6_fragment_b64} HTTP/1.1" '
        '200 '
        '2981 '
        '"-" '
        '"Mozilla/5.0 (X11; Linux x86_64)"'
    )
)


# ---------------------------------------------------------
# Extra normal traffic after the incident
# ---------------------------------------------------------

after_attack_times = [
    datetime(2026, 9, 18, 22, 18, 14),
    datetime(2026, 9, 18, 22, 20, 51),
    datetime(2026, 9, 18, 22, 23, 19),
    datetime(2026, 9, 18, 22, 27, 34),
    datetime(2026, 9, 18, 22, 31, 42),
]

for timestamp in after_attack_times:

    ip = random.choice(normal_ips)

    page = random.choice([
        "/",
        "/login.php",
        "/employee.php",
        "/assets/style.css",
    ])

    line = (
        f'{ip} - - '
        f'[{timestamp.strftime("%d/%b/%Y:%H:%M:%S +0530")}] '
        f'"GET {page} HTTP/1.1" '
        f'200 '
        f'{random.randint(300, 5000)} '
        f'"-" '
        f'"{random.choice(user_agents)}"'
    )

    lines.append(
        (
            timestamp,
            line
        )
    )


# ---------------------------------------------------------
# Sort everything chronologically
# ---------------------------------------------------------

lines.sort(
    key=lambda item: item[0]
)


# ---------------------------------------------------------
# Write access.log
# ---------------------------------------------------------

with ACCESS_LOG.open(
    "w",
    encoding="utf-8"
) as file:

    for _, line in lines:

        file.write(
            line + "\n"
        )


# =========================================================
# AUTHENTICATION LOG
# =========================================================


auth_lines = [

    (
        "Sep 18 21:50:04 "
        "blackline-portal auth: "
        "login attempt "
        "user=jcarter "
        "status=SUCCESS "
        "source=10.20.0.21"
    ),

    (
        "Sep 18 21:58:19 "
        "blackline-portal auth: "
        "login attempt "
        "user=asmith "
        "status=FAILED "
        "source=10.20.0.44"
    ),

    (
        "Sep 18 22:02:42 "
        "blackline-portal auth: "
        "login attempt "
        "user=mreed "
        "status=FAILED "
        "source=10.20.0.51"
    ),

    (
        "Sep 18 22:07:11 "
        "blackline-portal auth: "
        "login attempt "
        "user=jcarter "
        "status=SUCCESS "
        "source=10.20.0.21"
    ),

    (
        "Sep 18 22:11:03 "
        "blackline-portal auth: "
        "login attempt "
        "user=helpdesk "
        "status=FAILED "
        "source=10.20.0.32"
    ),

    (
        "Sep 18 22:14:37 "
        "blackline-portal auth: "
        "authentication anomaly "
        "source=198.51.100.77 "
        "result=ADMIN_SESSION_CREATED"
    ),

    (
        "Sep 18 22:14:42 "
        "blackline-portal auth: "
        "privileged page accessed "
        "source=198.51.100.77 "
        "user=unknown"
    ),

    (
        "Sep 18 22:15:11 "
        "blackline-portal auth: "
        "unusual audit request "
        "source=198.51.100.77"
    ),

    (
        "Sep 18 22:16:03 "
        "blackline-portal auth: "
        "case note endpoint accessed "
        "source=198.51.100.77 "
        "user=unknown"
    ),

    (
        "Sep 18 22:28:01 "
        "blackline-portal auth: "
        "login attempt "
        "user=jcarter "
        "status=SUCCESS "
        "source=10.20.0.21"
    ),

    (
        "Sep 18 22:32:45 "
        "blackline-portal auth: "
        "login attempt "
        "user=asmith "
        "status=SUCCESS "
        "source=10.20.0.44"
    ),
]


# ---------------------------------------------------------
# Write auth.log
# ---------------------------------------------------------

with AUTH_LOG.open(
    "w",
    encoding="utf-8"
) as file:

    for line in auth_lines:

        file.write(
            line + "\n"
        )


# =========================================================
# Finished
# =========================================================

print()
print("=" * 60)

print(
    "Blackline Corp Breach - Stage 5"
)

print(
    "Traces in the Logs"
)

print("=" * 60)

print()

print(
    "Stage 5 logs generated successfully."
)

print()

print(
    f"Access log : {ACCESS_LOG}"
)

print(
    f"Auth log   : {AUTH_LOG}"
)

print()

print(
    "Generated fictional CTF evidence only."
)

print("=" * 60)