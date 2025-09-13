import time
import random

#ChatGPT for word list

words = [
    "abandon", "ability", "absence", "academy", "account", "accuse", "achieve", "acquire", "across", "action",
    "adapt", "advice", "affect", "afford", "afraid", "agency", "agenda", "airline", "alcohol", "allege",
    "allow", "almost", "already", "alter", "amazing", "amount", "anchor", "ancient", "anger", "animal",
    "annual", "answer", "anxiety", "anybody", "apology", "appeal", "approve", "argue", "arise", "around",
    "arrive", "artist", "aspect", "assign", "assist", "assume", "attack", "attempt", "attend", "attract",
    "author", "average", "avenue", "award", "aware", "awesome", "awkward", "backup", "bargain", "barrier",
    "battery", "battle", "beauty", "become", "belief", "belong", "benefit", "beside", "betray", "beyond",
    "bitter", "blanket", "blessing", "blind", "borrow", "bottom", "bounce", "branch", "brave", "breeze",
    "brief", "bright", "broken", "budget", "burden", "butter", "button", "cactus", "camera", "cancel",
    "cannon", "canvas", "carbon", "career", "carpet", "castle", "casual", "cause", "ceiling", "celebrate",
    "center", "ceramic", "chance", "change", "charge", "charm", "cheap", "cheese", "choose", "chorus",
    "circle", "citizen", "clarify", "climate", "clinic", "clothes", "cloud", "cluster", "coach", "coast",
    "collar", "column", "comfort", "command", "comment", "commit", "compact", "compete", "compose", "concept",
    "concern", "confess", "confuse", "connect", "consent", "contest", "control", "convert", "cooler", "corner",
    "costume", "cottage", "council", "counter", "course", "coward", "cradle", "craft", "create", "credit",
    "crisis", "critic", "crystal", "culture", "curious", "custom", "damage", "danger", "daring", "debate",
    "decade", "decide", "declare", "decline", "default", "defeat", "defend", "define", "degree", "delay",
    "demand", "depend", "deposit", "desert", "desire", "detail", "detect", "device", "devote", "dialogue",
    "differ", "dignity", "direct", "discuss", "disease", "display", "dispute", "distant", "diverse", "divide",
    "doctor", "dollar", "domain", "donate", "double", "driven", "during", "eager", "early", "easily",
    "effect", "effort", "either", "elder", "elegant", "element", "embark", "embrace", "emerge", "emotion",
    "empire", "enable", "ending", "endorse", "engage", "engine", "enhance", "enough", "enroll", "ensure",
    "enter", "entire", "envious", "equal", "escape", "estate", "ethics", "evening", "evident", "exact",
    "except", "excuse", "expand", "expect", "expert", "expire", "explain", "explore", "express", "extend",
    "fabric", "factor", "failure", "famous", "fancy", "fantasy", "farmer", "fashion", "father", "fault",
    "feature", "fellow", "female", "festival", "fiction", "figure", "filter", "finally", "finger", "finish",
    "firearm", "flavor", "flight", "flower", "follow", "footer", "forbid", "forest", "formal", "former",
    "fortune", "forward", "found", "fragile", "freedom", "frequent", "friend", "fringe", "frozen", "future",
    "galaxy", "garage", "garden", "gather", "gender", "gentle", "genuine", "gesture", "ghost", "giant",
    "global", "golden", "gossip", "govern", "grace", "grade", "granny", "grasp", "gravity", "great",
    "greet", "grieve", "grocery", "growth", "guarantee", "guard", "guilty", "guitar", "habit", "hammer",
    "handle", "happen", "harbor", "hardly", "harvest", "hazard", "health", "height", "heroic", "hidden",
    "highly", "honest", "honor", "horror", "hunger", "hunter", "hurry", "husband", "ignore", "impact",
    "import", "impose", "improve", "impulse", "income", "indeed", "injure", "insight", "inspire", "intend",
    "invest", "invite", "island", "issue", "itself", "jacket", "jealous", "jelly", "journey", "judge",
    "junior", "jungle", "justice", "keeper", "kidney", "killer", "kindly", "kingdom", "kitchen", "kitten",
    "knight", "label", "laptop", "larger", "launch", "lawyer", "leader", "league", "learn", "legend",
    "lesson", "letter", "liberty", "lively", "locate", "locker", "lonely", "longer", "loyal", "lumber",
    "luxury", "magnet", "manage", "manual", "margin", "market", "master", "matrix", "matter", "maximum",
    "meaning", "measure", "medal", "medium", "member", "memory", "mentor", "merit", "message", "method",
    "middle", "mimic", "mining", "minute", "mirror", "mobile", "modern", "modest", "moment", "monster",
    "mostly", "motion", "mount", "museum", "mutual", "myself", "mystery", "native", "nature", "nearby",
    "nearly", "nervous", "network", "nobody", "normal", "notable", "notice", "notion", "novel", "nuclear",
    "nurture", "object", "oblige", "occupy", "occur", "office", "often", "oppose", "option", "orange",
    "orbit", "origin", "outfit", "outlet", "outlook", "output", "overcome", "oxygen", "packet", "paddle"
]

#ChatGPT generated ANSI color code list

colors = {
    "reset": "\033[0m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}

running = True

print("\n\033[93m-WPM Typing Test-")
time.sleep(0.05)

print("\n\033[92mInstructions:\033[37m\nType the words as they appear on the screen as fast as you can")

while running:

    #ChatGPT wrote time script for WPM calculation

    time.sleep(0.05)
    length = input("\n\033[93mHow many seconds should the test be?\033[37m")
    while not length.isdigit():
        time.sleep(0.05)
        print("\n\033[31mInvalid Input!\033[37m Please enter a whole, positive number") 
        time.sleep(0.05)
        length = input("\n\033[93mHow many seconds should the test be?\033[37m")

    length = int(length)

    start = ""
    while start != "Go":
        time.sleep(0.05)
        start = input("\n\033[92mType \"Go\" to start:\033[37m").capitalize()

    start_time = time.time()
    end_time = start_time + length
    characters = 0

    while time.time() < end_time:
        random_word = random.choice(words)
        time.sleep(0.05)
        print("\n\033[95m" + random_word)
        time.sleep(0.05)
        typed = input("\n\033[97mType Here:").lower()

        if typed == random_word:
            characters += len(random_word)
        else:
            pass

    elapsed_time = time.time() - start_time

    if elapsed_time == 0:
        wpm = 0
    else:
        minutes = elapsed_time / 60
        wpm = round((characters / 5) / minutes)

    print(f"\n\033[37mTest Completed. Your WPM:\033[93m {wpm}")

    again = ""
    while again != "Start":
        again = input("\n\033[37mType \"Start\" to test again").capitalize()
