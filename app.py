from drive.service import get_drive_service


def main():

    service = get_drive_service()

    results = (
        service.files()
        .list(
            pageSize=20,
            fields="files(id,name,mimeType)"
        )
        .execute()
    )

    files = results.get("files", [])

    if not files:
        print("No files found.")
        return

    print("\nGoogle Drive Files\n")

    for file in files:
        print(file["name"], "-", file["mimeType"])


if __name__ == "__main__":
    main()