import os
import face_recognition
import cv2
import datetime
import playsound
import click
from pathlib import Path


def capture_photo(filename):
    with cv2.VideoCapture(0) as cap:
        if not cap.isOpened():
            raise ValueError("Could not open camera")
        ret, frame = cap.read()
        if not ret:
            raise ValueError("Could not capture photo")
        cv2.imwrite(filename, frame)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("name")
@click.argument("known_dir", type=click.Path(exists=True))
def register(name, known_dir):
    user_dir = Path(f"user/{name}")
    user_dir.mkdir(parents=True, exist_ok=True)
    photo_filename = user_dir / f"{name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    print("Taking photo...")
    capture_photo(str(photo_filename))
    print(f"New face registered: {name}")


@cli.command()
@click.argument("known_dir", type=click.Path(exists=True))
def recognize(known_dir):
    known_faces = {}
    for filename in Path(known_dir).glob("*.jpg"):
        name = filename.stem
        image = face_recognition.load_image_file(str(filename))
        encoding = face_recognition.face_encodings(image)[0]
        known_faces[name] = encoding

    photo_filename = "temp.jpg"
    capture_photo(photo_filename)

    image = face_recognition.load_image_file(photo_filename)
    user_encoding = face_recognition.face_encodings(image)[0]

    matches = face_recognition.compare_faces(list(known_faces.values()), user_encoding)

    matched_index = None
    for i, match in enumerate(matches):
        if match:
            matched_index = i
            break

    if matched_index is not None:
        name = list(known_faces.keys())[matched_index]
        playsound.playsound(f"greetings/{name}.mp3")
    else:
        print("No match found")


if __name__ == "__main__":
    cli()
