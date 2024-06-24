import os
import argparse

# Define the function to update symlinks
def update_symlinks(directory, old_path, new_path, dry_run):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.islink(filepath):
                link_target = os.readlink(filepath)
                if link_target.startswith(old_path):
                    updated_target = link_target.replace(old_path, new_path, 1)
                    if not dry_run:
                        os.unlink(filepath)
                        os.symlink(updated_target, filepath)
                        print(f"Updated symlink: {link_target} -> {updated_target}")
                    else:
                        print(f"Would update symlink: {link_target} -> {updated_target}")

# Set up argument parsing
def main():
    parser = argparse.ArgumentParser(description="Update symlinks in a directory.")
    parser.add_argument("directory", nargs='?', help="The directory to search for symlinks.")
    parser.add_argument("old_path", nargs='?', help="The old mount path to be replaced.")
    parser.add_argument("new_path", nargs='?', help="The new mount path to replace with.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without updating symlinks.")

    args = parser.parse_args()

    # If arguments are not provided, enter interactive mode
    if not args.directory or not args.old_path or not args.new_path:
        print("Entering interactive mode. Please provide the following details:")
        directory = input("Directory to search for symlinks: ").strip()
        old_path = input("Old mount path to be replaced: ").strip()
        new_path = input("New mount path to replace with: ").strip()
        dry_run = input("Dry run? (yes/no): ").strip().lower() == 'yes'
    else:
        directory = args.directory
        old_path = args.old_path
        new_path = args.new_path
        dry_run = args.dry_run

    # Call the function with the collected or provided arguments
    update_symlinks(directory, old_path, new_path, dry_run)

if __name__ == "__main__":
    main()
