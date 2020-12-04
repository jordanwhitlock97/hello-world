num_nouns = 3
nouns_print = "Please input %d nouns separated by a space\n" #%d is the number of nouns
nouns_string = input(nouns_print % (num_nouns))
nouns = nouns_string.split(" ")

while num_nouns != len(nouns):
    print('The number of nouns inputted did not match the amount asked\n ')
    nouns_string = input(nouns_print % (num_nouns))
    nouns = nouns_string.split(" ")

num_verbs = 2
verbs_print = "Please input %d verbs separated by a space\n" #%d is the number of verbs
verbs_string = input(verbs_print % (num_verbs))
verbs = verbs_string.split(" ")

while num_verbs != len(verbs):
    print('The number of verbs inputted did not match the amount asked\n ')
    verbs_string = input(verbs_print % (num_verbs))
    verbs = verbs_string.split(" ")

num_adverbs = 2
adverbs_print = "Please input %d adverbs separated by a space\n" #%d is the number of adverbs
adverbs_string = input(adverbs_print % (num_adverbs))
adverbs = adverbs_string.split(" ")

while num_adverbs != len(adverbs):
    print('The number of adverbs inputted did not match the amount asked\n ')
    adverbs_string = input(adverbs_print % (num_adverbs))
    adverbs = adverbs_string.split(" ")

num_adjectives = 1
adjectives_print = "Please input %d adjectives separated by a space\n" #%d is the number of adjectives
adjectives_string = input(adjectives_print % (num_adjectives))
adjectives = adjectives_string.split(" ")

while num_adjectives != len(adjectives):
    print('The number of adjectives inputted did not match the amount asked\n ')
    adjectives_string = input(adjectives_print % (num_adjectives))
    adjectives = adjectives_string.split(" ")

print('Once upon a time in '+nouns[1]+'ville there was a boy who was very afraid of ' +nouns[1]+'s.')
print('The boy would '+verbs[0]+' in fright, and '+adverbs[1]+' '+verbs[1]+' with all he could when he saw one.')
print('When the sun would go down he was especially '+adjectives[0]+'. He would do his best to ')
print('make sure no '+nouns[1]+'s were around by '+verbs[0]+'ing in every direction, and swinging')
print('his ' +nouns[0]+' '+adverbs[0]+'.')