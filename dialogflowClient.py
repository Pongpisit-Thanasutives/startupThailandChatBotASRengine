import dialogflow
import json
def detect_intent_audio(project_id, session_id, audio_file_path, language_code):
    """Returns the result of detect intent with an audio file as input.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    session_client = dialogflow.SessionsClient()

    # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
    audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = 16000

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    with open(audio_file_path, 'rb') as audio_file:
        input_audio = audio_file.read()

    audio_config = dialogflow.types.InputAudioConfig(
        audio_encoding=audio_encoding, language_code=language_code,
        sample_rate_hertz=sample_rate_hertz)
    query_input = dialogflow.types.QueryInput(audio_config=audio_config)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
        input_audio=input_audio)

    result = {}
    artist = ''
    song = ''
    text = response.query_result.query_text
    if "song" in response.query_result.parameters:
        try:
            song = '{}'.format(response.query_result.parameters["song"][0])
        except IndexError:
            pass
    if "artist" in response.query_result.parameters:
        try:
            artist = '{}'.format(response.query_result.parameters["artist"][0])
        except IndexError:
            pass
    if artist == '' and 'เดอะทอย' in text:
        artist = 'เดอะทอย'
    intent = '{}'.format(response.query_result.intent.display_name)
    responseText = '{}'.format(response.query_result.fulfillment_text)

    print(text)
    print(song)
    print(artist)
    print(intent)
    print(responseText)

    result['text'] = text
    result['song'] = song
    result['artist'] = artist
    result['intent'] = intent
    result['responseText'] = responseText
    print(result)

    return result