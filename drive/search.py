def search_files(files, keyword):
    keyword = keyword.lower()

    return [
        file
        for file in files
        if keyword in file["name"].lower()
    ]