# Rapport du TP1 – Web Service SOAP avec JAX-WS

**Nom :** Mimouni  
**Prénom :** Saad  
**Numéro :** 12509798

---

## Objectif du TP

L’objectif de ce TP est de **déployer un Web Service SOAP** en utilisant la technologie **JAX-WS**.  
Le service permet d’exposer des opérations accessibles à distance via le protocole HTTP.

---

## 1. Définition de SOAP

**SOAP (Simple Object Access Protocol)** est un **protocole standard basé sur XML** qui permet l’échange de messages structurés entre des applications distribuées, indépendamment de la plateforme ou du langage de programmation utilisé.

SOAP est principalement utilisé pour implémenter des **Web Services** fiables, formels et fortement typés.

---

## 2. Concepts essentiels du SOAP et des Web Services

### 2.1 Web Service SOAP
Un **Web Service SOAP** est un service :
- Accessible via le réseau (HTTP)
- Décrit par un WSDL
- Communiquant à l’aide de messages SOAP (XML)

---

### 2.2 WSDL (Web Services Description Language)
Le **WSDL** est un fichier XML qui décrit :
- Les opérations disponibles du Web Service
- Les paramètres d’entrée et de sortie
- Le format des messages
- Le protocole et l’adresse du service


---

### 2.3 JAX-WS
**JAX-WS (Java API for XML Web Services)** est une API Java qui permet :
- De créer et publier des Web Services SOAP
- D’exposer des méthodes Java comme opérations distantes
- De générer automatiquement le WSDL

---

## 3. Publication du Service

- **Adresse du service : http://localhost:8888**  

- **Fichier WSDL : http://localhost:8888/?wsdl**  


---

## 4. Hiérarchie du Projet

```text
src/
├── Application.java
├── Etudiant.java
├── MonServiceWeb.java
└── readme.md
```
---

## 5. Structure et Rôle des Fichiers

| Fichier              | Rôle                                       |
| -------------------- | ------------------------------------------ |
| `Application.java`   | Publie le Web Service SOAP                 |
| `MonServiceWeb.java` | Définit les opérations du Web Service      |
| `Etudiant.java`      | Modèle de données représentant un étudiant |
| `readme.md`          | Documentation du projet                    |

# Test OpenProject integration
