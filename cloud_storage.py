import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BkQxylENEKdpL9KZtqxGsi_1sXGC4amcW_Z1_8Vk0_iGg7gkgSRitmaYKyDOr9RDimgg0drlZQe4uTFWyRwyxsiazi_MIqWTihoQZTPeQYMnsCBY-3Tv-TJKUPHwNjJEXGdnmt0HNmsF'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/91880/Downloads/please.txt'
    file_to = 'C:/Users/91880/Dropbox/Screenshots/please1.txt'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
