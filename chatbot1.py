import re
import long_responce as long 

def probabilty(message,recongnized_words,compulsory_word,single_responce=False):
	message_probabilty=0
	for word in message:
		if word in recongnized_words:
			message_probabilty+=1
	percentage=float(message_probabilty)/float(len(recongnized_words))
	#print(percentage*100)
	for word in message:
		if word in compulsory_word or single_responce:
			#print(percentage*100)
			return percentage*100
		else:
			return 0
			
	



def check_all_message(message):
	percentage_responce_dic={}

	def filler(bot_responce,recongnized_words=[],compulsory_word=[],single_responce=False):
		nonlocal percentage_responce_dic
		percentage_responce_dic[bot_responce]=probabilty(message,recongnized_words,compulsory_word,single_responce)
	#filler-----------------------------------------------------------------------------------------
	filler("hello",["hello","hey","hi","hai"],single_responce=True)	
	filler("I am doing,and you",["how","are","you"],["how"])
	filler("see you",["bye","goodbye"],single_responce=True)
	filler("Thank YOU",["i","love","you"],["love"])
	ls=[]

	for bot_responce,percentage in percentage_responce_dic.items():
		ls.append(percentage)
	#print(ls)
	#print(max(ls))	
	for bot_responce,percentage in percentage_responce_dic.items():	
		if percentage==max(ls) and percentage!=0:
			return bot_responce
			break
	if percentage==0:
		return long.unknown()
		
			


def get_responce(message): #>>>> sending message in list removing sympols
	split_message=re.split(r'\s+|[,;?!.-]\s*',message.lower())
	responce=check_all_message(split_message)
	return responce


while True:
	print("bot :"+get_responce(input("you :")))