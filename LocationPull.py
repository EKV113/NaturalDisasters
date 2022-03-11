import twint
import datetime
import pandas
# Configure
list_ = ["the", "i", "if"]
count=2
base = "2018-12-31 12:49:05"
base1 = datetime.datetime.strptime(base,'%Y-%m-%d %H:%M:%S')
date_list = [base1 - datetime.timedelta(days=x) for x in range(360)]

for i in list_:
    print(i)
    c = twint.Config()
    c.Search = i
    c.Pandas = True
    c.Since = "2015-01-01"
    c.Until = "2020-01-01"
    c.Location = True
    c.Limit = 1000
    c.Custom_csv = ["id", "user_id", "username", "date", "tweet"]
    c.Output = f"hh{count}.csv"

    twint.run.Search(c);
    Tweets_df = twint.storage.panda.Tweets_df
    count+=1
    Tweets_df.to_csv(f"hh_{count}.csv")

