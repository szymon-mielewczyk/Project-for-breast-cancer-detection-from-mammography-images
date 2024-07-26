import requests


resp = requests.post("http://localhost:5000/predict",

                    #  for sending image
                    #  files={"file": torchvision.io.read_image(path='mdb005.pgm')})
                    #  files={"file": open("img.jpg",'rb')})

                    #  for sending image path
                    files={"path": 'mdb005.pgm'})



print(resp.json())