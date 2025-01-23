# CopBot Application

CopBot is a Python-based automation tool designed specifically for automating tasks on the **online Supreme store**. However, please note that this code is **outdated** and may no longer work as intended due to changes in the Supreme website and modern browser compatibility requirements.

---

## Features

### User Interface

- Built using **Tkinter** with a tabbed interface for easy navigation.
- Tabs for:
  - Billing Information
  - Product Selection
  - Instructions
  - Account Management

### Automation

- **Web Automation**: Uses Selenium to interact with the Supreme store's website.
- **Order Processing**:
  - Searches for a product by keyword.
  - Selects product size and quantity.
  - Adds the product to the cart and completes the checkout process.

### Account Management

- Login system with options to save user credentials.
- Delete account functionality.
- Remember Me feature.

### Notifications

- Sends desktop notifications for tasks requiring user attention, such as CAPTCHA completion.

### Additional Features

- Real-time clock display in the GUI.
- Validation for inputs such as phone numbers and credit card details.

---

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.7+
- `tkinter`
- `selenium`
- `webdriver-manager`
- `win10toast`
- `threading`

You can install the required libraries using pip:

```bash
pip install selenium webdriver-manager win10toast
```

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/copbot.git
```

2. Navigate to the project directory:

```bash
cd copbot
```

3. Run the application:

```bash
python copbot.py
```

---

## How to Use

1. **Launch the Application**:
   - Run the script to open the main GUI.
2. **Login**:
   - Enter your username and password to log in.
   - Use the "Remember Me" checkbox to save your credentials.
3. **Manage Billing Details**:
   - Navigate to the "Billing" tab to enter and save billing information.
4. **Select Products**:
   - Go to the "Product" tab to enter product details (keywords, size, quantity, and page link).
   - Click "Run" to automate the purchase.
5. **Notifications**:
   - Watch for notifications to complete CAPTCHAs or confirm actions.

---

## How User Data is Saved

CopBot saves user data locally in plain text files. Here is how it works:

- When a user logs in for the first time, a file named after the username is created in the working directory.
- The file stores:
  - Username and password.
  - Billing details such as name, email, phone number, and address.
  - Payment information including card number, expiration date, and CVV.
- The "Remember Me" feature stores credentials in a separate file (`r`) for automatic login.

**Important**: As the data is saved in plain text files without encryption, it is not secure. Users should handle their files with care and avoid using sensitive real-world information.

---

## File Structure

```plaintext
copbot/
├── copbot.py       # Main application script
├── requirements.txt # List of dependencies
└── README.md        # Project documentation
```

---

## Known Issues

- CAPTCHA completion requires manual intervention.
- Limited to the Supreme store's website and may not work on other e-commerce platforms.
- This code is outdated and may not function due to website updates or changes in browser compatibility.

---

---

## Disclaimer

This tool was designed for educational purposes and specifically for the Supreme online store. The author is not responsible for any misuse of this application. Please note that the code is no longer functional due to updates on the Supreme website and modern browser requirements.

