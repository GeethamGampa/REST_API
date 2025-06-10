import requests

url = 'https://stephen-king-api.onrender.com/api/books'

response = requests.get(url)
search_dict = {
    0 : "carrie",
    1 : "salem's Lot",
    2 : "the shining",
    3 : "rage",
    4 : "The Stand",
    5 : "The Long Walk",
    6 : "The Dead Zone",
    7 : "Firestarter",
    8 : "Roadwork",
    9 : "Cujo",
    10: "The Running Man",
    11 : "The Dark Tower",
    12 : "Christine ",
    13 : "Pet Sematary",
    14 : "Cycle of the Werewolf",
    15 : "The Talisman",
    16 : "The Eyes of the Dragon",
    17 : "Thinner",
    18 : "It",
    19 : "The Dark Tower II: The Drawing of the Three",
    20 : "Misery"
}
if response.status_code == 200:
    result = response.json()
    # print(result['data'][20])
    #facts = data['paths']['/fact']
    #paths = data['paths']
    user_input = input("What's your title?")
    for k,v in search_dict.items():
        if v == user_input:
         Publisher =  result['data'][k]['Publisher'] 
         isbn =   result['data'][k]['ISBN']   
         print('Publisher-',Publisher,'ISBN-',isbn) 
          
else:
    print("Error:", response.status_code)