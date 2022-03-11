########### Python 3.2 #############
import urllib.request
import pandas as pd
#import sys
#sys.path.append('./ignore/') # append path to current python module
from creds import sub_key


df = pd.read_csv("hamburg_data.csv")
page = 3505
# make sure pages between 2400-2700 are in the dataset

while True:
    print(f"PageNumber = {str(page)}")
    
    try:
        url = "https://credium-api.azure-api.net/base/api/Building?City=Hamburg&PageNumber=" + str(page)

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': sub_key,
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        data = pd.read_json(response)
        #print(f"Response code: {response.getcode()}")
        #data = response.read()
        #print(response.getcode())
        #print(data)
        
        df = df.append(data, ignore_index=True)
        df.to_csv("hamburg_data.csv", index = False)
        page += 1 
        
        if page in list(range(0, 40001, 500)):
            filepath = f"./ignore/backup/hamburg_data_{str(page)}.csv"
            df.to_csv(filepath, index = False)

    except Exception as e:
        print(e)
        print("Error reached, exiting loop")
        break
