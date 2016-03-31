from pydub import AudioSegment

result = AudioSegment.from_mp3('songs/1.mp3')
for i in range(1, 2000 + 1):
    try:
        print(i)
        if i % 100 is 0:
            print('export')
            result.export('songs/result{}.mp3'.format(i), format='mp3')
            result = AudioSegment.from_mp3('songs/{}.mp3'.format(i))
        else:
            result += AudioSegment.from_mp3('songs/{}.mp3'.format(i))
    except Exception as err:
        print(err)
        pass
result.export('songs/result{}.mp3'.format(i), format='mp3')
