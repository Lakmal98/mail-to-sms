from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import Connection as dbCon
from pymongo import MongoClient

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


# class Gmail:

conn = dbCon.Connection('mail-to-sms')
print(conn.find_all('connection'))


def main():
# Main method goes here

if __name__ == '__main__':
    main()
