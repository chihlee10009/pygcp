# upload a file to a gcp bucket
# store half of caesar cipher encrypted sym key
import os
from google.cloud import storage

os.system("echo 'ICKd 4wX0B2LYfzx' > caesar_half04092025.txt")

class GCPmove:
    def __init__(self):
        #print(help(storage.Client))
        storage_obj = storage.Client(project="PyScribble")
        bucket = storage_obj.bucket("pyscribble_bucket")
        blob = bucket.blob("caehlf04092025.txt")
        blob.upload_from_filename("caesar_half04092025.txt")
        print("uploaded file")

GCPmove()
