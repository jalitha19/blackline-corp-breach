from PIL import Image
import piexif

image = Image.open("maya-reed.jpg")

exif = piexif.load(image.info["exif"])

print("=== Stage 1 Metadata ===")

for tag_id, value in exif["0th"].items():
    tag = piexif.TAGS["0th"][tag_id]["name"]

    if isinstance(value, bytes):
        value = value.decode(errors="ignore")

    print(f"{tag}: {value}")

for tag_id, value in exif["Exif"].items():
    tag = piexif.TAGS["Exif"][tag_id]["name"]

    if isinstance(value, bytes):
        value = value.decode(errors="ignore")

    print(f"{tag}: {value}")