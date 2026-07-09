# script.rpy
#
# Entry point only. Character/layout definitions live in characters.rpy and
# layouts.rpy; the actual story is split across script_chapter*.rpy files.
#
# How splitting works: Ren'Py loads *every* .rpy file in the game/ directory,
# so you don't "import" anything. You just define labels in separate files and
# move between them with `call` (returns here afterward) or `jump` (one-way).

label start:

    scene bg room
    show eileen happy

    jump chapter_select


# A looping chapter-select menu. Each choice `call`s a chapter (which returns
# here when it hits `return`), then `jump chapter_select` re-shows the menu.
# Because `call` comes back, the menu stays the table of contents.
label chapter_select:

    menu:
        m "Which chapter would you like to read?"

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

        "That's enough for now.":
            return

    # Loop back to the menu after a chapter returns.
    jump chapter_select
