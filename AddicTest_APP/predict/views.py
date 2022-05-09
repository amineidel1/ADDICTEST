from itertools import count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import User_experience

import pickle

# Create your views here.


def home(request):
    return render(request, "predict/index.html")


def about(request):
    return render(request, "predict/about.html")


def simulation(request):
    return render(request, "predict/simulation.html")


def resultat(request):
    Age = request.POST['ageSelect']
    Gender = request.POST['sexeSelect']
    Eduction = request.POST['eduSelect']
    Contry = request.POST['countrySelect']
    Ethnicity = request.POST['ethnicitySelect']
    Nscore = request.POST["nscore"]
    Escore = request.POST["escore"]
    Oscore = request.POST["oscore"]
    Ascore = request.POST["ascore"]
    Cscore = request.POST["cscore"]
    Impulsive = request.POST["Impulsive"]
    Ss = request.POST["SS"]

    # import ML model
    with open('ML_models/LR_gridSearchAlcohol.pickle', 'rb') as f:
        ML_model_Alcohol = pickle.load(f)
    with open('ML_models/LR_gridSearchNicotine.pickle', 'rb') as f:
        ML_model_Nicotine = pickle.load(f)
    with open('ML_models/LR_gridSearchCannabis.pickle', 'rb') as f:
        ML_model_Cannabis = pickle.load(f)
    with open('ML_models/LR_gridSearchAmphet.pickle', 'rb') as f:
        ML_model_Amphet = pickle.load(f)
    with open('ML_models/LR_gridSearchCoke.pickle', 'rb') as f:
        ML_model_Coke = pickle.load(f)
    with open('ML_models/LR_gridSearchEcstasy.pickle', 'rb') as f:
        ML_model_Ecstasy = pickle.load(f)
    with open('ML_models/LR_gridSearchLegalh.pickle', 'rb') as f:
        ML_model_Legalh = pickle.load(f)
    with open('ML_models/LR_gridSearchLSD.pickle', 'rb') as f:
        ML_model_LSD = pickle.load(f)
    with open('ML_models/LR_gridSearchMushrooms.pickle', 'rb') as f:
        ML_model_Mushrooms = pickle.load(f)

    Ethnicity = float(Ethnicity)
    # [[6.0, -0.46725, 0.80523, -0.84732, -1.0145, -1.37983, 0.40148]])
    # [[0.01364298 0.98635702]]

    proba_Alcohol = int(ML_model_Alcohol.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_Amphet = int(ML_model_Amphet.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_Coke = int(ML_model_Coke.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_Cannabis = int(ML_model_Cannabis.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_Ecstasy = int(ML_model_Ecstasy.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_Legalh = int(ML_model_Legalh.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_LSD = int(ML_model_LSD.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_Mushrooms = int(ML_model_Mushrooms.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)
    proba_Nicotine = int(ML_model_Nicotine.predict_proba(
        [[Ethnicity, Nscore, Escore, Oscore, Cscore, Impulsive, Ss]])[0][1] * 100)

    context = {'proba_Alcohol': proba_Alcohol, 'proba_Coke': proba_Coke, 'proba_Amphet': proba_Amphet, 'proba_Cannabis': proba_Cannabis,
               'proba_Ecstasy': proba_Ecstasy, 'proba_Legalh': proba_Legalh, 'proba_LSD': proba_LSD, 'proba_Mushrooms': proba_Mushrooms, 'proba_Nicotine': proba_Nicotine}

    new_user_exp = User_experience(Age=Age, Gender=Gender, Eduction=Eduction, Contry=Contry, Ethnicity=Ethnicity, Nscore=Nscore, Escore=Escore, Oscore=Oscore, Ascore=Ascore, Cscore=Cscore, Impulsive=Impulsive, SS=Ss, proba_Alcohol=proba_Alcohol,
                                   proba_Amphet=proba_Amphet, proba_Coke=proba_Coke, proba_Cannabis=proba_Cannabis, proba_Ecstasy=proba_Ecstasy, proba_Legalh=proba_Legalh, proba_LSD=proba_LSD, proba_Mushrooms=proba_Mushrooms, proba_Nicotine=proba_Nicotine)
    new_user_exp.save()

    return render(request, "predict/resultat.html", context)
