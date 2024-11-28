
import os
import json
import pandas as pd 
import traceback
import PyPDF2


from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.utils import get_table_data


quiz ={
  "1": {
    "mcq": "Who coined the term machine learning?",
    "options": {
      "a": "Donald Hebb",
      "b": "Arthur Samuel",
      "c": "Walter Pitts",
      "d": "Warren McCulloch"
    },
    "correct": "b"
  },
  "2": {
    "mcq": "What was the earliest machine learning model introduced by Arthur Samuel?",
    "options": {
      "a": "Speech recognition",
      "b": "Image classification",
      "c": "Checkers game",
      "d": "Pattern recognition"
    },
    "correct": "c"
  },
  "3": {
    "mcq": "Which book introduced the Hebbian theory?",
    "options": {
      "a": "The Organization of Behavior",
      "b": "Learning Machines",
      "c": "Computing Machinery and Intelligence",
      "d": "The History of Machine Learning"
    },
    "correct": "a"
  },
  "4": {
    "mcq": "In the 1960s, a learning machine called Cybertron was developed to analyze which of the following?",
    "options": {
      "a": "Sonar signals",
      "b": "Speech patterns",
      "c": "Electrocardiograms",
      "d": "All of the above"
    },
    "correct": "d"
  },
  "5": {
    "mcq": "According to Tom M. Mitchell, what is the definition of machine learning?",
    "options": {
      "a": "Improving computer performance",
      "b": "Learning from experience to improve task performance",
      "c": "Analyzing cognitive processes",
      "d": "Developing neural networks"
    },
    "correct": "b"
  }
}


quiz_json = json.dumps(quiz)    
   
quiz_table_data=get_table_data(quiz_json)
   
quiz= pd.DataFrame(quiz_table_data)


def get_quiz_data():
 
  
  return quiz
   
print(quiz)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   