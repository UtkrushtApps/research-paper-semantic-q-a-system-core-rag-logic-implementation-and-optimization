#!/bin/bash
set -e

echo "[INFO] Checking Docker installation..."
if ! command -v docker &>/dev/null; then
  echo "[ERROR] Docker is not installed."
  exit 1
fi
if ! command -v docker-compose &>/dev/null; then
  echo "[ERROR] docker-compose is not installed."
  exit 1
fi

echo "[INFO] Stopping and removing existing Chroma DB containers (if any)..."
docker-compose down

echo "[INFO] Starting empty Chroma DB service..."
docker-compose up -d chroma-db
sleep 2
echo "[INFO] Chroma DB running at http://localhost:8000"
