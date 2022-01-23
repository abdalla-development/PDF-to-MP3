import requests
from PyPDF2 import PdfFileReader
from gtts import gTTS
import os

MOBILE_PRODUCTION_KEY = "4747526f384bc3c004716a25baa32e83"
WEB_EVALUATION_KEY = "e74dc94bf1a0962453ae892632ee5389"
API_URL = "https://api.nexmo.com/v1/calls/:uuid/talk"


# Read The PDF File Specified & Get Both The Text and Number of Pages

data = ""
os.system("start C:/Users/abdo_/OneDrive/Desktop/Introduction.PDF")
temp = open('C:/Users/abdo_/OneDrive/Desktop/Introduction.PDF', 'rb')
PDF_read = PdfFileReader(temp)
number_of_pages = PDF_read.getNumPages()
file_page = PDF_read.getPage(0)
text_page = file_page.extractText()
for i in range(number_of_pages):
    first_page = PDF_read.getPage(i)
    page = first_page.extractText()
    data += f"page {i+1}  {page}"


# Creating The API Request
# parameters = {
#     "action": "convert",
#     "text": data,
#     "voice": "usenglishfemale",
#     "format": "mp3",
#     "frequency": 44100,
#     "bitrate": 128,
#     "speed": 1,
#     "startpadding": 1,
#     "endpadding": 1,
#     "pitch": 1,
#     "Apikey": WEB_EVALUATION_KEY,
#     "output": "rest"
# }
# headers = {
#     "text": data
# }
# response = requests.put(url=API_URL, headers=headers)
#
# print(response.raise_for_status())
#
#

language = "en"
# output = gTTS(text=text_page, lang=language, slow=False)
# output.save("pdf_mp3.mp3")
os.system("start pdf_mp3.mp3")
