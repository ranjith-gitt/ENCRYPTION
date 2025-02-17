# ENCRYPTION
# ADVANCED-ENCRYPTION-TOOL

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: RANJITH T

**INTERN ID**: CT08UZT

**DOMAIN**: Cyber Security & Ethical Hacking

**BATCH DURATION**: Febraury 15th, 2025 to March 15th, 2025

**MENTOR NAME**: NEELA SANTHOSH

# DESCRIPTION OF TASK PERFORMED

1. **Environment Setup**:  
   - The user is working in a **Kali Linux** environment.  
   - Python is used to run a custom AES-256 encryption tool.  

2. **Encryption Task**:  
   - The user selected the "Encrypt" option in the tool.  
   - Provided the file path `/home/kali/Documents/myfile.txt`.  
   - Encryption completed successfully, producing an encrypted file named `myfile.txt.enc`.  
   - The tool generated a random encryption key:  
     `f4b95d4ed27dfc8ec191338cf9c1e2516db12c2d54784445022d558ad1cce0`.

3. **Decryption Task**:  
   - The user selected the "Decrypt" option in the tool.  
   - Provided the path to the encrypted file: `/home/kali/Documents/encrypt_tool.spec`.  
   - Provided the encryption key generated earlier.  

4. **Error Encountered**:  
   - The decryption process failed with the error:  
     **`ValueError: Invalid padding bytes`**.  
   - This indicates that the provided encrypted file or key is invalid.  

5. **Troubleshooting Attempts**:  
   - The user rechecked the decryption process using the provided key and file but encountered the same error.

6. **Possible Issues Identified**:  
   - The wrong file (`encrypt_tool.spec`) might have been used instead of the correct `.enc` file.  
   - The encryption key or file data might have been altered or corrupted.  
   - The padding mechanism in the tool might be causing decryption issues. 

# OUTPUT

![Image](https://github.com/user-attachments/assets/6c7e61f2-f0ee-4480-a3bb-1aa88a55635d)

