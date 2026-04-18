import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    raw_input= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = raw_input, headers=header)
    response_text = response.text
    formatted_response = json.loads(response_text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotion_dict = {}
    dominant_emotion = 'anger'
    dominant_score = -1
    for emotion, score in emotions.items():
        if score > dominant_score:
            dominant_emotion = emotion
            dominant_score = score
        emotion_dict[emotion] = score
    emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict
    return emotions

