# Détection de faux billet 'DETECT ANOMIE'

DETECT ANOMIE est une société de consulting informatique qui propose des mission au ministère de l'intérieur, dans le cadre de la lutte contre la criminalité organisée, à l'office central pour la répression du faux monnayage (OCRFM).

L'OCRFM a été créé le 11 septembre 1929, en application de la Convention de Genève. Il centralise les renseignements pouvant faciliter les recherches, la prévention et la répression du faux monnayage.

Pour identifier les billets propices à être considérés comme des faux, il vous a été demandé d'effectuer une analyse exploratoire à l'aide d'algorithmes non supervisés à partir d'un jeu de données communiqué par l'OCRFM. Il vous faudra également construire un modèle de regression linéaire classant les billets et appliquer ce modèle à un nouveau jeu de données afin de classer ces nouveaux billets.

## Getting Started (=Avant de commencer)

### Prerequisites (=Pré-requis)

Installer :
- Python 3.5

Et installer les libraires suivantes :
- Jupyter Notebook 5.4.1
- Pandas 0.22.0
- Numpy 1.14.2
- SciPy 1.0.0
- MatplotLib 2.2.2
- Scikit-Learn 0.19.1

## Arborescense 
Dossier notebook : Contient le programme.
Dossier fichiers_csv : Contient les données utilisées.
Dossier presentation : Contient la présentation pdf et les images associées à cette présentation.
Dossier code : Contient le programme de détection des billets.
Dossier documents : Contient les ressources utilisées.

## Running

1. Pour réaliser l'analyse du jeu de données, ouvrer le notebook Jupyter (dossier 'notebook'), placez-vous au niveau de 'Analyses univariées' "run cells above".
2. Il est possible d'effectuer des analyses univariés et bivariés de chaque variable. Pour cela, selectionner la cellule en dessous de 'Analyses univariées' et sélectionner 'Run'. Choississez au choix l'analyse à réaliser et faites 'Run'. 
3. Pour lancer la suite de l'analyse (analyse exploratoire, classification et modélisation), placer-vous en dessous de la dernière cellule d'analyse et faites 'Run cells below'.

4. Pour réaliser la détection de faux billets, ouvrer le notebook Jupyter (dossier 'code') et faites 'Run'.




## Built With (=Fabriquer avec)

* [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) - The  web-based application suitable for capturing the whole computation process.
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) -  It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python
* [Numpy](http://www.numpy.org/) - NumPy is the fundamental package for scientific computing with Python.
*[Matplotlib](https://matplotlib.org/#) - Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
*[Scipy](https://docs.scipy.org/doc/scipy/reference/index.html) - SciPy (pronounced “Sigh Pie”) is open-source software for mathematics, science, and engineering.
*[Scikit-Learn](http://scikit-learn.org/stable/index.html) - Simple and efficient tools for data mining and data analysis.



## Authors

* **Thibault SCHMIT** - *Initial work* - [Silvock](https://github.com/Silvock)



## License

This project is licensed under the GNU GPL 3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Olivier Yoo - Mentor OpenClassrooms
