# Amazon Price Tracker

This is a Python-based script that tracks the price of a product on Amazon and sends an email alert when the product price drops below a specified threshold.

## Features

- Scrapes product details (price and title) from the Amazon product page.
- Tracks the price of the product.
- Sends an email notification when the price drops below a set target price.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed.
- An active Google account for sending emails via SMTP.
- Access to App Passwords in your Google account (required for SMTP).
- Environment variables set up for sensitive data (email, password, etc.).

## Setup

### Clone this repository:

    git clone <repo_url>
    cd amazon-price-tracker-project

## Install required libraries:

Ensure you have `requests`, `beautifulsoup4`, and `python-dotenv` libraries installed. You can install them using pip:

    pip install requests beautifulsoup4 python-dotenv

## Create a .env file:

In your project directory, create a .env file to store your email and password securely. Example:

    MY_EMAIL="your_email@gmail.com"
    MY_PASSWORD="your_app_password"
    TO_EMAIL="recipient_email@example.com"

## Customization

- You can modify the TARGET_PRICE in the script to adjust the price threshold according to your preference.
- You can add more features, such as tracking multiple products by repeating the code block for other URLs.

## Disclaimer

This project is intended for educational purposes only. The web scraping technique used here is not illegal as it complies with Amazon's terms of service for personal use. Please make sure to respect Amazon's robots.txt file and terms of use. Avoid using this script for commercial purposes or violating any laws or site policies.

