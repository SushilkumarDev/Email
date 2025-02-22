# Email Automation Script

## Overview
This project is an automated email-sending script built using Python. It allows users to send personalized emails with attachments via Gmail's SMTP server. The script is designed for job applications, business communications, and other professional email outreach.

## Features
- Sends automated emails with customizable subjects and HTML-formatted bodies.
- Supports attachments (e.g., resumes, documents).
- Uses Gmail's SMTP with TLS encryption for secure communication.
- Handles multiple recipients efficiently.
- Implements logging for debugging and monitoring.
- Secure credential handling through environment variables.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Required dependencies (install using the command below)

### Setup
```bash
pip install -r requirements.txt
```

### Required Environment Variables
To enhance security, avoid hardcoding credentials in the script. Instead, use environment variables:
```bash
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-mail-password"
```
Alternatively, you can store credentials securely in a `.env` file and load them with `dotenv`.

## Usage
Run the script with:
```bash
python send_email.py
```
Modify the `recipients` list in the script to specify email addresses.

## Security
For security best practices, refer to [SECURITY.md](SECURITY.md).

## Contribution Guidelines
We welcome contributions! Please follow our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and open an issue or submit a pull request.
