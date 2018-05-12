import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.decomposition import PCA
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering,KMeans
from sklearn.linear_model import LogisticRegression
sns.set(style="white")
from sklearn.externals import joblib
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog

def import_fichier():
    Canevas.delete(ALL) # on efface la zone graphique

    filename = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('gif files','.gif'),('all files','.*')])
    print(filename)
    data = pd.read_csv('../fichier_csv/{}'.format(filename))
    
def graph_decision(data):
    data_acp = data.copy()
    data_acp_ind = data.copy()
    data_acp.index = data_acp['is_genuine']
    del data_acp['is_genuine']

    X = data_acp.values
    n_components = 2

    pca = PCA(n_components=n_components)
    reduction = pca.fit_transform(X)

    for i in range(0, n_components):
        data_acp_ind['PC' + str(i + 1)] = reduction[:, i]

    #Regression 
    clf = joblib.load('algo_reg_log_plot.pkl')

    xx, yy = np.mgrid[-5:5:.01, -5:5:.01]
    grid = np.c_[xx.ravel(), yy.ravel()]


    probs = clf.predict_proba(grid)[:,1].reshape(xx.shape) #probabilité d'appartenir à True

    f, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contourf(xx, yy, probs,50, cmap="RdBu",
                          vmin=0, vmax=1)
    ax_c = f.colorbar(contour)
    ax_c.set_label("$P(y = 1)$")
    ax_c.set_ticks([0, .25, .5, .75, 1])

    ax.scatter(data_acp_ind['PC1'], data_acp_ind['PC2'], c=y, s=50,
               cmap="RdBu", vmin=-.2, vmax=1.2,
               edgecolor="white", linewidth=1)

    ax.set(aspect="equal",

           xlabel="PC1", ylabel="PC2")

def create_data_decision(X):
    #Dataframe
    clf2 = joblib.load('algo_reg_log.pkl')

    probaClasses = clf2.predict_proba(X)

    a = pd.Series(probaClasses[:,1],name='probas')
    test =pd.concat([data,a],axis=1)

    test['verif']=test['probas'] >=0.5
    return test




# Main window
Mafenetre = Tk()
Mafenetre.title("Test")

# Création d'un widget Menu
menubar = Menu(Mafenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Importer un fichier",command=import_fichier)
menufichier.add_command(label="Montrer  les décisions",command=create_data_decision)
menufichier.add_command(label="Montrer  le graphique",command=graph_decision)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Apropos)
menubar.add_cascade(label="Aide", menu=menuaide)

# Affichage du menu
Mafenetre.config(menu=menubar)

# Création d'un widget Canvas
Canevas = Canvas(Mafenetre)
Canevas.pack(padx=5,pady=5)

# Utilisation d'un dictionnaire pour conserver une référence
gifdict={}

Mafenetre.mainloop()