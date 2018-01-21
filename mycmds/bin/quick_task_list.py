#!/usr/bin/env python
from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import time 

#try:
#    import argparse
#    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
#except ImportError:
#    flags = None
flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/tasks-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/tasks.readonly'
SCOPES = 'https://www.googleapis.com/auth/tasks'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Tasks API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'tasks-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def setup_credentials():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('tasks', 'v1', http=http)
    return service 

def add_task(taskname,  description, timet):
    service = setup_credentials()
    task = {
      'title': taskname,
      'notes': description
    }

    strt = time.strftime("%Y-%m-%dT00:00:00.000Z",timet)
    task['due'] = strt
    result = service.tasks().insert(tasklist='@default', body=task).execute()
    # print (result['id'])
    return (result['id'])

# Note job items member : 'jobname', 'date', 'id', 'description'
def load_all_task(showDone = False):
    mytasks = []
    task = {}
    service = setup_credentials()
    # print ("Showdone:{}".format(showDone))
    if showDone is True:
        tasks = service.tasks().list(tasklist='@default').execute()
    else:
        tasks = service.tasks().list(tasklist='@default', showCompleted=False).execute()
    for task in tasks['items']:
        ## print(task)

        if u'due' in task.keys():
            
            if showDone is True and ( task['status'] != u'completed') :
                # print ("!!! >"+ task['status'])
                continue
            item = {}
            item['jobname'] = task['title']
            if showDone is True :
                item['date'] = task['completed']
            else:
                item['date'] = task['due']
            item['id'] = task['id']
            if 'notes' in task.keys():
                item['description'] = task['notes']
            
            #print (task['title'], task['due'])
            mytasks.append(item)
            #print(task)
    mytasks.sort()
    return mytasks


def compelte_task(gid):
    service = setup_credentials()
    tasks = service.tasks().list(tasklist='@default', showCompleted=False).execute()
    for ti in tasks['items']:
        if ti['id'] == gid:
            # print ("Found gid = {}".format(gid))
            ti['status'] = "completed"
            ti['completed'] = time.strftime("%Y-%m-%dT00:00:00.000Z", time.localtime())
            service.tasks().update(tasklist='@default', task=ti['id'], body=ti).execute()
            return True
    return False

def update_task(gid, title, note, due):
    service = setup_credentials()
    tasks = service.tasks().list(tasklist='@default', showCompleted=False).execute()
    for ti in tasks['items']:
        if ti['id'] == gid:
            # print ("Found gid = {}".format(gid))
            ti['title'] = title
            ti['notes'] = note
            ti['due'] = due
            service.tasks().update(tasklist='@default', task=ti['id'], body=ti).execute()
            return True
    return False


# list of items
def sync_to_tasklist(itemlist):
    service = setup_credentials()
    for item in itemlist:
        # print ("adding ")
        if item['id'] == 'new': 
            addtask = {
                'title': item['jobname'],
                'notes': item['description'],
                'due': item['date']}
            
            r = service.tasks().insert(tasklist='@default', body=addtask).execute()
            if r:
                print("INSERT OK")
         # Update
        elif item['actreq'] is 'del':
            compelte_task(item['id']) 
        elif item['actreq'] == 'edit':
            print("!!!", item['description'])
            update_task(item['id'], item['jobname'], item['description'], item['date']) 
    return load_all_task()



def main():
    """Shows basic usage of the Google Tasks API.

    Creates a Google Tasks API service object and outputs the first 10
    task lists.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('tasks', 'v1', http=http)

    tasks = service.tasks().list(tasklist='@default', showCompleted = True).execute()
    for task in tasks['items']:
        #print(task)
        if u'due' in task.keys():
            print (task['title'], task['due'], task['status'], task['completed'])
            # print(task)

    # complete 1st job
    ct = tasks['items'][0]
    # compelte_task(ct['id'])


    # Task Lists
#    tasklists = service.tasklists().list().execute()
#    print (tasklists)


#    task = {
#      'title': 'New Task',
#      'notes': 'Please complete me',
#      'due': '2010-10-15T12:00:00.000Z'
#    }

#    result = service.tasks().insert(tasklist='@default', body=task).execute()
#    print (result['id'])

#    results = service.tasklists().list(maxResults=10).execute()
#    items = results.get('items', [])
#    if not items:
#        print('No task lists found.')
#    else:
#        print('Task lists:')
#        print(items)
#        for item in items:
#            print(item[u'title'])
#            #print('{0} ({1})'.format(item[u'title'], item[u'id']))

if __name__ == '__main__':
    main()

