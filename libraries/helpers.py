def get_input(path_to_file):
    fs_content = []
    with open(path_to_file) as file:
        for line in file:
            if not line:
                continue
            fs_content.append(line.rstrip("\n"))

    print(f"Lines ingested: {len(fs_content)}") # Validate input file was read properly
    return fs_content
