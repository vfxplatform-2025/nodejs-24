# -*- coding: utf-8 -*-
name        = "nodejs"
version     = "24.21.0"
authors     = ["M83"]
description = "Node.js 24 LTS, compatible with Chromium/QtWebEngine builds"

build_requires = [
    "python-3.13.2",    # VFX 플랫폼 통일 파이썬 (configure용)
    # Node 24는 GCC >= 12.2 필요 → rezbuild.py에서 /opt/rh/gcc-toolset-13 사용
]

requires = [
    # 필요 시 OpenSSL, zlib, ICU 등 명시 가능
]

build_command = "python {root}/rezbuild.py install"

def commands():
    env.NodeJS_ROOT = "{root}"
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
