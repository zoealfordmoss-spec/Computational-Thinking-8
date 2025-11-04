import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial" "happy","abode", "banal", "charm", "dread", 
             "evoke", "flake", "gloat", "hasty", "incur", "joust", "kudos", "lanky", "mirth", "nudge", 
             "onset", "plume", "quirk", "rouse", "spade", "trust", "unzip", "vexed", "waltz", "xenon", 
             "yield", "zesty", "about", "barge", "cleat", "drone", "ember", "fable", "grain", "hovel", 
             "inane", "jaded", "knack", "lurid", "muted", "niche", "ochre", "prawn", "quiet", "rally", 
             "snarl", "trove", "undue", "vapor", "wager", "xylem", "yacht", "zonal", "braid", "caper", 
             "douse", "fazed", "globs", "lapse", "mower", "nadir", "quash", "stint", "tonic", "vivid", 
             "whelp", "zoned", "bliss", "crumb", "furry", "gecko", "hunch", "latch", "muted", "ravel", 
             "scamp", "stray", "vouch", "whiff", "zilch", "bravo", "crisp", "forge", "ghoul", "hymns", 
             "jaded", "lunge", "mirth", "pious", "quill", "shade", "slick", "swarm", "tepid", "upset", 
             "verve", "whine", "yoked", "zonal", "apple", "brave", "charm", "dream", "eagle", "fancy", 
             "grace", "happy", "ideal", "jolly", "kind", "lucky", "noble", "ocean", "peace", "quick", 
             "robin", "sunny", "tiger", "unity", "vivid", "whale", "xenon", "youth", "zebra", "angel", 
             "bliss", "candy", "daisy", "earth", "fairy", "gem", "heart", "ivory", "jazz", "kite", 
             "lemon", "magic", "north", "olive", "prism", "quiet", "rose", "smile", "spark", "trust", 
             "urban", "valor", "water", "yelp", "zest", "amber", "blast", "crate", "delta", "frost", 
             "grape", "haste", "inked", "joint", "knack", "larch", "marsh", "neigh", "oasis", "plume", 
             "quill", "relay", "shore", "spice", "trade", "usher", "vista", "witty", "xylos", "yacht", 
             "zippy", "aspic", "blimp", "clink", "drone", "elude", "flask", "gloom", "hound", "image", 
             "jaded", "kneed", "lever", "mural", "nadir", "orate", "press", "quack", "rover", "shade",
               "sling", "tardy", "udder", "valid", "whale", "xerox", "yarn", "zonal", "abyss", "barge", 
               "chide", "deter", "eerie", "fluke", "gaffe", "harsh", "inert", "juice", "kneel", "lipid", 
               "morph", "nylon", "ovate", "purge", "quire", "roost", "spine", "sting", "thump", "ultra", 
               "vogue", "wrath", "xerus", "yield", "zonal", "acorn", "bland", "clang", "ditch", "emote", 
               "fable", "ghost", "humor", "icing", "jaunt", "knave", "lease", "moist", "navel", "ozone", 
               "pique", "quirk", "rusty", "slate", "stomp", "twang", "unify", "vowel", "whelp", "xylol", 
               "yummy", "zesty", "agile", "bleed", "clove", "dingo", "epoch", "faint", "gloat", "hairy", 
               "irked", "joker", "knoll", "lanky", "mocha", "nifty", "opium", "prong", "quail", "sassy", 
               "sniff", "troll", "unlit", "vying", "whine", "xylem", "yowza", "zygote", "alloy", "blush", 
               "clown", "dizzy", "equal", "feast", "gorge", "helix", "irony", "joust", "knobs", "lurid", 
               "mucky", "noble", "organ", "proxy", "quota", "scamp", "slurp", "trunk", "unzip", "vixen", 
               "whoop", "xenon", "yodel", "zonal", "audio", "boast", "cower", "doubt", "exalt", "fetch", 
               "grime", "hinge", "indie", "judge", "knoll", "limit", "mango", "nooks", "onset", "punky", 
               "quest", "scorn", "snore", "tutor", "unlit", "valor", "worry", "xerox", "young", "zonal", 
               "ample", "bacon", "couch", "donor", "elves", "fluid", "group", "haste", "image", "jaded", 
               "knife", "light", "motor", "nylon", "outer", "pound", "quilt", "reign", "slide", "spire", 
               "twist", "upper", "verse", "wagon", "xray", "yeast", "zippy", "awake", "bonus", "crave", 
               "drive", "entry", "flame", "golly", "house", "inner", "jelly", "knead", "lucky", "mouse", 
               "night", "ocean", "plant", "quiet", "route", "small", "stair", "today", "under", "voice", 
               "write", "xylos", "yacht", "zesty" "agony", "aisle", "alter", "amend", "angle", "ankle", "antic", "anvil", "apron", "aroma",
"baste", "batch", "baton", "bellow", "blurt", "bonus", "bound", "bowel", "brace", "brisk",
"cable", "camel", "cater", "caulk", "chant", "chasm", "chime", "clamp", "clasp", "cloak",
"cleft", "climb", "clone", "cough", "cramp", "crate", "creek", "creep", "crimp", "crown",
"crude", "crush", "curio", "curse", "curve", "dairy", "daisy", "dealt", "debut", "defer",
"delta", "depth", "dilly", "dingo", "ditto", "dodge", "dogma", "doing", "donkey", "donor",
"douse", "dowel", "dozen", "draft", "drain", "drama", "dream", "dress", "drier", "drift",
"drill", "drink", "drive", "drool", "drown", "druid", "dryer", "duvet", "dwarf", "eager",
"eagle", "eaten", "ebony", "eclat", "edger", "eerie", "eight", "eject", "elbow", "elder",
"elect", "elite", "elope", "embed", "ember", "emcee", "empty", "enact", "endow", "enjoy",
"ensue", "entry", "epoch", "equal", "equip", "erase", "error", "essay", "ethos", "every",
"exalt", "excel", "exert", "exist", "expel", "exude", "fable", "facet", "fauna", "feast",
"fetal", "fetch", "fewer", "fiber", "field", "fiery", "fifth", "fifty", "filed", "filly",
"filth", "final", "finch", "first", "fixed", "flair", "flake", "flame", "flask", "flock",
"flood", "floor", "flour", "fluid", "fluke", "flung", "flush", "flute", "focus", "force",
"forge", "forth", "forty", "forum", "found", "frame", "fraud", "fresh", "frisk", "froth",
"fruit", "fully", "fungi", "fussy", "fuzzy", "gaily", "gamma", "gaunt", "gauze", "gavel",
"gecko", "gland", "gleam", "gloat", "glyph", "gnome", "godly", "golem", "goose", "gorge",
"grace", "grade", "graft", "grain", "grand", "grant", "grape", "graph", "grass", "grate",
"great", "greed", "greek", "green", "grill", "grime", "gripe", "groan", "groom", "gross",
"group", "grove", "grown", "guard", "guest", "guide", "guilt", "hairy", "halve", "happy",
"hardy", "haste", "haunt", "haven", "hazel", "heaps", "heard", "heart", "heave", "heavy",
"hence", "herds", "hiker", "hinge", "hippo", "hoard", "hobby", "homer", "honey", "horde",
"horse", "hotel", "house", "hover", "howdy", "human", "humid", "humor", "hurry", "husky",
"icily", "idiot", "igloo", "iliac", "image", "inane", "incur", "index", "inept", "inert",
"ingot", "inlet", "inner", "input", "irony", "irate", "issue", "ivory", "jaded", "jaunt",
"jelly", "joint", "joker", "jolly", "joust", "judge", "juice", "jumps", "kebab", "khaki",
"kiosk", "knack", "knead", "knife", "knock", "known", "koala", "kudos", "label", "labor",
"lanky", "lapse", "laser", "later", "latch", "laugh", "layer", "learn", "lease", "least",
"leave", "legal", "level", "levee", "libel", "light", "limit", "lined", "linen", "lipid",
"lithe", "livid", "logic", "locus", "lofty", "loner", "loose", "louse", "lower", "loyal",
"lucky", "lunch", "lunge", "lurid", "macho", "magic", "maize", "major", "maker", "mango",
"manic", "march", "marge", "marsh", "mason", "match", "mayor", "mealy", "meant", "media",
"mercy", "metal", "metro", "might", "minor", "mirth", "miser", "model", "moist", "moose",
"moral", "motif", "motor", "mount", "mouse", "mouth", "movie", "mower", "mucky", "muddy",
"mural", "music", "muted", "nadir", "naive", "natal", "navel", "neigh", "nerve", "never",
"niche", "night", "nifty", "noise", "north", "novel", "nurse", "nylon", "oasis", "ocean",
"ochre", "octet", "odium", "offer", "often", "okapi", "olive", "omega", "onion", "onset",
"opera", "orbit", "order", "organ", "other", "ought", "outer", "ovate", "ozone", "pager",
"paint", "panic", "panel", "paper", "parch", "parry", "party", "pause", "peace", "peach",
"pearl", "pedal", "pelted", "penal", "penis", "penny", "perch", "peril", "petty", "phase",
"phone", "photo", "piano", "piece", "pilot", "pique", "pitch", "pivot", "place", "plaid",
"plain", "plane", "plank", "plant", "plate", "plume", "plump", "poesy", "point", "poise",
"poker", "polar", "polka", "porch", "pound", "power", "prawn", "pride", "prime", "primp",
"print", "prior", "prize", "proof", "proud", "prove", "proxy", "prune", "pudgy", "pulse",
"pumice", "punch", "pupil", "purge", "pussy", "quack", "quaff", "quail", "quake", "qualm",
"query", "quest", "quiet", "quill", "quilt", "quite", "quota", "quote", "rabid", "radio",
"ragged", "raise", "rally", "ramen", "ranch", "range", "ranch", "rapid", "ratio", "raven",
"ready", "rebus", "recap", "recur", "refer", "refit", "regal", "reign", "relax", "relay",
"relic", "remit", "remix", "reply", "resin", "retch", "retro", "revel", "rhyme", "ridge",
"right", "rival", "river", "robot", "robin", "rodeo", "rogue", "roman", "roost", "rough",
"round", "route", "royal", "ruddy", "ruler", "rural", "rusty", "saber", "sable", "sacks",
"saint", "salad", "salon", "salty", "sassy", "sauce", "saute", "scald", "scale", "scamp",
"scans", "scare", "scarf", "scent", "scion", "scoff", "scold", "scoop", "scope", "score",
"scour", "scout", "scowl", "scram", "scuba", "seats", "sedan", "seeds", "seize", "sells",
"sense", "serum", "serve", "seven", "sever", "shack", "shade", "shaft", "shaky", "shale",
"shall", "shame", "shape", "shard", "share", "shark", "sharp", "shave", "sheaf", "shear",
"sheds", "sheen", "sheep", "sheer", "sheet", "shelf", "shell", "shift", "shine", "shiny",
"ships", "shirt", "shoal", "shock", "shoes", "shone", "shook", "shoot", "shops", "shore",
"shorn", "short", "shots", "shout", "shove", "shown", "shows", "showy", "shred", "shrub",
"shunt", "shush", "sided", "sides", "siege", "sieve", "sight", "sigma", "signs", "silky",
"silly", "since", "sinew", "singe", "sinks", "siren", "sixth", "sixty", "sized", "sizes",
"skate", "skier", "skies", "skill", "skimp", "skins", "skips", "skirt", "skull", "slabs",
"slack", "slain", "slang", "slant", "slaps", "slash", "slate", "slave", "sleek", "sleep",
"sleet", "slice", "slick", "slide", "slimy", "sling", "slope", "sloth", "slump", "slurp",
"small", "smart", "smash", "smear", "smell", "smile", "smirk", "smoke", "smoky", "snarl",
"sneer", "sniff", "snore", "snout", "snowy", "soaps", "sober", "socks", "solar", "solid",
"solve", "sonar", "sorry", "sound", "south", "space", "spade", "spare", "spark", "spasm",
"speak", "speed", "spell", "spend", "spent", "spice", "spill", "spine", "spire", "split",
"spoil", "spoke", "sport", "spray", "spree", "squid", "stack", "staff", "stage", "stain",
"stair", "stake", "stamp", "stand", "stare", "start", "state", "stats", "staid", "steal",
"steam", "steel", "steer", "stiff", "still", "sting", "stint", "stock", "stole", "stone",
"stood", "store", "storm", "story", "stove", "strap", "straw", "stray", "strip", "stump",
"subtle", "suite", "sunny", "super", "swamp", "swear", "sweep", "sweet", "swell", "swift",
"swing", "swirl", "syrup", "table", "tango", "taper", "tardy", "tawny", "taxes", "teach",
"tease", "teeth", "tempo", "tendy", "tenor", "tenet", "terse", "thank", "their", "theme",
"there", "these", "thief", "thigh", "thing", "think", "third", "thorn", "those", "three",
"threw", "throb", "throw", "thumb", "thump", "thyme", "tibia", "tidal", "tiger", "tight",
"tiled", "timed", "timer", "timid", "title", "toast", "today", "token", "tomeo", "tonic",
"topic", "total", "towed", "tower", "towns", "toxic", "trace", "track", "trade", "trail",
"train", "trait", "tramp", "trans", "trap", "trash", "tread", "treat", "trend", "trial",
"tribe", "trick", "troop", "truck", "truly", "trunk", "trust", "truth", "tuber", "tulip",
"tummy", "tutor", "tweed", "twice", "twist", "typed", "typo", "udder", "ultra", "umbra",
"unfit", "unify", "union", "unite", "unity", "upper", "upset", "urban", "usage", "usual",
"usurp", "vague", "valid", "valor", "value", "valve", "vapor", "vegan", "venom", "verse",
"verve", "vicar", "video", "vigil", "vigor", "viral", "virus", "visit", "visor", "vista",
"vital", "vivid", "vocal", "vogue", "voice", "vowed", "vowel", "wager", "wagon", "waist",
"waive", "waltz", "waste", "watch", "water", "wedge", "weigh", "weird", "welsh", "whale",
"wharf", "wheat", "wheel", "whelp", "where", "while", "whine", "whiny", "whirl", "white",
"whole", "whoop", "whore", "whose", "wicked", "widen", "wider", "widow", "width", "wield",
"wight", "willy", "wince", "winch", "windy", "wiped", "wired", "wiser", "wiser", "wispy",
"witch", "witty", "woman", "women", "worry", "worse", "worst", "worth", "wound", "woven",
"wraith", "wrath", "wreck", "write", "wrong", "wrote", "xenon", "xerox", "xylem", "yacht",
"yappy", "yappy", "yeast", "yodel", "young", "youth", "yummy", "zebra", "zesty", "zilch",
"zippy", "zonal", "zoned", "zonked", "zombi"]




hidden_word = random.choice(word_list)
print("ZODLE:")



# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"


       
    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")