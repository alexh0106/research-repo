import pandas as pd
import sys
from pytrends.request import TrendReq

def format_file_name (unformatted):
        formatted = ""
        for ch in unformatted:
                if ch == "(":
                        break
                if ch == " ":
                        ch = "_"
                formatted = formatted + ch
        if formatted[:-1] == "_":
                formatted = formatted[:-1]
        return formatted.lower()

data_repository_path = "news_trends/"
company_filepath = data_repository_path + "news_companies.txt"
tracker_filepath = data_repository_path + "news_tracker.txt"
no_data_filepath = data_repository_path + "news_no_data.txt"
data_gathering_timeframe = 'all'
search_type = 'news'
category = ''
trend_request = TrendReq(hl='en-us', tz=360)

company_list = file(company_filepath, "r")

for company in company_list:
        tracker_file = file(tracker_filepath, "r")
        already_gathered = False
        for already_gathered_name in tracker_file:
                if company == already_gathered_name:
                        already_gathered = True
                        print("data already gathered for " + company.rstrip())
        tracker_file.close()
        if already_gathered == False:
                company = company.rstrip()
                tracker_file = file(tracker_filepath, "a+")
                tracker_file.write(company + "\n")
                tracker_file.close()
                kw_list = []
                kw_list.append(company)
                trend_request.build_payload(kw_list, timeframe=data_gathering_timeframe)
                interest_over_time = trend_request.interest_over_time()
                if interest_over_time.empty:
                        print("no data found for " + company)
                else:
                        tracker_file = file(tracker_filepath, "a+")
                        tracker_file.write(company + "\n")
                        data_file = file(data_repository_path + format_file_name(company) + ".csv", "w")
			dates = []
                        for date in interest_over_time.index:
                                date_as_string = str(date)
                                dates.append(date_as_string[:-9])
                        data_arr = []
                        for data_points in interest_over_time.get(company):
                                data_arr.append(data_points)
                        data_file.write("dates, " + company + "\n")
                        for date, data_points in zip(dates, data_arr):
                                data_file.write(date + ", " + str(data_points) + "\n")
                        data_file.close()
                        print("file created for " + company)
