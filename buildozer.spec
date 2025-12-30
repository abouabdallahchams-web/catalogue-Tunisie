[app]
# (str) Titre de ton application
title = Mon Catalogue Tunisie

# (str) Nom du paquet (sans espaces, sans majuscules)
package.name = cataloguetunisie

# (str) Domaine
package.domain = org.tunisie

# (str) Source code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# (list) Application requirements
requirements = python3,kivy,requests,urllib3,certifi,charset-normalizer,idna

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
"Mise à jour permissions"
