


import pandas as pd


data = {
    
    "IP":["1.1.1.1","1.2.3.4","4.5.6.8,","5.8.9.4"],
    "User_Agent":["Mozilla", "Bot", "Crawler","Bot"],
    "Requests":[5,50,10,100]

}

df = pd.DataFrame(data)
print(df)

df["High_request"]= df["Requests"] > 40
print(df)

df["sus_user_agent"]= df["User_Agent"].str.contains("Bot|Crawler", case = True)
print(df)



df ["Is_bot"]= df["High_request"] | df["sus_user_agent"]

print(df)