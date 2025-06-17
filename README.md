<p align="center">
    <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">PASSGEN-WEBAPP</h1></p>
<p align="center">
	<em><code>❯ hiden</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/hidengit/PassGen-webapp?style=default&logo=opensourceinitiative&logoColor=white&color=8e00b7" alt="license">
	<img src="https://img.shields.io/github/last-commit/hidengit/PassGen-webapp?style=default&logo=git&logoColor=white&color=8e00b7" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/hidengit/PassGen-webapp?style=default&color=8e00b7" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/hidengit/PassGen-webapp?style=default&color=8e00b7" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table des matières

- [📍 Présentation](#-overview)
- [👾 Fonctionnalités](#-features)
- [📁 Structure du projet](#-project-structure)
  - [📂 Détail des fichiers](#-project-index)
- [🚀 Démarrage](#-getting-started)
  - [☑️ Prérequis](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Utilisation](#🤖-usage)
- [🔰 Contribuer](#-contributing)
- [🎗 License](#-license)

---

## 📍 Présentation

PassGen-webapp est une application web interactive développée avec Streamlit permettant de générer des mots de passe aléatoires et sécurisés selon des critères personnalisables (longueur, types de caractères). 

---

## 👾 Fonctionnalités

- ✅ Interface simple avec curseurs et cases à cocher

- 🔐 Génération sécurisée de mots de passe aléatoires

- ✏️ Longueur configurable (entre 8 et 32 caractères)

- 🔠 Inclusion ou exclusion des majuscules, minuscules, chiffres et symboles

- ♻️ Bouton de régénération immédiate

---

## 📁 Structure du projet

```sh
└── PassGen-webapp/
    ├── README.md
    ├── generator.py
    └── main.py
```


### 📂 Détail des fichiers
<details open>
	<summary><b><code>PASSGEN-WEBAPP/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/hidengit/PassGen-webapp/blob/master/main.py'>main.py</a></b></td>
				<td>Fichier principal de l'application : interface utilisateur avec Streamlit</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/hidengit/PassGen-webapp/blob/master/generator.py'>generator.py</a></b></td>
				<td>Fonction pour générer les mots de passe</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Démarrage

### ☑️ Prérequis

- **Python 3.7 ou supérieur**
- **pip**

### ⚙️ Installation

Installez PassGen-webapp en utilisant l’une des méthodes suivantes :

**Installation depuis le code source :**

1. Clonez le dépôt `PassGen-webapp`:
```sh
❯ git clone https://github.com/hidengit/PassGen-webapp
```

2. Accédez au répertoire du projet :
```sh
❯ cd PassGen-webapp
```

3. Installez les dépendances du projet :

```sh
❯ pip install streamlit
```

### 🤖 Utilisation

Lancer l'application :

```sh
❯ streamlit run main.py
```

ou

```sh
❯ python3 -m streamlit run main.py
```

---

## 🔰 Contribuer

- **💬 [Participer aux discussions](https://github.com/hidengit/PassGen-webapp/discussions)**: Partagez vos idées, donnez votre avis ou posez des questions.
- **🐛 [Signaler un problème](https://github.com/hidengit/PassGen-webapp/issues)**: Soumettez les bugs trouvés ou proposez de nouvelles fonctionnalités pour le projet ``PassGen-webapp``.
- **💡 [Soumettre une Pull Request](https://github.com/hidengit/PassGen-webapp/blob/main/CONTRIBUTING.md)**: Consultez les Pull Requests existantes et soumettez les vôtres.

<details closed>
<summary>Lignes directrices pour contribuer</summary>

1. **Fork du dépôt**: Commencez par forker le dépôt du projet sur votre compte GitHub.
2. **Cloner en local**: Clonez le dépôt forké sur votre machine locale à l'aide d’un client Git.
   ```sh
   git clone https://github.com/hidengit/PassGen-webapp
   ```
3. **Créer une nouvelle branche**: Travaillez toujours sur une nouvelle branche avec un nom descriptif.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Effectuer vos modifications**: Développez et testez vos modifications en local.
5. **Commit de vos changements**: Faites un commit avec un message clair décrivant vos modifications.
   ```sh
   git commit -m 'Ajout de la fonctionnalité x.'
   ```
6. **Pousser sur GitHub**: Poussez vos changements vers votre dépôt forké.
   ```sh
   git push origin new-feature-x
   ```
7. **Soumettre une Pull Request**: Créez une Pull Request vers le dépôt d’origine. Décrivez clairement les modifications et leurs motivations.
8. **Revue**: Une fois votre PR examinée et approuvée, elle sera fusionnée dans la branche principale. Félicitations pour votre contribution !
</details>

<details closed>
<summary>Graphique des contributeurs</summary>
<br>
<p align="left">
   <a href="https://github.com{/hidengit/PassGen-webapp/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=hidengit/PassGen-webapp">
   </a>
</p>
</details>

---

## 🎗 Licence

Ce projet est sous licence [MIT](https://choosealicense.com/licenses/mit/). Consultez le fichier [LICENSE](https://choosealicense.com/licenses/) pour plus d'informations.

---