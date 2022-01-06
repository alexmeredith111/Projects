import pyloudnorm
import soundfile


data, rate = soundfile.read("/home/alex/Documents/PyloudLUFS/test.wav") # load audio (with shape (samples, channels))
meter = pyloudnorm.Meter(rate) # create BS.1770 meter
loudness = meter.integrated_loudness(data) # measure loudness

def LUFSget(loudness):
    if loudness == float(loudness):
        print(loudness,'db')

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
            loudness_normalized_audio = pyloudnorm.normalize.loudness(data, loudness, normalizerate)
            print('clip normalized to', normalizerate, 'db', 'from', loudness, 'db')
            soundfile.write('/home/alex/Documents/PyloudLUFS/processed/test_new.wav',loudness_normalized_audio, samplerate=41000)
        else:
            print('please enter a number between -54 and 0')

def main():
    mainloop = 0 
    print('----------LUFS Edit----------')
    LUFSget(loudness)
    while mainloop == 0:
        mainprompt = input('would you like to choose a preset[1], create a custom normalize[2] or exit[0]')
        mainprompt = int(mainprompt)
        if mainprompt == 0:
            break

        if mainprompt == 2:
            typeprompt = input('what type of normalization would you like to select? (peak or loudness)- ').lower()
            normalizerate = input('and db of normalization between -54 and 0- ')
            Normalize(loudness, data, normalizerate, typeprompt)

        if mainprompt == 1:
            typeprompt = 'loudness'
            presetprompt = input('''
            You can choose from 8 loudness presets:
            [1] Spotify loud -11dB
            [2] Alexa, Spotify, Tidal, Youtube -14dB
            [3] Deezer -15 dB
            [4] Apple, AES streaming recommendation -16dB
            [5] Sony Entertainment -18dB
            [6] EU R128 Broadcast -23 dB
            [7] US TV ATSC A/85 Broadcast -24dB
            [8] Netflix Online streaming -27dB
            ''')
        if presetprompt == '1':
            normalizerate = -11
            Normalize(loudness, data, normalizerate, typeprompt)

        if presetprompt == '2':
            normalizerate = -14
            Normalize(loudness, data, normalizerate, typeprompt)

        if presetprompt == '3':
            normalizerate = -15
            Normalize(loudness, data, normalizerate, typeprompt)

        if presetprompt == '4':
            normalizerate = -16
            Normalize(loudness, data, normalizerate, typeprompt)

        if presetprompt == '5':
            normalizerate = -18
            Normalize(loudness, data, normalizerate, typeprompt)

        if presetprompt == '6':
            normalizerate = -23
            Normalize(loudness, data, normalizerate, typeprompt)

        if presetprompt == '7':
            normalizerate = -24
            Normalize(loudness, data, normalizerate, typeprompt)

        if presetprompt == '8':
            normalizerate = -27
            Normalize(loudness, data, normalizerate, typeprompt)




if __name__ == '__main__':
    main()


'''
the normalize function allows the user to specify the type of normalization peak or loudness. eventually i will create presets for industry standard
LUFS specifications that the user can quickly choose from. 
things i need to add to this funtion-
    -i need to allow for the use of any name without the user needing to rename the file to test.wav -medium fix - urgency 5
    -i need to allow multiple files to be normalized at once - medium fix - urgency 4
    -i need to allow for video file's audio to be accepted without the user needing to bounce the audio seperately - medium/hard fix - urgency 4 
    (this will eventually be more urgent when making presets for netflix or youtube etc...)
    -allow for different audio files - medium fix - urgency 8 -WORKING IN SEPERATE SCRIPT, NEED TO FIND A WAY OF IMPLEMENTING IT!!!
    -maybe create a nice looking terminal tool before starting the GUI interface - medium/hard fix - urgency 2

    
the LUFSget function simply gets the LUFS as an input, converts it from a str to a float. 
i can use this when it comes to creating a gui way down the line with the meter variable. 

GUI ideas-
    -create a visual LUFS meter with the meter variable.
    -create a drag and drop system for files.
    -create some kind of audio player within the interface.

You will need to do test cases too!!!
'''