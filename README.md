# Proxy-PY
##Proxy IP Scraper and Tester

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)

## Description

This Python script is designed to scrape a list of proxy IP addresses from a specific website and then test the proxies to determine if they are functioning. The script is primarily used for collecting a list of working proxy IP addresses that can be used for various web scraping or network-related tasks.

## Features

- **Scraping Proxies:**
   - The script utilizes the `requests` library and regular expressions (`re`) to extract IP addresses with associated port numbers from "https://free-proxy-list.net/".

- **Testing Proxies:**
   - It tests the extracted proxy IP addresses by making requests to "https://httpbin.org/ip" using the proxies to check their functionality.
   - Working proxies are displyed 

- **Multithreading:**
   - The script employs multithreading using the `threading` library to make the proxy testing process more efficient by testing multiple proxies concurrently.

## Usage

1. Clone or download this repository to your local machine.

2. Install the required Python libraries if you haven't already:

3.Run the script

## Note

- The script is intended for educational and research purposes and should be used in compliance with the terms of use of the targeted websites.
- Be mindful of any legal and ethical considerations when using proxy IP addresses.

## Requirements

- Python 3.x
- Required Python libraries: `requests`, `re`, `threading`, `random`

## Contribution

Feel free to fork, modify, or contribute to this script for your specific needs. If you encounter any issues or have ideas for improvements, please create a GitHub issue or submit a pull request.


   


