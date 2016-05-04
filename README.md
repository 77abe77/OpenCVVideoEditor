
<h1>OpenCV Video Editor</h1>

<h2> Usage </h2>
```python
OpenCVVideoEditor('/path/to/videofile')
```

<h2> Description </h2>
<p>This is a simple class that takes in a video file path and builds a video editor over a 
OpenCV window. </p>
<p> It provides the following features: </p>
<ul>
  <li>Seek Bar</li>
  <li>Pause/Play</li>
  <li>Deleting a selected range of frames</li>
  <li>Replay</li>
</ul>

<p>Currently this video editor is set up as part of my Neural Network RC Car project, so
it plays a custom video file that contains keyboard direction along with raw pixel data.
This can be easily modified by simply removing the following lines of code: </p>
```python
 # Drawing Direction Indicator
 # Up
 cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 50),
                      (self.frameWidth/2 + 10, self.frameHeight - 30),
                      (255,255,255))
 # Down
 cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 25),
                      (self.frameWidth/2 + 10, self.frameHeight - 5),
                      (255,255,255))
 # Left
 cv2.rectangle(frame, (self.frameWidth/2 - 35, self.frameHeight - 25),
                      (self.frameWidth/2 - 15, self.frameHeight - 5),
                      (255,255,255))
 # Right
 cv2.rectangle(frame, (self.frameWidth/2 + 15, self.frameHeight - 25),
                      (self.frameWidth/2 + 35, self.frameHeight - 5),
                      (255,255,255))

 if direction == 'F':
    cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 50),
                                         (self.frameWidth/2 + 10, self.frameHeight - 30),
                                         (255,255,255), -1)
 elif direction == 'B':
    cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 25),
                                         (self.frameWidth/2 + 10, self.frameHeight - 5),
                                         (255,255,255), -1)
 elif direction == 'L':
    cv2.rectangle(frame, (self.frameWidth/2 - 35, self.frameHeight - 25),
                                         (self.frameWidth/2 - 15, self.frameHeight - 5),
                                         (255,255,255), -1)
 elif direction == 'R':
    cv2.rectangle(frame, (self.frameWidth/2 + 15, self.frameHeight - 25),
                                         (self.frameWidth/2 + 35, self.frameHeight - 5),
                                         (255,255,255), -1)


  ```
<p>AND</p>
```python
frame = frame.split('\t')
direction = frame[0]
```
