# analyze21

Natural Language Machine Learning as a Service command line tool.

In order to use this app,  open the command line in your 21 Computer and run the following commands:

    $ 21 buy http://10.244.107.98:4002/machine?text="enter text here"

JSON RESPONSE:
[
  {
    "language": "en",
    "entities": [
      {
        "mentions": [
          {
            "text": {
              "beginOffset": -1,
              "content": "Bitcoin"
            }
          }
        ],
        "type": "OTHER",
        "name": "Bitcoin",
        "salience": 1,
        "metadata": {
          "wikipedia_url": "http://en.wikipedia.org/wiki/Bitcoin"
        }
      }
    ]
  },
  {
    "documentSentiment": {
      "polarity": 1,
      "magnitude": 0.2
    },
    "language": "en"
  }
]
