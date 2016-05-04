# OpenCVVideoEditor.py
# Author: Abe Millan
import cv2
import numpy as np


class OpenCVVideoEditor():
        '''Simple Class Wrapper for a OpenCV Based Video Editor.
           Functionality: SeekBar, Pause, Crop Video Scale'''
        def __init__(self, filename):
            self.frameHeight = 288
            self.frameWidth = 352
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Loading Screen
            screen = np.zeros((self.frameHeight, self.frameWidth), np.uint8)
            cv2.putText(screen,'Loading Video...',
                                        (100,self.frameHeight/2),
                                        font,
                                        0.5, (255,255,255), 1)

            cv2.imshow('Editor', screen)


            # Load the Film into main memory (Basically one big buffer)
            # This is a very naive way of doing loading the video into main memory
            # It assumes the video is not too big and therefore can fit conservatively
            # in memory
            video = open(filename, 'r+')

            frames = video.readlines()


            # State Variables
            self.showControlsFlag = False
            self.pausingFlag = False
            self.selectingFlag = False
            self.startingFrame = -1
            self.endingFrame = -1
            self.currentFrame = 0
            self.lastFrame = len(frames) - 1

            # Set up
            self.setUpWindow()


            # Start Screen (Display Controls)
            screen = np.zeros((self.frameHeight, self.frameWidth), np.uint8)
            cv2.putText(screen,'Press any key to start...',
                                        (70,self.frameHeight/2),
                                        font,
                                        0.5, (255,255,255), 1)
            cv2.putText(screen,'Controls',
                                        (self.frameWidth - 100, 20),
                                        font,
                                        0.5, (255,255,255), 1)
            cv2.putText(screen,'c: hide/show controls',
                                        (self.frameWidth - 150, 35),
                                        font,
                                        0.4, (255,255,255), 1)
            cv2.putText(screen,'space: play/pause',
                                        (self.frameWidth - 150, 50),
                                        font,
                                        0.4, (255,255,255), 1)
            cv2.putText(screen,'s: crop mode',
                                        (self.frameWidth - 150, 65),
                                        font,
                                        0.4, (255,255,255), 1)
            cv2.putText(screen,'q: quit',
                                        (self.frameWidth - 150, 80),
                                        font,
                                        0.4, (255,255,255), 1)
            cv2.imshow('Editor', screen)

            if chr(cv2.waitKey(0) & 255) == 'q':
                self.lastFrame = self.currentFrame


            # Main Loop
            while self.currentFrame <= self.lastFrame:
                cv2.setTrackbarPos('Frame:', 'Editor', self.currentFrame)

                # Strip the frames to raw pixels
                # This follows the naive formate of 'Direction'\t'RawPixel'
                frame = frames[self.currentFrame].strip()
                frame = frame.split('\t')
                direction = frame[0]

                frame = np.resize(np.fromstring(frame[1],
                                  dtype = np.uint8),
                                  (self.frameHeight, self.frameWidth))


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
                elif direction == 'FR':
                    cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 50),
                                         (self.frameWidth/2 + 10, self.frameHeight - 30),
                                         (255,255,255), -1)
                    cv2.rectangle(frame, (self.frameWidth/2 + 15, self.frameHeight - 25),
                                         (self.frameWidth/2 + 35, self.frameHeight - 5),
                                         (255,255,255), -1)
                elif direction == 'FL':
                    cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 50),
                                         (self.frameWidth/2 + 10, self.frameHeight - 30),
                                         (255,255,255), -1)
                    cv2.rectangle(frame, (self.frameWidth/2 - 35, self.frameHeight - 25),
                                         (self.frameWidth/2 - 15, self.frameHeight - 5),
                                         (255,255,255), -1)
                elif direction == 'BR':
                    cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 25),
                                         (self.frameWidth/2 + 10, self.frameHeight - 5),
                                         (255,255,255), -1)
                    cv2.rectangle(frame, (self.frameWidth/2 + 15, self.frameHeight - 25),
                                         (self.frameWidth/2 + 35, self.frameHeight - 5),
                                         (255,255,255), -1)
                elif direction == 'BL':
                    cv2.rectangle(frame, (self.frameWidth/2 - 10, self.frameHeight - 25),
                                         (self.frameWidth/2 + 10, self.frameHeight - 5),
                                         (255,255,255), -1)
                    cv2.rectangle(frame, (self.frameWidth/2 - 35, self.frameHeight - 25),
                                         (self.frameWidth/2 - 15, self.frameHeight - 5),
                                         (255,255,255), -1)


                # Actions
                if not self.pausingFlag:
                    self.currentFrame = self.currentFrame + 1

                if self.selectingFlag:
                    cv2.putText(frame, "Select",
                                        (10, 20),
                                        font,
                                        0.6, (255,255,255), 1)
                if self.showControlsFlag:
                    cv2.putText(frame,'c: hide controls',
                                                (self.frameWidth - 120, 20),
                                                font,
                                                0.4, (255,255,255), 1)
                    cv2.putText(frame,'space: play/pause',
                                                (self.frameWidth - 120, 35),
                                                font,
                                                0.4, (255,255,255), 1)
                    cv2.putText(frame,'s: crop mode',
                                                (self.frameWidth - 120, 50),
                                                font,
                                                0.4, (255,255,255), 1)
                    cv2.putText(frame,'q: quit',
                                                (self.frameWidth - 120, 65),
                                                font,
                                                0.4, (255,255,255), 1)
                else:
                    cv2.putText(frame, "c: show controls",
                                        (self.frameWidth - 120, 20),
                                        font,
                                        0.4, (255,255,255), 1)

                if self.currentFrame == self.lastFrame:
                    # Display Replay option
                    endScreen = np.zeros((self.frameHeight, self.frameWidth), np.uint8)
                    cv2.putText(endScreen,'Video Ended:',
                                                (100, self.frameHeight/2 - 15),
                                                font,
                                                0.5, (255,255,255), 1)
                    cv2.putText(endScreen,'space: replay',
                                                (100, self.frameHeight/2),
                                                font,
                                                0.4, (255,255,255), 1)
                    cv2.putText(endScreen,'any key: exit',
                                                (100, self.frameHeight/2 + 15),
                                                font,
                                                0.4, (255,255,255), 1)
                    cv2.imshow('Editor', endScreen)

                    endOption = cv2.waitKey(0)

                    if ' ' == chr(endOption & 255):
                        self.currentFrame = 0



                cv2.imshow('Editor', frame)


                # Control Logic
                option = cv2.waitKey(30)
                if ' ' == chr(option & 255):
                    self.pausingFlag = not self.pausingFlag
                elif 'c' == chr(option & 255):
                    self.showControlsFlag = not self.showControlsFlag

                elif 's' == chr(option & 255):
                    if self.pausingFlag:
                        self.selectingFlag = not self.selectingFlag
                        if self.selectingFlag:
                            print('StartFrame')
                            self.startingFrame = self.currentFrame
                        else:
                            print('EndFrame')
                            self.endingFrame = self.currentFrame

                            # If there is no valid range, exit out of select mode
                            if self.startingFrame == self.endingFrame:
                                continue

                            # Crop Decision Screen
                            screen = np.zeros((self.frameHeight, self.frameWidth), np.uint8)
                            cv2.putText(screen,'Selected frames:',
                                                        (10, 20),
                                                        font,
                                                        0.4, (255,255,255), 1)
                            cv2.putText(screen,'Options:',
                                                        (100, self.frameHeight/2 - 15),
                                                        font,
                                                        0.5, (255,255,255), 1)
                            cv2.putText(screen,'d: remove selected frames',
                                                        (100, self.frameHeight/2),
                                                        font,
                                                        0.4, (255,255,255), 1)
                            cv2.putText(screen,'any key: cancel',
                                                        (100, self.frameHeight/2 + 15),
                                                        font,
                                                        0.4, (255,255,255), 1)
                            cv2.putText(screen, "{} to {}".format(self.startingFrame, self.endingFrame),
                                                (120, 20),
                                                font,
                                                0.4, (255,255,255), 1)
                            cv2.imshow('Editor', screen)

                            cropOption = cv2.waitKey(0)
                            # Remove Selected Frames Case
                            if 'd' == chr(cropOption & 255):
                                # Fix the possilitity of self.startingFrame > self.endingFrame
                                if self.startingFrame > self.endingFrame:
                                    temp = self.endingFrame
                                    self.endingFrame = self.startingFrame
                                    self.startingFrame = temp

                                # Rewrite the file Display a Loading Screen
                                frameCount = 0
                                video.seek(0)
                                for line in frames:
                                    if frameCount < self.startingFrame:
                                        video.write(line)
                                    if frameCount > self.endingFrame:
                                        video.write(line)
                                    frameCount = frameCount + 1

                                video.truncate()

                                # Reset all the State Variables and load the new film
                                self.currentFrame = 0
                                video.seek(0)
                                frames = video.readlines()
                                self.lastFrame = len(frames) - 1
                                cv2.destroyWindow('Editor')
                                self.setUpWindow()

                            self.startingFrame = -1
                            self.endingFrame = -1



                elif 'q' == chr(option & 255):
                    video.close()
                    break

        def setUpWindow(self):
            cv2.namedWindow('Editor')
            cv2.resizeWindow('Editor', self.frameWidth, self.frameHeight + 70) # Taller b/c trackbar
            cv2.createTrackbar('Frame:', 'Editor', 0, self.lastFrame,
                                                      self.trackerPositionUpdate)
        def trackerPositionUpdate(self, val):
            # The first condition is there because sometimes the callback
            # will erroneously give a val a value of zero. So we ignore the case
            if (val != 0) and abs(val - self.currentFrame) > 5:
                self.currentFrame = val

if __name__ == "__main__":
    OpenCVVideoEditor('../supportingFiles/newVideoLog.txt')
