from allennlp.predictors.predictor import Predictor
import pickle

with open("paras.txt", "rb") as fp:
  paras = pickle.load(fp)
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")

def answeruserquestion(ques):
  probs=[]
  answers=[]
  for p in paras:
    answers.append("result['best_span_str']")
    probs.append(3)
  i = probs.index(max(probs))
  return answers[i]

a = answeruserquestion("In what country is Normandy located?")
print(a)