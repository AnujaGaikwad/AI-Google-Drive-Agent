from drive.service import get_drive_service
from drive.search import search_files


def main():
    service = get_drive_service()

    results = (
        service.files()
        .list(
            pageSize=100,
            fields="files(id,name,mimeType,createdTime,modifiedTime)",
        )
        .execute()
    )

    files = results.get("files", [])

    keyword = input("Search file: ").strip()

    matched_files = search_files(files, keyword)

    if not matched_files:
        print("\nNo matching files found.")
        return

    print(f"\nFound {len(matched_files)} file(s)\n")

    for file in matched_files:
        print("=" * 70)
        print(f"Name      : {file['name']}")
        print(f"Type      : {file['mimeType']}")
        print(f"Created   : {file['createdTime']}")
        print(f"Modified  : {file['modifiedTime']}")

if __name__ == "__main__":
    main()

print("App started")