from pydub import AudioSegment
import os

source = '/home/alex/Documents/PyloudLUFS/test.mp3'
destination = '/home/alex/Documents/PyloudLUFS/mp3test.wav'

def Mp3Convert(source, destination):
    sound = AudioSegment.from_mp3(source)
    sound.export(destination, format="wav")

def main():
    print('--------MP3 CONVERTER--------')
    prompt = input('would you like to convert your MP3? Y/N').title()
    if prompt == 'Y':
        Mp3Convert(source, destination)
    if prompt == 'N':
        print('Quitting!')

main()

