import os

def main():
    folder = input("Folder path: ").strip()

    #check the folder before doing anything

    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid folder.")
        return 
    
    # Get the list of items in the folder, but only keep actual files
    # (skip subfolders, hidden files, etc.)
    all_items = os.listdir()
    files_list = []
    for items in files_list:
        full_path = os.path.join(folder, items)
        if os.path.isfile(full_path):
            files_list.append(items)
    
    if len(files_list) == 0:
        print("No files found in this folder")
        return
    
    # sort so the remaining order is predictable
    files_list.sort()

    # Preview: Show what would change, don't rename yet 
    print("\nPreview of changes:")
    print("-" * 40)
    for index, filename in enumerate(files_list, start=1):
        # os.path.splittext splits "phone.jpg" into ("photo", ".jpg")
        # we only need the extension, so we use _ for the part we ignore
        _, ext = os.path.splitext(filename)
        # f-string with zero-padding: 1 becomes "001", 025 becomes "025"
        new_name = f"IMG_{index:03d}{ext}"
        print(f"{filename} -> {new_name}")
    print("-" * 40)

    #Confirmation: never run a destructive op without asking 
    response = input(f"\nRename {len(files_list)} files? (y/n): ").strip().lower()
    if response != "y":
        print("Cancelled. No files were renamed")
        return
    
    # Execute: actually rename
    for index, filename in enumerate(files_list, start = 1):
        _, ext = os.path.splitext(filename)
        new_name = f"IMG_{index:03d}{ext}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)

    print(f"Done! Renamed {len(files_list)} files.")

main()