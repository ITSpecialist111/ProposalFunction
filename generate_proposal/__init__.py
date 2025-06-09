import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, outputBlob: func.Out[str]) -> func.HttpResponse:
    logging.info("Received request.")

    try:
        proposal_payload = req.get_json()
        logging.info(f"Received payload: {proposal_payload}")

        # Validate
        required_fields = ["title", "client"]
        missing = [field for field in required_fields if field not in proposal_payload]
        if missing:
            return func.HttpResponse(
                json.dumps({"status": "error", "message": f"Missing fields: {', '.join(missing)}"}),
                status_code=400,
                mimetype="application/json"
            )

        # Save to blob
        outputBlob.set(json.dumps(proposal_payload))

        return func.HttpResponse(
            json.dumps({"status": "success", "message": "Proposal saved to blob storage."}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(
            json.dumps({"status": "error", "message": "Invalid JSON payload."}),
            status_code=400,
            mimetype="application/json"
        )

