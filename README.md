# RetailScraper
Webscraper written with the Scrapy framework.

http://scrapy.org/

To use, you must specify the following command while in the Scrapy folder.

Go to the RETAILSCRAPER directory and run the following command:

	scrapy crawl ProductSpider -o C:\desired\output\path\desiredName.csv
	
At the prompt, enter the source text file:

	C:\example\texfile\location\filename.txt
	
The text file must consist of UTF coded URLS each on a separate line.

Press enter and the spider will crawl your websites, grab their info and put it in a CSV file you defined in the first command.