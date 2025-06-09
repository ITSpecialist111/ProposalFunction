import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Received request.")

    try:
        proposal_payload = req.get_json()
        logging.info(f"Received payload: {proposal_payload}")

        # Validation
        required_fields = ["title", "client"]
        missing = [field for field in required_fields if field not in proposal_payload]

        if missing:
            return func.HttpResponse(
                json.dumps({
                    "status": "error",
                    "message": f"Missing fields: {', '.join(missing)}"
                }),
                status_code=400,
                mimetype="application/json"
            )

        # TODO: Save to storage/database here

        return func.HttpResponse(
            json.dumps({
                "status": "success",
                "message": "Proposal received and processed",
                "data": proposal_payload
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(
            json.dumps({"status": "error", "message": "Invalid request"}),
            status_code=400,
            mimetype="application/json"
        )

