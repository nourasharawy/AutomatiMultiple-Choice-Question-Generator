# Reka
import re
import RAKE
import spacy
import operator
import neuralcoref
import sys
import nltk
from nltk import tokenize
from textblob import Word
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
import random
import copy

# **********************************************************Keyword extraction*****************************************

############### global var###################

keyword_dic_NER = {}  # de feha el kelma w el NER index 0 w mena haydef l POS index 1
keyword_dic_sents = {}  # de feha kol klma w sents bta3tha
qustions = []
answers = []
Rakelist = []
################# get keywords with rake################
'''
# with open("/content/drive/My Drive/Cinderella_story.txt", 'r',encoding = "ISO-8859-1") as f:
# content = f.read()
text = str(
There was once a rich man whose wife lay sick, and when she felt her end drawing near she called to her only daughter to come near her bed, and said, “ dear child, be pious and good, and Allah will always take care of you, and I will look down upon you from heaven, and will be with you.” And then she closed her eyes and expired. The man took to himself another wife. The new wife brought two daughters home with her. They were beautiful and fair in appearance, but at heart were ugly. “Is the stupid creature to sit in the same room with us?” said they. “Those who eat food must earn it. She can be our kitchen-maid!” They took away her pretty dresses, and put on her an old grey kirtle, and gave her wooden shoes to wear. “Just look now at the proud princess, how she is decked out!” they laughed, and then they sent her into the kitchen. There she was obliged to do heavy work from morning to night, get up early in the morning, draw water, make the fires, cook, and wash. Besides that, the sisters did their utmost to torment her, mocking her, and strewing peas and lentils among the ashes, and setting her to pick them up. In the evenings, when she was quite tired out with her hard day’s work, she had no bed to lie on, but was obliged to rest on the hearth among the cinders. And as she always looked dusty and dirty, they named her Cinderella. It happened one day that the father went to the fair, and he asked his two step-daughters what he should bring back for them. “Fine clothes!” said one. “Pearls and jewels!” said the other. “But what will you have, Cinderella?” said he. “The first twig, father, that strikes against your hat on the way home; that is what I should like you to bring me.” So he bought for the two step-daughters fine clothes, pearls, and jewels, and on his way back, as he rode through a green lane, a hazel-twig struck against his hat; and he broke it off and carried it home with him. And when he reached home he gave to the step-daughters what they had wished for, and to Cinderella he gave the hazel-twig. She thanked him, and went to her mother’s grave, and planted this twig there, weeping so bitterly that the tears fell upon it and watered it, and it flourished and became a fine tree. Cinderella went to see it three times a day, and wept and prayed, and each time a white bird rose up from the tree, and if she uttered any wish the bird brought her whatever she had wished for. Now it came to pass that the king ordained a festival that should last for three days, and to which all the beautiful young women of that country were bidden, so that the king’s son might choose a bride from among them. When the two stepdaughters heard that they too were invited, they felt very pleased, and they called Cinderella, and said, “Comb our hair, brush our shoes, and make our buckles fast, we are going to the wedding feast at the king’s castle.” Cinderella, when she heard this, could not help crying, for she too would have liked to go to the dance, and she begged her step-mother to allow her. “What, you Cinderella!” said she. “In all your dust and dirt, you want to go to the festival! You that have no dress and no shoes!” But as she persisted in asking, at last the step-mother said, “I have strewed a dish-full of lentils in the ashes, and if you can pick them all up again in two hours you may go with us.” Then the maiden went to the backdoor that led into the garden, and called out, “O gentle doves, O turtle-doves, and all the birds that be. The lentils that in ashes lie, come and pick up for me! The good must be put in the dish. The bad you may eat if you wish.” Then there came to the kitchen-window two white doves, and after them some turtle-doves, and at last a crowd of all the birds under heaven, chirping and fluttering, and they alighted among the ashes; and the doves nodded with their heads, and began to pick, peck, pick, peck, and then all the others began to pick, peck, pick, peck, and put all the good grains into the dish. Before an hour was over all was done, and they flew away. Then the maiden brought the dish to her step-mother, feeling joyful, and thinking that now she should go to the feast; but the step-mother said, “No, Cinderella, you have no proper clothes, and you do not know how to dance, and you would be laughed at!” And when Cinderella cried for disappointment, she added, “If you can pick two dishes full of lentils out of the ashes, nice and clean, you shall go with us,” thinking to herself 
that it wasn’t possible. When she had thrown two dishes full of lentils among the ashes the maiden went through the backdoor into the garden, and cried, “O gentle doves, O turtle-doves, and all the birds that be. The lentils that in ashes lie, come and pick up for me!”            So there came to the kitchen-window two white doves, and then some turtle-doves, and at last a crowd of all the other birds under heaven, chirping and fluttering, and they alighted among the ashes, and the doves nodded with their heads and began to pick, peck, pick, peck, and then all the others began to pick, peck, pick, peck, and put all the good grains into the dish. And before half-an-hour was over it was all done, and they flew away. Then the maiden took the dishes to the stepmother, feeling joyful, and thinking that now she should go with them to the feast; but she said: “All this is of no good to you; you cannot come with us, for you have no proper clothes, and cannot dance; you would put us to shame.” Then she turned her back on poor Cinderella, and made haste to set out with her two proud daughters. And as there was no one left in the house, Cinderella went to her mother’s grave, under the hazel bush, and cried,  “Little tree, little tree, shake over me, That silver and gold may come down and cover me.” Then the bird threw down a dress of gold and silver, and a pair of slippers embroidered with silk and silver. , And in all haste she put on the dress and went to the festival. But her step-mother and sisters did not know her, and thought she must be a foreign princess, she looked so beautiful in her golden dress. Of Cinderella they never thought at all, and supposed that she was sitting at home, arid picking the lentils out of the ashes. The King’s son came to meet her, and took her by the hand and danced with her, and he refused to stand up with anyone else, so that he might not be obliged to let go her hand; and when any one came to claim it he answered, “She is my partner.” And when the evening came she wanted to go home, but the prince said he would go with her to take care of her, for he wanted to see where the beautiful maiden lived. But she escaped him, and jumped up into the pigeon-house. Then the prince waited until the father came, and told him the strange maiden had jumped into the pigeon-house. The father thought to himself, “It cannot surely be Cinderella,” and called for axes and hatchets, and had the pigeon-house cut down, but there was no one in it. And when they entered the house there sat Cinderella in her dirty clothes among the cinders, and a little oil-lamp burnt dimly in the chimney; for Cinderella had been very quick, and had jumped out of the pigeon-house again, and had run to the hazel bush; and there she had taken off her beautiful dress and had laid it on the grave, and the bird had carried it away again, and then she had put on her little gray kirtle again, and had sat down in. the kitchen among the cinders. The next day, when the festival began anew, and the parents and step-sisters had gone to it, Cinderella went to the hazel bush and cried, “Little tree, little tree, shake over me, That silver and gold may come down and cover me.” Then the bird cast down a still more splendid dress than on the day before. And when she appeared in it among the guests everyone was astonished at her beauty. The prince had been waiting until she came, and he took her hand and danced with her alone. And when anyone else came to invite her he said, “She is my partner.” And when the evening came she wanted to go home, and the prince followed her, for he wanted to see to what house she belonged; but she broke away from him, and ran into the garden at the back of the house. There stood a fine large tree, bearing splendid pears; she leapt as lightly as a squirrel among the branches, and the prince did not know what had become of her. So he waited until the father came, and then he told him that the strange maiden had rushed from him, and that he thought she had gone up into the pear-tree. The father thought to himself, “It cannot surely be Cinderella,” and called for an axe, and felled the tree, but there was no one in it. And when they went into the kitchen there sat Cinderella among the cinders, as usual, for she had got down the other side of the tree, and had taken back her beautiful clothes to the bird on the hazel bush, and had put on her old grey kirtle again. On the third day, when the parents and the step-children had set off, Cinderella went again to her mother’s grave, and said to the tree, “Little tree, little tree, shake over me, That silver and gold may come down and cover me.” Then the bird cast down a dress, the like of which had never been seen for splendor and brilliancy, and slippers that were of gold. And when she appeared in this dress at the feast nobody knew what to say for wonderment. The prince danced with her alone, and if any- one else asked her he answered, “She is my partner.” 
And when it was evening Cinderella wanted to go home, and the prince was about to go with her, when she ran past him so quickly that he could not follow her. But he had laid a plan, and had caused all the steps to be spread with pitch, so that as she rushed down them the left shoe of the maiden remained sticking in it. The prince picked it up, and saw that it was of gold, and very small and slender. The next morning he went to the father and told him that none should be his bride save the one whose foot the golden shoe should fit. Then the two sisters were very glad, because they had pretty feet. The eldest went to her room to try on the shoe, and her mother stood by. But she could not get her great toe into it, for the shoe was too small; then her mother handed her a knife, and said, “Cut the toe off, for when you are queen you will never have to go on foot.” So the girl cut her toe off, squeezed her foot into the shoe, concealed the pain, and went down to the prince. Then he took her with him on his horse as his bride, and rode off. They had to pass by the grave, and there sat the two pigeons on the hazel bush, and cried, “There they go, there they go! There is blood on her shoe; The shoe is too small, Not the right bride at all!” Then the prince looked at her shoe, and saw the blood flowing. And he turned his horse round and took the false bride home again, saying she was not the right one, and that the other sister must try on the shoe. So she went into her room to do so, and got her toes comfortably in, but her heel was too large. Then her mother handed her the knife, saying, “Cut a piece off your heel; when you are queen you will never have to go on foot.” So the girl cut a piece off her heel, and thrust her foot into the shoe, concealed the pain, and went down to the prince, who took his bride before him on his horse and rode off. When they passed by the hazel bush the two pigeons sat there and cried,  “There they go, there they go! There is blood on her shoe; The shoe is too small, Not the right bride at all!” Then the prince looked at her foot, and saw how the blood was flowing from the shoe, and staining the white stocking. And he turned his horse round and brought the false bride home again. “This is not the right one,” said he, “have you no other daughter?” “No,” said the man, “only my dead wife left behind her a little girl, Cinderella; it is impossible that she can be the bride.” But the King’s son ordered her to be sent for, but the mother said, “Oh no! she is much too dirty, I could not let her be seen.” But he had her fetched, and so Cinderella had to appear. First she washed her face and hands quite clean, and went in and curtseyed to the prince, who held out to her the golden shoe. Then she sat down on a stool, drew her foot out of the heavy wooden shoe, and slipped it into the golden one, which fitted it perfectly. And when she stood up, and the prince looked in her face, he knew again the beautiful maiden that had danced with him, and he cried, “This is the right bride!” The step-mother and the two sisters were thunderstruck, and grew pale with anger; but he put Cinderella before him on his horse and rode off. And as they passed the hazel bush, the two white pigeons cried,  “There they go, there they go! No blood on her shoe; The shoe’s not too small, The right bride is she after all.” And when they had thus cried, they came flying after and perched on Cinderella’s shoulders, one on the right, the other on the left, and so remained. And when her wedding with the prince was to be held the false sisters came, hoping to curry favor, and to take part in the festivities. So as the bridal procession went to the church, the eldest walked on the right side and the younger on the left, and the pigeons picked out an eye of each of them. And as they returned the elder was on the left side and the younger on the right, and the pigeons picked out the other eye of each of them. And so they were condemned to go blind for the rest of their days because of their wickedness and falsehood.
 )  # /////////////////////////////henamomken t7to l text lly htsht8lo 3leh 3la tol


output = re.sub('([\n\r\t ]{2,})', ' ', text)
rake_object = RAKE.Rake(RAKE.SmartStopList())
All_keywords = rake_object.run(output, maxWords=2)
#####################################
nlp = spacy.load('en_core_web_lg')
neuralcoref.add_to_pipe(nlp)
doc = nlp(output)
output = doc._.coref_resolved  ############# el text elly m3aya dlw2ty m3mol replacy le kol damer
doc = nlp(output)
# Extract keywords
for word in All_keywords:
    if word[1] >= 4:
        Rakelist.append(word[0])
for ent in doc.ents:
    keyword_dic_NER[ent.text] = [ent.label_]
#########################
for word in Rakelist:
    for sent in doc.sents:
        tmp_sent = str(sent)
        if " " not in tmp_sent:
            if word in str(tmp_sent):
                tmpword = " " + word + " "
                qustions.append(tmp_sent.replace(tmpword, "........"))
                answers.append(word)
        else:
            if word in str(tmp_sent):
                qustions.append(tmp_sent.replace(word, "........"))
                answers.append(word)
for word in keyword_dic_NER.keys():
    sents = []
    for sent in doc.sents:
        tmp_sent = str(sent)
        if " " not in tmp_sent:
            if word in str(tmp_sent):
                tmpword = " " + word + " "
                sents.append(tmp_sent)
                qustions.append(tmp_sent.replace(tmpword, "........"))
                answers.append(word)
        else:
            if word in str(tmp_sent):
                sents.append(tmp_sent)
                qustions.append(tmp_sent.replace(word, "........"))
                answers.append(word)
    keyword_dic_sents[word] = sents
###################
# print(Rakelist)
# print(keyword_dic_NER)
# print(keyword_dic_sents)
# print(qustions)
# print(answers)
'''
# **********************************************************End Keyword extraction*****************************************

############################################################################################################################
############################################################################################################################
############################################################################################################################

# **********************************************************  Gen Modal Questions*****************************************
############### global var###################


dic_tmp = {}  # dictionary carries the Modal Questions Generated
dic1 = {}  # Simple dictionary carries simple sentens
keyword_Questions_dic = {}
distractors_dic = {}  # dictionary carries the distractors for each word
Y_N_Question_dic = {}  # dictionary carries finally Yes or No questions
lemmatizer = WordNetLemmatizer()
md_word = 'ad'  # string used in Modal verb below
a = 'a'  # a dummy var used
questions = list()
answers = []
Y_N_Ques = []
Y_N_List = []
################### End Global Var#########

# Load English tokenizer, tagger, parser, NER and word vectors
# nlp = spacy.load("en_core_web_sm")
########################################### LISTS #############################################
#############VBN List############## verb to have
VBN1 = ['NNP', 'VBZ', 'VBN']
VBN2 = ['PRP', 'VBZ', 'VBN']
VBN3 = ['NNPS', 'VBP', 'VBN']
VBN4 = ['PRP', 'VBP', 'VBN']
VBN5 = ['NNP', 'VBD', 'VBN']
VBN6 = ['PRP', 'VBD', 'VBN']
VBN7 = ['NNPS', 'VBD', 'VBN']
VBN8 = ['NNS', 'VBP', 'VBN']
VBN9 = ['NN', 'VBZ', 'VBN']
VBN10 = ['NNS', 'VBD', 'VBN']
VBN11 = ['NN', 'VBD', 'VBN']
#############End VBN List##############

### present continous Lists ###
PRC1 = ['NNP', 'VBZ', 'VBG', 'NN']  # Mina is playing football
PRCIN1 = ['NNP', 'VBG', 'VBZ', 'NN', 'IN', 'NN']  # Mina is playing football in club
PRCDT1 = ['NNP', 'VBG', 'VBZ', 'NN', 'IN', 'DT', 'NN']  # Mina is playing football in the club
PRC2 = ['NNPS', 'VBP', 'VBG', 'NN']  # Ali and Hazem  are playing football
PRCIN2 = ['NNPS', 'VBG', 'VBP', 'NN', 'IN', 'NN']  # Mina and Omar are playing football in club
PRCDT2 = ['NNPS', 'VBG', 'VBP', 'NN', 'IN', 'DT', 'NN']  # Mina and Omar are playing football in the club
PRC3 = ['PRP', 'VBZ', 'VBG', 'NN']  # He is playing football
PRCIN3 = ['PRP', 'VBG', 'VBZ', 'NN', 'IN', 'NN']  # He is playing football in club
PRCDT3 = ['PRP', 'VBG', 'VBZ', 'NN', 'IN', 'DT', 'NN']  # He is playing football in the club
PRC4 = ['PRP', 'VBP', 'VBG', 'NN']  # They are playing football
PRCIN4 = ['PRP', 'VBG', 'VBP', 'NN', 'IN', 'NN']  # They are playing football in club
PRCDT4 = ['PRP', 'VBG', 'VBP', 'NN', 'IN', 'DT', 'NN']  # They are playing football in the club
PRC5 = ['NN', 'VBG', 'VBZ', 'NN']  # cat is making voice
PRCIN5 = ['NN', 'VBG', 'VBZ', 'NN', 'IN', 'NN']  # cat is making voice in room
PRCDT5 = ['NN', 'VBG', 'VBZ', 'NN', 'IN', 'DT', 'NN']  # cat is making voice in the room
PRC6 = ['NNS', 'VBG', 'VBP', 'NN']  # cats are making voice
PRCIN6 = ['NNS', 'VBG', 'VBP', 'NN', 'IN', 'NN']  # cats are making voice in room
PRCDT6 = ['NNS', 'VBG', 'VBP', 'NN', 'IN', 'DT', 'NN']  # cats are making voice in the room
### end present continous Lists ###

### past continous Lists ##
PAC1 = ['NNP', 'VBD', 'VBG', 'NN']  # Mina was playing football
PACIN1 = ['NNP', 'VBG', 'VBD', 'NN', 'IN', 'NN']  # Mina was playing football in club
PACDT1 = ['NNP', 'VBG', 'VBD', 'NN', 'IN', 'DT', 'NN']  # Mina was playing football in the club
PAC2 = ['NNPS', 'VBD', 'VBG', 'NN']  # Ali and Hazem  were playing football
PACIN2 = ['NNPS', 'VBG', 'VBD', 'NN', 'IN', 'NN']  # Mina and Omar were playing football in club
PACDT2 = ['NNPS', 'VBG', 'VBD', 'NN', 'IN', 'DT', 'NN']  # Mina and Omar were playing football in the club
PAC3 = ['PRP', 'VBD', 'VBG', 'NN']  # He was playing football
PACIN3 = ['PRP', 'VBG', 'VBD', 'NN', 'IN', 'NN']  # He was playing football in club
PACDT3 = ['PRP', 'VBG', 'VBD', 'NN', 'IN', 'DT', 'NN']  # He was playing football in the club
PAC4 = ['PRP', 'VBD', 'VBG', 'NN']  # They were playing football
PACIN4 = ['PRP', 'VBG', 'VBD', 'NN', 'IN', 'NN']  # They were playing football in club
PACDT4 = ['PRP', 'VBG', 'VBD', 'NN', 'IN', 'DT', 'NN']  # They were playing football in the club
PAC5 = ['NN', 'VBG', 'VBD', 'NN']  # cat was making voice
PACIN5 = ['NN', 'VBG', 'VBD', 'NN', 'IN', 'NN']  # cat was making voice in room
PACDT5 = ['NN', 'VBG', 'VBD', 'NN', 'IN', 'DT', 'NN']  # cat was making voice in the room
PAC6 = ['NNS', 'VBG', 'VBD', 'NN']  # cats were making voice
PACIN6 = ['NNS', 'VBG', 'VBD', 'NN', 'IN', 'NN']  # cats were making voice in room
PACDT6 = ['NNS', 'VBG', 'VBD', 'NN''IN', 'DT', 'NN']  # cats were making voice in the room

### end past continous Lists ##

########## present simple Lists ############
PRS1 = ['NNP', 'VBZ', 'NN']  # Mina plays football
PRSIN1 = ['NNP', 'VBZ', 'NN', 'IN', 'NN']  # Mina plays football in club ---------------momkn Mina plays club XD:
PRSDT1 = ['NNP', 'VBZ', 'NN', 'IN', 'DT', 'NN']  # Mina plays football in the club
PRS2 = ['PRP', 'VBZ', 'NN']  # He plays football
PRSIN2 = ['PRP', 'VBZ', 'NN', 'IN', 'NN']  # He plays football in club
PRSDT2 = ['PRP', 'VBZ', 'NN', 'IN', 'DT', 'NN']  # He plays football in the club
PRS3 = ['NNPS', 'VBP', 'NN']  # Hazem and Noura play football
PRSIN3 = ['NNPS', 'VBP', 'NN', 'IN', 'NN']  # Hazem and Noura play football in club
PRSDT3 = ['NNPS', 'VBP', 'NN', 'IN', 'DT', 'NN']  # Hazem and Noura play football in the club
PRS4 = ['PRP', 'VBP', 'NN']  # They play football
PRSIN4 = ['PRP', 'VBP', 'NN', 'IN', 'NN']  # They play football in club
PRSDT4 = ['PRP', 'VBP', 'NN', 'IN', 'DT', 'NN']  # They play football in the club
PRS5 = ['NN', 'VBZ', 'NN']  # cat makes voice
PRSIN5 = ['NN', 'VBZ', 'NN', 'IN', 'NN']  # cat makes voice in room
PRSDT5 = ['NN', 'VBZ', 'NN', 'IN', 'DT', 'NN']  # cat makes voice in the room
PRS6 = ['NNS', 'VBP', 'NN']  # cats make voice
PRSIN6 = ['NNS', 'VBP', 'NN', 'IN', 'NN']  # cats make voice in room
PRSDT6 = ['NNS', 'VBP', 'NN', 'IN', 'DT',
          'NN']  # cats make voice in the room --------------------------------------------

########### End present simple Lists #########

########### past simple Lists #################
PAS1 = ['NNP', 'VBD', 'NN']  # Mina played football
PASIN1 = ['NNP', 'VBD', 'NN', 'IN', 'NN']  # Mina played football in club ---------------momkn Mina played club XD:
PASDT1 = ['NNP', 'VBD', 'NN', 'IN', 'DT', 'NN']  # Mina played football in the club
PAS2 = ['PRP', 'VBD', 'NN']  # He played football
PASIN2 = ['PRP', 'VBD', 'NN', 'IN', 'NN']  # He played football in club
PASDT2 = ['PRP', 'VBD', 'NN', 'IN', 'DT', 'NN']  # He played football in the club
PAS3 = ['NNPS', 'VBD', 'NN']  # Hazem and Noura played football
PASIN3 = ['NNPS', 'VBD', 'NN', 'IN', 'NN']  # Hazem and Noura played football in club
PASDT3 = ['NNPS', 'VBD', 'NN', 'IN', 'DT', 'NN']  # Hazem and Noura played football in the club
PAS4 = ['PRP', 'VBD', 'NN']  # They played football
PASIN4 = ['PRP', 'VBD', 'NN', 'IN', 'NN']  # They played football in club
PASDT4 = ['PRP', 'VBD', 'NN', 'IN', 'DT', 'NN']  # They played football in the club
PAS5 = ['NN', 'VBD', 'NN']  # cat made voice
PASIN5 = ['NN', 'VBD', 'NN', 'IN', 'NN']  # cat made voice in room
PASDT5 = ['NN', 'VBD', 'NN', 'IN', 'DT', 'NN']  # cat made voice in the room
PAS6 = ['NNS', 'VBD', 'NN']  # cats made voice
PASIN6 = ['NNS', 'VBD', 'NN', 'IN', 'NN']  # cats made voice in room
PASDT6 = ['NNS', 'VBD', 'NN', 'IN', 'DT', 'NN']  # cats made voice in the room

##########End past simple Lists ############


########### MD Lists ###########
MD1 = ['MD', 'NNP', 'VB', 'NN']  # Mina will play football
MD2 = ['MD', 'PRP', 'VB', 'NN']  # He will play football
MD3 = ['MD', 'NNPS', 'VB', 'NN']  # Mina and Omar will play football
MD4 = ['MD', 'PRP', 'VB', 'NN']  # They will play football
MD5 = ['MD', 'NN', 'VB']  # Machine will produce product ----------------------
MD6 = ['MD', 'NNS', 'VB', 'NN']  # Machines will produce product ---------------------------------
############End MD Lists #########

####JJ####
JJ1 = ['NNP', 'VBZ', 'JJ']  # Mina is tall
JJ2 = ['NNPS', 'VBP', 'JJ']  # Mina and Ali are tall
JJ3 = ['PRP', 'VBZ', 'JJ']  # He is tall
JJ4 = ['PRP', 'VBP', 'JJ']  # They are tall
JJ5 = ['NN', 'VBZ', 'JJ']  # Tree is tall
JJ6 = ['NNS', 'VBP', 'JJ']  # Trees are tall


########################################### End LISTS #############################################


# *************************************************Generate Modal Questions **************************************************************

def gen_Modal_Question(keyword_dic_sents):
    """
     outputs question from the given text
    """
    try:
        # txt = TextBlob(string)
        # for line in txt.sentences:
        for key in keyword_dic_sents.keys():
            """
               outputs question from the given text
               """
            # print(keyword_dic_sents[line])
            # print(entity.text, entity.label_)

            answers.append(key)
            # print(key)
            for sentence in keyword_dic_sents[key]:
                # print(sentence)
                if type(sentence) is str:  # If the passed variable is of type string.
                    line = TextBlob(sentence)  # Create object of type textblob.blob.TextBlob
                # print(line)
                bucket = {}  # Create an empty dictionary

                for i, j in enumerate(line.tags):  # line.tags are the parts-of-speach in English
                    if j[1] not in bucket:
                        bucket[j[1]] = i  # Add all tags to the dictionary or bucket variable

                question = ''  # Create an empty string

                # With the use of conditional statements the dictionary is compared with the list created above
                # print(line.tags)
                #####################################################################gen modal ##########################################################################################
                ######################################## VBN ##################################################
                if all(key in bucket for key in VBN1):  # 'NNP', 'VBZ'  ,'VBN' in sentence.
                    question = 'Has' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN1')
                    questions.append(question)

                elif all(key in bucket for key in VBN2):  # 'PRP', 'VBZ'  ,'VBN' in sentence.
                    question = 'Has' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN2')
                    questions.append(question)

                elif all(key in bucket for key in VBN3):  # 'NNP', 'VBP'  ,'VBN' in sentence.
                    question = 'Have' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN3')
                    questions.append(question)

                elif all(key in bucket for key in VBN4):  # 'PRP', 'VBP'  ,'VBN' in sentence.

                    question = 'Have' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN4')
                    questions.append(question)

                elif all(key in bucket for key in VBN5):  # 'NNP', 'VBD'  ,'VBN' in sentence.
                    question = 'Had' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN5')
                    questions.append(question)

                elif all(key in bucket for key in VBN6):  # 'PRP', 'VBD'  ,'VBN' in sentence.
                    question = 'Had' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN6')
                    questions.append(question)

                elif all(key in bucket for key in VBN7):  # 'NNPS', 'VBD'  ,'VBN' in sentence.
                    question = 'Had' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN7')
                    questions.append(question)
                elif all(key in bucket for key in VBN8):  # 'NNPS', 'VBD'  ,'VBN' in sentence.
                    question = 'Have' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('VBN8')
                    questions.append(question)
                elif all(key in bucket for key in VBN9):  # 'NNPS', 'VBD'  ,'VBN' in sentence.
                    question = 'Has' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + '?'
                    # print('VBN9')
                    questions.append(question)
                elif all(key in bucket for key in VBN10):  # 'NNPS', 'VBD'  ,'VBN' in sentence.
                    question = 'Had' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + '?'
                    # print('VBN10')
                    questions.append(question)
                elif all(key in bucket for key in VBN11):  # 'NNPS', 'VBD'  ,'VBN' in sentence.
                    question = 'Had' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBN']] + ' ' + '?'
                    # print('VBN11')
                    questions.append(question)
                ########################################### End VBN ##################################?????????????????????????!!!!!!!!!!!!!!!!!!'''

                ########################################### present continouse #############################
                elif all(key in bucket for key in PRC1):  # 'NNP', 'VBG', 'VBZ', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRC1")
                    questions.append(question)

                elif all(key in bucket for key in PRCIN1):  # 'NNP', 'VBG', 'VBZ', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCIN1")
                    questions.append(question)

                elif all(key in bucket for key in PRCDT1):  # 'NNP', 'VBG', 'VBZ', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCDT1")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRC2):  # 'NNP', 'VBG', 'VBZ' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRC2")
                    questions.append(question)

                elif all(key in bucket for key in PRCIN2):  # 'NNP', 'VBG', 'VBZ' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCIN2")
                    questions.append(question)

                elif all(key in bucket for key in PRCDT2):  # 'NNP', 'VBG', 'VBZ' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCDT2")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRC3):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRC3")
                    questions.append(question)

                elif all(key in bucket for key in PRCIN3):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCIN3")
                    questions.append(question)

                elif all(key in bucket for key in PRCDT3):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCDT3")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRC4):  # 'NNPS', 'VBG', 'VBP' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRC4")
                    questions.append(question)

                elif all(key in bucket for key in PRCIN4):  # 'NNPS', 'VBG', 'VBP' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCIN4")
                    questions.append(question)

                elif all(key in bucket for key in PRCDT4):  # 'NNPS', 'VBG', 'VBP' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCDT4")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRC5):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + "anything" + ' ' + '?'
                    # print("PRC5")
                    questions.append(question)

                elif all(key in bucket for key in PRCIN5):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + "anything" + ' ' + '?'
                    # print("PRCIN5")
                    questions.append(question)

                elif all(key in bucket for key in PRCDT5):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['IN']] + ' ' + "anything" + ' ' + '?'
                    # print("PRCDT5")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRC6):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRC6")
                    questions.append(question)

                elif all(key in bucket for key in PRCIN6):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCIN6")
                    questions.append(question)

                elif all(key in bucket for key in PRCDT6):  # 'NNPS', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PRCDT6")
                    questions.append(question)

                ########################## Past Cont. ###################################

                elif all(key in bucket for key in PAC1):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Was' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PAC1")
                    questions.append(question)

                elif all(key in bucket for key in PACIN1):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Was' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PACIN1")
                    questions.append(question)

                elif all(key in bucket for key in PACDT1):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Was' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PACDT1")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PAC2):  # 'NNP', 'VBG', 'VBD', 'IN' in sentence.
                    question = 'Were' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PAC2")
                    questions.append(question)

                elif all(key in bucket for key in PACIN2):  # 'NNP', 'VBG', 'VBD', 'IN' in sentence.
                    question = 'Were' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PACIN2")
                    questions.append(question)

                elif all(key in bucket for key in PACDT2):  # 'NNP', 'VBG', 'VBD', 'IN' in sentence.
                    question = 'Were' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PACDT2")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PAC3):  # 'NNP', 'VBG', 'VBD' in sentence.
                    if line.words[bucket['PRP']] in ['he', 'she', 'it']:
                        question = 'Was' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print("PAC3")
                        questions.append(question)

                elif all(key in bucket for key in PACIN3):  # 'NNP', 'VBG', 'VBD' in sentence.
                    if line.words[bucket['PRP']] in ['he', 'she', 'it']:
                        question = 'Was' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print("PACIN3")
                        questions.append(question)

                elif all(key in bucket for key in PACDT3):  # 'NNP', 'VBG', 'VBD' in sentence.
                    if line.words[bucket['PRP']] in ['he', 'she', 'it']:
                        question = 'Was' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print("PACDT3")
                        questions.append(question)
                        # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PAC4):  # 'NNPS', 'VBG', 'VBD' in sentence.
                    if line.words[bucket['PRP']] in ['i', 'you', 'we', 'they']:
                        question = 'Were' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print("PAC4")
                        questions.append(question)

                elif all(key in bucket for key in PACIN4):  # 'NNPS', 'VBG', 'VBD' in sentence.
                    if line.words[bucket['PRP']] in ['i', 'you', 'we', 'they']:
                        question = 'Were' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print("PACIN4")
                        questions.append(question)

                elif all(key in bucket for key in PACDT4):  # 'NNPS', 'VBG', 'VBD' in sentence.
                    if line.words[bucket['PRP']] in ['i', 'you', 'we', 'they']:
                        question = 'Were' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print("PACDT4")
                        questions.append(question)
                        # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PAC5):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Was' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + "anything" + ' ' + '?'
                    # print("PAC5")
                    questions.append(question)

                elif all(key in bucket for key in PACIN5):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Was' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['IN']] + ' ' + "anything" + ' ' + '?'
                    # print("PACIN5")
                    questions.append(question)

                elif all(key in bucket for key in PACDT5):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Was' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['IN']] + ' ' + "anything" + ' ' + '?'
                    # print("PACDT5")
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PAC6):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Were' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PAC6")
                    questions.append(question)

                elif all(key in bucket for key in PACIN6):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Were' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PACIN6")
                    questions.append(question)

                elif all(key in bucket for key in PACDT6):  # 'PRP', 'VBG', 'VBP', 'IN' in sentence.
                    question = 'Were' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBG']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print("PACDT6")
                    questions.append(question)

                ############################## Present Simple ######################################
                elif all(key in bucket for key in PRS1):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Does' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRS1')
                    questions.append(question)

                elif all(key in bucket for key in PRSIN1):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Does' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSIN1')
                    questions.append(question)

                elif all(key in bucket for key in PRSDT1):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Does' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSDT1')
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRS2):  # 'NNP', 'VBZ' in sentence.
                    question = 'Does ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRS2')
                    questions.append(question)

                elif all(key in bucket for key in PRSIN2):  # 'NNP', 'VBZ' in sentence.
                    question = 'Does ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSIN2')
                    questions.append(question)

                elif all(key in bucket for key in PRSDT2):  # 'NNP', 'VBZ' in sentence.
                    question = 'Does ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSDT2')
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRS3):  # 'NNPS', 'VBP', 'NN' in sentence
                    question = 'Do' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRS3')
                    questions.append(question)

                elif all(key in bucket for key in PRSIN3):  # 'NNPS', 'VBP', 'NN' in sentence
                    question = 'Do' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSIN3')
                    questions.append(question)

                elif all(key in bucket for key in PRSDT3):  # 'NNPS', 'VBP', 'NN' in sentence
                    question = 'Do' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSDT3')
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRS4):  # 'NNP', 'VBZ' in sentence.
                    question = 'Do ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRS4')
                    questions.append(question)

                elif all(key in bucket for key in PRSIN4):  # 'NNP', 'VBZ' in sentence.
                    question = 'Do ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSIN4')
                    questions.append(question)

                elif all(key in bucket for key in PRSDT4):  # 'NNP', 'VBZ' in sentence.
                    question = 'Do ' + line.words[bucket['PRP']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSDT4')
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRS5):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Does' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + '?'
                    # print('PRS5')
                    questions.append(question)

                elif all(key in bucket for key in PRSIN5):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Does' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['IN']] + ' ' + "anything" + ' ' + '?'
                    # print('PRSIN5')
                    questions.append(question)

                elif all(key in bucket for key in PRSDT5):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Does' + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VBZ']].singularize() + ' ' + line.words[bucket['IN']] + ' ' + "anything" + ' ' + '?'
                    # print('PRSDT5')
                    questions.append(question)
                    # -----------------------------------------------------------------------------------------------------------#
                elif all(key in bucket for key in PRS6):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Do' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRS6')
                    questions.append(question)

                elif all(key in bucket for key in PRSIN6):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Do' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSIN6')
                    questions.append(question)

                elif all(key in bucket for key in PRSDT6):  # 'NNP', 'VBZ', 'NN' in sentence
                    question = 'Do' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[
                        bucket['VBP']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('PRSDT6')
                    questions.append(question)
                    ########################################### End present simple #################################

                ##################################################### MD ###########################################
                elif all(key in bucket for key in MD1):  # 'NNP', 'VB' in sentence.
                    md_word = line.words[bucket['MD']]
                    question = md_word.capitalize() + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
                        bucket['VB']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('MD1')
                    questions.append(question)

                elif all(key in bucket for key in MD2):  # 'PRP', 'VB' in sentence.
                    if line.words[bucket['PRP']] in ['he', 'she', 'it']:
                        md_word = line.words[bucket['MD']]
                        question = md_word.capitalize() + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VB']].singularize() + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print('MD2')
                        questions.append(question)

                elif all(key in bucket for key in MD3):  # 'NNPS', 'VB' in sentence.
                    md_word = line.words[bucket['MD']]
                    question = md_word.capitalize() + ' ' + line.words[
                        bucket['NNPS']] + ' ' + line.words[bucket['VB']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                    # print('MD3')
                    questions.append(question)

                elif all(key in bucket for key in MD4):  # 'NNS', 'VB' in sentence.
                    if line.words[bucket['PRP']] in ['i', 'you', 'we', 'they']:
                        md_word = line.words[bucket['MD']]
                        question = md_word.capitalize() + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
                            bucket['VB']] + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        # print('MD4')
                        questions.append(question)

                elif all(key in bucket for key in MD5):  # 'NNP', 'VB' in sentence.
                    md_word = line.words[bucket['MD']]
                    question = md_word.capitalize() + ' ' + line.words[bucket['NN']] + ' ' + line.words[
                        bucket['VB']].singularize() + ' ' + "anything" + ' ' + '?'
                    # print('MD5')
                    questions.append(question)

                elif all(key in bucket for key in MD6):  # 'NNP', 'VB' in sentence.
                    md_word = line.words[bucket['MD']]
                    question = md_word.capitalize() + ' ' + line.words[
                        bucket['NNS']] + ' ' + line.words[bucket['VB']].singularize() + ' ' + line.words[
                                   bucket['NN']] + ' ' + '?'
                    # print('MD6')
                    questions.append(question)
                    ####################################### End MD ###############################################
                    ###################################### JJ ####################################################
                elif all(key in bucket for key in JJ1):  # 'NNP', 'VB' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['JJ']] + '?'
                    # print('JJ1')
                    questions.append(question)

                elif all(key in bucket for key in JJ2):  # 'PRP', 'VB' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNPS']] + ' ' + line.words[bucket['JJ']] + '?'
                    # print('JJ2')
                    questions.append(question)

                elif all(key in bucket for key in JJ3):  # 'NNPS', 'VB' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[bucket['JJ']] + '?'
                    # print('JJ3')
                    questions.append(question)

                elif all(key in bucket for key in JJ4):  # 'NNPS', 'VB' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['PRP']] + ' ' + line.words[bucket['JJ']] + '?'
                    # print('JJ4')
                    questions.append(question)

                elif all(key in bucket for key in JJ5):  # 'NNS', 'VB' in sentence.
                    question = 'Is' + ' ' + line.words[bucket['NN']] + ' ' + line.words[bucket['JJ']] + '?'
                    # print('JJ5')
                    questions.append(question)

                elif all(key in bucket for key in JJ6):  # 'NNS', 'VB' in sentence.
                    question = 'Are' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[bucket['JJ']] + '?'
                    # print('JJ6')
                    questions.append(question)
                ####################################### END JJ ###########################################################
                ########################################### Past simple #################################
                try:
                    if all(key in bucket for key in PAS1):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNP']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PAS1')
                            questions.append(question)

                    elif all(key in bucket for key in PASIN1):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNP']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PASIN1')
                            questions.append(question)

                    elif all(key in bucket for key in PASDT1):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did' + line.words[bucket['NNP']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PASDT1')
                            questions.append(question)
                        # -----------------------------------------------------------------------------------------------------------#
                    elif all(key in bucket for key in PAS2):  # 'NNP', 'VBZ' in sentence.
                        if line.words[bucket['PRP']] in ['he', 'she', 'it']:
                            question = 'Did ' + line.words[
                                bucket['PRP']] + ' ' + lemmatizer.lemmatize(
                                line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                            if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                                a = 'a'
                            else:
                                # print('PAS2')
                                questions.append(question)

                    elif all(key in bucket for key in PASIN2):  # 'NNP', 'VBZ' in sentence.
                        if line.words[bucket['PRP']] in ['he', 'she', 'it']:
                            question = 'Did ' + line.words[
                                bucket['PRP']] + ' ' + lemmatizer.lemmatize(
                                line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                            if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                                a = 'a'
                            else:
                                # print('PASIN2')
                                questions.append(question)

                    elif all(key in bucket for key in PASDT2):  # 'NNP', 'VBZ' in sentence.
                        if line.words[bucket['PRP']] in ['he', 'she', 'it']:
                            question = 'Did ' + line.words[
                                bucket['PRP']] + ' ' + lemmatizer.lemmatize(
                                line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                            if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                                a = 'a'
                            else:
                                print('PASDT2')
                                questions.append(question)
                            # -----------------------------------------------------------------------------------------------------------#
                    elif all(key in bucket for key in PAS3):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNPS']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PAS3')
                            questions.append(question)

                    elif all(key in bucket for key in PASIN3):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNPS']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PASIN3')
                            questions.append(question)

                    elif all(key in bucket for key in PASDT3):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNPS']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PASDT3')
                            questions.append(question)
                        # -----------------------------------------------------------------------------------------------------------#
                    elif all(key in bucket for key in PAS4):  # 'NNP', 'VBZ' in sentence.
                        if line.words[bucket['PRP']] in ['i', 'you', 'we', 'they']:
                            question = 'Did ' + line.words[
                                bucket['PRP']] + ' ' + lemmatizer.lemmatize(
                                line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                            if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                                a = 'a'
                            else:
                                # print('PAS4')
                                questions.append(question)

                    elif all(key in bucket for key in PASIN4):  # 'NNP', 'VBZ' in sentence.
                        if line.words[bucket['PRP']] in ['i', 'you', 'we', 'they']:
                            question = 'Did ' + line.words[
                                bucket['PRP']] + ' ' + lemmatizer.lemmatize(
                                line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                            if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                                a = 'a'
                            else:
                                # print('PASIN4')
                                questions.append(question)

                    elif all(key in bucket for key in PASDT4):  # 'NNP', 'VBZ' in sentence.
                        if line.words[bucket['PRP']] in ['i', 'you', 'we', 'they']:
                            question = 'Did ' + line.words[
                                bucket['PRP']] + ' ' + lemmatizer.lemmatize(
                                line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                            if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                                a = 'a'
                            else:
                                # print('PASDT4')
                                questions.append(question)
                            # -----------------------------------------------------------------------------------------------------------#
                    elif all(key in bucket for key in PAS5):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NN']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + "anything" + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PAS5')
                            questions.append(question)

                    elif all(key in bucket for key in PASIN5):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NN']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + "anything" + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PASIN5')
                            questions.append(question)


                    elif all(key in bucket for key in PASDT5):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NN']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + "anything" + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PASDT5')
                            questions.append(question)
                        # -----------------------------------------------------------------------------------------------------------#
                    elif all(key in bucket for key in PAS6):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNS']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PAS6')
                            questions.append(question)

                    elif all(key in bucket for key in PASIN6):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNS']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            # print('PASIN6')
                            questions.append(question)

                    elif all(key in bucket for key in PASDT6):  # 'NNP', 'VBZ' in sentence.
                        question = 'Did ' + line.words[bucket['NNS']] + ' ' + lemmatizer.lemmatize(
                            line.words[bucket['VBD']], pos="v") + ' ' + line.words[bucket['NN']] + ' ' + '?'
                        if (lemmatizer.lemmatize(line.words[bucket['VBD']], pos="v") == 'be'):
                            a = 'a'
                        else:
                            print('PASDT6')
                            questions.append(question)
                    else:
                        a = 'a'

                except:
                    a = 'a'
                ############################################### End past simple #####################################
                # When the tags are generated 's is split to ' and s. To overcome this issue.
                if 'VBZ' in bucket and line.words[bucket['VBZ']] == "’":
                    question = question.replace(" ’ ", "'s ")
                    questions.append(question)

                # Print the genetated questions as output.
                # if question != '':
                # print('\n', 'Question: ' + question)
            keyword_Questions_dic[key] = questions.copy()
            questions.clear()


    except:
        # print(' ')
        print("No Modal Questions Generated! Please revise your text.")
        # keyword_Questions_dic[key] = "No Modal Questions Generated! Please revise your text."

    return (keyword_Questions_dic)


# ********************************************************** End Gen Modal Questions*****************************************

############################################################################################################################
############################################################################################################################
############################################################################################################################

# ********************************************************** Gen Yes or NO Questions*****************************************

def gen_y_N_Question(dic_tmp, distractors_dic):
    # Y_N_Question_dic = copy.deepcopy(dic_tmp)
    random_numer = random.randint(0, 2)  # to choose one distractor randomly form 3 distractors

    for key in dic_tmp:  # for every key in dic
        old_word = key  # the original keyword
        new_word = distractors_dic[key][random_numer]  # randomly choose a distractor
        key_len = len(dic_tmp[key])  # number of questions related to this key

        for ques in range(key_len):  # for each questions related to this key
            correct_Ques = dic_tmp[key][ques]  # the original question
            if (
                    key in correct_Ques):  # if the key substring of correct question? ; because when sentence converted to ques it sometimes does not still contain the key!
                fake_Ques = correct_Ques.replace(old_word, new_word)  # construct the fake question
                dic_tmp[key][ques] = [correct_Ques, 'Yes', fake_Ques, 'No']  # append the correct and incorrect question
            else:
                dic_tmp[key][ques] = [correct_Ques, 'Yes', correct_Ques,
                                      'Yes']  # this case appends the correct question only ,because no fake question had been constructed
    return (dic_tmp)


# **********************************************************End Gen Yes or NO Questions*****************************************

############################################################################################################################
############################################################################################################################
############################################################################################################################

# ********************************************************** Gen distractors*****************************************

# it's simulated dictionary as the output of  distractors Generation task
distractors_dic['two'] = ['one', 'four', 'five']
distractors_dic['morning to night'] = ['evening to night', 'morning to morning', 'night to night']
distractors_dic['early in the morning'] = ['early in the evening', 'late in the evening', 'early in the night']
distractors_dic['day'] = ['hour', 'week', 'year']
distractors_dic['Cinderella'] = ['Snow_White', 'Rabinzill', 'Yassmin']
distractors_dic['one day'] = ['one hour', 'one week ', 'one year ']
distractors_dic['one'] = ['two', 'three', 'four']
distractors_dic['first'] = ['second', 'third', 'fourth']
distractors_dic['three'] = ['one', 'four', 'five']
distractors_dic['three days'] = ['three hour', 'three week', 'three year']
distractors_dic['Comb'] = ['Miror', 'Ring', 'Cup']
distractors_dic['two hours'] = ['two days', 'two weeks', 'two years']
distractors_dic['half-an-hour'] = ['half-an-days', 'half-an-weeks', 'half-an-years']
distractors_dic['The King’s'] = ['The boy’s', 'The queen’s', 'The child’s']
distractors_dic['The next day'] = ['The next hour', 'The next week', 'The next year']
distractors_dic['the day before'] = ['the hour before', 'the week before', 'the year before']
distractors_dic['the third day'] = ['the first day', ' the second day', 'the fourth day']
distractors_dic['The next morning'] = ['The last morning', 'The following morning', 'this morning']
distractors_dic['First'] = ['Second', 'Third', 'Fourth']
distractors_dic['two pigeons days'] = ['two pigeons hours', 'two pigeons weeks', 'two pigeons years']


# ********************************************************** End Gen distractors*****************************************
##############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################
########################################################## Convert dic to list ##########################################################################
def convert_dic_List(Y_N_Question_dic):
    for key in Y_N_Question_dic:
        for sent in Y_N_Question_dic[key]:
            if (sent[3] == 'No'):  # this condition prevent repetetion
                Y_N_Ques = [sent[0], ["Yes", "No"], sent[
                    1]]  # sent[0] is the correct question ,["Yes" , "No"] is the option list , and sent[1] the 'yes' answer
                Y_N_List.append(Y_N_Ques)
                Y_N_Ques = [sent[2], ["Yes", "No"], sent[
                    3]]  # sent[2] is the fake question ,["Yes" , "No"] is the option list ,and sent[3] the 'no' answer
                Y_N_List.append(Y_N_Ques)
    return Y_N_List


########################################################## End Convert dic to list ############################################################
###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################


# **********************************************************write_Y_N_qustions*****************************************
def write_Y_N_qustions(Y_N_List):
    f = open("/content/drive/My Drive/Question_Cinderella_story.txt", "w")
    Q_num = 0
    for i in Y_N_List:
        Q_num = Q_num + 1
        tmp = str(Q_num) + "- " + i[0] + "\n"
        f.write(tmp)
    f.close()


# ********************************************************** End write_Y_N_qustions*****************************************

# **********************************************************write_Y_N_Answer*****************************************
def write_Y_N_Answer(Y_N_List):
    f = open("/content/drive/My Drive/Answer_Cinderella_story.txt", "w")
    Q_num2 = 0
    for i in Y_N_List:
        Q_num2 = Q_num2 + 1
        tmp = str(Q_num2) + "- " + i[2] + "\n"
        f.write(tmp)
    f.close()


# ********************************************************** End write_Y_N_qustions*****************************************
############################################################################################################################
############################################################################################################################
############################################################################################################################
'''
def main():
    dic_tmp = gen_Modal_Question(keyword_dic_sents)
    Y_N_Question_dic = gen_y_N_Question(dic_tmp, distractors_dic)
    Y_N_List = convert_dic_List(Y_N_Question_dic)
    write_Y_N_qustions(Y_N_List)
    write_Y_N_Answer(Y_N_List)

    # print(dic_tmp)
    # print(Y_N_Question_dic)


if __name__ == "__main__":
    main()

'''