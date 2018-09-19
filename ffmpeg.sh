ffmpeg -framerate 1/5 -i %d.jpg -c:v libx264 -vf "fps=24,format=yuv420p" out.mp4
