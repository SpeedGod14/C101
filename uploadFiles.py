import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:

                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload( f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.BF4oMeiwyoZIvVVykL81Q5pTHw8vJbfmlfqqXkFk4FPrDxqR8LP1OY8eH49dXeFgxcs7a0Cll9pLK18xVbNxk5HP1rr1vLJUSQxfVsySoBX7ivCo_s6Ky4msF-twAGqIe6vRTWA'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder that you want to move: ")
    file_to = input("Enter the dropbox path: ")

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()