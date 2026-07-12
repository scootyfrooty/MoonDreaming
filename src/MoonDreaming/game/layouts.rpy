# layouts.rpy
#
# Custom text layout(s). Layout 1 (ADV) and Layout 2 (NVL) are provided by the
# stock screens.rpy, so only the third "cinematic" layout needs custom code.

# Layout 1: ADV (ADVENTURE) is the "generic" visual novel layout. Text box on bottom
# Layout 2: NVL (NOVEL) is left aligned, stacking dialouge
# Layout 3: Cinematic is full screen

################################################################################
## Layout 3: Cinematic say screen
################################################################################
## A say screen must contain a text displayable with id "what" so that Ren'Py
## can drive slow text / click-to-continue. Optionally a text with id "who" for
## the speaker's name. Everything else is up to you.

transform cinematic_appear:
    alpha 0.0
    linear 0.4 alpha 1.0

screen cinematic_say(who, what):
    style_prefix "cinematic"
    zorder 100

    ## Full-screen dim behind the text.
    add "#0000004b"

    frame:
        at cinematic_appear

        vbox:
            if who is not None:
                text who id "who"
            text what id "what"
            


################################################################################
## Cinematic styles
################################################################################

style cinematic_frame is empty:
    xfill True
    yfill True

style cinematic_vbox:
    xfill True
    yalign 0.4
    spacing 10

style cinematic_who:
    size 45
    text_align 1
    color "#bab0bf"
    outlines [(2, "#000000", 0, 0)]

style cinematic_what:
    xmaximum 1200
    text_align 0.5
    xalign 0.5
    size 55
    line_leading 12
    color "#bab0bf"
    outlines [(2, "#000000", 0, 0)]
