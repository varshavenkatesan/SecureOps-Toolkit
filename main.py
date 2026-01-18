#!/usr/bin/env python3
"""
SecureOps Toolkit - Main Controller
====================================
A comprehensive Python-based security toolkit for educational purposes.

Modules:
1. File Integrity Checker - Monitor file changes using SHA-256 hashing
2. Web Vulnerability Scanner - Detect SQL Injection and XSS vulnerabilities
3. Penetration Testing Toolkit - Port scanning and brute force simulation

Author: Varsha Venkatesan
Purpose: Educational and Security Research Only
"""

import sys
import os
from pathlib import Path


def print_banner():
    """Display the toolkit banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║              SECUREOPS SECURITY TOOLKIT                   ║
    ║                                                           ║
    ║            Python-Based Cybersecurity Tools               ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    
    ⚠️  EDUCATIONAL PURPOSE ONLY ⚠️
    Use responsibly and ethically. Only test systems you own
    or have explicit authorization to test.
    """
    print(banner)


def print_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("SELECT A MODULE")
    print("="*60)
    print("\n1. File Integrity Checker")
    print("   └─ Monitor file changes using SHA-256 hashing")
    print("\n2. Web Vulnerability Scanner")
    print("   └─ Detect SQL Injection and XSS vulnerabilities")
    print("\n3. Penetration Testing Toolkit")
    print("   └─ Port scanning and authentication testing")
    print("\n4. About This Toolkit")
    print("\n5. Exit")
    print("\n" + "="*60)


def run_file_integrity_checker():
    """Launch the File Integrity Checker module."""
    try:
        # Import the module
        sys.path.insert(0, str(Path(__file__).parent / "file_integrity_checker"))
        from integrity_checker import main as fic_main
        
        print("\n[*] Launching File Integrity Checker...")
        fic_main()
        
    except ImportError as e:
        print(f"\n[ERROR] Failed to load File Integrity Checker: {e}")
        print("[!] Ensure the module is properly installed.")
    except KeyboardInterrupt:
        print("\n\n[*] Returning to main menu...")


def run_web_vulnerability_scanner():
    """Launch the Web Vulnerability Scanner module."""
    try:
        # Import the module
        sys.path.insert(0, str(Path(__file__).parent / "web_vulnerability_scanner"))
        from scanner import main as scanner_main
        
        print("\n[*] Launching Web Vulnerability Scanner...")
        scanner_main()
        
    except ImportError as e:
        print(f"\n[ERROR] Failed to load Web Vulnerability Scanner: {e}")
        print("[!] Ensure the module is properly installed.")
        print("[!] Install dependencies: pip install -r requirements.txt")
    except KeyboardInterrupt:
        print("\n\n[*] Returning to main menu...")


def run_pentesting_toolkit():
    """Launch the Penetration Testing Toolkit module."""
    try:
        # Import the module
        sys.path.insert(0, str(Path(__file__).parent / "pentesting_toolkit"))
        from port_scanner import main as port_scanner_main
        from brute_forcer import main as brute_forcer_main
        
        print("\n[*] Launching Penetration Testing Toolkit...")
        print("\n--- Penetration Testing Menu ---")
        print("1. Port Scanner")
        print("2. Brute Force Simulator")
        print("3. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            port_scanner_main()
        elif choice == '2':
            brute_forcer_main()
        elif choice == '3':
            return
        else:
            print("[!] Invalid choice")
            
    except ImportError as e:
        print(f"\n[ERROR] Failed to load Penetration Testing Toolkit: {e}")
        print("[!] Ensure the module is properly installed.")
    except KeyboardInterrupt:
        print("\n\n[*] Returning to main menu...")


def show_about():
    """Display information about the toolkit."""
    about_text = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                  ABOUT SECUREOPS TOOLKIT                  ║
    ╚═══════════════════════════════════════════════════════════╝
    
    Version: 1.0.0
    Purpose: Educational Cybersecurity Toolkit
    
    MODULES:
    --------
    
    1. File Integrity Checker
       - SHA-256 hashing for file verification
       - Baseline creation and comparison
       - Detects modifications, additions, deletions
       
    2. Web Vulnerability Scanner
       - SQL Injection detection
       - Cross-Site Scripting (XSS) detection
       - Payload-based testing
       
    3. Penetration Testing Toolkit
       - Port scanning (TCP)
       - Brute force simulation
       - Educational demonstrations
    
    ETHICAL USAGE:
    --------------
    ✓ Personal learning and education
    ✓ Authorized security testing
    ✓ Research in controlled environments
    
    ✗ Unauthorized access attempts
    ✗ Malicious activities
    ✗ Violating laws or regulations
    
    DISCLAIMER:
    -----------
    This toolkit is provided for EDUCATIONAL PURPOSES ONLY.
    The authors are not responsible for misuse or damage caused
    by this software. Always obtain proper authorization before
    testing any system you do not own.
    
    LEGAL NOTICE:
    -------------
    Unauthorized access to computer systems is illegal under
    laws such as the Computer Fraud and Abuse Act (CFAA) and
    similar legislation worldwide. Use responsibly.
    
    For more information, see README.md
    """
    print(about_text)
    input("\nPress Enter to continue...")


def main():
    """Main controller function."""
    try:
        # Display banner
        print_banner()
        
        # Main loop
        while True:
            try:
                # Display menu
                print_menu()
                
                # Get user choice
                choice = input("\nEnter your choice (1-5): ").strip()
                
                # Route to appropriate module
                if choice == '1':
                    run_file_integrity_checker()
                    
                elif choice == '2':
                    run_web_vulnerability_scanner()
                    
                elif choice == '3':
                    run_pentesting_toolkit()
                    
                elif choice == '4':
                    show_about()
                    
                elif choice == '5':
                    print("\n[*] Thank you for using SecureOps Toolkit!")
                    print("[*] Remember: Use your knowledge ethically.\n")
                    sys.exit(0)
                    
                else:
                    print("\n[!] Invalid choice. Please select 1-5.")
                    
            except KeyboardInterrupt:
                print("\n\n[*] Interrupted. Returning to menu...")
                continue
                
    except KeyboardInterrupt:
        print("\n\n[*] Exiting SecureOps Toolkit. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
