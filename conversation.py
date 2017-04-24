from watson_developer_cloud import ConversationV1
from json import JSONEncoder

def conversation_fun():
	
	conversation = ConversationV1(
	username='f4f78f13-490f-4ea4-b7a8-d5ebf470011d',
	password='pr0IqFp70Dyl',
	version='2017-02-03')

	return conversation