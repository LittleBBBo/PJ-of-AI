from Engine import *
from Utils import *

class RuleBasedSystem:
    def __init__(self, rules, workingMemory):
        self.rules = rules
        self.workingMemory = workingMemory

        self.workingMemoryList = [parseStringToArray(x) for x in self.workingMemory]

    def generateInferences(self):
        self.workingMemoryList = inferNewFacts(self.rules, self.workingMemoryList)
        self.workingMemory = [parseArrayToString(x) for x in self.workingMemoryList]

class Rule:
    def __init__(self, name, antecedents, consequents):
        self.name = name
        self.antecedents = antecedents
        self.consequents = consequents

        self.antecedentList = [parseStringToArray(x) for x in self.antecedents]
        self.consequentList = [parseStringToArray(x) for x in self.consequents]

verbIs = Rule('verb-is', ['is'], ['is = Verb'])
verbWent = Rule('verb-went', ['went'], ['went = Verb'])
verbRan = Rule('verb-ran', ['ran'], ['ran = Verb'])
verbBought = Rule('verb-bought', ['bought'], ['bought = Verb'])
verbGo = Rule('verb-go', ['go'], ['go = Verb'])
verbHave = Rule('verb-have', ['have'], ['have = Verb'])
verbBe = Rule('verb-be', ['be'], ['be = Verb'])
verbMake = Rule('verb-make', ['make'], ['make = Verb'])
verbSee = Rule('verb-see', ['see'], ['see = Verb'])

adverbQuickly = Rule('adverb-quickly', ['quickly'], ['quickly = Adverb'])
adverbLoudly = Rule('adverb-loudly', ['loudly'], ['loudly = Adverb'])
adverbEasily = Rule('adverb-Easily', ['easily'], ['easily = Adverb'])

pronounHe = Rule('pronoun-he', ['he'], ['he = Pronoun'])
pronounShe = Rule('pronoun-she', ['she'], ['she = Pronoun'])
pronounIt = Rule('pronoun-it', ['it'], ['it = Pronoun'])
pronounI = Rule('pronoun-i', ['i'], ['i = Pronoun'])
pronounThey = Rule('pronoun-they', ['they'], ['they = Pronoun'])
pronounWe = Rule('pronoun-we', ['we'], ['we = Pronoun'])
pronounThem = Rule('pronoun-them', ['them'], ['them = Pronoun'])
pronounThat = Rule('pronoun-that', ['that'], ['that = Pronoun'])

nounTime = Rule('noun-time', ['time'], ['time = Noun'])
nounFood = Rule('noun-food', ['food'], ['food = Noun'])
nounItem = Rule('noun-item', ['item'], ['item = Noun'])
nounPlace = Rule('noun-place', ['place'], ['place = Noun'])
nounStore = Rule('noun-store', ['store'], ['store = Noun'])
nounEssence = Rule('noun-essence', ['essence'], ['essence = Noun'])

adjectiveGood = Rule('adjective-good', ['good'], ['good = Adjective'])
adjectiveNew = Rule('adjective-new', ['new'], ['new = Adjective'])
adjectiveFirst = Rule('adjective-first', ['first'], ['first = Adjective'])
adjectiveBig = Rule('adjective-big', ['big'], ['big = Adjective'])
adjectiveOld = Rule('adjective-old', ['old'], ['old = Adjective'])
adjectiveLast = Rule('adjective-last', ['last'], ['last = Adjective'])
adjectiveBrobdingnagian = Rule('adjective-brobdingnagian', ['brobdingnagian'], ['brobdingnagian = Adjective'])

prepositionTo = Rule('preposition-to', ['to'], ['to = Preposition'])
prepositionOf = Rule('preposition-of', ['of'], ['of = Preposition'])
prepositionIn = Rule('preposition-in', ['in'], ['in = Preposition'])
prepositionFor = Rule('preposition-for', ['for'], ['for = Preposition'])
prepositionWith = Rule('preposition-with', ['with'], ['with = Preposition'])
prepositionOn = Rule('preposition-on', ['on'], ['on = Preposition'])
prepositionUp = Rule('preposition-up', ['up'], ['up = Preposition'])

determinerThe = Rule('determiner-the', ['the'], ['the = Determiner'])
determinerA = Rule('determiner-a', ['a'], ['a = Determiner'])
determinerAn = Rule('determiner-an', ['an'], ['an = Determiner'])
determinerNo = Rule('determiner-no', ['no'], ['no = Determiner'])
determinerThat = Rule('determiner-that', ['that'], ['that = Determiner'])

beginningSentence = Rule('begin-sentence', ['BEGIN_SENTENCE precedes ?word'], ['?word = Noun', '?word = Pronoun'])
adverbRule = Rule('adverb-placement', ['?word1 precedes ?word2', '?word2 = Verb'], ['?word1 = Adverb'])
adjectiveRule1 = Rule('adjective-placement1', ['?word1 precedes ?word2', '?word2 = Noun'], ['?word1 = Adjective'])
adjectiveRule2 = Rule('adjective-placement2', ['?word1 precedes ?word2', '?word2 = Pronoun'], ['?word1 = Adjective'])
adjectiveRule3 = Rule('adjective-placement3', ['?word1 precedes ?word2', '?word2 = Adjective'], ['?word1 = Adjective'])
adjectiveRule4 = Rule('adjective-placement4', ['?word1 precedes ?word2', '?word1 = Verb'], ['?word2 = Adjective'])
determinerRule1 = Rule('determiner-placement1', ['?word1 precedes ?word2', '?word2 = Noun'], ['?word1 = Determiner'])
determinerRule2 = Rule('determiner-placement2', ['?word1 precedes ?word2', '?word2 = Pronoun'], ['?word1 = Determiner'])
nounRule1 = Rule('noun-placement1', ['?word1 precedes ?word2', '?word1 = Determiner'], ['?word2 = Noun'])
nounRule2 = Rule('noun-placement2', ['?word1 precedes ?word2', '?word2 = Verb'], ['?word1 = Noun'])
nounRule3 = Rule('noun-placement3', ['?word1 precedes ?word2', '?word2 precedes ?word3', '?word1 = Preposition', '?word2 = Determiner'], \
                     ['?word3 = Noun'])
pronounRule1 = Rule('pronoun-placement1', ['?word1 precedes ?word2', '?word2 = Verb'], ['?word1 = Pronoun'])
pronounRule2 = Rule('pronoun-placement2', ['?word1 precedes ?word2', '?word2 precedes ?word3', '?word1 = Preposition', '?word2 = Determiner'], \
                     ['?word3 = Pronoun'])
verbRule1 = Rule('verb-placement1', ['?word1 precedes ?word2', '?word1 = Noun'], ['?word2 = Verb'])
verbRule2 = Rule('verb-placement2', ['?word1 precedes ?word2', '?word1 = Pronoun'], ['?word2 = Verb'])
verbRule3 = Rule('verb-placement3', ['?word1 precedes ?word2', '?word2 = Preposition'], ['?word1 = Verb'])

Rules = [verbIs, verbWent, verbRan, verbBought, verbGo, verbHave, verbBe, verbMake, verbSee, \
             adverbQuickly, adverbLoudly, adverbEasily, \
             pronounHe, pronounShe, pronounIt, pronounI, pronounThey, pronounWe, pronounThem, pronounThat, \
             nounTime, nounFood, nounItem, nounPlace, nounStore, nounEssence, \
             adjectiveGood, adjectiveNew, adjectiveFirst, adjectiveBig, adjectiveOld, adjectiveLast, adjectiveBrobdingnagian, \
             prepositionTo, prepositionOf, prepositionIn, prepositionFor, prepositionWith, prepositionOn, prepositionUp, \
             determinerThe, determinerA, determinerAn, determinerNo, determinerThat, \
             beginningSentence, adverbRule, adjectiveRule1, adjectiveRule2, adjectiveRule3, adjectiveRule4, \
             determinerRule1, determinerRule2, nounRule1, nounRule2, pronounRule1, pronounRule2, verbRule1, verbRule2, verbRule3]

def tagSentence(sentence):
    def extractTags(factList):
        returnList = []
        for fact in factList:
            if len(fact) == 3:
                if fact[1] == "=" and fact[0] != "BEGIN_SENTENCE" and fact[0] != "END_SENTENCE":
                    returnList.append(fact)
        return returnList

    convertedSentence = parseStringToArray(sentence)

    additionalFacts = []
    additionalFacts.append("BEGIN_SENTENCE precedes " + convertedSentence[0])
    i = 1
    while i < len(convertedSentence):
        additionalFacts.append(convertedSentence[i - 1] + " precedes " + convertedSentence[i])
        i += 1
    additionalFacts.append(convertedSentence[i - 1] + " precedes END_SENTENCE")
    convertedSentence.extend(additionalFacts)

    WorkingMemory = convertedSentence

    system = RuleBasedSystem(Rules, WorkingMemory)
    system.generateInferences()

    extractedTagList = extractTags(system.workingMemoryList)

    finalTagSet = {}
    for tag in extractedTagList:
        if not tag[0] in finalTagSet:
            finalTagSet[tag[0]] = tag

    finalTags = []

    initialSentence = parseStringToArray(sentence)
    for word in initialSentence:
        for tag in finalTagSet.values():
            if tag[0] == word:
                finalTags.append(tag)
                break

    finalTags = [parseArrayToString(x) for x in finalTags]

    return finalTags


