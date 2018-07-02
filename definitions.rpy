# Declare images used by this game. We can use the new LayeredImage
# function to create our sprites.

#begin basic_layeredimage
init -1:

    $ evil = False            

layeredimage augustina:

    always:
        "augustina_base"

    group outfit:

        attribute dress:
            "augustina_outfit_dress"

        attribute jeans:
            "augustina_outfit_jeans"

    group eyes:

        attribute open default:
            "augustina_eyes_open"
            #default True

        attribute wink:
            "augustina_eyes_wink"

    group eyebrows:

        attribute normal default:
            "augustina_eyebrows_normal"

        attribute oneup:
            "augustina_eyebrows_oneup"

    group mouth:

        #pos (100, 100)

        attribute smile default:
            "augustina_mouth_smile"

        attribute happy:
            "augustina_mouth_happy"

    if evil:
        "augustina_glasses_evil"

    else:
        "augustina_glasses"
#end basic_layeredimage

#begin auto_layeredimage
layeredimage augustina:

    always:
        "augustina_base"

    group outfit:
        attribute dress
        attribute jeans

    group eyes:
        attribute open default
        attribute wink

    group eyebrows:
        attribute normal default
        attribute oneup

    group mouth:
        #pos (100, 100)
        attribute smile default
        attribute happy

    if evil:
        "augustina_glasses_evil"
    else:
        "augustina_glasses"
#end auto_layeredimage

#begin auto_shortli
layeredimage augustina:

    always "augustina_base"

    group outfit auto

    group eyes auto:
        attribute open default

    group eyebrows auto:
        attribute normal default

    group mouth auto:
        #pos (100, 100)
        attribute smile default

    if evil:
        "augustina_glasses_evil"
    else:
        "augustina_glasses"
#end auto_shortli

#begin li_animated
layeredimage august:

    always "august_base"

    group outfit auto

    group eyes auto:
        attribute open default

        attribute blinking:
            "blinking"

    group eyebrows auto:
        attribute normal default

    group mouth auto:
        attribute smile default

    group glasses auto

    group emotion auto
#end li_animated

#begin animations
image blinking:

    "august_eyes_open"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "august_eyes_half"
    .1
    "august_eyes_closeddown"
    .1
    "august_eyes_half"
    .1
    repeat

#end animations

#begin li_doll
layeredimage doll:

    always "doll_base"

    # possible outfits

    if outfit == 1:

        "doll_outfit_swimsuit"

    elif outfit == 2:

        "doll_outfit_jeans"

    elif outfit == 3:

        "doll_outfit_dress"

    group eyes auto:
        attribute open default

    group eyebrows auto:
        attribute normal default

    group mouth auto:
        attribute smile default

    if glasses == 1:

        "doll_glasses_purple"

    elif glasses == 2:

        "doll_glasses_pink"

    elif glasses == 3:

        "doll_glasses_blue"

#end li_doll

#begin sideimage
image side august = LayeredImageProxy("august", Transform(crop=(0, 0, 497, 400), zoom=0.7, xoffset=-50))
#end sideimage

#begin sideimage_name
define au = Character("Augustina", image="august")
#end sideimage_name