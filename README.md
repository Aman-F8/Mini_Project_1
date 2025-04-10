# **Automation Testing Summary for GUVI.in using Selenium and pytest**  

## **Objective**  
- Automate the GUVI.in web application using Python Selenium and pytest framework.  
- Validate functionality through positive and negative test scenarios.  

## **Tools Used**  
- **Python Selenium** (for browser automation)  
- **pytest** (for test framework)  
- **Supported Browsers**: Chrome, Firefox, Edge, Safari  

## **Test Suite Overview**  

### **Test Case 1: URL Validation**  
- Verify if the URL `https://www.guvi.in` is valid and accessible.  

### **Test Case 2: Webpage Title Verification**  
- Check if the webpage title matches:  
  - **Expected Title**: *"GUVI | Learn the code in your native language"*  

### **Test Case 3: Login Button Validation**  
1. Check if the **Login button** is visible.  
2. Verify if the **Login button** is clickable.  

### **Test Case 4: Sign-Up Button Validation**  
1. Check if the **Sign-Up button** is visible.  
2. Verify if the **Sign-Up button** is clickable.  

### **Test Case 5: Sign-In Page Redirection**  
- Click the **Sign-Up button** and verify redirection to:  
  - `https://www.guvi.in/sign-in/`  
- Ensure the page exists and loads correctly.  

### **Test Case 6: Successful Login & Logout**  
1. **Login** with valid credentials and verify success.  
2. **Logout** and confirm the session ends properly.  

### **Test Case 7: Invalid Login Attempt**  
1. Attempt login with **invalid credentials**.  
2. Capture and verify the **error message**.  

## **Conclusion**  
- The test suite covers **navigation, UI elements, authentication (valid & invalid), and session management**.  
- Ensures functionality across different scenarios for a robust user experience.  

---  
This summary provides a structured overview of the automation testing process for GUVI.in. 🚀
