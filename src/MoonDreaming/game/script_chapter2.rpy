# script_chapter2.rpy
#
# Chapter Two. Demonstrates Layout 2 (NVL) and swapping back to ADV.

label chapter_two:

    # ---- Swap to Layout 2: NVL (full-screen novel mode) ----------------------
    # `nvl clear` wipes any previous NVL page. NVL characters (kind=nvl) then
    # stack their lines up the screen instead of using the bottom textbox.

    nvl clear

    nm "[LOREM_MED]"

    nk "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    nm "[LOREM_LONG]"

    # Clear the page before continuing so it doesn't overflow.
    nvl clear

    nk "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet."

    nm "Consectetur, adipisci velit, sed quia non numquam eius modi tempora."

    # ---- Swap back to Layout 1: ADV ------------------------------------------
    # `nvl clear` closes out the NVL page; speaking with an ADV character drops
    # us back into the bottom textbox.

    nvl clear

    e "Et harum quidem rerum facilis est et expedita distinctio."

    m "The end."

    return
