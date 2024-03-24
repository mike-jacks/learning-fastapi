# learning-fastapi

Practicing Fast API buildinging and making requests to it.

## Installation

Download files and create a new python virtual environment and run:  
`pip install -r requirements.txt`

## Start the Uvicorn server on your local machine

To start the uivocorn server, run:  
`python fastapi/main.py`

## Make Requests using python program

To make requests through the custom request python program, run:  
 `python make_requests.py`

### Instructions to make requests

You can use the following syntax to make requests:  
 `request_type path id_number activity`

FYI: Two items are preloaded int the todo list for a response to initial get request.

Examples:  
 `get /todo` -- Submits a get request to /todo. Will return a list of all items in todo list.  
 `post /todo 3 Learning to Code` -- Submits a post request to /todo. This will add another item to the todo list with id set to 3 and activity set to 'Learning to Code'  
 `put /todo 2 Fishing` -- Submits a put request to /todo. This will update item with id: 2 to set the activity to 'Fishing'.
`delete /todo 1` -- Submits a delete request to /todo. This will delete item with id: 1 from the to do list.
