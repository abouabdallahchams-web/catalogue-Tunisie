[app]

# (str) Title of your application
title = Mon Catalogue Tunisie

# (str) Package name
package.name = cataloguetunisie

# (str) Package domain (needed for android packaging)
package.domain = org.tunisie

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests,urllib3,certifi,charset-normalizer,idna

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (list) The Android archs to build for.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True
