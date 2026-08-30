# Web Data Scraper

## Overview

This project demonstrates basic web scraping using Python. The program retrieves publicly accessible webpage content, parses the HTML structure, identifies required elements, and extracts information from the page.

## Objectives

- Understand the fundamentals of web scraping.
- Retrieve webpage content programmatically.
- Parse HTML documents.
- Extract specific webpage elements.
- Display or store extracted information.
- Develop basic web automation skills.

## Technologies Used

- Python 3.x
- Requests
- Beautiful Soup (`bs4`)
- HTML parsing

## Workflow

1. Import the required libraries.
2. Specify the webpage URL.
3. Send an HTTP request.
4. Retrieve the HTML content.
5. Parse the HTML using Beautiful Soup.
6. Locate the required HTML elements.
7. Extract the desired information.
8. Display the extracted data.

## Implementation

The project uses:

- `requests.get()` to retrieve webpage content.
- `BeautifulSoup()` to parse HTML.
- `find_all()` to locate webpage elements.
- `.text` to extract readable text.

The implemented example extracts heading information from a publicly accessible webpage.

## Learning Outcomes

This project provides practical experience in HTTP requests, HTML parsing, automated information extraction, and basic web-data collection.

## Author

M. Ayshwarya
