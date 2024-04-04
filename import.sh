#!/bin/bash
currentpath="$1"
endpath="$2"
usenetmount="/mnt/remote/usenet"
getcutpathradarr () { while read data; do echo "$data" | rev | cut -d'/' -f 1-3 | rev; done; }
getcutpathsonarr () { while read data; do echo "$data" | rev | cut -d'/' -f 1-4 | rev; done; }

if [[ $currentpath = *'symlinks'* ]]; then
    mv "$currentpath" "$endpath"
    echo "moved $currentpath to $endpath" >> /scripts/arrs/move.log
elif [[ $currentpath = *'complete/radarr'* ]]; then
    rclone copyto "$currentpath" usenet:/"$(echo $endpath | getcutpathradarr)" --log-file /scripts/arrs/rclone.log  --config /config/rclone/rclone.conf
    rm -rf "$currentpath"
    ln -s -d -f "$usenetmount"/"$(echo $endpath | getcutpathradarr)" "$endpath"
    echo "linked $usenetmount/$(echo $endpath | getcutpathradarr) to $endpath" >> /scripts/arrs/rclone.log
elif [[ $currentpath = *'complete/sonarr'* ]]; then
    rclone copyto "$currentpath" usenet:/"$(echo $endpath | getcutpathsonarr)" --log-file /scripts/arrs/rclone.log --config /config/rclone/rclone.conf
    rm -rf "$currentpath"
    ln -s -d -f "$usenetmount"/"$(echo $endpath | getcutpathsonarr)" "$endpath"
    echo "linked $usenetmount/$(echo $endpath | getcutpathsonarr) to $endpath" >> /scripts/arrs/rclone.log
fi
