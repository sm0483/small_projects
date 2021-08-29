import re

def message_probability(user_message,recongnized_words,required_words,single_responce=False):
    probability=0
    for word in user_message:
        if word in recongnized_words:
            probability=probability+1
    #calculating probability-----------------
    percentage=float(probability)/float(len(recongnized_words))
    percentage=percentage*100

    return percentage


def messagAnal(user_message):
    highest_required_list={}

    def response(bot_responce,recongnized_words,required_words=[],single_responce=False):
        nonlocal highest_required_list
        highest_required_list[bot_responce]=message_probability(user_message,recongnized_words,required_words)
    #responce----------------------------------------------------------------------------------------------------------
    response("hello",["hello","hi","hai","heyo"],single_responce=True)
    response("i am fine! how are you?",["how","are","you","doing"],["how"])
    response("1 year",["how","old","are","you"],["old"])    
    ls=[]


    for x,y in highest_required_list.items():
        ls.append(y)
    for x,y in highest_required_list.items():
        if y==max(ls):
            return x






def get_responce(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response =messagAnal(split_message)
    return response

while True:
    print("bot: "+ get_responce(input("you: ")))