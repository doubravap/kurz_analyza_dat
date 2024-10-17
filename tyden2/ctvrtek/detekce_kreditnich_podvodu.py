## Importy
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
from matplotlib import pyplot as plt

# scikit-learn modely pro klasifikaci
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# scikit-learn rozdeleni dat a predzpracovani
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.metrics import accuracy_score, balanced_accuracy_score, recall_score
from sklearn.metrics import matthews_corrcoef, make_scorer

# imbalanced-learn knihovna pro praci s nevyvazenymi datasety
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss