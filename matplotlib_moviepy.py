"""

Testing MoviePy animations of Matplotlib plots against Matplotlib animations made
with Matplotlib's animation module.

MoviePy produces an animation of better quality (Matplotlib's has
JPEG-style artefacts), lighter (126k for MoviePy, 456k for Matplotlib), and is
faster (generating the animation takes 7 seconds with MoviePy, against 14s
for Matplotlib).

Not sure where the problem is. For the quality/size, it may be a matter of
codecs or whatever.

For the speed, it may be due to the fact that Matplotlib converts the frame into
some compressed image format (I believe it is PNG by default) and sends them to
ffmpeg, which then must decode it. MoviePy sends 



"""

#============
# MATPLOTLIB
#============


import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(5,5))
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x), lw=3)

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    
anim = FuncAnimation(fig, animate, np.arange(1, 200), interval=50)

t = time.time()
anim.save("test_mpl.mp4", writer='ffmpeg')
print "Animation with Matplotlib : %.02f seconds"%(time.time() - t)



#=========
# MOVIEPY
#=========


import time
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

fig, ax = plt.subplots( figsize=(6,6), facecolor=[1,1,1] )
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x), lw=3)

def make_frame(t):
    line.set_ydata(np.sin(x+2*t))  # update the data
    return mplfig_to_npimage(fig)

anim = VideoClip(make_frame, duration=10)

t = time.time()
anim.write_videofile("test_mpl_mpy.mp4", fps=20)
print "Animation with MoviePy : %.02f seconds"%(time.time() - t)