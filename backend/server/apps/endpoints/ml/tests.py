from django.test import TestCase

from backend.server.apps.ml.failure_classifier.random_forest import RandomForestClassifier

class MLTest(TestCase):
    def test_rf_algorithm(self):
        input_data = {




        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('', response['label'])

