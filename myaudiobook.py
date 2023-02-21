import pyttsx3
import PyPDF2

engine = pyttsx3.init()

book = open('the journey of two wings (1).pdf','rb') #give your book saved file name
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

play = pyttsx3.init()
print('playing audio book')

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 130)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

for num in range(0, num_pages):
    page = pdf_reader.getPage(num)
    data = page.extractText()
    play.say(data)
    play.runAndWait()