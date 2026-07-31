#!/usr/bin/env python3
"""Strip identifying metadata from a subject photo before it goes in the game.

    tools/scrub-photo.py A-07 ~/Downloads/ziggy.jpg

Writes photos/a-07-1.jpg, fully re-encoded so no metadata survives, and
reports anything identifying that was found on the way in.

This handles metadata only. Text burned into the pixels — a name badge, a
watermark, a screenshot of a profile page with the name in the header — is
not something this can see. Look at the output yourself before shipping it.
"""

import sys
from pathlib import Path

from PIL import Image, ExifTags

# EXIF tags that carry a person, a place, or a device back to an individual.
IDENTIFYING = {
    "Artist", "Copyright", "XPAuthor", "XPComment", "XPKeywords", "XPSubject",
    "XPTitle", "ImageDescription", "UserComment", "CameraOwnerName",
    "BodySerialNumber", "LensSerialNumber", "GPSInfo", "Make", "Model",
    "Software", "DateTime", "DateTimeOriginal", "DateTimeDigitized",
}

MAX_EDGE = 1400  # the frame renders at ~560px wide; this is generous for retina


def found_metadata(img):
    """Yield human-readable descriptions of identifying metadata present."""
    exif = img.getexif()
    if not exif:
        return

    for tag_id, value in exif.items():
        name = ExifTags.TAGS.get(tag_id, f"Tag{tag_id}")
        if name not in IDENTIFYING:
            continue
        if name == "GPSInfo":
            yield "GPS location"
        else:
            text = str(value).strip().strip("\x00")
            if text:
                yield f"{name}: {text[:60]}"


def scrub(code, source, index):
    img = Image.open(source)

    leaks = list(found_metadata(img))

    # Re-encode through a bare pixel buffer. Constructing a new Image from
    # raw data is what guarantees nothing rides along — passing exif=None to
    # save() still preserves other metadata blocks (ICC, IPTC, XMP).
    clean = Image.new(img.mode, img.size)
    clean.putdata(list(img.convert(img.mode).getdata()))
    clean = clean.convert("RGB")

    if max(clean.size) > MAX_EDGE:
        clean.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)

    out_dir = Path(__file__).resolve().parent.parent / "photos"
    out_dir.mkdir(exist_ok=True)
    dest = out_dir / f"{code.lower()}-{index}.jpg"
    clean.save(dest, "JPEG", quality=88, optimize=True)

    return dest, leaks, clean.size


def main():
    if len(sys.argv) < 3:
        sys.exit(f"usage: {sys.argv[0]} <subject-code> <photo> [photo ...]")

    code, sources = sys.argv[1], sys.argv[2:]
    written = []

    for i, source in enumerate(sources, start=1):
        path = Path(source).expanduser()
        if not path.is_file():
            sys.exit(f"not a file: {path}")

        dest, leaks, size = scrub(code, path, i)
        written.append(dest)

        print(f"{path.name} -> {dest.relative_to(dest.parent.parent)}  {size[0]}x{size[1]}")
        if leaks:
            print("  removed:")
            for leak in leaks:
                print(f"    - {leak}")
        else:
            print("  removed: nothing identifying found")

    listing = ", ".join(f"'photos/{d.name}'" for d in written)
    print(f"\nphotos: [{listing}]")
    print("Check the images by eye for visible names before committing.")


if __name__ == "__main__":
    main()
