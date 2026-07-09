# script_chapter1.rpy
#
# Chapter One. Demonstrates Layout 1 (ADV) and swapping to Layout 3 (Cinematic).

label chapter_one:

    # ---- Swap to Layout 3: Cinematic -----------------------------------------
    # No mode switch needed: we just speak with a character bound to the
    # cinematic_say screen (see characters.rpy). The previous ADV window hides
    # automatically because these lines use a different screen.

    cn "Our makeup and our clothes are a mundane armor against a hostile world."

    cn "Leaves less room for others to attack us and get under our tender skin, their criticisms are only of the external shell. Our ugly, strange, true, fleshy selves are safe within."

    cn "And if they kill us anyway, at least we'll be the perfect, beautiful victim. Still safe. Still unknowable."

    cn "But who are we, truly?"

call chapter_two
