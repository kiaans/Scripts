#!/usr/bin/python2 
#Last.fm utilities for MPD

import gtk
import pynotify
import os
import pylast

MPD_LIBRARY_LOCATION = "/home/krsumeet/Music"
API_KEY = "yourkey"
API_SECRET = "your secret"
username = "username"
#Enter the hash directly.
password_hash = "hash of pwd"

class MPDTest:
        
    def __init__(self):
        #Initing the pynotif
        pynotify.init("mpd")
        n = pynotify.Notification("Action for current song", "What do you wanna do?")
        n.set_urgency(pynotify.URGENCY_LOW)
        n.set_timeout(5)
        n.add_action("action_delete", "Delete", self.deleteSong)
        n.add_action("no_dontdelete", "Hide", self.doNothing)
        n.add_action("love_on_lastfm", "Love on Last.fm", self.love_on_lastfm) 
        n.connect("closed", self.closeit)
        n.show()
        gtk.main()

    def deleteSong(self, notifyObj, action):
        print "Deleting the song"
        mpcProcess = os.popen("mpc -f %file%")
        try:
            # [:-1] to delete the trailing newline
            os.remove(MPD_LIBRARY_LOCATION+mpcProcess.readline()[:-1])
            #Deleting song from playlist
            os.popen("mpc del $(mpc -f %position% | head -n 1)")
        except:
            print "Something really went wrong"
        notifyObj.close()
        gtk.main_quit()

  
    def doNothing(self,notifyObj, action):
        notifyObj.close()
        gtk.main_quit()

    def closeit(self, notifyObj):
        notifyObj.close()
        gtk.main_quit()

    def love_on_lastfm(self, notifyObj, action):
        print "Loving track on last.fm"
        network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)
        
        artist = os.popen('mpc -f "%artist%" | head -n 1').read()
        title = os.popen('mpc -f "%title%" | head -n 1').read()

        track = network.get_track(artist, title)
        notifyObj.close()
        gtk.main_quit()
        track.love()
 
        #Confirming the user that the track has been loved by retrieving the last loved track from last.fm
        last_loved_track = str(network.get_user(username).get_loved_tracks(limit=1)[0][0])
        love_notification = pynotify.Notification("Last loved track confirmation", last_loved_track + " is your last loved track")
        love_notification.set_timeout(3)
        love_notification.show()

if __name__ == "__main__":
    obj = MPDTest()
