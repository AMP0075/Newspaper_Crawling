# Newspaper_Crawling
The aim of this project is to help users research and extract information about the
topic of their choosing from conventional news as well as social media. The output
will be in tabular form with required attributes. Automating the process will save
hours of precious time wasted in searching browsing through and organizing news
paper articles from the web manually. A user can specify:
1. The search keywords,
2. News portal from given options(TOI, The Hindu, etc)
3. Attributes required for articles(Date, heading, body, category,link etc.)
4. Output Format(csv,json, excel)
5. Time range.
The projects will use the concepts of concurrent programming to speed up the
process of web scrapping thereby optimally using the internet bandwidth to its full
Extent.

Frontend-
  InputForm:
  Made using Tkinter. Consisting of entry fields, checkboxes, radio button and Find button.

Backend-
  ScrapAbstract: A super class which handles all the functionality of instantiating and running threads to scrap data. Also consists of abstract methods to parse various attributes like Date, Heading, Link, Paper, Article , Category, City from the website, which are implemented by the respective subclasses. Calls the methods according to requirements provided by the user. Data provided by the user are instantiated as data members which are used by the subclasses for various functionality.


  ScrapToi: Implements the actual functionality of scrapping the required data according to the HTML DOM model of the Times of India. Returns the date format to standardize the date. Loops through the start and end date to fetch the page links and add them to the queue.

  ScrapHindu: Implements the actual functionality of scrapping the required data according to the HTML DOM model of the Times of India. Returns the date format to standardize the date. Loops through the start and end date to fetch the page links and add them to the queue.

  Convert: A module consisting of functions to convert file according to choice provided by theuser. It handles the plumbing methods of saving the data into usable file according to name passes as parameter. Also combines the data from both the newspapers to a single file with standardized data.

Steps to Run:
1) Clone the project and run the InputForm File.
2) Fill the form and click the find button.


