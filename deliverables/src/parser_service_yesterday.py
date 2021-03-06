from bs4 import BeautifulSoup
import pandas as pd

class ParserServiceYesterday:

    @staticmethod
    def create_df_worldometer(raw_data):
        """
        Parses the raw HTML response from Worldometer and returns a DataFrame from it
        @Params:
        raw_data (string): request.text from Worldometer
        @Returns:
        DataFrame
        """
        soup = BeautifulSoup(raw_data, features="html.parser")

        COLUMNS = ["Country", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active Cases", "Serious/Critical", "Tot Cases/1M pop","Tot Deaths/1M pop","Total Tests","Tests/1M pop"]

        _id = "main_table_countries_yesterday"

        countries_data = soup.find("table", attrs={"id": _id}).find("tbody").findAll("tr")

        parsed_data = []

        for country in countries_data:
            parsed_data.append([data.get_text().replace("\n","") for data in country.findAll("td")])

        return pd.DataFrame(parsed_data, columns=COLUMNS)

    @staticmethod
    def parse_last_updated(raw_data):
        """
        Parses the raw HTML response from Worldometer and returns the lastest update time from the webpage
        @Params:
        raw_data (string): request.text from Worldometer
        @Returns:
        Last updated time (string)
        """
        #TODO: 
        soup = BeautifulSoup(raw_data, features="html.parser")

        last_updated = soup.find("div", {"style": "font-size:13px; color:#999; margin-top:5px; text-align:center"})
        
        return last_updated.text