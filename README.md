# Web Scraping Indeed.com for Data Science Job Requirements in Hong Kong
*By Danny Vu*

This data analysis will be using Python's Scrapy framework to scrape Indeed.com for Data Science Job Requirements. Indeed does have a [REST API](https://github.com/indeedassessments/api-documentation) but at the time of this writing, the API is still under construction so I will be performing web scraping.

<img src="data/indeed-750.jpg" alt="Indeed.com" style="width: 300px;"/>

After the web scraping of web pages linked to the search term `Data Science`, I will be analyzing the job description and generating a word cloud visualization of the top skills required for Data Science roles in Hong Kong.

<img src="data/Generic_DataScienceWordCloud.jpeg" alt="Data Science Word Cloud" style="width: 500px;"/>

### Business Question: What are the main skills that a Data Scientist needs in Hong Kong?

<img src="data/Data Science Life Cycle.png" alt="Data Science Life Cycle" style="width: 500px;"/>

### Part 1: Data Mining

What is web scraping? It is extracting content from websites. First you need to study the website to know what information it has and where to get it from. Specifically, using HTML tags and CSS ids.

Why would you do it? If you don't have an API to get information you can programatically get data from a web page when no API's have been necessarily provided.

We will be using Scrapy - a complete Python framework used for automatic web crawling and scraping. This will deal with the communication aspect of the operation between the server hosting the target website and our python console.
