from googleapiclient.discovery import build

from drive.auth import authenticate


def get_drive_service():
    credentials = authenticate()

    service = build(
        "drive",
        "v3",
        credentials=credentials,
    )

    return service