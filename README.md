## Overview

### Token linking

To link recieved  via POST request to the register/ endpoint token
please link that token to your chat sending it to https://t.me/message_api_bot

## API calls

### Create new profile `register/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-d "{
     "username": username,
     "first_name": first_name,
     "last_name": last_name
    "}"
"<hostname>/api/v1/register"
```

Response:

```
"Your token is 15c94c2f8b3af674174959e346b2ec88781a2956"
```

### Send new message `messages/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-H "Authorization: Bearer <your token>"
-d "{
     "message": message,
    "}"
"<hostname>/api/v1/messages"
```

Response:

```
"Message has been sent"
```


### Retrieve your's messages `messages/`

Method: `GET`

```
curl -XPOST
-H "Content-Type: application/json"
-H "Authorization: Bearer <your token>"
"<hostname>/api/v1/messages"
```

Response:

```
[
    {
        "message":"first",
        "date":"2023-01-10T12:24:03.328352Z"
    },
    {
        "message":"second",
        "date":"2023-01-10T12:29:54.719498Z"
    }
]

```