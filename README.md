# kivy
My kivy projects. Helpful functions and examples of how to use kivy.

# Important lessons (often learned the hard way)

Properies are important if you want text to dynamically change via kivi script, but sometimes you can get away with self.x or something similar to this. Probably has to do with where you are in the inheritance tree.

kv scripts are helpfull

make sure that you name things correctly

android.txt file should have this in it
title: X
author: X
orientation: X

you could also use buildozer...
you might need buildozer to compile it into something to put on the Play Store...
 
 
probably need a mac to make an IOS compatable app.


# NOTES

YOU CAN MAKE AN APK!!!!!! (theoretically comprable thing exists for ios...)

USE buildozer==0.30

it actually works, I think later versions are broken...

for now you have to copy paste over the apk once it is compiled

put it in some directory and then click install

you will be asked if you want to download from "unknown source"

Temporarily allow this (seems dangerous to permanantely do this... setting is found under secutiry in settings)

there you go!!

# buildozer

pretty easy 

use version 0.30

say 

buildozer android debug deploy

pretty much

not much usefull stuff in config file...
