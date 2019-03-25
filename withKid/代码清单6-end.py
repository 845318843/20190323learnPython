# try items
# item2
import easygui
yourname = easygui.enterbox("hi, what's your name?")
yourroom = easygui.enterbox(" what's your room num?")

yourstreet = easygui.enterbox(" what's your street?")
yourcity = easygui.enterbox(" what's your city?")

yourprovince = easygui.enterbox(" what's your province?")
yourlocalcode = easygui.enterbox(" what's your local code?")

sentence = yourname + "\n" + yourroom + " " + yourstreet +\
           "\n" + yourcity + ", " + yourprovince + "\n" + yourlocalcode
easygui.msgbox(sentence)
