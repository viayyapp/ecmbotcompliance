from watson_developer_cloud import ConversationV1
from json import JSONEncoder

def conversation_fun():
	
	conversation = ConversationV1(
	username='8f852f62-ded3-4c89-b696-f6999670f391',
	password='wMCxakn17KSZ',
	version='2017-04-24')

	return conversation