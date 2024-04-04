import os

def find_broken_symlinks(directory, dry_run=False):
    broken_symlinks = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if os.path.islink(path):
                target = os.readlink(path)
                if "/mnt/remote/realdebrid" in target and not os.path.exists(target):
                    broken_symlinks.append(path)
                    if not dry_run:
                        os.unlink(path)
    return broken_symlinks

directory = "/mnt/plex"
dry_run = True  # Set to False to actually remove broken symlinks
broken_symlinks = find_broken_symlinks(directory, dry_run)

if dry_run:
    print("Broken symlinks found (dry run):")
    for symlink in broken_symlinks:
        print(symlink)
else:
    print("Broken symlinks removed.")
