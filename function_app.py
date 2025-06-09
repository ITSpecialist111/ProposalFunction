import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Received request.")

    try:
        proposal_payload = req.get_json()
        logging.info(f"Received payload: {proposal_payload}")
        
        # Do something with the JSON (e.g., save to blob, queue, etc.)
        return func.HttpResponse("Proposal received and processed.", status_code=200)

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
