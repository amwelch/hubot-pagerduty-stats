#!/usr/bin/env python

#Original code by Luke Carmichael (https://github.com/halfaleague)

import json
import argparse
import pandas 

from hipster import Hipster

def readdates(token, room):
    hipchat = Hipster(token)
    adfs = []
    for i in range(1, 19):
        date = '2015-06-{:02d}'.format(i)
        data = hipchat.get_messages(room_id=room_id, date=date)
        if data.get('status') == 400:
#            print 'skipping date', date
            continue
        messages = data['data']['messages']
        if not messages:
#            print date,messages
            continue
        name_date_text = [(x['from']['name'], x['date'], x['message']) for x in messages]
        names, date, text = zip(*name_date_text)
        df = pandas.DataFrame({'name':names, 'date':date, 'text':text})
        df['mlen'] = df['text'].str.len()
        adfs.append(df)

    return pandas.concat(adfs)

def parse_args():
    p = argparse.ArgumentParser(description = \
    '''
    Get stats about a Hipchat's room history
    ''')
    p.add_argument('--token', type=str, default = None, help = "API token used to connect to the room")
    p.add_argument('--room', type=str, default = None, help = "The room to connect to")
  
    args = p.parse_args()
    return args

def main():
    args = parse_args()
    df = readdates(args.token, args.room)
    df_gb = df.groupby(['name'])
    df = df_gb.sum()
    print json.dumps(df['mlen'].to_dict())
 
if __name__=="__main__":
    main()   
