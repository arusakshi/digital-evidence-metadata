#!/usr/bin/env python3
"""
Digital Evidence Metadata Extractor

Collects filesystem metadata and SHA-256 hashes for a file without
modifying the original evidence.

Use only on evidence or files you are authorized to examine.
"""

import argparse
import hashlib
import json
import mimetypes
import os
import platform
from datetime import datetime, timezone
from pathlib import Path


def calculate_sha256(file_path, chunk_size=8192):
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(chunk_size):
            sha256.update(chunk)

    return sha256.hexdigest()


def collect_metadata(file_path):
    path = file_path.resolve()
    stat = path.stat()

    return {
        "file_name": path.name,
        "absolute_path": str(path),
        "file_size_bytes": stat.st_size,
        "file_extension": path.suffix.lower() or "None",
        "mime_type": mimetypes.guess_type(path.name)[0] or "unknown",
        "created_time": datetime.fromtimestamp(
            stat.st_ctime, tz=timezone.utc
        ).isoformat(),
        "modified_time": datetime.fromtimestamp(
            stat.st_mtime, tz=timezone.utc
        ).isoformat(),
        "accessed_time": datetime.fromtimestamp(
            stat.st_atime, tz=timezone.utc
        ).isoformat(),
        "sha256": calculate_sha256(path),
        "operating_system": platform.system(),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract forensic metadata and SHA-256 hash from a file."
    )
    parser.add_argument("file", help="Path to the evidence file")
    parser.add_argument(
        "-o",
        "--output",
        help="Optional JSON output path",
    )
    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.is_file():
        raise SystemExit(f"File not found: {file_path}")

    metadata = collect_metadata(file_path)

    print("\nDigital Evidence Metadata")
    print("=" * 30)

    for key, value in metadata.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    if args.output:
        output_path = Path(args.output)
        with output_path.open("w", encoding="utf-8") as output_file:
            json.dump(metadata, output_file, indent=4)
        print(f"\nMetadata saved to: {output_path}")


if __name__ == "__main__":
    main()
