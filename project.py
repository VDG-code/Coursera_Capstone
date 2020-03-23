import pandas as pd
df=pd.read_csv('https://cocl.us/datascience_survey_data')
df.head()
df.columns = ['Topics','Very Interested','Somewhat Interested','Not Interested']
df.head()
