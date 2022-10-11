import os
from imbox import Imbox
import traceback
import sys
import time
import pdf_data
import retrieve_hidden_info

class MailChecker():
    def __init__(self) -> None:
        self.data = retrieve_hidden_info.json_data() 
        self.host = "imap.gmail.com"
        self.username = f'{self.data.retrieve("username")}'
        self.password = f'{self.data.retrieve("mail_password")}'
        self.download_folder = f'{self.data.retrieve("path")}'
        self.object = pdf_data.reader()
        self.mail = Imbox(self.host, username=self.username, password=self.password, ssl=True, ssl_context=None, starttls=False)
        self.messages = self.mail.messages()
        print("Checker begun")
        self.checker()

    def checker(self):        
        while True:
            unread_inbox_messages = self.mail.messages(unread=True)
            if len(unread_inbox_messages) == 0:
                pass
            else:
                if not os.path.isdir(self.download_folder):
                    os.makedirs(self.download_folder, exist_ok=True)
                for (uid, message) in self.mail.messages(unread=True):
                    self.mail.mark_seen(uid)
                    for idx, attachment in enumerate(message.attachments):
                        try:
                            sndr = message.sent_from
                            att_fn = attachment.get('filename')
                            download_path = f"{self.download_folder}/{att_fn}"
                            with open(download_path, "wb") as fp:
                                fp.write(attachment.get('content').read())
                                self.sender(att_fn, sndr, self.download_folder)
                        except:
                            print(traceback.print_exc())
    def sender(self, att_fn, sndr, path):
        self.object.reciever(att_fn, sndr, path)
        unread_inbox_messages = self.mail.messages(unread=True)
        print("sender")
        if len(unread_inbox_messages) == 0:
            self.checker()

if __name__ == "__main__":
    app = MailChecker()