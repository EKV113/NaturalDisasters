import twint
import os

# search dates (since)
since_date = ['2006-06-28','2006-05-18', '2006-07-24']

# search dates (until)
until_date = ['2006-06-30', '2006-05-20', '2006-07-26']

# ID
IDs = ['20060628CHN1', '20060518CHN2', '20060724CHN3']

def search():
    for i, j, k in zip((range(len(since_date))), (range(len(until_date))), (range(len(IDs)))):
        c = twint.Config()
        c.Search = "the OR i OR to OR a OR and OR is OR in OR it OR you OR of OR for OR on OR my OR s OR that OR at OR with OR me OR do"
        c.Since = since_date[i]
        c.Until = until_date[j]
        c.Limit = 10
        c.Store_csv = True
        c.Output = IDs[k]

        twint.run.Search(c)

search()
                
                                        
