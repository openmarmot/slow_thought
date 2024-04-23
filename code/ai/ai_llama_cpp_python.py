
'''
Language : Python 3.x
email : andrew@openmarmot.com
notes : ai based on the llama_cpp_python implementation

 ref for the module : https://github.com/abetlen/llama-cpp-python
'''


#import built in packages
import os
import requests

#import external packages
from llama_cpp import Llama # pip install llama-cpp-python

#import local packages
from ai.ai_base import AIBase

class AILlamaCpp(AIBase):
    def __init__(self):
        self.loaded=False
        self.llm=None
        self.model_url=None
        self.model_path=None
        self.max_sequence_length=32768
        self.max_tokens=512
        self.max_threads=4
        self.gpu_layers=0
        self.system_message=""

    #---------------------------------------------------------------------------
    def download_model(self):
        '''attempt to download the model file'''
    
        # Check if the file exists
        if os.path.exists(self.model_path):
            print(f"File {self.model_path} already exists.")
        else:
            # Attempt to download the file
            try:
                print(f"Downloading {self.model_path}...")
                response = requests.get(self.model_url)
                response.raise_for_status()  # Raises an HTTPError if the response was an HTTP error

                # Write the file to disk
                with open(self.model_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {self.model_path}.")
            except requests.RequestException as e:
                print(f"Failed to download {self.model_path}. Error: {e}")    

    #---------------------------------------------------------------------------
    def generate_response(self,question):
        '''generate a response from model inference'''
        if self.loaded==False:
            self.load()

        prompt="<|im_start|>system\n"+self.system_message
        prompt+="<|im_end|>\n<|im_start|>user\n"+question 
        prompt+="<|im_end|>\n<|im_start|>assistant"
        data=self.llm(prompt,max_tokens=self.max_tokens,stop=["</s>"], echo=False )
        
        return data["choices"][0]['text']

    #---------------------------------------------------------------------------     
    def load(self):
        '''load the model into memory'''
        self.download_model()

        self.llm = Llama(
            model_path=self.model_path,
            n_ctx=self.max_sequence_length,
            n_threads=self.max_threads,
            n_gpu_layers=self.gpu_layers
        )

        self.loaded=True
    
    #---------------------------------------------------------------------------
    def unload(self):
        '''unload the model from memory'''
        self.llm=None
        self.loaded=False

