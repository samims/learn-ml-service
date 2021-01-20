from django.db import models


class Endpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class MLAlgorithm(models.Model):
    parent_endpoint = models.ForeignKey(to=Endpoint, on_delete=models.CASCADE, related_name='ml_algorithms')
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class MLAlgorithmStatus(models.Model):
    parent_ml_algorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class MLRequest(models.Model):
    parent_ml_algorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name='ml_requests')
    input_data = models.TextField()
    full_response = models.TextField()
    response = models.TextField()
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
