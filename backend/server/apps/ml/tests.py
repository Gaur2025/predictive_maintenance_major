import inspect
from apps.ml.registry import MLRegistry


from django.test import TestCase

from backend.server.apps.ml.failure_classifier.random_forest import RandomForestClassifier

class MLTest(TestCase):
    def test_rf_algorithm(self):
        input_data = {
    "setting1": -0.0007,  
    "setting2": -0.0004,
    "setting3": 100,
    "s1": 518.67,
    "s2": 641.82,
    "s3": 1589.7,
    "s4": 1400.6,
    "s5": 14.62,
    "s6": 21.61,
    "s7": 554.36,
    "s8": 2388.06,
    "s9": 9046.19,
    "s10": 1.3,
    "s11": 47.47,
    "s12": 521.66,
    "s13": 2388.02,
    "s14": 8138.62,
    "s15": 8.4195,
    "s16": 0.03,
    "s17": 392,
    "s18": 2388,
    "s19": 100,
    "s20": 39.06,
    "s21": 23.419,
    "av1": 518.67,
    "av2": 641.82,
    "av3": 1589.7,
    "av4": 1400.6,
    "av5": 14.62,
    "av6": 21.61,
    "av7": 554.36,
    "av8": 2388.06,
    "av9": 9046.19,
    "av10": 1.3,
    "av11": 47.47,
    "av12": 521.66,
    "av13": 2388.02,
    "av14": 8138.62,
    "av15": 8.4195,
    "av16": 0.03,
    "av17": 392,
    "av18": 2388,
    "av19": 100,
    "av20": 39.06,
    "av21": 23.419,
    "sd1": 0,
    "sd2": 0,
    "sd3": 0,
    "sd4": 0,
    "sd5": 0,
    "sd6": 0,
    "sd7": 0,
    "sd8": 0,
    "sd9": 0,
    "sd10": 0,
    "sd11": 0,
    "sd12": 0,
    "sd13": 0,
    "sd14": 0,
    "sd15": 0,
    "sd16": 0,
    "sd17": 0,
    "sd18": 0,
    "sd19": 0,
    "sd20": 0,
    "sd21": 0
        }
        my_alg = RandomForestClassifier() 
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('', response['label'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "income_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Piotr"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)

