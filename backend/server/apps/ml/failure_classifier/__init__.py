import joblib
import pandas as pd

class RandomForestClassifier:

    '''
    The constructor which loads preprocessing objects and
    Random Forest Object (created with Jupyter Notebook).
    '''
    def __init__(self):
        path_to_artifacts = "../../research"
        self.values_fill_missing = joblib.load(path_to_artifacts + "train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "random_forest.joblib")



    '''
    The method which takes as input JSON data, converts it to
    Pandas Dataframe and apply preprocessing.
    '''
    def preprocessing(self, input_data):
        # JSON to pandas dataframe.
        input_data = pd.DataFrame(input_data, index=[0])
        # fill missing values
        input_data.fillna(self.values_fill_missing)
        # Convert categoricals
        for column in [






        ]:
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])

        return input_data



    '''
    The method that calls ML for computing predictions on prepared data.
    '''
    def predict(self, input_data):
        return self.model.predict_proba(input_data)


    '''
    The method that applies post-processing on prepared data.
    '''
    def post_processing(self, input_data):
        label = "Component Failed"
        if input_data[1] > 0.5:
            label = "Working Fine!!"
        return {"probability": input_data[1], "label": label, "status": "OK"}

    
    '''
    The method that combines: preprocessing, predict and postprocessing and
    returns JSON object with the response.
    '''
    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0] # Only one sample
            prediction = self.post_processing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction



