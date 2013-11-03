#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# (c) 2013, Phil Eichinger, phil@zankapfel.net

import tweepy
import pygame
import time
from RPIO import PWM
import RPIO

lastangle=-1

def angle2time(angle):
    if( angle >= 180):
      return 2360
    elif( angle <= 0 ):
      return 490
    else:
      return ((2360-490)/180*angle+490)

def diff(angle):
   if( lastangle == -1 ):
     return angle
   if( angle > lastangle ):
     return angle-lastangle
   elif( angle < lastangle):
     return lastangle-angle
   else:
     return 0

def set_angle(angle):
  servos = PWM.Servo()
  diff_angle=diff(angle)
  if( diff_angle <> 0 ):
    servos.set_servo(18,angle2time(angle))
    global lastangle
    lastangle=angle
    sleeptime=float((0.5/180)*diff_angle)
    if( sleeptime < 0.01):
      sleeptime=0.01
    print "sleeptime is "+str(sleeptime)
    print "diff_angle is "+str(diff_angle)
    time.sleep(0.5)
    servos.stop_servo(18)


#OAuth Klumpert
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
  

class StreamListener(tweepy.StreamListener):
  def on_status(self, tweet):
    print 'on_status'

  def on_error(self, status_code):
    print 'Error: ' + repr(status_code)
    return False

  def on_data(self, data):
#do something
    print 'We got ONE!!!!11elf'
    birdistheword()

    def on_timeout(self):
      print('Timeout...')

def birdistheword():
  pygame.mixer.music.play()
  RPIO.output(17, True)
  set_angle(0)
  set_angle(90)
  set_angle(0) 
  RPIO.output(17,False)
  RPIO.cleanup()
  #wait for music to play
  if( wait_for_completion ):
    print 'waiting'
    while( pygame.mixer.music.get_busy()):
      pass


pygame.mixer.init()
pygame.mixer.music.load("cuckoo-clock.mp3")
RPIO.setup(17, RPIO.OUT)

wait_for_completion = False
listen_for = ['#cuckoo']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
   
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
l = StreamListener()

streamer = tweepy.Stream(auth=auth, listener=l)
setTerms = listen_for

print 'Cuckoo twitter client for stilnest starting up'
print 'listening for %s' % listen_for
print 'waiting for every tweet: %s' % wait_for_completion

#bailout if no network connection
#initscript is responsible for restart

while( True ):
  try:
    streamer.filter(track = setTerms)
    print 'Got stream'
  except:
    print 'No network?'
    time.sleep(5)
