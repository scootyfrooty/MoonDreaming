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
    call chapter_one from _call_chapter_one
