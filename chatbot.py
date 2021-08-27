import re
import long_responce as long

def message_probabilty(user_message,recongnised_words=[]):
	message_certanity=0

	for word in user_message:
		if word in recongnised_words:
			message_certanity+=1

	return flaot(message_certanity)/flaot(len(user_message))*100

def check_all_messages(user_list):
	









def get_responce(user_input):
	user_list=re.split('\s+|[!,.?-]\s*',user_input)
	user_list=[word for word in user_list if word!=""]
	responce =check_all_messages(user_list)
	return responce
	




while True:
	print('bot:'+get_responce(input('you: ')))

