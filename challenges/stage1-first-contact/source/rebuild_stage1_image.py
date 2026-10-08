from PIL import Image
import piexif
import os

INPUT = "maya-reed-base.png"
OUTPUT = "maya-reed.jpg"

img = Image.open(INPUT).convert("RGB")

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

img.save(
    OUTPUT,
    "JPEG",
    quality=95,
    exif=exif_bytes
)

print("[+] Realistic Maya Reed profile image created")
print("[+] Stage 1 EXIF flag embedded")
print("[+] Stage 6 fragment RAVEN embedded")
print("[+] Output:", os.path.abspath(OUTPUT))