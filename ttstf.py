import pyttsx3 as tts
import sys
import argparse

def GrabVoiceIndex(voices):
    ret = ''

    for i in range(len(voices)):
        ret += f"{i}: {voices[i].name}\n"

    return ret


# Usual argparse stuff
parser = argparse.ArgumentParser(description="\tEasy invoicer from the commandline.\n\n\tHow to use:\n\npython --number 109 --logo 'C://Location_To_Logo.png' --company 'COMPANY' 'STREET' 'CITY / STATE / ZIP' 'NUMBER' --idate 09.09.019 --work 'Item' 'Description' 2000 1",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--voice','-v', type=int, default=0,
                    help="the number of the invoice")
parser.add_argument('--text','-t', type=str, default="You didn't input anything to say",
                    help="to point to a file, use 'filename*.txt' for example")
parser.add_argument('--speed','-s', type=int, default=150,
                    help="the number of the invoice")
parser.add_argument('-vc', "--voice_chooser", action='store_true',
    help='add -bl to remove all blank lines')
args = parser.parse_args()

# Check the input
isFile = len(args.text.split('*.')) > 1

# Communicate to user what input was detected
print(f"Inputted {'A file' if isFile else 'Raw Input'}")

# Init the tts engine
e = tts.init()

# Set up some voice settings
voices = e.getProperty('voices')
e.setProperty('rate', args.speed)

# Init voice chooser
if args.voice_chooser:
    args.voice = int(input(f"Which voice would you like to use?\n{GrabVoiceIndex(voices)}"))

# Set the voice
who = voices[args.voice]
e.setProperty('voice', who.id)

# Communicat to the user what voice they'll be using
print(f"Using voice: {who.name}")

# Need a ref for all the stuff we are going to say
speak = []

# If input is a file,
if isFile:
    # Open it
    with open(args.text.replace('*', ''), 'r', encoding='utf8') as f:
        #
        speak = f.read().split('\n')
        print(speak)
else:
    speak.append(args.text)

# Run our speaking loop
for s in speak:
    e.say(s)
    e.runAndWait()

# I am going to figure out how to just save all that to a file nice & easy.
# e.save_to_file(args.text, './intro.aiff')