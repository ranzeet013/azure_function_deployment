import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def train_random_forest_model():
    """
    Trains a RandomForestClassifier model on the Iris dataset.

    Loads the Iris dataset, splits it into training and testing sets, 
    trains a RandomForestClassifier, and then saves the model to a 
    pickle file named 'iris_model.pkl'.
    """
    # Load the Iris dataset
    iris = load_iris()
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)
    
    # Initialize the RandomForestClassifier model
    model = RandomForestClassifier()
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    
    # Save the trained model to a pickle file
    with open('iris_model.pkl', 'wb') as f:
        pickle.dump(model, f)

# Call the function to train and save the model
train_random_forest_model()
