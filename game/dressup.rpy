### Dress-Up Screen
# Adapted from leon's [tutorial] Dress up game thread
# https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=14559

init python:
    outfit, glasses  = 1, 1 # default dressup items
    outfit_styles_num, glasses_styles_num = 3, 3 # number of styles for each dressup item
    
screen dressup_example():

    ## Ensure this appears on top of other screens.
    zorder 100

    frame:

        xalign 0.5
        xsize 700
        yfill True

        hbox:

            xalign 0.5
            yalign 0.15
            spacing 400

            textbutton _("<") action SetVariable('glasses', max(glasses-1,0))
            textbutton _(">") action SetVariable('glasses',min(glasses+1,glasses_styles_num))

        add "doll" xalign 0.5

        hbox:

            xalign 0.5
            yalign 0.5
            spacing 400

            textbutton _("<") action SetVariable('outfit', max(outfit-1,0))
            textbutton _(">") action SetVariable('outfit',min(outfit+1,outfit_styles_num))

        textbutton _("Done") action Jump('dressup_game') xalign 0.99 yalign 1.0