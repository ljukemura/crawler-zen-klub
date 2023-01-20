# Zen-klub data crawler

This project uses Python and the `requests` and `pandas` libraries to crawl data from the Zenklub website (https://zenklub.com.br/) and save it to a CSV file.

## How to use

1. Make sure you have Python and the required libraries (`requests` and `pandas`) installed on your machine.
2. Clone or download the project files.
3. Run the script using `python zenklub_crawler.py` in your command line.
4. The script will make a request to the Zenklub API and retrieve data for the first 30 professionals.
5. The data will be saved to a CSV file named `zen-klub.csv` in the same directory as the script.

## Customization

You can change the number of professionals to retrieve by modifying the `limit` variable.

**Note**: The script is set to run the loop once and retrieve 30 professionals. The variable `b` is not being used in this script. The variable `a` is also not being used in this script.

## Disclaimer

Please note that this script is intended for educational and research purposes only. Use of this script for any other purpose may be in violation of Zenklub's terms of service and could result in your IP address being blocked.
