import pyloudnorm
import soundfile
form pydub import AudioSegment
import os

#Prints a read out of the pre processed audio loudness.
def LUFSget(loudness):
    if loudness == float(loudness):
        print(loudness,'db')


#Function for normalizing, will only work with wav files at the moment.
def Normalize(loudness, data, normalizerate, typeprompt):
    if typeprompt == 'peak':
        normalizerate = int(normalizerate)
        if -55 <= normalizerate <= 1:
            peak_normalized_audio = pyloudnorm.normalize.peak(data, normalizerate)
            print('clip normalized to', normalizerate, 'db', 'from', loudness, 'db')
            soundfile.write('test_new.wav',peak_normalized_audio, samplerate=41000)
        else:
            print('please enter a number between -54 and 0')

    if typeprompt == 'loudness':
        normalizerate = int(normalizerate)
        if -55 <= normalizerate <= 1:

            loudness_normalized_audio = pyloudnorm.normalize.loudness(data,
            loudness, normalizerate)

            print('clip normalized to',
            normalizerate, 'db', 'from', loudness, 'db')

            soundfile.write(
                '/home/alex/Documents/PyloudLUFS/processed/test_new.wav',
                loudness_normalized_audio, samplerate=41000)

        else:
            print('please enter a number between -54 and 0')


#Simple MP3 to WAV converter.
def Mp3Convert(source, destination):
    sound = AudioSegment.from_mp3(source)
    sound.export(destination, format="wav")


#File extension seperation function here!
