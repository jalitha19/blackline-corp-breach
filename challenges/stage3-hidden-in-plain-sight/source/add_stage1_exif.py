import piexif

IMAGE = "maya-reed-stage3.jpg"

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

piexif.insert(exif_bytes, IMAGE)

print("[+] Stage 1 EXIF metadata restored")
print("[+] Stage 1 flag: BLK{exif_leaks_identity}")
print("[+] Case Fragment: RAVEN")
print("[+] Stage 3 stego payload should remain intact")