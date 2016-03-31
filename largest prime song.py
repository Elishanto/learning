from pydub import AudioSegment
import os, threading

notes = []
for filename in os.listdir('notes'):
    if filename.endswith('.wav'):
        notes.append(AudioSegment.from_wav('notes/' + filename)[:200])

with open('M74207281.txt') as f:
    result = notes[int(f.read(1))]
    i = 0
    while True:
        try:
            c = int(f.read(1))
            if c is not 0 and not c:
                break
            if i > 0 and i % 500 is 0:
                print(i)
                threading.Thread(target=result.export, args=('songs/{}.mp3'.format(i // 500), 'mp3')).start()
                result = notes[c]
            else:
                print(i)
                result += notes[c]
            i += 1
        except ValueError:
            pass
