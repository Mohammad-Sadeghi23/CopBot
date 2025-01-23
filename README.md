# CopBot

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
