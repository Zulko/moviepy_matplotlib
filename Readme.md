Repo made for the following issue on github/Matplotlib:


I compared writing a video using Matplotlib's animation module, with writing the same Matplotlib video using my library MoviePy instead of Animation.save().

See [here](https://github.com/Zulko/matplotlib_moviepy) for details and results.

It turns out that MoviePy produces an animation of better quality (Matplotlib's has
JPEG-compression-style artefacts) and much lighter (95k for MoviePy, 456k for Matplotlib).
MoviePy is also faster (generating the animation takes 6 seconds with MoviePy, against 12s
for Matplotlib).


The codes of the animation with matplotlib.Animation and MoviePy are a little different but I made sure the two clips had the same number of frames, same fps, (almost) the same size, same writer (FFMPEG), etc. so I really believe this shows that Animation.save(), or at least its defaults, could be improved.


Not sure where the problem is. For the quality/size, it may be a matter of
codecs or whatever, I'm sure it can be tuned.  For the speed, it may be due to
the fact that Matplotlib converts the frame into some compressed image format
(I believe it is PNG by default) and sends them to ffmpeg, which then must
decode it. MoviePy sends the raw RGB snapshot of the matplotlib canvas directly
to ffmpeg (no encoding/decoding needed).

Maybe it would be possible to have by default matplotlib send directly a raw RGB input to ffmpeg (or avconv),
like MoviePy does ?