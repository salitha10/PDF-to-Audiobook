import pyttsx3 as tts
import PyPDF2 as pdf
import pygame
import keyboard

#Add your pdf file to the directory and replace the name in file open

speaker = tts.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) #0 for male 1 for female

#rate
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-50)

#volume
volume = speaker.getProperty('volume')
#speaker.setProperty('volume', volume-0.25)

def onWord(name, location, length):
   print ('word', name, location, length)

#Open file
file = open("myfile.pdf", "rb")
pdfreader = pdf.PdfFileReader(file)
pagecount = pdfreader.getNumPages()

print("Processing...")
for pg in range (pagecount):
    print("*", end=" ")
    page = pdfreader.getPage(pg)
    text = page.extractText()
    #speaker.connect('started-word', onWord)
    #text to speech
    #speaker.say(text)
    speaker.save_to_file(text, './Audio/page {}.wav'.format(pg+1))
    speaker.runAndWait()

pygame.init()
print("\nStart reading...\n press Space to Pause and UnPause ")
while pg in range(pagecount):
    print("Page {}".format(pg+1))
    pygame.mixer.music.load('./Audio/page {}.wav'.format(pg+1))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.delay(100)
        keyboard.wait('space')
        pygame.mixer.music.pause()
        keyboard.wait('space')
        pygame.mixer.music.unpause()














