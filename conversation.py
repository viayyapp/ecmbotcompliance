from watson_developer_cloud import ConversationV1
from json import JSONEncoder

def conversation_fun():
	
	conversation = ConversationV1(
	username='18c651c1-c2f4-403a-88bd-a920bd753c88',
	password='42HMzjtHrvCf',
	version='2017-04-24')

	return conversation