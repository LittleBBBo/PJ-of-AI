def isVar(string):
    return string[0] == '?'


def substituteVariables(substitutions, expression):
    resultingExpression = []
    hadSubstitution = True
    while hadSubstitution:
        hadSubstitution = False
        for term in expression:
            if type(term) is list:
                substitutedMultiPartTerm = substituteVariables(substitutions, term)
                resultingExpression.append(substitutedMultiPartTerm)
            elif isVar(term):
                if term in substitutions:
                    resultingExpression.append(substitutions[term])
                    hadSubstitution = True
                else:
                    resultingExpression.append(term)
            else:
                resultingExpression.append(term)
        expression = resultingExpression
        resultingExpression = []
    return expression


def unification(substitution, pattern1, pattern2):
    if pattern1 == [] or pattern2 == []:
        if pattern1 == pattern2:
            return substitution
        return False
    elif type(pattern1) is list and type(pattern2) is list:
        newSubstitutions = unification(substitution, pattern1[0], pattern2[0])
        if newSubstitutions != False:
            newSubstitutions.update(substitution)
            return unification(newSubstitutions, pattern1[1: len(pattern1)], pattern2[1: len(pattern2)])
        return False
    elif isVar(pattern1):
        if pattern1 in substitution:
            return unification(substitution, substitution[pattern1], pattern2)
        if type(pattern2) is list:
            if contains(pattern1, pattern2):
                return False
        return {pattern1: pattern2}
    elif isVar(pattern2):
        if pattern2 in substitution:
            return unification(substitution, pattern1, substitution[pattern2])
        if type(pattern1) is list:
            if contains(pattern2, pattern1):
                return False
        return {pattern2: pattern1}
    elif pattern1 == pattern2:
        return substitution

    return False


def contains(expression, expressionList):
    for element in expressionList:
        if type(element) is list and not contains(expression, element):
            return True
        if expression == element:
            return True
    return False


def matchAntecedent(antecedents, workingMemory, substitutions):
    firstElement = antecedents[0]
    otherElements = antecedents[1: len(antecedents)]
    return matchIndividualAntecedent(firstElement, otherElements, [], workingMemory, substitutions)


def matchIndividualAntecedent(antecedent, antecedents, states, workingMemory, substitutions):
    if len(workingMemory) == 0:
        return states
    fact = workingMemory[0]
    workingMemory = workingMemory[1: len(workingMemory)]
    newSubstitutions = unification(substitutions, antecedent, fact)
    if newSubstitutions != False:
        newState = []
        newState.append(antecedents)
        newState.append(newSubstitutions)
        states.append(newState)
        return matchIndividualAntecedent(antecedent, antecedents, states, workingMemory, substitutions)
    else:
        return matchIndividualAntecedent(antecedent, antecedents, states, workingMemory, substitutions)


def executeSubstitution(substitutions, consequents, workingMemory):
    newFacts = []
    for consequent in consequents:
        newPattern = substituteVariables(substitutions, consequent)
        if not newPattern in workingMemory:
            newFacts.append(newPattern)
    return newFacts


def matchRule(rule, workingMemory):
    ruleName = rule.name
    antecedents = rule.antecedentList
    consequents = rule.consequentList

    def match(queue, newWorkingMemory):
        if len(queue) == 0:
            return newWorkingMemory
        currentAntecedents, currentSubstitutions = queue.pop()
        if currentAntecedents == []:
            newFacts = executeSubstitution(currentSubstitutions, consequents, newWorkingMemory)
            newWorkingMemory.extend(newFacts)
            return match(queue, newWorkingMemory)
        else:
            newState = matchAntecedent(currentAntecedents, workingMemory, currentSubstitutions)
            if newState == []:
                return match(queue, newWorkingMemory)
            queue.extend(newState)
            return match(queue, newWorkingMemory)

    return match(matchAntecedent(antecedents, workingMemory, {}), [])


def checkExisting(item, fullList):
    for element in fullList:
        if item == element:
            return True
    return False


def matchAllRules(rules, workingMemory):
    newPatterns = []
    for rule in rules:
        newFacts = matchRule(rule, workingMemory)
        for fact in newFacts:
            if not fact in workingMemory and not fact in newPatterns:
                newPatterns.append(fact)
    return newPatterns


def inferNewFacts(rules, workingMemory):
    newPatterns = matchAllRules(rules, workingMemory)
    while newPatterns:
        workingMemory.extend(newPatterns)
        newPatterns = matchAllRules(rules, workingMemory)
    return workingMemory
