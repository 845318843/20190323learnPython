# import easygui
# easygui.msgbox("Hello There!")


# import easygui
# user_response = easygui.msgbox("Hello there!")

# 6-1
import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
                           choices = ['Vanilla','Chocolate','Strawberry'])
easygui.msgbox("you picked " + flavor)
