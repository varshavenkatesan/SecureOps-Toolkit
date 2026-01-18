# File Integrity Checker

## Overview

The File Integrity Checker is a security monitoring tool that detects unauthorized modifications to files in a specified directory. It uses SHA-256 cryptographic hashing to create a baseline of file integrity and compare it against current states.

## Features

- **Baseline Creation**: Creates a snapshot of all files with their SHA-256 hashes
- **Change Detection**: Identifies modified, new, and deleted files
- **Recursive Scanning**: Monitors entire directory trees
- **Detailed Reporting**: Clear output showing all detected changes
- **JSON Storage**: Portable baseline format for easy backup

## How It Works

1. **Hashing**: Each file is read and its SHA-256 hash is calculated
2. **Baseline Storage**: Hashes are stored in `baseline.json`
3. **Comparison**: On subsequent runs, current hashes are compared against the baseline
4. **Alert**: Any discrepancies are reported with details

## Use Cases

- Detect unauthorized file modifications
- Monitor system configuration files
- Verify software integrity
- Audit file changes in critical directories
- Educational purposes - learn about cryptographic hashing

## Installation

No additional dependencies required. Uses Python standard library.

```bash
# Navigate to the module directory
cd file_integrity_checker

# Run the checker
python integrity_checker.py
```

## Usage

### Interactive Mode

Run the script and follow the menu:

```bash
python integrity_checker.py
```

**Menu Options:**
1. **Create Baseline** - Initial scan to establish baseline
2. **Check Integrity** - Compare current state against baseline
3. **View Baseline Info** - Display baseline metadata
4. **Exit** - Close the program

### Example Workflow

```
Step 1: Create a baseline
========================================
$ python integrity_checker.py
> Enter your choice: 1
> Enter directory path: /path/to/monitor

[+] Scanned 50 files
[+] Baseline created successfully!

Step 2: Modify a file (outside the tool)
========================================
$ echo "malicious content" >> /path/to/monitor/config.txt

Step 3: Check integrity
========================================
$ python integrity_checker.py
> Enter your choice: 2
> Enter directory path: /path/to/monitor

[!] CHANGES DETECTED

[!] MODIFIED FILES (1):
    [-] config.txt
        Old hash: 5f4dcc3b5aa765d6...
        New hash: 9af15b336e6a9619...
```

## Code Structure

### Main Class: `FileIntegrityChecker`

**Methods:**
- `calculate_hash(file_path)` - Calculates SHA-256 hash of a file
- `scan_directory(directory_path)` - Scans all files in directory
- `create_baseline(directory_path)` - Creates initial baseline
- `load_baseline()` - Loads baseline from JSON
- `check_integrity(directory_path)` - Compares current state to baseline

### Baseline Format

```json
{
    "timestamp": "2026-01-18 10:30:00",
    "directory": "/path/to/monitored/directory",
    "file_count": 50,
    "hashes": {
        "file1.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "file2.py": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
    }
}
```

## Security Considerations

### Strengths
- **SHA-256** is cryptographically secure
- Detects any bit-level changes
- Resistant to collision attacks

### Limitations
- **No real-time monitoring** - Manual or scheduled checks required
- **Baseline security** - Protect `baseline.json` from tampering
- **Not a prevention tool** - Only detects changes after they occur

### Best Practices
1. Store baseline on read-only media or separate system
2. Run checks regularly (cron/scheduled tasks)
3. Integrate with alerting systems for production use
4. Monitor the baseline file itself for integrity

## Educational Value

This tool demonstrates:
- Cryptographic hashing (SHA-256)
- File system operations in Python
- Data persistence with JSON
- Security monitoring concepts
- Change detection algorithms

## Future Enhancements

- Real-time file system monitoring (watchdog)
- Email/SMS alerts on change detection
- Digital signature for baseline protection
- Web dashboard for visualization
- Database backend for large-scale monitoring
- Whitelisting for expected changes

## Technical Details

**Algorithm**: SHA-256 (Secure Hash Algorithm 256-bit)  
**Language**: Python 3.x  
**Dependencies**: Standard library only (hashlib, os, json, pathlib)  
**Storage**: JSON format  
**Performance**: Handles large files with chunked reading (4KB blocks)

## Ethical Usage

⚠️ **Important**: This tool is for:
- Monitoring your own systems
- Educational purposes
- Authorized security assessments

**Do NOT use to:**
- Monitor systems without authorization
- Violate privacy or terms of service
- Perform unauthorized audits

## License

Educational use only. Use responsibly and ethically.

---

**Module 1 of SecureOps Toolkit**  
For more modules, see the main project README.
