from IPython.core.magic import (Magics, magics_class, line_cell_magic)
import logging
import requests
import json

URL = "https://firestore.googleapis.com/v1/projects/jupyter-post-cell/databases/(default)/documents/exercises"

@magics_class
class PostContent(Magics):

    @line_cell_magic
    def post_content(self, line, cell=None):
        if(line.startswith("register")):
           _, user =  line.strip().split(" ")
           self.user = user
           self.url  = URL
           print("Registering")
        else:
            exercise = line.strip()
            try:
                data= {'fields': 
                    {'user':{"stringValue":self.user}, 'exercise':{"stringValue":exercise}, 'cell':{"stringValue":cell}}
                }

                headers = {'Content-Type': 'application/json'}

                #print(cell)
                #print(json.dumps(data))

                resp = requests.post(self.url, data=json.dumps(data), headers=headers)

                if(resp.ok): print("cell posted for evaluation")
                else: print(resp.text)                

            except Exception as inst:
                logging.error(inst)
            get_ipython().run_cell(cell)
