# 🔎 Digital Evidence Metadata Extractor

A Python-based digital forensics utility that collects basic filesystem metadata and a **SHA-256 cryptographic hash** from a file.

The tool is designed for forensic learning and authorized evidence-analysis workflows. It reads the target file and does not modify its contents.

## Features

- Extracts file name and extension
- Reports file size
- Identifies the MIME type when available
- Collects filesystem timestamps
- Generates a SHA-256 hash
- Records the operating system used for examination
- Displays results in the terminal
- Optionally exports metadata to JSON

## Requirements

- Python 3.8+
- No external packages required

## Usage

Analyze a file:

```bash
python metadata_extractor.py sample_evidence.txt
```

Save the results as JSON:

```bash
python metadata_extractor.py sample_evidence.txt --output evidence_metadata.json
```

## Example Output

```text
Digital Evidence Metadata
==============================
File Name: Sample_Evidence.txt
File Size Bytes: 128
File Extension: .txt
Mime Type: text/plain
Created Time: 2026-09-29T...
Modified Time: 2026-09-29T...
Accessed Time: 2026-09-29T...
Sha256: ...
Operating System: Windows
```

## Forensic Concepts

- Digital evidence identification
- File metadata
- Cryptographic hashing
- SHA-256 integrity verification
- Evidence documentation
- Forensic examination

## Why SHA-256?

A cryptographic hash creates a fixed-length representation of the file's contents. Investigators can calculate the hash again later and compare the values to help determine whether the file contents have changed.

## Project Structure

```text
digital-evidence-metadata/
├── metadata_extractor.py
├── README.md
├── .gitignore
└── sample_evidence.txt
```

## Important Forensic Note

This tool is intended for educational and authorized forensic analysis. For real investigations, preserve the original evidence, maintain chain-of-custody documentation, use validated forensic acquisition procedures, and work from appropriate forensic copies rather than altering original evidence.

> The metadata collected by this lightweight tool should not be treated as a complete forensic examination.

## Author

**Sakshi Aru**  
MCA — Cybersecurity & Digital Forensics
