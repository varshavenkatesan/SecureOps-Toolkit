#!/usr/bin/env python3
"""
File Integrity Checker
======================
Monitors file integrity by calculating and comparing SHA-256 hash values.
Detects modifications, additions, and deletions of files in a directory.

Author: Varsha Venkatesan
Purpose: Educational - File Integrity Monitoring
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path


class FileIntegrityChecker:
    """
    A file integrity monitoring system that tracks changes to files
    in a specified directory using SHA-256 hashing.
    """
    
    def __init__(self, baseline_file="baseline.json"):
        """
        Initialize the File Integrity Checker.
        
        Args:
            baseline_file (str): Path to the JSON file storing baseline hashes
        """
        self.baseline_file = baseline_file
        self.baseline_path = Path(__file__).parent / baseline_file
        
    def calculate_hash(self, file_path):
        """
        Calculate SHA-256 hash of a file.
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            str: SHA-256 hash in hexadecimal format, or None if error
        """
        try:
            sha256_hash = hashlib.sha256()
            
            # Read file in chunks to handle large files efficiently
            with open(file_path, "rb") as f:
                # Read file in 4KB chunks
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
                    
            return sha256_hash.hexdigest()
        except (IOError, OSError) as e:
            print(f"[ERROR] Cannot read file {file_path}: {e}")
            return None
    
    def scan_directory(self, directory_path):
        """
        Scan a directory and calculate hashes for all files.
        
        Args:
            directory_path (str): Path to the directory to scan
            
        Returns:
            dict: Dictionary mapping file paths to their SHA-256 hashes
        """
        file_hashes = {}
        
        # Validate directory path
        if not os.path.exists(directory_path):
            print(f"[ERROR] Directory not found: {directory_path}")
            return file_hashes
            
        if not os.path.isdir(directory_path):
            print(f"[ERROR] Path is not a directory: {directory_path}")
            return file_hashes
        
        print(f"\n[*] Scanning directory: {directory_path}")
        
        # Walk through directory recursively
        for root, dirs, files in os.walk(directory_path):
            # Skip hidden directories and common excludes
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            
            for filename in files:
                # Skip hidden files
                if filename.startswith('.'):
                    continue
                    
                file_path = os.path.join(root, filename)
                
                # Calculate hash
                file_hash = self.calculate_hash(file_path)
                if file_hash:
                    # Store relative path for portability
                    relative_path = os.path.relpath(file_path, directory_path)
                    file_hashes[relative_path] = file_hash
                    
        print(f"[+] Scanned {len(file_hashes)} files")
        return file_hashes
    
    def create_baseline(self, directory_path):
        """
        Create a baseline of file hashes for the specified directory.
        
        Args:
            directory_path (str): Path to the directory to monitor
        """
        print("\n" + "="*60)
        print("CREATING BASELINE")
        print("="*60)
        
        # Scan directory and get file hashes
        file_hashes = self.scan_directory(directory_path)
        
        if not file_hashes:
            print("[!] No files found or unable to scan directory")
            return
        
        # Prepare baseline data
        baseline_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "directory": os.path.abspath(directory_path),
            "file_count": len(file_hashes),
            "hashes": file_hashes
        }
        
        # Save baseline to JSON file
        try:
            with open(self.baseline_path, 'w') as f:
                json.dump(baseline_data, f, indent=4)
            print(f"\n[+] Baseline created successfully!")
            print(f"[+] Baseline file: {self.baseline_path}")
            print(f"[+] Total files monitored: {len(file_hashes)}")
        except IOError as e:
            print(f"[ERROR] Failed to save baseline: {e}")
    
    def load_baseline(self):
        """
        Load the baseline from JSON file.
        
        Returns:
            dict: Baseline data, or None if not found
        """
        if not self.baseline_path.exists():
            print(f"[!] Baseline file not found: {self.baseline_path}")
            print("[!] Please create a baseline first using option 1")
            return None
            
        try:
            with open(self.baseline_path, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"[ERROR] Failed to load baseline: {e}")
            return None
    
    def check_integrity(self, directory_path):
        """
        Compare current directory state against baseline.
        Detect modified, new, and deleted files.
        
        Args:
            directory_path (str): Path to the directory to check
        """
        print("\n" + "="*60)
        print("FILE INTEGRITY CHECK")
        print("="*60)
        
        # Load baseline
        baseline = self.load_baseline()
        if not baseline:
            return
        
        print(f"[*] Baseline created: {baseline['timestamp']}")
        print(f"[*] Original directory: {baseline['directory']}")
        
        # Get current file hashes
        current_hashes = self.scan_directory(directory_path)
        
        if not current_hashes:
            print("[!] Unable to scan directory")
            return
        
        # Extract baseline hashes
        baseline_hashes = baseline['hashes']
        
        # Detect changes
        modified_files = []
        new_files = []
        deleted_files = []
        
        # Check for modified and existing files
        for file_path, current_hash in current_hashes.items():
            if file_path in baseline_hashes:
                if current_hash != baseline_hashes[file_path]:
                    modified_files.append(file_path)
            else:
                new_files.append(file_path)
        
        # Check for deleted files
        for file_path in baseline_hashes:
            if file_path not in current_hashes:
                deleted_files.append(file_path)
        
        # Display results
        print("\n" + "-"*60)
        print("INTEGRITY CHECK RESULTS")
        print("-"*60)
        
        if not modified_files and not new_files and not deleted_files:
            print("\n[✓] NO CHANGES DETECTED - All files match baseline")
        else:
            print(f"\n[!] CHANGES DETECTED")
            
            if modified_files:
                print(f"\n[!] MODIFIED FILES ({len(modified_files)}):")
                for file_path in modified_files:
                    print(f"    [-] {file_path}")
                    print(f"        Old hash: {baseline_hashes[file_path][:16]}...")
                    print(f"        New hash: {current_hashes[file_path][:16]}...")
            
            if new_files:
                print(f"\n[+] NEW FILES ({len(new_files)}):")
                for file_path in new_files:
                    print(f"    [+] {file_path}")
            
            if deleted_files:
                print(f"\n[-] DELETED FILES ({len(deleted_files)}):")
                for file_path in deleted_files:
                    print(f"    [-] {file_path}")
        
        # Summary
        print("\n" + "-"*60)
        print("SUMMARY")
        print("-"*60)
        print(f"Baseline files: {len(baseline_hashes)}")
        print(f"Current files:  {len(current_hashes)}")
        print(f"Modified:       {len(modified_files)}")
        print(f"New:            {len(new_files)}")
        print(f"Deleted:        {len(deleted_files)}")
        print("-"*60)


def main():
    """
    Main function to run the File Integrity Checker interactively.
    """
    checker = FileIntegrityChecker()
    
    print("\n" + "="*60)
    print("FILE INTEGRITY MONITORING SYSTEM")
    print("="*60)
    print("\nThis tool monitors file integrity using SHA-256 hashing.")
    print("It can detect modifications, additions, and deletions.\n")
    
    while True:
        print("\n--- MENU ---")
        print("1. Create Baseline")
        print("2. Check Integrity")
        print("3. View Baseline Info")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            directory = input("\nEnter directory path to monitor: ").strip()
            if directory:
                checker.create_baseline(directory)
            else:
                print("[!] Invalid directory path")
                
        elif choice == '2':
            directory = input("\nEnter directory path to check: ").strip()
            if directory:
                checker.check_integrity(directory)
            else:
                print("[!] Invalid directory path")
                
        elif choice == '3':
            baseline = checker.load_baseline()
            if baseline:
                print("\n" + "-"*60)
                print("BASELINE INFORMATION")
                print("-"*60)
                print(f"Created:        {baseline['timestamp']}")
                print(f"Directory:      {baseline['directory']}")
                print(f"Files monitored: {baseline['file_count']}")
                print("-"*60)
                
        elif choice == '4':
            print("\n[*] Exiting File Integrity Checker...")
            break
            
        else:
            print("[!] Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
