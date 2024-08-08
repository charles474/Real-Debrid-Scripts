Scripts I use to help maintain symlinks with Real-debrid and organise my library.

# Discard
Created by @west.
- Removes torrents from Real-Debrid that do not have a symlink attached to them.

Change `path/to/debrid/mount` to the parent folder where all your links/symlinks point to.

Change `path/to/symlinks` to the parent media (plex) folder where all your symlinks are.

###### Usage
To run without deleting torrents
```bash
python3 discard.py --dry-run
```

To run deleting torrents
```bash
python3 discard.py --no-confirm
```

# Symclean
- rewrites symlinks if some were made using the old volume mapping method (/mount/torrents) to the new volume mapping method (/mnt/remote/realdebrid)
- read the code and make the neccessary changes as per needed for your use case.

###### Usage
To run without updating symlink paths
```bash
python3 symclean.py [--dry-run] [directory] [old_path] [new_path]
```

To run updating symlink paths
```bash
python3 symclean.py [directory] [old_path] [new_path]
```

# Start/Stop/Restart
- does the action for all the containers that access Zurg in case of failed order of start where zurg/rclone starts after the other containers on a reboot.

# Zurgupdate
- Stops all containers accessing zurg, cd into zurg directory, compose zurg down, prunes unused images, prunes unused volume data, docker compose up -d, waits 60seconds and then starts the stopped containers.

# Brokensymlink
- Change the directories to match your ones.
- Run first with `dryrun = True`
- Test to see if the symlinks listed are truly broken
- Change dryrun config to `False`
- Rune the script again

# Import
- This is used to work with usenet-drive, to create a symlink on import from `/mnt/remote/usenet/{Media}` to `/mnt/plex/{Media}`
- this also respects realdebrid symlinks found in `/mnt/symlinks/{Media}` and moves them to `/mnt/plex/{Media}`
