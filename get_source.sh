#!/bin/bash

set -e

VERSION="24.21.0"
SRC_DIR="$(dirname "$0")/source"
TARBALL="node-v${VERSION}.tar.gz"
URL="https://nodejs.org/dist/v${VERSION}/${TARBALL}"

mkdir -p "${SRC_DIR}"
cd "${SRC_DIR}"

if [ -f "${TARBALL}" ]; then
    echo "✅ Already downloaded: ${TARBALL}"
else
    echo "⬇️  Downloading Node.js ${VERSION}..."
    curl -LO "${URL}"
    echo "✅ Download complete"
fi

