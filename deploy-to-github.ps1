# SecureOps Toolkit - Git Deployment Script
# Run these commands one by one in PowerShell

Write-Host "================================" -ForegroundColor Cyan
Write-Host "SecureOps Toolkit - Git Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
Write-Host "[*] Checking Git installation..." -ForegroundColor Yellow
if (Get-Command git -ErrorAction SilentlyContinue) {
    Write-Host "[+] Git is installed!" -ForegroundColor Green
    git --version
} else {
    Write-Host "[!] Git is not installed!" -ForegroundColor Red
    Write-Host "[!] Please install Git from: https://git-scm.com/download/win" -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "[*] Current directory:" -ForegroundColor Yellow
Get-Location

Write-Host ""
$confirm = Read-Host "Is this the SecureOps-Toolkit directory? (yes/no)"
if ($confirm -ne "yes") {
    Write-Host "[!] Please navigate to the SecureOps-Toolkit directory first" -ForegroundColor Red
    Write-Host "[!] Use: cd C:\SecureOps-Toolkit" -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Step 1: Initialize Git Repository" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Initialize Git repository
Write-Host "[*] Initializing Git repository..." -ForegroundColor Yellow
git init

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Step 2: Configure Git (First Time Setup)" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Configure Git user
Write-Host "[*] Configuring Git user..." -ForegroundColor Yellow
$gitName = Read-Host "Enter your name (e.g., Varsha Venkatesan)"
$gitEmail = Read-Host "Enter your email (e.g., varsha@example.com)"

git config user.name "$gitName"
git config user.email "$gitEmail"

Write-Host "[+] Git configured!" -ForegroundColor Green
Write-Host "    Name: $gitName" -ForegroundColor White
Write-Host "    Email: $gitEmail" -ForegroundColor White

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Step 3: Add Files to Git" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Add all files
Write-Host "[*] Adding all files to Git..." -ForegroundColor Yellow
git add .

Write-Host "[+] Files added!" -ForegroundColor Green
Write-Host ""
Write-Host "[*] Files to be committed:" -ForegroundColor Yellow
git status --short

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Step 4: Create Initial Commit" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Create initial commit
Write-Host "[*] Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: SecureOps Toolkit v1.0.0

- File Integrity Checker with SHA-256 hashing
- Web Vulnerability Scanner (SQL Injection & XSS detection)
- Penetration Testing Toolkit (Port Scanner & Brute Force Simulator)
- Comprehensive documentation and testing guides
- Educational focus with ethical usage guidelines

Author: Varsha Venkatesan"

Write-Host "[+] Initial commit created!" -ForegroundColor Green

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Step 5: Connect to GitHub" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[!] IMPORTANT: You need to create a GitHub repository first!" -ForegroundColor Red
Write-Host ""
Write-Host "1. Go to: https://github.com/new" -ForegroundColor Yellow
Write-Host "2. Repository name: SecureOps-Toolkit" -ForegroundColor Yellow
Write-Host "3. Description: Educational Python-based security toolkit" -ForegroundColor Yellow
Write-Host "4. Choose Public or Private" -ForegroundColor Yellow
Write-Host "5. DO NOT initialize with README, .gitignore, or license" -ForegroundColor Yellow
Write-Host "6. Click 'Create repository'" -ForegroundColor Yellow
Write-Host ""

$created = Read-Host "Have you created the GitHub repository? (yes/no)"
if ($created -ne "yes") {
    Write-Host ""
    Write-Host "[*] Please create the repository on GitHub first, then run this script again." -ForegroundColor Yellow
    Write-Host "[*] Or continue manually with these commands:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "git remote add origin https://github.com/YOUR_USERNAME/SecureOps-Toolkit.git" -ForegroundColor Cyan
    Write-Host "git branch -M main" -ForegroundColor Cyan
    Write-Host "git push -u origin main" -ForegroundColor Cyan
    exit
}

Write-Host ""
$username = Read-Host "Enter your GitHub username"

# Add remote origin
Write-Host ""
Write-Host "[*] Adding GitHub remote..." -ForegroundColor Yellow
git remote add origin "https://github.com/$username/SecureOps-Toolkit.git"

Write-Host "[+] Remote added!" -ForegroundColor Green

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Step 6: Push to GitHub" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Rename branch to main
Write-Host "[*] Setting main branch..." -ForegroundColor Yellow
git branch -M main

# Push to GitHub
Write-Host ""
Write-Host "[*] Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "[*] You may be prompted for GitHub credentials..." -ForegroundColor Yellow
Write-Host ""

git push -u origin main

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "[+] Your repository is now live at:" -ForegroundColor Green
Write-Host "    https://github.com/$username/SecureOps-Toolkit" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Next steps:" -ForegroundColor Yellow
Write-Host "    1. Visit your repository and verify all files are uploaded" -ForegroundColor White
Write-Host "    2. Add repository description and topics" -ForegroundColor White
Write-Host "    3. Add a LICENSE file (see DEPLOYMENT.md)" -ForegroundColor White
Write-Host "    4. Pin the repository to your profile" -ForegroundColor White
Write-Host "    5. Share your project on LinkedIn/Twitter!" -ForegroundColor White
Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Thank you for using SecureOps Toolkit!" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
