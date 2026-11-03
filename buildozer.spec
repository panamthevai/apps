[app]
title = MyPythonApp
package.name = mypythonapp
package.domain = org.panamthevai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,flask
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
