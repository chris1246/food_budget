import os
from imbox import Imbox
import traceback
import sys
import time
import pdf_data

class MailChecker():
    def __init__(self) -> None:
        self.host = "imap.gmail.com"
        self.username = "*"
        self.password = '*'
        self.download_folder = "*"
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
                            #print(sndr[0])
                            att_fn = attachment.get('filename')
                            download_path = f"{self.download_folder}/{att_fn}"
                            #print(download_path)
                            with open(download_path, "wb") as fp:
                                fp.write(attachment.get('content').read())
                                #print(attachment.get('content').read())
                                self.sender(att_fn, sndr)
                                
                        except:
                            print(traceback.print_exc())
    def sender(self, att_fn, sndr):
        self.object.reciever(att_fn, sndr)
        unread_inbox_messages = self.mail.messages(unread=True)
        print("sender")
        if len(unread_inbox_messages) == 0:
            self.checker()

if __name__ == "__main__":
    app = MailChecker()