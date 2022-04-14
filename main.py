import requests
from datetime import date, timedelta
import pandas as pd


MY_API_KEY = "7bcdc60c-acdb-4d66-b823-5cb2b1a4ffd4"
API_ENDPOINT = 'http://content.guardianapis.com/search'
my_params = {
    'from-date': "",
    'to-date': "",
    'q' : "Brexit",
    'order-by': "newest",
    'show-fields': 'all',
    'page-size': 200,
    'api-key': MY_API_KEY
}
start_date = date(2018,1,1)
end_date = date.today()
dayrange = range((end_date - start_date).days + 1)
all_results = []
for daycount in dayrange:
    dt = start_date + timedelta(days=daycount)
    datestr = dt.strftime('%Y-%m-%d')
    my_params['from-date'] = datestr
    my_params['to-date'] = datestr
    current_page = 1
    total_pages = 1
    while current_page <= total_pages:
        print("...page", current_page)
        my_params['page'] = current_page
        resp = requests.get(API_ENDPOINT, my_params)
        data = resp.json()
        all_results.extend(data['response']['results'])
        # if there is more than one page
        current_page += 1
        total_pages = data['response']['pages']

df = pd.DataFrame.from_dict(all_results)
df.to_csv("results.csv")


