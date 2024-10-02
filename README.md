


# Django Admin Automation Script

This script automates the process of reading data from a CSV file and submitting it to a Django web interface using Selenium WebDriver.

## Requirements

Before running the script, you need to have the following installed:

### 1. Python 3.x

Make sure you have Python installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### 2. Required Python Packages

Install the necessary Python packages using `pip`:

```bash
pip install selenium pandas
```

- **Selenium**: This is a browser automation framework that allows you to control web browsers programmatically.
- **Pandas**: This is a library used for data manipulation, and it will be used to read the CSV file.

### 3. Chrome and ChromeDriver

You need Google Chrome installed on your system, as well as ChromeDriver to interface Selenium with Chrome.

#### Steps to Install ChromeDriver:
1. Download ChromeDriver from the official site: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
2. Make sure that the version of ChromeDriver matches your installed version of Google Chrome.
3. Extract and place the ChromeDriver executable in a known directory.
4. Update the `chrome_driver_path` in the script with the path to your ChromeDriver executable.

### 4. CSV File

Ensure you have a CSV file containing the data you want to input. The script expects the CSV to have specific columns such as `first_name`, `last_name`, `email`, and `phone_number`.

Sample CSV structure:
```csv
first_name,last_name,email,phone_number,gender
John,Doe,john.doe@example.com,555-1234,male
Jane,Smith,jane.smith@example.com,555-5678,female
```

## Setup and Configuration

1. **Script Configuration**:
    - Open the script `automation_script.py`.
    - Update the `csv_file` path with the location of your CSV file.
    - Update the `admin_url` with the Django admin URL.
    - Modify the `username` and `password` variables with your Django admin credentials.
    - Adjust the form field names (e.g., `first_name`, `last_name`, etc.) if they differ from your model.

2. **Run the Script**:
    After configuring the script, run it as follows:

```bash
python automation_script.py
```

## Usage

The script performs the following tasks:

1. Logs in to the Django admin interface using your credentials.
2. Reads each row of the CSV file and enters the data into the appropriate form fields.
3. Submits the form for each row, adding new records to the Django admin.
4. Logs out and closes the browser after all records are processed.

## Troubleshooting

### Common Issues:
1. **ChromeDriver Version Mismatch**: Ensure that your ChromeDriver version matches your installed Chrome browser version.
2. **Timeout Errors**: Increase the `WebDriverWait` timeout if the web page is loading slowly.
3. **Incorrect Form Field Names**: Ensure that the form field names in the script (`By.NAME`) match those in the Django admin interface.

