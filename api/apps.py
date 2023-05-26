import os
import xgboost as xgb
from django.apps import AppConfig
from django.conf import settings



xgb_model = xgb.Booster()
MODEL_FILE = os.path.join(settings.MODELS, "model.json")
xgb_model.load_model(MODEL_FILE)
class ApiConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    model = xgb_model
