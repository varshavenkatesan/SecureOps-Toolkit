# 🧪 Testing Guide - SecureOps Toolkit

This guide helps you verify that all modules are working correctly.

---

## 📋 Pre-Test Checklist

Before testing, ensure:
- [ ] Python 3.8+ is installed (`python --version`)
- [ ] Dependencies are installed (`pip install -r requirements.txt`)
- [ ] You're in the SecureOps-Toolkit directory
- [ ] You have proper permissions (run as user, not admin unless needed)

---

## 🔬 Module 1: File Integrity Checker Test

### Test 1: Basic Functionality

```bash
# Step 1: Create a test directory
mkdir test_files
echo "Original content" > test_files/file1.txt
echo "Another file" > test_files/file2.txt

# Step 2: Run the integrity checker
cd file_integrity_checker
python integrity_checker.py

# Step 3: Choose option 1 (Create Baseline)
# Enter path: ../test_files

# Expected result:
# [+] Scanned 2 files
# [+] Baseline created successfully!
```

### Test 2: Change Detection

```bash
# Step 1: Modify a file
echo "Modified content" > ../test_files/file1.txt

# Step 2: Run integrity checker again
python integrity_checker.py

# Step 3: Choose option 2 (Check Integrity)
# Enter path: ../test_files

# Expected result:
# [!] MODIFIED FILES (1):
#     [-] file1.txt
```

### Test 3: New File Detection

```bash
# Step 1: Add a new file
echo "New file" > ../test_files/file3.txt

# Step 2: Check integrity
python integrity_checker.py
# Option 2, path: ../test_files

# Expected result:
# [+] NEW FILES (1):
#     [+] file3.txt
```

### Test 4: Deleted File Detection

```bash
# Step 1: Delete a file
# (On Windows: del ..\test_files\file2.txt)
rm ../test_files/file2.txt  # Linux/Mac

# Step 2: Check integrity
python integrity_checker.py
# Option 2, path: ../test_files

# Expected result:
# [-] DELETED FILES (1):
#     [-] file2.txt
```

### ✅ Module 1 Success Criteria
- Baseline creation works
- Detects modified files
- Detects new files
- Detects deleted files
- No crashes or errors

---

## 🌐 Module 2: Web Vulnerability Scanner Test

### Test 1: Payload Database

```bash
cd ../web_vulnerability_scanner
python payloads.py

# Expected output:
# [*] SQL Injection Payloads: 20
# [*] XSS Payloads: 20+
# Shows vulnerability information
```

### Test 2: URL Validation

```bash
python scanner.py

# Test with invalid URL first
# Enter: invalid-url
# Expected: Error message about invalid URL

# Test with valid URL
# Enter: http://example.com
# Expected: Proceeds to authorization prompt
```

### Test 3: Safe Test Target

**⚠️ WARNING**: Only test authorized sites!

Recommended safe test sites:
- http://testphp.vulnweb.com (intentionally vulnerable)
- http://demo.testfire.net (IBM test site)
- Your own local test server

```bash
python scanner.py

# Enter URL: http://testphp.vulnweb.com/artists.php?artist=1
# Confirm authorization: yes

# Expected result:
# [*] Testing SQL Injection
# [*] Testing XSS
# [+] Vulnerability report generated
```

### Test 4: Parameter Detection

```bash
# Test URL with parameters
python scanner.py

# URL: http://example.com/page?id=1&name=test
# Should detect and test both 'id' and 'name' parameters
```

### ✅ Module 2 Success Criteria
- Payloads load correctly
- URL validation works
- Scanner runs without crashes
- Results are displayed clearly
- Authorization check works

---

## 🛠️ Module 3: Penetration Testing Toolkit Test

### Test 3.1: Utility Functions

```bash
cd ../pentesting_toolkit
python utils.py

# Expected output:
# [*] Testing IP validation
# [*] Testing port validation
# [*] Common port services
# All tests pass with correct results
```

### Test 3.2: Port Scanner - Localhost

```bash
python port_scanner.py

# Step 1: Enter target
# Target: 127.0.0.1 (or localhost)

# Step 2: Confirm authorization
# Authorization: yes

# Step 3: Choose scan type
# Type: 1 (Common Ports)

# Expected result:
# [+] Port XX/tcp open SERVICE
# Shows open ports on your machine
# Completes without errors
```

### Test 3.3: Port Scanner - Custom Range

```bash
python port_scanner.py

# Target: 127.0.0.1
# Authorization: yes
# Type: 2 (Custom Range)
# Range: 80-443

# Expected result:
# Scans ports 80-443
# Shows any open ports in that range
# Displays timing information
```

### Test 3.4: DNS Resolution

```bash
python port_scanner.py

# Target: localhost
# Should resolve to 127.0.0.1

# Target: google.com
# Should resolve to IP address
```

### Test 3.5: Brute Force Simulator

```bash
python brute_forcer.py

# Step 1: Acknowledge educational purpose
# Answer: yes

# Step 2: Select target
# Choose: admin

# Step 3: Start simulation
# Answer: yes

# Expected result:
# Shows attack progress
# Finds credentials (admin:admin123)
# Displays educational insights
# No actual network activity
```

### ✅ Module 3 Success Criteria
- Utilities work correctly
- Port scanner detects open ports
- DNS resolution works
- Brute force simulator runs
- Educational information displays
- No actual attacks performed

---

## 🎮 Main Controller Test

### Test: Menu Navigation

```bash
cd ..
python main.py

# Test each menu option:
```

**Option 1: File Integrity Checker**
- Should launch Module 1
- Should return to menu after exit

**Option 2: Web Vulnerability Scanner**
- Should launch Module 2
- Should return to menu after exit

**Option 3: Penetration Testing Toolkit**
- Should show sub-menu
- Should launch port scanner or brute forcer

**Option 4: About**
- Should display information
- Should return to menu

**Option 5: Exit**
- Should exit cleanly

**Invalid Input**
- Should show error message
- Should not crash

### ✅ Main Controller Success Criteria
- All menu options work
- Navigation is smooth
- Error handling works
- Can exit cleanly
- No crashes

---

## 🐛 Common Issues & Solutions

### Issue 1: ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'requests'`

**Solution**:
```bash
pip install requests
```

### Issue 2: Permission Denied (Port Scanner)

**Error**: Permission errors or no ports detected

**Solution**:
```bash
# Use localhost for testing
# Scan common ports only (option 1)
# Reduce thread count if needed
```

### Issue 3: File Not Found (Integrity Checker)

**Error**: Directory not found

**Solution**:
```bash
# Use absolute paths
# Check directory exists
# On Windows: Use forward slashes or double backslashes
# Example: C:/Users/Name/test_files
```

### Issue 4: Import Error (Modules)

**Error**: Cannot import from payloads, utils, etc.

**Solution**:
```bash
# Run from correct directory
cd web_vulnerability_scanner
python scanner.py

# Not:
python web_vulnerability_scanner/scanner.py
```

### Issue 5: Baseline JSON Error

**Error**: JSON decode error

**Solution**:
```bash
# Delete baseline.json and recreate
cd file_integrity_checker
del baseline.json  # Windows
rm baseline.json   # Linux/Mac
python integrity_checker.py
# Choose option 1 to create new baseline
```

---

## 📊 Test Results Template

Use this to track your testing:

```
SecureOps Toolkit - Test Results
================================

Date: _______________
Python Version: _______________
OS: _______________

Module 1: File Integrity Checker
[ ] Baseline creation          Pass/Fail
[ ] Change detection          Pass/Fail
[ ] New file detection        Pass/Fail
[ ] Deleted file detection    Pass/Fail
Notes: _______________________________

Module 2: Web Vulnerability Scanner
[ ] Payload loading           Pass/Fail
[ ] URL validation           Pass/Fail
[ ] SQL injection test       Pass/Fail
[ ] XSS test                Pass/Fail
Notes: _______________________________

Module 3: Penetration Testing
[ ] Utility functions        Pass/Fail
[ ] Port scanner (localhost) Pass/Fail
[ ] DNS resolution          Pass/Fail
[ ] Brute force simulator   Pass/Fail
Notes: _______________________________

Main Controller
[ ] Menu navigation         Pass/Fail
[ ] Module launching       Pass/Fail
[ ] Error handling         Pass/Fail
[ ] Exit functionality     Pass/Fail
Notes: _______________________________

Overall Status: Pass/Fail
Additional Comments: _______________
```

---

## 🔍 Validation Checklist

### Code Quality
- [ ] All Python files run without syntax errors
- [ ] No undefined variables or functions
- [ ] Import statements work correctly
- [ ] Error handling works as expected

### Functionality
- [ ] Each module performs its intended function
- [ ] Results are accurate and meaningful
- [ ] User inputs are validated
- [ ] Edge cases are handled

### User Experience
- [ ] Clear prompts and instructions
- [ ] Readable output formatting
- [ ] Appropriate error messages
- [ ] Smooth navigation between menus

### Security & Ethics
- [ ] Authorization confirmations present
- [ ] Ethical warnings displayed
- [ ] No hardcoded credentials
- [ ] Safe defaults used

### Documentation
- [ ] README files are complete
- [ ] Usage examples work
- [ ] Code comments are clear
- [ ] Installation instructions accurate

---

## 🎯 Performance Benchmarks

Expected performance on modern hardware:

**File Integrity Checker**
- 1,000 files: < 5 seconds
- 10,000 files: < 30 seconds

**Web Vulnerability Scanner**
- Single parameter: 10-30 seconds
- Multiple parameters: 30-60 seconds

**Port Scanner**
- Common ports (14): 2-5 seconds
- Port range 1-1000: 20-40 seconds
- All ports (65535): 15-30 minutes

**Brute Force Simulator**
- 25 passwords: 3-5 seconds
- Includes 0.1s delay per attempt

---

## ✅ Final Verification

Once all tests pass:

1. **Clean Up Test Files**
```bash
rm -rf test_files  # Linux/Mac
rmdir /s test_files  # Windows
```

2. **Reset Baseline**
```bash
cd file_integrity_checker
# Edit baseline.json to reset it
```

3. **Document Results**
- Fill out test results template
- Note any issues encountered
- Save for reference

4. **Ready for Use!**
- Toolkit is fully functional
- All modules tested and verified
- Ready for educational use

---

## 🎓 Next Steps After Testing

1. **Read All Documentation**
   - Main README.md
   - QUICKSTART.md
   - Module READMEs

2. **Experiment Safely**
   - Set up local test environment
   - Try different scenarios
   - Modify and customize

3. **Learn the Concepts**
   - Study underlying security principles
   - Research vulnerabilities
   - Practice ethical hacking

4. **Share Responsibly**
   - Help others learn
   - Contribute improvements
   - Promote ethical usage

---

## 📞 Report Issues

If tests fail:

1. **Check This Guide**
   - Review common issues section
   - Verify prerequisites
   - Follow troubleshooting steps

2. **Document the Problem**
   - What were you doing?
   - What happened?
   - What did you expect?
   - Error messages?

3. **Seek Help**
   - Check documentation
   - Search online
   - Ask in communities
   - Open GitHub issue

---

## 🏁 Testing Complete!

If all tests pass:
✅ **Congratulations!** Your SecureOps Toolkit is fully operational.

If some tests fail:
⚠️ Review the troubleshooting section and try again.

**Remember**: This is an educational tool. Use it responsibly and ethically!

---

*Happy Testing! 🧪*
