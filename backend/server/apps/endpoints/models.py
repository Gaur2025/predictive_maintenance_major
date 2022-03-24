from django.db import models
from django.forms import CharField

# Create your models here


class Endpoint(models.Model):
    '''
        The Endpoint object represents ML API Endpoint"

        Attributes:
            name : The name of the endpoint, will be used in API url
            owner : The string with owner name
            created_at : The date when endpoint was created
    '''

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):
    '''
        The MLAlgorithm represents the ML algorithm objects.

        Attributes:
            name : name of the algorithm
            description : short description os how the algorithm works
            code : code of the algorithm
            version : version of the algorithm
            owner : name of the owner
            created_at : date when algorithm was created
            parent_endpoint : reference to the endpoint
    '''

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    '''
        MLAlgorithmStatus represents the status of algorithm which can change with time.

        Attributes:
            status : status of algorithm in the endpoint. (Can be = testing, staging, production, ab_testing)
            active : boolean flag which point to currently active status
            created_by : name of creator
            created_at : date of status creation
            parent_mlalgorithm : reference to corresponding MLAlgorithm

    '''

    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE, related_name="status")


class MLRequest(models.Model):
    '''
        The MLRequest will keep information about all requests to ML algorithms.

        Attributes:
            input_data : input data to ML algorithm in JSON format.
            full_response : response of the ML algorithm.
            response : reponse of the algorithm in JSON format.
            feedback : feedback about response in JSON format.
            created_at : date when request was created.
            parent_mlalgorithm : reference to MlAlgorithm used to compute response.

    '''

    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE)
