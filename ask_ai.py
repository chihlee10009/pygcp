#   set an environment variable that stores half the caesar cipber encrypted sym key
#   reach out to the pyscribble_bucket and grab the file caesar_half.txt key
#   combine the caesar_half.txt file with the other half of the symkey environment variable
#   decrypt casesar cipher encypted sym key
#   read in AES encrypted API key from a file on the local server 
#   use the sym key to decrypt the api key
#   use gemini
# one file to do caesar_cipher encrypt / decrypt
# one file to upload and download from GCP bucket
# handle encrypt / decrypt and ask gemini a question
import os
import cryptography
import cryptography.fernet
import google.generativeai as genai
from GCPmove_class import GCPmove
import caesar_cryptography_operation as hail_caesar

local_enc_file = os.environ["ENC_FILE"]
half_sym_key = os.environ["SYMKEY"]
caesar_key = os.environ["CAESAR"]
gcp_obj = GCPmove()
with open(gcp_obj.downloaded_file_name, "r") as fid:
    half_downloaded_key = fid.read()

os.system(f"rm {gcp_obj.downloaded_file_name}")
half_downloaded_key = half_downloaded_key[:-1]
symkey = half_downloaded_key + half_sym_key
symkey = hail_caesar.caesar(symkey, -int(caesar_key))
symkey = symkey.encode("ascii")

#TODO: create a variable to store a bash environment
#  variable which holds the name of the encrypted api key file
with open(local_enc_file, "rb") as fid:
    api_key = fid.read()

fer_obj = cryptography.fernet.Fernet(symkey)

api_key = fer_obj.decrypt(api_key)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
print("gemini is thinking...")
response = model.generate_content("what is deepseek?")
print(response.text)



