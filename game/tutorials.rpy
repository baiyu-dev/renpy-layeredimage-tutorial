label tutorial_newbie:
    
    a "As a visual novel engine, Ren'Py is capable of displaying visuals along with text, just like it is right now. These can be standalone images, or parts of images placed on top of each other to form a new image."

    a "If you played \"The Question\" game that comes with the engine and opened up the source files, you'll see that all the visual assets are located in a folder named \"images\"."

    a "All of Sylvie's sprites are standalone image files that contain all the elements needed to be a sprite on their own, meaning that each file has her body and face rendered."

    show august side ah with dissolve

    a "Now, I'd like you to open up the \"images\" folder for this project."

    a "Go ahead and take a peek at each of the files in your default image program."

    show august blinking smallah with dissolve

    a "Notice how my outfits and facial features are separated into files of their own. Unlike Sylvie, I don't have a dedicated file for my \"smile\" emotion."

    show august dizzy frown bigsurprise with dissolve

    a "In total, there's 53 separate files for all the possible combinations I can have. I don't feel like doing the math, but you can imagine how long it'd take to export each of those individually."

    show august normal wink laugh -dizzy with dissolve

    a "Instead, I let Ren'Py put these files together to make up my sprites. This way, I'm not limited to just one expression that can convey a \"smile\" emotion."

    show august closedup smile with dissolve

    a "That's what LayeredImage is capable of. Amazing, right?"

    show august blinking smile with dissolve

    return
    
label tutorial_veteran:

    show august oneup wink smile with dissolve

    a "Most people know how to display standalone images in Ren'Py, but if you've ever had a character with lots of different emotions, you may have used a combination of {b}Composite(){/b} and {b}ConditionSwitch(){/b}, or other similar functions."

    show august frown tired unsure with dissolve

    a "While those do work, the code behind it is oftentimes messy and suboptimal. The new {b}LayeredImage{/b} function intends to replace older methods and make it simpler to accomplish the same thing."

    show august normal blinking smile with dissolve

    a "Not only that, but it also works better than {b}ConditionSwitch{/b} in most cases and can be used in the {b}Interactive Director{/b}."

    a "I recommend switching your sprites over to LayeredImage if possible, especially if your project is in the earlier stages of programming."

    a "If you don't want to though, other methods of compiling images together will still work regardless. You do you!"

    return

label tutorial_basics:
    
    show example basic_layeredimage

    a "Take a look at this excerpt from the documentation. This is a very basic example of how to set up a LayeredImage."

    show august smile with dissolve

    a "Like with our traditional image definitions, we start off with {b}layeredimage{/b} to let Ren'Py know we want to custom define something. We can put this before {b}label start:{/b} or even in a completely different .rpy file."

    show august closedup laugh with dissolve

    a "The nice thing about Ren'Py being based on Python is that the syntax is simple to understand. For the sprite, we want to make sure there's something there when we mention it, so we put an {b}always{/b} followed by the base of the sprite."

    show august blinking happy with dissolve

    a "No matter what clothes I'm wearing, or what my expression is, I'm going to have a body as long as I'm on the screen."

    a "Now that we've told Ren'Py what image will be a constant part of the sprite, we move onto our individual {b}group{/b} blocks. These are the parts that can change on the sprite."

    show august smile with dissolve

    a "Our first {b}group{/b} tells Ren'Py what outfits I can wear. As you can see, I have two {b}attribute{/b}s defined there: dress and jeans."

    a "Right now I am wearing my jeans. Let me show you my dress, it's super cute!"

    hide august jeans with moveoutright

    pause (2)

    show august dress wink happy regular with moveinright

    a "Tada! See? It's still me, but now I'm wearing a different outfit. The {b}attribute{/b} part of the code tells Ren'Py what different types of layers fit into the {b}group{/b} category."

    a "I should only be able to wear either my jeans or my dress, but not both at the same time."

    show august blinking smile with dissolve

    a "If you continue to scroll through the code, you'll find that a few of the {b}attribute{/b}s also have {b}default{/b} at the end."

    a "This tells Ren'Py to assume that I will have those parts on in case nothing else is specified."

    show august dark cryfunny bigsurprise with dissolve

    a "It'd be really scary if I showed up but didn't have a face at all!"

    show august blinking smile -dark with dissolve

    a "Finally, when you get to the end of the code, you'll see a variable being mentioned. In this case, it is the variable {i}evil{/i}, which was set to {i}False{/i} before we started the {b}layeredimage{/b} definition."

    show august oneup happy evil with dissolve

    #$ evil = True 

    a "Maybe I'm angry at you, or being sneaky. At some point in the game, the {i}evil{/i} variable was set to {i}True{/i}."

    show august normal smile regular with dissolve

    #$ evil = False

    a "When the {i}evil{/i} variable is set to {i}False{/i}, my glasses will look normal."

    a "One last thing I want to mention is that the order of the groups does matter when you write your {b}layeredimage{/b} definitions. The code referring to my glasses is after the {b}group{/b} for my eyes, that way I wear my glasses over my eyes."

    hide example

    return

label tutorial_auto:

    a "Believe it or not though, we can still reduce the number of lines of code being used!"

    show august closedup smile with dissolve

    show example auto_layeredimage

    a "Behold, the power of automatic determination! For image filenames, at least."

    show august blinking happy with dissolve

    a "This acomplishes the same thing as the code I showed you the first time around, but this time we let Ren'Py do the legwork for finding what files correspond to each attribute."

    a "When you do it this way, it is important to note that your filenames should have be organized in a way that Ren'Py can recognize."

    show august smile with dissolve

    a "You may put them in individual subfolders, but remember to give everything a unique name, otherwise the engine may not display the correct image."

    hide example

    a "You don't need to specify \"images/sprites/Augustina/\" or anything like that beforehand when you do this, which is very convenient."

    show august happy evil with dissolve

    a "Believe it or not, we can still do it even more efficiently!"

    show example auto_shortli

    a "This is about as short as it gets. After the {b}group{/b} is defined, we add {b}auto{/b} to the end of it. This tells Ren'Py to find every file that fits into that group, without us having to write which attributes belong to what."

    show august wink regular smile with dissolve

    a "As with the previous method, unique filenames are important in order for this to work."

    a "As they say, a good programmer is a lazy programmer. The less lines of code you need to write, the better."

    show august blinking smile with dissolve

    hide example

    return

label tutorial_animation:

    a "Have you noticed what my eyes have been doing for a while now? I actually do have my eyes animated to make it look like I'm blinking."

    show example animations

    a "Animation and Transformation Language, known as ATL, can be used to animate still images. This blinking animation is composed of three frames in total."

    a "ATL can be used to accomplish quite a bit if you know what you're doing. I won't go too much into it since this isn't the place for it, but you should definitely study ATL to give your project some flair."

    hide example

    a "Since the animation for blinking has been defined in the code, we will have to manually add it to {b}layeredimage{/b}  definition."

    show example li_animated

    a "Lucky for us, it's as simple as putting it down as another {b}attribute{/b}."

    a "You can add as many custom animations as you'd like to your sprites this way."

    hide example

    return

label tutorial_sideimage:
    
    a "Some games add an image of a character near the textbox, usually referred to as a Side Image."

    a "Ren'Py has had a unique way of defining these images for a while now, as well as linking it to another version of the same sprite that appears in the middle of the screen as normal."

    show example sideimage

    au "We also happen to have that for LayeredImages!"

    show august wink smile with dissolve

    au "Notice the {b}LayeredImageProxy{/b} that precedes the image being duplicated and the dimensions of the side image. This makes it so that way any updates to the main sprite is reflected in the side sprite as well."

    au "For example, let me change clothes again."

    hide august with moveoutright

    pause (2)

    show august swimsuit blinking happy with moveinright

    au "See how my side image has also been updated so I'm wearing my swimsuit?"

    hide august with moveoutright

    pause (2)

    show august dress closedup smile regular with moveinright

    hide example

    au "It's a very handy feature to have."

    show example sideimage_name

    au "Be sure to add the corresponding image tag to the speaker's name so that the side image will display properly."

    show august blinking happy with dissolve

    hide example

    return

label demo_dressup:

    a "A lot of players like customizable protagonists. Allowing players to change their player avatar was something that was definitely possible using older methods, but it was very messy and confusing."

    a "It's a little less so using LayeredImage. Want to give it a try?"

    hide august

    call screen dressup_example

    label dressup_game:

        show doll happy with dissolve

        a "Are you done?"

        menu:

            "Yes":

                a "Cool!"

            "No":

                a "Let's get back into it then."

                hide doll

                call screen dressup_example

    show example li_doll

    a "Here's the code for the sprite itself. It's a bit lengthy, but it works."

    a "For the complete dress up screen code, please open {b}dressup.rpy{/b}."

    hide example

    hide doll with moveoutleft

    pause 1.0

    show august jeans blinking smile regular at left with moveinleft

    return