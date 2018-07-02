# The script of the game goes in this file.

# Declare characters used by this game.

define a = Character("Augustina")

# Set up the main tutorial menu. Code taken from the official tutorial
# written by Pytom.

init python:

    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("Introduction To LayeredImage"))

    Tutorial("tutorial_newbie", _("For New Users"))
    Tutorial("tutorial_veteran", _("For Experienced Users"))
    Tutorial("tutorial_basics", _("Setting Up LayeredImage"))
    Tutorial("tutorial_auto", _("Automatic Definitions"))

    Section(_("The Bells and Whistles"))

    Tutorial("tutorial_animation", _("Animated Parts"))
    Tutorial("tutorial_sideimage", _("Side Images"))
    Tutorial("demo_dressup", _("Dress Up Game Demo"))

screen tutorials(adj):

    frame:
        xsize 600
        xalign 0.5
        ysize 700
        yalign 0.5

        #has side "c r b"

        vbox:
            for i in tutorials:

                if i.kind == "tutorial":

                    textbutton i.title:
                        action Return(i)
                        left_padding 20
                        xfill True

                else:

                    null height 30
                    text i.title alt "" xalign 0.5
                    null height 20

        #bar adjustment adj style "vscrollbar"

        textbutton _("That's all I need to know."):
            action Return(False)
            xalign 0.5
            yalign 1.0 


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()

# True if this is the first time through the tutorials.
default tutorials_first_time = True

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show augustina jeans at center

    with dissolve

    # These display lines of dialogue.

    a "\"You've created a new Ren'Py game.\""

    a "\"Once you add a story, pictures, and music, you can release it to the world!\""

    show augustina wink with dissolve

    a "... At least, that's what Eileen would say."

    show augustina open happy with dissolve

    a "Hi, I'm Augustina! I'm here to introduce you to the new LayeredImage function that came with Ren'Py 7."

    a "If you've read the {a=https://renpy.org/doc/html/layeredimage.html}documentation for LayeredImage{/a}, it may look a bit daunting at first. But that's why I'm here to help."

    a "There's a lot to go through. Where would you like to start?"

label tutorials:
    
    if tutorials_first_time:

        show augustina at left with move

        hide augustina

        show august jeans happy blinking regular at left

    else:

        a "Anything else you need help with?"

    $ tutorials_first_time = False
    $ renpy.choice_for_skipping()

    call screen tutorials(adj=tutorials_adjustment)

    $ tutorial = _return

    if not tutorial:
        jump end

    if tutorial.move_before:

        show august at center with ease

    $ reset_example()

    call expression tutorial.label from _call_expression

    if tutorial.move_after:

        show august at left with ease

    jump tutorials

label end:

    show august happy at center with move

    a "Think you got it from here? Good! I look forward to seeing what you'll make in the future."

    a "This unofficial tutorial was brought to you by: BáiYù for writing it, Deji for the Augustina Sprite, Mugenjohncel for the backgrounds, and PyTom and the rest of the Ren'Py team for their hard work on the engine."

    a "We also want to thank everyone who helped test out the tutorial and gave us pointers on which parts needed the most clairification."

    show august wink smile with dissolve

    a "And of course, thank you for viewing this tutorial. Good luck on your projects!"

    # Returning from the top level quits the game.
    return