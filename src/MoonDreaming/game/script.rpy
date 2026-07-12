# script.rpy
#
# Entry point only. Character/layout definitions live in characters.rpy and
# layouts.rpy; the actual story is split across script_chapter*.rpy files.
#
# How splitting works: Ren'Py loads *every* .rpy file in the game/ directory,
# so you don't "import" anything. You just define labels in separate files and
# move between them with `call` (returns here afterward) or `jump` (one-way).

###########################################################################################
##MISC DEFINITIONS
###########################################################################################

transform hop:
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

define _scene_show_hide_transition = Dissolve(0.25)
define fadehold = Fade(0.5, 1.0, 0.5)

#############################################################################################

label start:
    call chapter_one

    scene bg houseback
    call chapter_one
    call chapter_two
    call chapter_three
    call chapter_four
    call chapter_five
    call chapter_six
    call chapter_seven
    call chapter_eight
    call chapter_nine
    call chapter_ten
    return

# A looping chapter-select menu. Each choice `call`s a chapter (which returns
# here when it hits `return`), then `jump chapter_select` re-shows the menu.
# Because `call` comes back, the menu stays the table of contents.
label chapter_select:

    menu:

        "1: Intro":
            call chapter_one

        "2: Roommates":
            call chapter_two

        "3: Cafe":
            call chapter_three

        "4: Sophia call":
            call chapter_four

        "5: First group yoga":
            call chapter_five

        "6: A later group class":
            call chapter_six

        "7: Emily & Ana talk about Silvia":
            call chapter_seven

        "8: One on one in yoga studio":
            call chapter_eight

        "9: Rejection":
            call chapter_nine

        "10: Climax":
            call chapter_ten

    # Loop back to the menu after a chapter returns.
    jump chapter_select
