import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#nltk.download_shell()

messages = [line.rstrip() for line in open('SMSSpamCollection')]

for mess_no, message in enumerate(messages[:10]):
    print(mess_no,message)

messages = pd.read_csv('SMSSpamCollection',sep='\t',names=['label','message'])

messages['length']=messages['message'].apply(len)

#messages['length'].plot.hist(bins=150)

print(messages[messages['length']>900])

messages.hist(column='length',by='label',bins=60,figsize=(12,4))
plt.show()



