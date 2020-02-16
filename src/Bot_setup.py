try:
    import urllib
    import json
    import os
    import requests
    from flask import (Flask,request, make_response)
    from random import randint
except Exception as e:
    print("Some modules are missing {}".format(e))
# Flask app should start in global layout
app = Flask(__name__)
# whenever you make request /webhook
# Following calls are made
# webhook ->
# -----------> Process requests
# ---------------------------->get_data()
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        req = request.get_json(silent=True, force=True)
        res = processRequest(req)
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r
def processRequest(req):
    # Get all the Query Parameter
    query_response = req["queryResult"]
    print(query_response)
    text = query_response.get('queryText', None)
    parameters = query_response.get('parameters', None)
    res = get_data()
    return res
def get_data():
    # enter your api key here
    api_key = 'AIzaSyDS7FCSvZSoJBUt7fsa-wtNlokIz58TIMI'

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    req = request.get_json(silent=True, force=True) #input('Search query: ')
    query_response = req['queryResult']
    query = query_response.get('queryText')
    # print("My Query see this: " + str(query))

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query +
                     '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']

    # keep looping upto length of y
    cuisines = []
    for i in range(len(y)):
        # Print value corresponding to the
        # 'name' key at the ith index of y
        # cuisines[i] = str(i+1)
        # value = randint(0, cuisines.__len__() - 1)
        # print(cuisines[value])
        cuisines.append(y[i]['name'])
        rand_num = randint(0, len(cuisines))
    speech = "webhook response hello"
    return {
        "fulfillmentText": cuisines[rand_num],
    }
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')
    
    r = requests.get(url + 'query=' + query + '&location=37.228382,-80.423416&radius=8000'
                     '&key=' + api_key)
