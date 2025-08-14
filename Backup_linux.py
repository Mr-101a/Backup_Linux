#!/usr/bin/env python3
import os
import shutil
from datetime import datetime
import time

def find_usb():
    
    media_path = f"/media/{os.getlogin()}"
    if not os.path.exists(media_path):
        return None
    mounts = [os.path.join(media_path, d) for d in os.listdir(media_path) if os.path.ismount(os.path.join(media_path, d))]
    return mounts[0] if mounts else None

def backup_to_usb(usb_path):
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(usb_path, f".backup_{timestamp}")
    os.makedirs(backup_folder, exist_ok=True)

    home_dir = os.path.expanduser("~")
    folders_to_backup = ["", "Downloads", "Music"]  

    for f in folders_to_backup:
        src = os.path.join(home_dir, f)
        if os.path.exists(src):
            dest = os.path.join(backup_folder, f)
            try:
                shutil.copytree(src, dest)
            except Exception:
                pass  

def main():
    print("Detecting USB flash drive...")
    usb = None
    
    while usb is None:
        usb = find_usb()
        time.sleep(1)
    backup_to_usb(usb)
    print("Backup completed successfully!")

if __name__ == "__main__":
    main()

#written by Mr.101
