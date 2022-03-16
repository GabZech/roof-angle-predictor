########### Python 3.2 #############
import urllib.request
import pandas as pd
from creds import sub_key


page = 8500 # set to the same number as the last backup file

df = pd.read_csv(f"./ignore/backup/hamburg_data_{page}.csv")
#df = pd.DataFrame() # use this instead if no backup is available

page = page + 1

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
        page += 1 
        
        if page in list(range(0, 40001, 500)):
            filepath = f"./ignore/backup/hamburg_data_{str(page)}.csv"
            df.to_csv(filepath, index = False)

    except Exception as e:
        print(e)
        print("Error reached, exiting loop")
        break



