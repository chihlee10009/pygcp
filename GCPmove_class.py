# upload a file to a gcp bucket
# store half of caesar cipher encrypted sym key
import os
from google.cloud import storage


class GCPmove:
    def __init__(self):
        self.downloaded_file_name = "caesar_half04102025.txt"
        self.storage_obj = storage.Client(project="PyScribble")
        self.bucket = self.storage_obj.bucket("pyscribble_bucket")
        blob = self.bucket.blob("caehlf04092025.txt")
        # blob.download_to_filename(self.downloaded_file_name)
        # print(f"downloaded file")

    def gcp_read(self, filename):
        blob = self.bucket.blob(filename)
        downloaded_as_string = blob.download_as_string()
        print(f"downloaded as string")
        return downloaded_as_string
        
    def gcp_upload(self, enc_uat):
        self.uploaded_file_name = "hug_face_uat"
        blob = self.bucket.blob(self.uploaded_file_name)
        blob.upload_from_string(enc_uat)
        print("uploaded_uat file")

if __name__ == "__main__":
    gcp_move_obj = GCPmove()
