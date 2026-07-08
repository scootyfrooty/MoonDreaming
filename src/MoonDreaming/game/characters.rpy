# characters.rpy
#
# Central place for character definitions and reusable text. Keeping these out
# of the chapter files means the story files stay short and you only edit a
# character's voice/color/layout in one spot.

################################################################################
## Layout 1: ADV (standard bottom textbox)
################################################################################
## These use the built-in "say" screen. Nothing special required.

define e = Character("Eileen", color="#c8ffc8")
define m = Character(None)  # plain narrator (no name)


################################################################################
## Layout 2: NVL (full-screen novel mode)
################################################################################
## Passing `kind=nvl` routes these characters through the built-in "nvl" screen
## instead of the "say" screen. Remember to call `nvl clear` in the script when
## you enter/reset NVL mode.

define a = Character("Ana", kind=nvl, color="#639e52")
define e = Character("Emily", kind=nvl, color="#9e4744")
define s = Character("Silvia", kind=nvl, color="#2b50d7")
define o = Character("Sophia", kind=nvl, color="#747272")
define b = Character("Barista", kind=nvl, color="#747272")
define n = Character(None, kind=nvl)  # NVL narrator (unnamed)


################################################################################
## Layout 3: Cinematic (custom centered overlay)
################################################################################
## `screen="cinematic_say"` binds these characters to the custom say screen
## defined in layouts.rpy. Anything spoken by them renders centered on screen
## with no textbox.

define ca = Character("Ana", screen="cinematic_say", color="#639e52")
define ce = Character("Emily", screen="cinematic_say", color="#9e4744")
define cs = Character("Silvia", screen="cinematic_say", color="#2b50d7")
define co = Character("Sophia",screen="cinematic_say", color="#747272")
define tv = Character ("TV Narrator", screen="cinematic_say", color="#747272")
define cn = Character(None, screen="cinematic_say")  # cinematic narration


################################################################################
## Reusable lorem-ipsum snippets
################################################################################
## Defining longer lines here keeps the chapter files readable and lets you
## reuse the same text in multiple places.

define LOREM_SHORT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
define LOREM_MED = "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation."
define LOREM_LONG = "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
