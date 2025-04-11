"""
Testing 10 Quotes from each of the following Plays:
    Titus Andronicus
    Timon of Athens
    Coriolanus
    Antony and Cleopatra
    Two Gentlemen of Verona
    Troilus and Cressida
    Pericles, Prince of Tyre
    Richard III
    Henry VIII
    Henry VI, part III
Used to get performance metrics: precision, recall, f1, similarity-score
~10-word quotes
Most quotes taken from Royal Shakespeare Company RSC.org.uk
"""
import json
import os


def main():
    testing_quotes = {
        'Titus_Andronicus': [
            "content thee prince i will restore to thee the people's",
            "and make them know what 'tis to let a queen",
            "she is a woman therefore may be wooed she is",
            "madam though venus govern your desires saturn is dominator over mine",
            "vengeance is in my heart death in my hand blood and revenge are hammering in my head",
            "the worse to her the better loved of me",
            "alas a crimson river of warm blood like to a",
            "doth rise and fall between thy rosed lips coming and going with thy honey breath",
            "alas poor man grief has so wrought on him",
            "villain, what hast thou done that which thou canst not undo",
        ],
        'Timon_of_Athens': [
            "i am not of that feather to shake off",
            "here's that which is too weak to be a sinner",
            "like madness is the glory of this life",
            "men shut their doors against a settling sun",
            "their blood is caked ‘tis cold it selfdom flows",
            "every man has his fault and honesty is his",
            "what beast couldst thou be that were not subject to a beast",
            "the moon's an arrant thief and her pale fire she snatches from the sun",
            "you are an alchemist make gold of that",
            "'here lies a wretched corpse, of wretched soul bereft."
        ],
        'Coriolanus': [
            "my rage is gone and i am struck with sorrow",
            "more of your conversation would infect my brain being the herdsmen of the beastly plebeians",
            "his nature is too noble for the world he would not flatter neptune for his trident",
            "action is eloquence and the eyes of the ignorant more learned than the ears",
            "anger's my meat i sup upon myself and so shall starve with feeding",
            "the beast with many heads butts me away",
            "let me have war say i it exceeds peace as far as day does night",
            "he that hath a will to die by himself fears it not from another",
            "we loved him but like beasts and cowardly nobles gave way unto your clusters",
            "then let the pebbles on the hungry beach fillip the stars",
        ],
        'Antony_and_Cleopatra': [
            "and you shall in him the triple pillar of the world transformed into a strumpet's fool",
            "let rome in tiber melt and the wide arch of the ranged empire fall",
            "o happy horse to bear the weight of antony",
            "my salad days when i was green in judgment cold in blood",
            "age cannot wither her nor custom stale her infinite variety",
            "the odds is gone and there is nothing left remarkable beneath the visiting moon",
            "shall be brought drunken forth and i shall see some squeaking cleopatra",
            "now boast thee death in thy possession lies a lass unparalleled",
            "she shall be buried by her antony no grave upon the earth shall clip in it",
            "you lie up to the hearing of the gods",
        ],
        'Two_Gentlemen_of_Verona': [
            "for he was more than over shoes in love",
            "i have no other but a woman's reason i think him so",
            "they do not love that do not show their love",
            "o hateful hands to tear such loving words",
            "injurious wasps to feed on such sweet honey",
            "o how this spring of love resembleth the uncertain glory of an april day",
            "i'll be as patient as a gentle stream and make a pastime of each weary step",
            "that man that hath a tongue i say is no man",
            "love is like a child that longs for everything he can come by",
            "o heaven were man but constant he were perfect",
        ],
        'Troilus_and_Cressida': [
            "her bed is india there she lies a pearl",
            "things won are done joy's soul lies in the doing",
            "the heavens themselves the planets and this centre observe degree priority and place",
            "there is seen the baby figure of the giant mass of things to come at large",
            "we turn not back the silks upon the merchant when we have spoiled them",
            "the common curse of mankind folly and ignorance be thine in great revenue",
            "they say all lovers swear more performance than they are able",
            "time hath my lord a wallet at his back",
            "one touch of nature makes the whole world kin",
            "the strong base and building of my love is at the very centre of the earth drawing all things to it"
        ],
        'Pericles': [
            "to sing a song that old was sung from ashes ancient gower is come",
            "for death remembered should be like a mirror who tells us life's but breath to trust it error",
            "few love to hear the sins they love to act",
            "murder's as near as lust as flame to smoke",
            "'tis time to feat when tyrants seems to kiss",
            "who makes the fairest show means most deceit",
            "opinion's but a fool that makes us scan the outward habit for the inward man",
            "the diamonds of a most praised water doth appear",
            "that she would make a puritan of the devil if he should cheapen a kiss of her",
            "o come be buried a second time within these arms",
        ],
        'RichardIII': [
            "now is the winter of our discontent made glorious summer by this sun of york",
            "thos weak piping time of peace have no delight to pass away the time",
            "and therefore since i cannot prove a lover to entertain these fair well-spoken days",
            "was ever woman in this humour wooed was ever woman in this humour won",
            "since every jack became a gentleman there's many a gentle person made a jack",
            "and thus i clothe my naked villany with old odd ends stolen out of holy writ",
            "so wise so young they say do never live long",
            "true hope is swift and flies with swallow's wings",
            "conscience is but a word that cowards use devised at first to keep the strong in awe",
            "my conscience hath a thousand several tongues and every tongue brings in a several tale",
        ],
        'HenryVIII': [
            "be to yourself as you would to your friend",
            "heat not a furnace for your foe so hot that it do singe yourself",
            "'tis but the fate of place and the rough brake that virtue must go through",
            "i have touched the highest point of all my greatness",
            "i shall fall like a bright exhalation in the evening",
            "i feel within me a peace above all earthly dignities",
            "love thyself last cherish those hearts that hate thee",
            "men's evil manners live in brass their virtues we write in water",
            "those about her from her stall read the perfect ways of honour",
            "you knkoe no more than other but you frame things that are known alike",
        ],
        'HenryVI_partIII': [
            "farewell faint-hearted and degenerate king in whose cold blood no spark of honour bides",
            "how sweet a thing it is to wear a crown",
            "o tiger's heart wrapt in a woman's hide",
            "to weep is to make less the depth of grief",
            "the smallest worm will turn being trodden on and doves will peck in safeguard of their brood",
            "o god methinks it were a happy life to be no better than a homely swain",
            "let me embrace the sour adversaries for wise men say it is the wisest course",
            "my crown is in my heart not on my head",
            "for trust not him that hath once broken faith",
            "and live we how we can yet die we must",
        ]


    }

    # write these to /data/testing/quotes.json
    filepath = os.path.join(os.path.dirname(__file__), "../data", "testing", "quotes.json")
    with open(filepath, "w") as writer:
        json.dump(testing_quotes, writer)
    



if __name__ == "__main__":
    main()