import pandas as pd 
import re

data_abusive = pd.read_csv('abusive.csv')
data_alay = pd.read_csv('new_kamusalay.csv', encoding='iso-8859-1',header=None)
data_alay =data_alay.rename(columns={0: 'original', 1: 'replacement'})

def lowercase(text):
    return text.lower()

def remove_unnecessary_char(text):
    text = re.sub('\n',' ',text) # Remove every '\n'
    text = re.sub('rt',' ',text) # Remove every retweet symbol
    text = re.sub('user',' ',text) # Remove every username
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',text) # Remove every URL
    text = re.sub('  +', ' ', text) # Remove extra spaces
    return text
    
def remove_nonaplhanumeric(text):
    text = re.sub('[^0-9a-zA-Z]+', ' ', text) 
    return text

data_alay_new_map = dict(zip(data_alay['original'], data_alay['replacement']))

#merubah kata kata alay menjadi kata kata baku
def normalize_alay(text):
    return ' '.join([data_alay_new_map[word] if word in data_alay_new_map else word for word in text.split(' ')])
def preprocess(text):
    text = lowercase(text) # 1
    text = remove_nonaplhanumeric(text) # 2
    text = remove_unnecessary_char(text) # 2
    text = normalize_alay(text) # 3
    return text