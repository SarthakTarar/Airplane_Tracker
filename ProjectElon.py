import requests
data = requests.get("")
print(data)

import requests
data = requests.get("").json()
if data["states"] != None:
    print(f"The longitude of the plane is: {data['states'][0][5]}")
    print(f"The latitude of the plane is: {data['states'][0][6]}")

else:
    print("The plane is currently on the ground!")
print("The plane is currently on the ground!")

#Send the notification
import smtplib, ssl

sender =''
password ='' 

receiver = ''

body_msg ='''Subject: Tracking Results
You have used our application please check your responses. '''

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
    server.login(sender,password)
    server.sendmail(sender, receiver,body_msg)

#%%
import folium
import requests
import time
def generate_map(points):
    map = folium.Map(location=[0,0], zoom_start=2)
    folium.PolyLine(points, color='black').add_to(map)
    map.save("map.html")
points = []
while True:
    data = requests.get("").json()
    if data["states"] != None:
        points.append((data['states'][0][6], data['states'][0][5]))
        generate_map(points)
    else:    
     print("The plane is currently on the ground!")
    time.sleep(60)
#%%    
