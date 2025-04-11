# upload a file to a gcp bucket
# store half of caesar cipher encrypted sym key
import os
from google.cloud import storage


class GCPmove:
    def __init__(self):
        self.downloaded_file_name = "caesar_half04102025.txt"
        storage_obj = storage.Client(project="PyScribble")
        bucket = storage_obj.bucket("pyscribble_bucket")
        blob = bucket.blob("caehlf04092025.txt")
        blob.download_to_filename(self.downloaded_file_name)
        print(f"downloaded file")

if __name__ == "__main__":
    GCPmove()
