from watson_developer_cloud import TextToSpeechV1

def text_to_speech_fun():

	text_to_speech = TextToSpeechV1(
		username= 'f4f78f13-490f-4ea4-b7a8-d5ebf470011d',
		password= 'pr0IqFp70Dyl'
	# username='8921eb13-5eb4-4286-9add-5a7870ba4ecf',
	# password='tKJBMhuw42nL',
	x_watson_learning_opt_out=True)

	return text_to_speech