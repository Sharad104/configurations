import os
import urllib.request
import zipfile
import shutil

# Define variables
ZIP_URL = "https://github.com/Sharad104/mpv-config/archive/refs/heads/main.zip"
TEMP_DIR = os.path.join(os.environ["TEMP"], "mpv-config")
ZIP_FILE = os.path.join(TEMP_DIR, "mpv-config.zip")
MPV_CONFIG_DIR = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "mpv")

# Create a temporary directory for download
if os.path.exists(TEMP_DIR):
    shutil.rmtree(TEMP_DIR)
os.makedirs(TEMP_DIR)

# Download ZIP file
print("Downloading mpv-config ZIP file...")
try:
    urllib.request.urlretrieve(ZIP_URL, ZIP_FILE)
    print("Download completed.")
except Exception as e:
    print("Download failed:", e)
    shutil.rmtree(TEMP_DIR)
    exit()

# Extract ZIP file
print("Extracting ZIP file...")
try:
    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall(TEMP_DIR)
    print("Extraction completed.")
except Exception as e:
    print("Extraction failed:", e)
    shutil.rmtree(TEMP_DIR)
    exit()

# Move the extracted files to the MPV config directory
if not os.path.exists(MPV_CONFIG_DIR):
    os.makedirs(MPV_CONFIG_DIR)

# Copy contents to MPV config directory
source_dir = os.path.join(TEMP_DIR, "mpv-config-main", "mpv")
for item in os.listdir(source_dir):
    s = os.path.join(source_dir, item)
    d = os.path.join(MPV_CONFIG_DIR, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)

# Clean up
shutil.rmtree(TEMP_DIR)

print(f"MPV configuration installed successfully in {MPV_CONFIG_DIR}.")
