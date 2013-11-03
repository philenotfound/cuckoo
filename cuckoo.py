#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# (c) 2013, Phil Eichinger, phil@zankapfel.net

import tweepy
import pygame
import time

#OAuth Klumpert
consumer_key = 'YATD2iNsgGc4IbByonVwIw'
consumer_secret = 'RTYQC2uGTspFHAkVFMhbibnkMxX9QEatglKiNzKSdJ8'
access_token = '136590716-aUoInrZvBskV9ScL9o9AAt71Pokyd0hBpqLEIFxO'
access_token_secret = 'Cc3hdNdkVxtMlcFxqMNysg3TgGOFtObTdBhVXRNSmbc7c'
  

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
  #wait for music to play
  if( wait_for_completion ):
    print 'waiting'
    while( pygame.mixer.music.get_busy()):
      pass


pygame.mixer.init()
pygame.mixer.music.load("aktuell.wav")

wait_for_completion = False
listen_for = ['#pipifein']

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
