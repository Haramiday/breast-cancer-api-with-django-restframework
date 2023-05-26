from django.shortcuts import render
import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
import xgboost as xgb
import os
from django.conf import settings

class CancerPrediction(APIView):
    def post(self, request):
        data = request.data
        radius_mean = data['radius_mean']
        texture_mean = data['texture_mean']
        perimeter_mean = data['perimeter_mean']
        area_mean = data['area_mean']
        smoothness_mean = data['smoothness_mean']
        concavity_mean = data['concavity_mean']
        concave_points_mean = data['concave points_mean']
        

        dic = {'radius_mean':[radius_mean], 'texture_mean':[texture_mean], 'perimeter_mean':[perimeter_mean],
       'area_mean':[area_mean], 'smoothness_mean':[smoothness_mean], 'concavity_mean':[concavity_mean],
       'concave points_mean':[concave_points_mean]}
        d_f = pd.DataFrame(dic)
        
        lin_reg_model = ApiConfig.model
        predicted = lin_reg_model.predict(xgb.DMatrix(d_f))[0]
        predicted = int(np.round(predicted))
        if predicted == 1:
        	case = "Malignant"
        else:
        	case = "Benign"
        response_dict = {"Result": case}
        return Response(response_dict, status=200)

