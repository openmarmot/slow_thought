'''
Language : Python 3.x
email : andrew@openmarmot.com
notes : builds/defines AI objects

'''


#import built in packages

#import external packages

#import local packages
from ai.ai_llama_cpp_python import AILlamaCpp


#---------------------------------------------------------------------------
def get_ai_object(name):
    '''returns a new ai object'''
    download_folder='./downloads/'

    z=None

    if name=='CapyBaraHermes 2.5 Mistral 7B - GGUF':
        z=AILlamaCpp()
        z.model_url='https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF/resolve/main/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf'
        z.model_path=download_folder+'capybarahermes-2.5-mistral-7b.Q4_K_M.gguf'


    return z