from PIL import Image, ImageDraw, ImageFont
import piexif
import os

WIDTH = 1200
HEIGHT = 1200

img = Image.new("RGB", (WIDTH, HEIGHT), "#0f172a")
draw = ImageDraw.Draw(img)

# Background
draw.rectangle((0, 0, WIDTH, HEIGHT), fill="#0f172a")
draw.ellipse((-200, -250, 700, 650), fill="#1d4ed8")
draw.ellipse((650, 650, 1450, 1450), fill="#164e63")

# Corporate card
draw.rounded_rectangle(
    (170, 170, 1030, 1030),
    radius=60,
    fill="#f8fafc"
)

# Avatar
draw.ellipse(
    (380, 280, 820, 720),
    fill="#cbd5e1"
)

# Simple fictional silhouette
draw.ellipse(
    (500, 360, 700, 560),
    fill="#475569"
)

draw.rounded_rectangle(
    (440, 540, 760, 760),
    radius=100,
    fill="#475569"
)

# Text helper
try:
    title_font = ImageFont.truetype("arialbd.ttf", 58)
    body_font = ImageFont.truetype("arial.ttf", 34)
    small_font = ImageFont.truetype("arial.ttf", 25)
except:
    title_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

draw.text(
    (430, 800),
    "Maya Reed",
    fill="#0f172a",
    font=title_font
)

draw.text(
    (410, 875),
    "Infrastructure Analyst",
    fill="#2563eb",
    font=body_font
)

draw.text(
    (420, 930),
    "Blackline Corporation",
    fill="#64748b",
    font=small_font
)

# ---------------------------
# EXIF METADATA
# ---------------------------

zeroth_ifd = {
    piexif.ImageIFD.ImageDescription:
        "Blackline Corp archived employee profile | Case Fragment: RAVEN",

    piexif.ImageIFD.Make:
        "Blackline Corporate Media",

    piexif.ImageIFD.Model:
        "BL-CAM-0427",

    piexif.ImageIFD.Software:
        "Blackline Media Archive",

    piexif.ImageIFD.Artist:
        "Maya Reed"
}

exif_ifd = {
    piexif.ExifIFD.UserComment:
        b"ASCII\x00\x00\x00BLK{exif_leaks_identity}"
}

exif_dict = {
    "0th": zeroth_ifd,
    "Exif": exif_ifd,
    "GPS": {},
    "1st": {},
    "thumbnail": None
}

exif_bytes = piexif.dump(exif_dict)

source_output = "maya-reed.jpg"

img.save(
    source_output,
    "jpeg",
    quality=95,
    exif=exif_bytes
)

print("[+] Stage 1 image created")
print("[+] File:", os.path.abspath(source_output))
print("[+] EXIF flag embedded")
print("[+] Stage 6 fragment embedded")