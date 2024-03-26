from typing import Union

import os

from dotenv import load_dotenv

load_dotenv()


def str2bool(v):
    if isinstance(v, bool):
        return v
    if not v or not isinstance(v, str):
        return False
    return v.lower() in ("yes", "true", "t", "1")


TURN_OFF_PAREA_LOGGING = str2bool(os.getenv("TURN_OFF_PAREA_LOGGING", False))

PAREA_OS_ENV_EXPERIMENT_UUID = "_PAREA_EXPERIMENT_UUID"
PAREA_DVC_DIR = ".parea"
PAREA_DVC_METRICS_FILE = str(os.path.join(PAREA_DVC_DIR, "metrics.json"))
PAREA_DVC_YAML_FILE = str(os.path.join(PAREA_DVC_DIR, "dvc.yaml"))

CHUNK_DONE_SENTINEL = "data: [DONE]"

OPENAI_MODEL_INFO: dict[str, dict[str, Union[float, int, dict[str, int]]]] = {
    "gpt-3.5-turbo-0301": {
        "prompt": 1.5,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 4096},
    },
    "gpt-3.5-turbo-0613": {
        "prompt": 1.5,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 4096},
    },
    "gpt-3.5-turbo-16k": {
        "prompt": 3.0,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 16385, "max_prompt_tokens": 16385},
    },
    "gpt-3.5-turbo-16k-0301": {
        "prompt": 3.0,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 16385, "max_prompt_tokens": 16385},
    },
    "gpt-3.5-turbo-16k-0613": {
        "prompt": 3.0,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 16385, "max_prompt_tokens": 16385},
    },
    "gpt-3.5-turbo-1106": {
        "prompt": 1.0,
        "completion": 2.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 4096},
    },
    "gpt-3.5-turbo-0125": {
        "prompt": 0.5,
        "completion": 2.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 16385},
    },
    "gpt-3.5-turbo": {
        "prompt": 0.5,
        "completion": 2.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 16385},
    },
    "gpt-3.5-turbo-instruct": {
        "prompt": 1.5,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 4096},
    },
    "gpt-4": {
        "prompt": 30.0,
        "completion": 60.0,
        "token_limit": {"max_completion_tokens": 8192, "max_prompt_tokens": 8192},
    },
    "gpt-4-0314": {
        "prompt": 30.0,
        "completion": 60.0,
        "token_limit": {"max_completion_tokens": 8192, "max_prompt_tokens": 8192},
    },
    "gpt-4-0613": {
        "prompt": 30.0,
        "completion": 60.0,
        "token_limit": {"max_completion_tokens": 8192, "max_prompt_tokens": 8192},
    },
    "gpt-4-32k": {
        "prompt": 60.0,
        "completion": 120.0,
        "token_limit": {"max_completion_tokens": 32768, "max_prompt_tokens": 32768},
    },
    "gpt-4-32k-0314": {
        "prompt": 60.0,
        "completion": 120.0,
        "token_limit": {"max_completion_tokens": 32768, "max_prompt_tokens": 32768},
    },
    "gpt-4-32k-0613": {
        "prompt": 60.0,
        "completion": 120.0,
        "token_limit": {"max_completion_tokens": 32768, "max_prompt_tokens": 32768},
    },
    "gpt-4-vision-preview": {
        "prompt": 30.0,
        "completion": 60.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 128000},
    },
    "gpt-4-turbo-preview": {
        "prompt": 10.0,
        "completion": 30.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 128000},
    },
    "gpt-4-1106-preview": {
        "prompt": 10.0,
        "completion": 30.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 128000},
    },
    "gpt-4-0125-preview": {
        "prompt": 10.0,
        "completion": 30.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 128000},
    },
}
AZURE_MODEL_INFO: dict[str, dict[str, Union[float, int, dict[str, int]]]] = {
    "gpt-35-turbo": {
        "prompt": 1.5,
        "completion": 2.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 4096},
    },
    "gpt-35-turbo-0301": {
        "prompt": 1.5,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 4096},
    },
    "gpt-35-turbo-0613": {
        "prompt": 1.5,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 4096},
    },
    "gpt-35-turbo-16k": {
        "prompt": 3.0,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 16384, "max_prompt_tokens": 16384},
    },
    "gpt-35-turbo-16k-0301": {
        "prompt": 3.0,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 16384, "max_prompt_tokens": 16384},
    },
    "gpt-35-turbo-16k-0613": {
        "prompt": 3.0,
        "completion": 4.0,
        "token_limit": {"max_completion_tokens": 16384, "max_prompt_tokens": 16384},
    },
    "gpt-4": {
        "prompt": 30.0,
        "completion": 60.0,
        "token_limit": {"max_completion_tokens": 8192, "max_prompt_tokens": 8192},
    },
    "gpt-4-0314": {
        "prompt": 30.0,
        "completion": 60.0,
        "token_limit": {"max_completion_tokens": 8192, "max_prompt_tokens": 8192},
    },
    "gpt-4-0613": {
        "prompt": 30.0,
        "completion": 60.0,
        "token_limit": {"max_completion_tokens": 8192, "max_prompt_tokens": 8192},
    },
    "gpt-4-32k": {
        "prompt": 60.0,
        "completion": 120.0,
        "token_limit": {"max_completion_tokens": 32768, "max_prompt_tokens": 32768},
    },
    "gpt-4-32k-0314": {
        "prompt": 60.0,
        "completion": 120.0,
        "token_limit": {"max_completion_tokens": 32768, "max_prompt_tokens": 32768},
    },
    "gpt-4-32k-0613": {
        "prompt": 60.0,
        "completion": 120.0,
        "token_limit": {"max_completion_tokens": 32768, "max_prompt_tokens": 32768},
    },
    "gpt-4-1106-preview": {
        "prompt": 10.0,
        "completion": 20.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 128000},
    },
    "gpt-4-vision": {
        "prompt": 10.0,
        "completion": 30.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 128000},
    },
    "gpt-35-turbo-instruct": {
        "prompt": 10.0,
        "completion": 30.0,
        "token_limit": {"max_completion_tokens": 4096, "max_prompt_tokens": 128000},
    },
}

instant_pricing = {"prompt": 1.63, "completion": 5.51}
claude_pricing = {"prompt": 8.00, "completion": 24.00}
ANTHROPIC_MODEL_INFO: dict[str, dict[str, Union[float, int, dict[str, float]]]] = {
    "claude-instant-1.1": {
        "token_limit": {
            "max_prompt_tokens": 9000,
            "max_completion_tokens": 4096,
        },
        **instant_pricing,
    },
    "claude-instant-1": {
        "token_limit": {
            "max_prompt_tokens": 100000,
            "max_completion_tokens": 4096,
        },
        **instant_pricing,
    },
    "claude-instant-1.2": {
        "token_limit": {
            "max_prompt_tokens": 100000,
            "max_completion_tokens": 4096,
        },
        **instant_pricing,
    },
    "claude-instant-1-100k": {
        "token_limit": {
            "max_prompt_tokens": 100000,
            "max_completion_tokens": 4096,
        },
        **instant_pricing,
    },
    "claude-instant-1.1-100k": {
        "token_limit": {
            "max_prompt_tokens": 100000,
            "max_completion_tokens": 4096,
        },
        **instant_pricing,
    },
    "claude-1": {
        "token_limit": {
            "max_prompt_tokens": 9000,
            "max_completion_tokens": 4096,
        },
        **claude_pricing,
    },
    "claude-2": {
        "token_limit": {
            "max_prompt_tokens": 100000,
            "max_completion_tokens": 4096,
        },
        **claude_pricing,
    },
    "claude-1-100k": {
        "token_limit": {
            "max_prompt_tokens": 100000,
            "max_completion_tokens": 4096,
        },
        **claude_pricing,
    },
    "claude-1.2": {
        "token_limit": {
            "max_prompt_tokens": 9000,
            "max_completion_tokens": 4096,
        },
        **claude_pricing,
    },
    "claude-1.3": {
        "token_limit": {
            "max_prompt_tokens": 9000,
            "max_completion_tokens": 4096,
        },
        **claude_pricing,
    },
    "claude-1.3-100k": {
        "token_limit": {
            "max_prompt_tokens": 100000,
            "max_completion_tokens": 4096,
        },
        **claude_pricing,
    },
    "claude-2.1": {
        "token_limit": {
            "max_prompt_tokens": 200000,
            "max_completion_tokens": 4096,
        },
        **claude_pricing,
    },
    "claude-3-opus-20240229": {
        "token_limit": {
            "max_prompt_tokens": 200000,
            "max_completion_tokens": 4096,
        },
        "prompt": 15.00,
        "completion": 75.00,
    },
    "claude-3-sonnet-20240229": {
        "token_limit": {"max_prompt_tokens": 200000, "max_completion_tokens": 4096},
        "prompt": 3.00,
        "completion": 15.00,
    },
    "claude-3-haiku-20240307": {
        "token_limit": {"max_prompt_tokens": 200000, "max_completion_tokens": 4096},
        "prompt": 0.25,
        "completion": 1.25,
    },
}
ALL_NON_AZURE_MODELS_INFO = {**OPENAI_MODEL_INFO, **ANTHROPIC_MODEL_INFO}

NOUNS = (
    "abac",
    "abbs",
    "aces",
    "acid",
    "acne",
    "acre",
    "acts",
    "ados",
    "adze",
    "afro",
    "agas",
    "aged",
    "ages",
    "agio",
    "agma",
    "airs",
    "airt",
    "aits",
    "akes",
    "alap",
    "albs",
    "alga",
    "ally",
    "alto",
    "amah",
    "ambo",
    "amie",
    "amyl",
    "ankh",
    "apex",
    "aqua",
    "arcs",
    "areg",
    "aria",
    "aril",
    "arks",
    "army",
    "auks",
    "aune",
    "aura",
    "awls",
    "awns",
    "axon",
    "azan",
    "baby",
    "bade",
    "bael",
    "bags",
    "bait",
    "ball",
    "banc",
    "bang",
    "bani",
    "barb",
    "bark",
    "bate",
    "bats",
    "bawl",
    "beak",
    "bean",
    "beep",
    "belt",
    "berk",
    "beth",
    "bias",
    "bice",
    "bids",
    "bind",
    "bise",
    "bish",
    "bite",
    "boar",
    "boat",
    "body",
    "boff",
    "bold",
    "boll",
    "bolo",
    "bomb",
    "bond",
    "book",
    "boor",
    "boot",
    "bort",
    "bosk",
    "bots",
    "bott",
    "bout",
    "bras",
    "bree",
    "brig",
    "brio",
    "buck",
    "buhl",
    "bump",
    "bunk",
    "bunt",
    "buoy",
    "byes",
    "byte",
    "cane",
    "cant",
    "caps",
    "care",
    "cart",
    "cats",
    "cedi",
    "ceps",
    "cere",
    "chad",
    "cham",
    "chat",
    "chay",
    "chic",
    "chin",
    "chis",
    "chiv",
    "choc",
    "chow",
    "chum",
    "ciao",
    "cigs",
    "clay",
    "clip",
    "clog",
    "coal",
    "coat",
    "code",
    "coed",
    "cogs",
    "coho",
    "cole",
    "cols",
    "colt",
    "conk",
    "cons",
    "cony",
    "coof",
    "cook",
    "cool",
    "coos",
    "corm",
    "cors",
    "coth",
    "cows",
    "coze",
    "crag",
    "craw",
    "cree",
    "crib",
    "cuds",
    "cull",
    "cult",
    "curb",
    "curn",
    "curs",
    "cusp",
    "cuss",
    "cwms",
    "cyma",
    "cyst",
    "dabs",
    "dado",
    "daff",
    "dais",
    "daks",
    "damn",
    "dams",
    "darg",
    "dart",
    "data",
    "dawk",
    "dawn",
    "daws",
    "daze",
    "dean",
    "debs",
    "debt",
    "deep",
    "dees",
    "dele",
    "delf",
    "dent",
    "deys",
    "dhow",
    "digs",
    "dirk",
    "dita",
    "diva",
    "divs",
    "doek",
    "doge",
    "dogs",
    "dogy",
    "dohs",
    "doit",
    "dole",
    "doll",
    "dolt",
    "dona",
    "dook",
    "door",
    "dops",
    "doss",
    "doxy",
    "drab",
    "drop",
    "drum",
    "duad",
    "duct",
    "duff",
    "duke",
    "dunk",
    "dunt",
    "ears",
    "ease",
    "eggs",
    "eild",
    "emeu",
    "emus",
    "envy",
    "epha",
    "eric",
    "erns",
    "esne",
    "esse",
    "ewes",
    "expo",
    "eyas",
    "eyot",
    "eyry",
    "fare",
    "farl",
    "farm",
    "feds",
    "feel",
    "fees",
    "feme",
    "fess",
    "fibs",
    "fids",
    "fils",
    "firm",
    "fish",
    "flab",
    "flap",
    "flea",
    "flew",
    "flex",
    "flip",
    "flit",
    "flus",
    "flux",
    "foil",
    "fond",
    "food",
    "fool",
    "ford",
    "fore",
    "frit",
    "friz",
    "froe",
    "funs",
    "furl",
    "fuss",
    "fuzz",
    "gaby",
    "gaff",
    "gale",
    "gang",
    "gaol",
    "gape",
    "gash",
    "gaur",
    "gaze",
    "gear",
    "genu",
    "gest",
    "geum",
    "ghat",
    "gigs",
    "gimp",
    "gird",
    "girl",
    "glee",
    "glen",
    "glia",
    "glop",
    "gnat",
    "goad",
    "goaf",
    "gobs",
    "gonk",
    "good",
    "goos",
    "gore",
    "gram",
    "gray",
    "grig",
    "grip",
    "grot",
    "grub",
    "gude",
    "gula",
    "gulf",
    "guns",
    "gust",
    "gyms",
    "gyro",
    "hack",
    "haet",
    "hajj",
    "hake",
    "half",
    "halm",
    "hard",
    "harl",
    "hask",
    "hate",
    "he'd",
    "heck",
    "heel",
    "heir",
    "help",
    "hems",
    "here",
    "hill",
    "hips",
    "hits",
    "hobo",
    "hock",
    "hogs",
    "hold",
    "holy",
    "hood",
    "hoot",
    "hope",
    "horn",
    "hose",
    "hour",
    "hows",
    "huck",
    "hugs",
    "huia",
    "hulk",
    "hull",
    "hunk",
    "hunt",
    "huts",
    "hymn",
    "ibex",
    "ices",
    "iglu",
    "impi",
    "inks",
    "inti",
    "ions",
    "iota",
    "iron",
    "jabs",
    "jags",
    "jake",
    "jass",
    "jato",
    "jaws",
    "jean",
    "jeer",
    "jerk",
    "jest",
    "jiao",
    "jigs",
    "jill",
    "jinn",
    "jird",
    "jive",
    "jock",
    "joey",
    "jogs",
    "joss",
    "jota",
    "jots",
    "juba",
    "jube",
    "judo",
    "jump",
    "junk",
    "jura",
    "juts",
    "jynx",
    "kago",
    "kail",
    "kaka",
    "kale",
    "kana",
    "keek",
    "keep",
    "kefs",
    "kegs",
    "kerf",
    "kern",
    "keys",
    "kibe",
    "kick",
    "kids",
    "kifs",
    "kill",
    "kina",
    "kind",
    "kine",
    "kite",
    "kiwi",
    "knap",
    "knit",
    "koas",
    "kobs",
    "kyat",
    "lack",
    "lahs",
    "lair",
    "lama",
    "lamb",
    "lame",
    "lats",
    "lava",
    "lays",
    "leaf",
    "leak",
    "leas",
    "lees",
    "leks",
    "leno",
    "libs",
    "lich",
    "lick",
    "lien",
    "lier",
    "lieu",
    "life",
    "lift",
    "limb",
    "line",
    "link",
    "linn",
    "lira",
    "loft",
    "loge",
    "loir",
    "long",
    "loof",
    "look",
    "loot",
    "lore",
    "loss",
    "lots",
    "loup",
    "love",
    "luce",
    "ludo",
    "luke",
    "lulu",
    "lure",
    "lush",
    "magi",
    "maid",
    "main",
    "mako",
    "male",
    "mana",
    "many",
    "mart",
    "mash",
    "mast",
    "mate",
    "math",
    "mats",
    "matt",
    "maul",
    "maya",
    "mays",
    "meal",
    "mean",
    "meed",
    "mela",
    "mene",
    "mere",
    "merk",
    "mesh",
    "mete",
    "mice",
    "milo",
    "mime",
    "mina",
    "mine",
    "mirk",
    "miss",
    "mobs",
    "moit",
    "mold",
    "molt",
    "mome",
    "moms",
    "monk",
    "moot",
    "mope",
    "more",
    "morn",
    "mows",
    "moxa",
    "much",
    "mung",
    "mush",
    "muss",
    "myth",
    "name",
    "nard",
    "nark",
    "nave",
    "navy",
    "neck",
    "newt",
    "nibs",
    "nims",
    "nine",
    "nock",
    "noil",
    "noma",
    "nosh",
    "nowt",
    "nuke",
    "oafs",
    "oast",
    "oats",
    "obit",
    "odor",
    "okra",
    "omer",
    "oner",
    "ones",
    "orcs",
    "ords",
    "orfe",
    "orle",
    "ossa",
    "outs",
    "over",
    "owls",
    "pail",
    "pall",
    "palp",
    "pams",
    "pang",
    "pans",
    "pant",
    "paps",
    "pate",
    "pats",
    "paws",
    "pear",
    "peba",
    "pech",
    "pecs",
    "peel",
    "peer",
    "pees",
    "pein",
    "peri",
    "phon",
    "pice",
    "pita",
    "pith",
    "play",
    "plop",
    "plot",
    "plow",
    "plug",
    "plum",
    "polo",
    "pomp",
    "pond",
    "pons",
    "pony",
    "poof",
    "pope",
    "poss",
    "pots",
    "pour",
    "prad",
    "prat",
    "prep",
    "prob",
    "prof",
    "prow",
    "puck",
    "puds",
    "puke",
    "puku",
    "pump",
    "puns",
    "pupa",
    "purl",
    "pyre",
    "quad",
    "quay",
    "quey",
    "quiz",
    "raid",
    "rail",
    "rain",
    "raja",
    "rale",
    "rams",
    "rand",
    "rant",
    "raps",
    "rasp",
    "razz",
    "rede",
    "reef",
    "reif",
    "rein",
    "repp",
    "rial",
    "ribs",
    "rick",
    "rift",
    "rill",
    "rime",
    "rims",
    "ring",
    "rins",
    "rise",
    "rite",
    "rits",
    "roam",
    "robe",
    "rods",
    "roma",
    "rook",
    "rort",
    "rotl",
    "roup",
    "roux",
    "rube",
    "rubs",
    "ruby",
    "rues",
    "rugs",
    "ruin",
    "runs",
    "ryas",
    "sack",
    "sacs",
    "saga",
    "sail",
    "sale",
    "salp",
    "salt",
    "sand",
    "sang",
    "sash",
    "saut",
    "says",
    "scab",
    "scow",
    "scud",
    "scup",
    "scut",
    "seal",
    "seam",
    "sech",
    "seed",
    "seep",
    "seer",
    "self",
    "sena",
    "send",
    "sera",
    "sere",
    "shad",
    "shah",
    "sham",
    "shay",
    "shes",
    "ship",
    "shoe",
    "sick",
    "sida",
    "sign",
    "sike",
    "sima",
    "sine",
    "sing",
    "sinh",
    "sink",
    "sins",
    "site",
    "size",
    "skat",
    "skin",
    "skip",
    "skis",
    "slaw",
    "sled",
    "slew",
    "sley",
    "slob",
    "slue",
    "slug",
    "smut",
    "snap",
    "snib",
    "snip",
    "snob",
    "snog",
    "snot",
    "snow",
    "snub",
    "snug",
    "soft",
    "soja",
    "soke",
    "song",
    "sons",
    "sook",
    "sorb",
    "sori",
    "souk",
    "soul",
    "sous",
    "soya",
    "spit",
    "stay",
    "stew",
    "stir",
    "stob",
    "stud",
    "suds",
    "suer",
    "suit",
    "sumo",
    "sums",
    "sups",
    "suqs",
    "suss",
    "sway",
    "syce",
    "synd",
    "taal",
    "tach",
    "taco",
    "tads",
    "taka",
    "tale",
    "tamp",
    "tams",
    "tang",
    "tans",
    "tape",
    "tare",
    "taro",
    "tarp",
    "tart",
    "tass",
    "taus",
    "teat",
    "teds",
    "teff",
    "tegu",
    "tell",
    "term",
    "thar",
    "thaw",
    "tics",
    "tier",
    "tiff",
    "tils",
    "tilt",
    "tint",
    "tipi",
    "tire",
    "tirl",
    "toby",
    "tods",
    "toea",
    "toff",
    "toga",
    "toil",
    "toke",
    "tola",
    "tole",
    "tomb",
    "toms",
    "torc",
    "tors",
    "tort",
    "tosh",
    "tote",
    "tret",
    "trey",
    "trio",
    "trug",
    "tuck",
    "tugs",
    "tule",
    "tune",
    "tuns",
    "tuts",
    "tyke",
    "tyne",
    "typo",
    "ulna",
    "umbo",
    "unau",
    "unit",
    "upas",
    "user",
    "uvea",
    "vacs",
    "vane",
    "vang",
    "vans",
    "vara",
    "vase",
    "veep",
    "veer",
    "vega",
    "veil",
    "vela",
    "vent",
    "vies",
    "view",
    "vina",
    "vine",
    "vise",
    "vlei",
    "volt",
    "vows",
    "wads",
    "waft",
    "wage",
    "wain",
    "walk",
    "want",
    "wart",
    "wave",
    "waws",
    "weal",
    "wean",
    "weds",
    "weep",
    "weft",
    "weir",
    "weka",
    "weld",
    "wens",
    "weys",
    "whap",
    "whey",
    "whin",
    "whit",
    "whop",
    "wide",
    "wife",
    "wind",
    "wine",
    "wino",
    "wins",
    "wire",
    "wise",
    "woes",
    "wont",
    "wool",
    "work",
    "worm",
    "wort",
    "yack",
    "yank",
    "yapp",
    "yard",
    "yate",
    "yawl",
    "yegg",
    "yell",
    "yeuk",
    "yews",
    "yips",
    "yobs",
    "yogi",
    "yoke",
    "yolk",
    "yoni",
    "zack",
    "zags",
    "zest",
    "zhos",
    "zigs",
    "zila",
    "zips",
    "ziti",
    "zoea",
    "zone",
    "zoon",
)  # noqa: E501, Q000, N806

ADJECTIVES = (
    "about",
    "above",
    "abuzz",
    "acerb",
    "acold",
    "acred",
    "added",
    "addle",
    "adept",
    "adult",
    "adunc",
    "adust",
    "afoul",
    "after",
    "agape",
    "agaze",
    "agile",
    "aging",
    "agley",
    "aglow",
    "ahead",
    "ahull",
    "aided",
    "alary",
    "algal",
    "alike",
    "alive",
    "alone",
    "aloof",
    "alpha",
    "amber",
    "amiss",
    "amort",
    "ample",
    "amuck",
    "angry",
    "anile",
    "apeak",
    "apish",
    "arced",
    "areal",
    "armed",
    "aroid",
    "ashen",
    "aspen",
    "astir",
    "atilt",
    "atrip",
    "aulic",
    "aural",
    "awash",
    "awful",
    "awing",
    "awned",
    "axile",
    "azoic",
    "azure",
    "baggy",
    "baked",
    "balky",
    "bally",
    "balmy",
    "banal",
    "bandy",
    "bardy",
    "bared",
    "barer",
    "barky",
    "basal",
    "based",
    "baser",
    "basic",
    "batty",
    "bawdy",
    "beady",
    "beaky",
    "beamy",
    "beaut",
    "beefy",
    "beery",
    "beige",
    "bendy",
    "bifid",
    "bijou",
    "biped",
    "birch",
    "bitty",
    "blame",
    "bland",
    "blank",
    "blear",
    "blest",
    "blind",
    "blond",
    "blown",
    "blowy",
    "bluer",
    "bluff",
    "blunt",
    "boned",
    "bonny",
    "boozy",
    "bored",
    "boric",
    "bosky",
    "bosom",
    "bound",
    "bovid",
    "bowed",
    "boxed",
    "braky",
    "brash",
    "brief",
    "briny",
    "brisk",
    "broad",
    "broch",
    "brood",
    "brown",
    "brute",
    "buggy",
    "bulgy",
    "bumpy",
    "burly",
    "burnt",
    "burry",
    "bushy",
    "busty",
    "butch",
    "buxom",
    "cadgy",
    "cagey",
    "calmy",
    "campy",
    "canny",
    "caped",
    "cased",
    "catty",
    "cauld",
    "cedar",
    "cered",
    "ceric",
    "chary",
    "cheap",
    "cheek",
    "chewy",
    "chief",
    "chill",
    "chirk",
    "choky",
    "cissy",
    "civil",
    "cleft",
    "coaly",
    "color",
    "comfy",
    "comic",
    "compo",
    "conic",
    "couth",
    "coxal",
    "crack",
    "crank",
    "crash",
    "crass",
    "crisp",
    "cronk",
    "cross",
    "crude",
    "cruel",
    "crumb",
    "cured",
    "curly",
    "curst",
    "cushy",
    "cutty",
    "cynic",
    "dated",
    "dazed",
    "dedal",
    "deism",
    "diazo",
    "dicey",
    "dingy",
    "direr",
    "dirty",
    "dishy",
    "dizzy",
    "dolce",
    "doped",
    "dopey",
    "dormy",
    "dorty",
    "dosed",
    "dotal",
    "dotty",
    "dowdy",
    "dowie",
    "downy",
    "dozen",
    "drawn",
    "dread",
    "drear",
    "dress",
    "dried",
    "ducky",
    "duddy",
    "dummy",
    "dumpy",
    "duple",
    "dural",
    "dusky",
    "dusty",
    "dutch",
    "dying",
    "eager",
    "eaten",
    "ebony",
    "edged",
    "eerie",
    "eight",
    "elder",
    "elect",
    "elfin",
    "elite",
    "empty",
    "enate",
    "enemy",
    "epoxy",
    "erect",
    "ethic",
    "every",
    "extra",
    "faced",
    "faery",
    "faint",
    "famed",
    "fancy",
    "farci",
    "fatal",
    "fated",
    "fatty",
    "fazed",
    "felon",
    "fenny",
    "ferny",
    "fetal",
    "fetid",
    "fewer",
    "fiery",
    "fifty",
    "filar",
    "filmy",
    "final",
    "fined",
    "finer",
    "finny",
    "fired",
    "first",
    "fishy",
    "fixed",
    "fizzy",
    "flaky",
    "flamy",
    "flash",
    "flawy",
    "fleet",
    "flory",
    "flown",
    "fluid",
    "fluky",
    "flush",
    "focal",
    "foggy",
    "folio",
    "forky",
    "forte",
    "forty",
    "found",
    "frail",
    "frank",
    "freed",
    "freer",
    "fresh",
    "fried",
    "front",
    "frore",
    "fuggy",
    "funky",
    "funny",
    "furry",
    "fusil",
    "fussy",
    "fuzzy",
    "gabby",
    "gamer",
    "gamey",
    "gamic",
    "gammy",
    "garni",
    "gauge",
    "gaunt",
    "gauzy",
    "gawky",
    "gawsy",
    "gemmy",
    "genal",
    "genic",
    "ghast",
    "gimpy",
    "girly",
    "glare",
    "glary",
    "glial",
    "glued",
    "gluey",
    "godly",
    "gooey",
    "goofy",
    "goosy",
    "gouty",
    "grade",
    "grand",
    "grapy",
    "grave",
    "gross",
    "group",
    "gruff",
    "guest",
    "gules",
    "gulfy",
    "gummy",
    "gushy",
    "gusty",
    "gutsy",
    "gutta",
    "gypsy",
    "gyral",
    "hadal",
    "hammy",
    "handy",
    "hardy",
    "hasty",
    "hated",
    "hazel",
    "heady",
    "heapy",
    "hefty",
    "heigh",
    "hempy",
    "herby",
    "hexed",
    "hi-fi",
    "hilly",
    "hired",
    "holey",
    "honey",
    "hooly",
    "hoven",
    "huger",
    "hulky",
    "humid",
    "hunky",
    "hyoid",
    "idled",
    "iliac",
    "inane",
    "incog",
    "inert",
    "inner",
    "inter",
    "iodic",
    "ionic",
    "irate",
    "irony",
    "itchy",
    "jaggy",
    "jammy",
    "japan",
    "jazzy",
    "jerky",
    "jetty",
    "joint",
    "jowly",
    "juicy",
    "jumpy",
    "jural",
    "kacha",
    "kaput",
    "kempt",
    "keyed",
    "kinky",
    "known",
    "kooky",
    "kraal",
    "laced",
    "laigh",
    "lairy",
    "lamer",
    "lardy",
    "larky",
    "lated",
    "later",
    "lathy",
    "leady",
    "leafy",
    "leaky",
    "leary",
    "least",
    "ledgy",
    "leery",
    "legal",
    "leggy",
    "lento",
    "level",
    "licht",
    "licit",
    "liege",
    "light",
    "liked",
    "liney",
    "lippy",
    "lived",
    "livid",
    "loamy",
    "loath",
    "lobar",
    "local",
    "loony",
    "loose",
    "loral",
    "losel",
    "lousy",
    "loved",
    "lower",
    "lowly",
    "lowse",
    "loyal",
    "lucid",
    "lucky",
    "lumpy",
    "lunar",
    "lurid",
    "lushy",
    "lying",
    "lyric",
    "macho",
    "macro",
    "magic",
    "major",
    "malar",
    "mangy",
    "manky",
    "manly",
    "mardy",
    "massy",
    "mated",
    "matte",
    "mauve",
    "mazed",
    "mealy",
    "meaty",
    "medal",
    "melic",
    "mesic",
    "mesne",
    "messy",
    "metal",
    "miffy",
    "milky",
    "mined",
    "minim",
    "minor",
    "minus",
    "mired",
    "mirky",
    "misty",
    "mixed",
    "modal",
    "model",
    "moire",
    "molar",
    "moldy",
    "moody",
    "moony",
    "mopey",
    "moral",
    "mossy",
    "mothy",
    "motor",
    "mousy",
    "moved",
    "mucid",
    "mucky",
    "muddy",
    "muggy",
    "muley",
    "mural",
    "murky",
    "mushy",
    "muted",
    "muzzy",
    "myoid",
    "naggy",
    "naive",
    "naked",
    "named",
    "nasty",
    "natal",
    "naval",
    "nervy",
    "newsy",
    "nicer",
    "niffy",
    "nifty",
    "ninth",
    "nitty",
    "nival",
    "noble",
    "nodal",
    "noisy",
    "non-U",
    "north",
    "nosed",
    "noted",
    "nowed",
    "nubby",
    "oaken",
    "oared",
    "oaten",
    "obese",
    "ocher",
    "ochre",
    "often",
    "ohmic",
    "oiled",
    "olden",
    "older",
    "oleic",
    "olive",
    "optic",
    "ortho",
    "osmic",
    "other",
    "outer",
    "ovoid",
    "owing",
    "owned",
    "paced",
    "pagan",
    "paled",
    "paler",
    "pally",
    "paper",
    "pappy",
    "parky",
    "party",
    "pasty",
    "pavid",
    "pawky",
    "peaky",
    "pearl",
    "peart",
    "peaty",
    "pedal",
    "peppy",
    "perdu",
    "perky",
    "pesky",
    "phony",
    "piano",
    "picky",
    "piled",
    "piney",
    "pious",
    "pique",
    "pithy",
    "platy",
    "plump",
    "plush",
    "podgy",
    "potty",
    "power",
    "prest",
    "pricy",
    "prima",
    "prime",
    "print",
    "privy",
    "prize",
    "prone",
    "proof",
    "prosy",
    "proud",
    "proxy",
    "pseud",
    "pucka",
    "pudgy",
    "puffy",
    "pukka",
    "pupal",
    "purer",
    "pursy",
    "pushy",
    "pyoid",
    "quack",
    "quare",
    "quasi",
    "quiet",
    "quits",
    "rabic",
    "rabid",
    "radio",
    "raked",
    "randy",
    "rapid",
    "rarer",
    "raspy",
    "rathe",
    "ratty",
    "ready",
    "reedy",
    "reeky",
    "refer",
    "regal",
    "riant",
    "ridgy",
    "right",
    "riled",
    "rimed",
    "rindy",
    "risen",
    "risky",
    "ritzy",
    "rival",
    "riven",
    "robed",
    "rocky",
    "roily",
    "roman",
    "rooky",
    "ropey",
    "round",
    "rowdy",
    "ruddy",
    "ruled",
    "rummy",
    "runic",
    "runny",
    "runty",
    "rural",
    "rusty",
    "rutty",
    "sable",
    "salic",
    "sandy",
    "sappy",
    "sarky",
    "sassy",
    "sated",
    "saved",
    "savvy",
    "scald",
    "scaly",
    "scary",
    "score",
    "scrap",
    "sedgy",
    "seely",
    "seral",
    "sewed",
    "shaky",
    "sharp",
    "sheen",
    "shier",
    "shill",
    "shoal",
    "shock",
    "shoed",
    "shore",
    "short",
    "shyer",
    "silky",
    "silly",
    "silty",
    "sixth",
    "sixty",
    "skint",
    "slack",
    "slant",
    "sleek",
    "slier",
    "slimy",
    "slung",
    "small",
    "smart",
    "smoky",
    "snaky",
    "sneak",
    "snide",
    "snowy",
    "snuff",
    "so-so",
    "soapy",
    "sober",
    "socko",
    "solar",
    "soled",
    "solid",
    "sonic",
    "sooth",
    "sooty",
    "soppy",
    "sorer",
    "sound",
    "soupy",
    "spent",
    "spicy",
    "spiky",
    "spiny",
    "spiry",
    "splay",
    "split",
    "sport",
    "spumy",
    "squat",
    "staid",
    "stiff",
    "still",
    "stoic",
    "stone",
    "stony",
    "store",
    "stout",
    "straw",
    "stray",
    "strip",
    "stung",
    "suave",
    "sudsy",
    "sulfa",
    "sulky",
    "sunny",
    "super",
    "sural",
    "surer",
    "surfy",
    "surgy",
    "surly",
    "swell",
    "swept",
    "swish",
    "sworn",
    "tabby",
    "taboo",
    "tacit",
    "tacky",
    "tamed",
    "tamer",
    "tangy",
    "taped",
    "tarot",
    "tarry",
    "tasty",
    "tatty",
    "taunt",
    "tawie",
    "teary",
    "techy",
    "telic",
    "tenor",
    "tense",
    "tenth",
    "tenty",
    "tepid",
    "terse",
    "testy",
    "third",
    "tidal",
    "tight",
    "tiled",
    "timid",
    "tinct",
    "tined",
    "tippy",
    "tipsy",
    "tonal",
    "toned",
    "tonic",
    "toric",
    "total",
    "tough",
    "toxic",
    "trade",
    "treed",
    "treen",
    "trial",
    "truer",
    "tubal",
    "tubby",
    "tumid",
    "tuned",
    "tutti",
    "twill",
    "typal",
    "typed",
    "typic",
    "umber",
    "unapt",
    "unbid",
    "uncut",
    "undue",
    "undug",
    "unfed",
    "unfit",
    "union",
    "unlet",
    "unmet",
    "unwed",
    "unwet",
    "upper",
    "upset",
    "urban",
    "utile",
    "uveal",
    "vagal",
    "valid",
    "vapid",
    "varus",
    "vatic",
    "veiny",
    "vital",
    "vivid",
    "vocal",
    "vogie",
    "volar",
    "vying",
    "wacky",
    "wally",
    "waney",
    "warty",
    "washy",
    "waspy",
    "waste",
    "waugh",
    "waxen",
    "webby",
    "wedgy",
    "weeny",
    "weepy",
    "weest",
    "weird",
    "welsh",
    "wersh",
    "whist",
    "white",
    "whity",
    "whole",
    "wider",
    "wight",
    "winey",
    "wired",
    "wised",
    "wiser",
    "withy",
    "wonky",
    "woods",
    "woozy",
    "world",
    "wormy",
    "worse",
    "worst",
    "woven",
    "wrath",
    "wrier",
    "wrong",
    "wroth",
    "xeric",
    "yarer",
    "yolky",
    "young",
    "yucky",
    "yummy",
    "zesty",
    "zingy",
    "zinky",
    "zippy",
    "zonal",
)  # noqa: E501, Q000, N806
