from transformers import pipeline

models_dict = {"Sentiment Analysis": 'cardiffnlp/twitter-roberta-base-sentiment',
               "Language Detection": 'ivanlau/language-detection-fine-tuned-on-xlm-roberta-base',
               "Spam Detection": 'svalabs/twitter-xlm-roberta-crypto-spam',
               "Toxicity Classification": 'EIStakovskii/xlm_roberta_base_multilingual_toxicity_classifier_plus',
               "Fake News Classification": 'jy46604790/Fake-News-Bert-Detect'
               }

sent_dict = {'LABEL_0': 'negative',
             'LABEL_1': 'neutral',
             'LABEL_2': 'positive'}

toxc_dict = {'LABEL_0': 'not toxic',
             'LABEL_1': 'toxic', }
fake_dict = {'LABEL_0': 'fake news',
             'LABEL_1': 'real news', }


def predict(text, task):
    model_path = models_dict[task]

    ppl = pipeline(model=model_path, tokenizer=model_path)
    result = ppl(text)
    if task == 'Sentiment Analysis':
        return sent_dict[result[0]['label']]
    if task == 'Language Detection':
        return result[0]['label']
    if task == 'Toxicity Classification':
        return toxc_dict[result[0]['label']]
    if task == 'Fake News Classification':
        return fake_dict[result[0]['label']]

    return result[0]['label']
