import logging
import pickle
import os
import json
import azure.functions as func

# Load the model when the function is initialized
MODEL_PATH = os.path.join(os.path.dirname(__file__), "iris_model.pkl")
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function to handle HTTP requests for model predictions.

    This function receives a JSON payload containing input data, uses a pre-trained 
    machine learning model to make predictions, and returns the predictions in JSON format.

    Parameters:
    req (func.HttpRequest): The incoming HTTP request object.

    Returns:
    func.HttpResponse: The HTTP response containing the predictions in JSON format or 
                       an error message and appropriate HTTP status code if an error occurs.
    """
    logging.info('PredictModel function processed a request.')

    try:
        # Parse JSON request body
        req_body = req.get_json()
        input_data = req_body.get('data')

        # Ensure input data is a list of lists (samples)
        if not isinstance(input_data, list) or not all(isinstance(i, list) for i in input_data):
            return func.HttpResponse("Invalid input data format", status_code=400)

        # Make predictions using the loaded model
        predictions = model.predict(input_data)

        # Return the predictions as JSON
        return func.HttpResponse(
            json.dumps({"predictions": predictions.tolist()}),
            mimetype="application/json",
            status_code=200
        )

    except ValueError:
        # Return error if JSON format is invalid
        return func.HttpResponse("Invalid JSON format", status_code=400)
    except Exception as e:
        # Log any unexpected errors and return an error response
        logging.error(f"Error during prediction: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
