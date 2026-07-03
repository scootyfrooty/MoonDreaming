# script_chapter1.rpy
#
# Chapter One. Demonstrates Layout 1 (ADV) and swapping to Layout 3 (Cinematic).

label chapter_one:

    # ---- Layout 1: ADV (standard bottom textbox) -----------------------------
    # Normal characters render through the built-in "say" screen.

    e "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    m "[LOREM_MED]"

    e "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris."

    # ---- Swap to Layout 3: Cinematic -----------------------------------------
    # No mode switch needed: we just speak with a character bound to the
    # cinematic_say screen (see characters.rpy). The previous ADV window hides
    # automatically because these lines use a different screen.

    cm "[LOREM_SHORT]"

    ce "Excepteur sint occaecat cupidatat non proident."

    cm "[LOREM_LONG]"

    # ---- Swap back to Layout 1: ADV ------------------------------------------
    # Speak with an ADV character again and the bottom textbox returns.

    e "Sed ut perspiciatis unde omnis iste natus error sit voluptatem."

    m "That was chapter one."

    return
