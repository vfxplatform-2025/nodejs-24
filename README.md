# nodejs 24.21.0 (Major v24)

VFX Platform 2025 compatible build package for nodejs.

## Package Information

- **Package Name**: nodejs
- **Version**: 24.21.0
- **Major Version**: 24
- **Repository**: vfxplatform-2025/nodejs-24
- **Description**: Node.js 24 LTS, compatible with Chromium/QtWebEngine builds

## Build Instructions

```bash
rez-build -i
```

## Package Structure

```
nodejs/
├── 24.21.0/
│   ├── package.py      # Rez package configuration
│   ├── rezbuild.py     # Build script
│   ├── get_source.sh   # Source download script (if applicable)
│   └── README.md       # This file
```

## Installation

When built with `install` target, installs to: `/core/Linux/APPZ/packages/nodejs/24.21.0`

## Version Strategy

This repository contains **Major Version 24** of nodejs. Different major versions are maintained in separate repositories:

- Major v24: `vfxplatform-2025/nodejs-24`

## VFX Platform 2025

This package is part of the VFX Platform 2025 initiative, ensuring compatibility across the VFX industry standard software stack.

## Notes


- Node.js 24 requires GCC >= 12.2. The rez `gcc-11.5.0` package is too old,
  so `rezbuild.py` builds with `/opt/rh/gcc-toolset-13` (override with `NODE_GCC_TOOLSET`).
