from flask import Flask, jsonify, request

# créer l'application Flask
app = Flask(__name__)

# une liste des employées
employees = [ {"id":1, "name":"Rayan", "age":25, "company":"Google", "role":"Junior Software Engineer"},
              {"id":2, "name":"Saad", "age":23, "company":"Meta", "role":"Junior Software Engineer"},
              {"id":3, "name":"Christophe", "age":35, "company":"Microsoft", "role":"senior architect"},
              {"id":4, "name":"Adrien", "age":30, "company":"Microsoft", "role":"project manager"},
              {"id":5, "name":"Julien", "age":55, "company":"Google", "role":"executive director"} ]

# tableau initial (utilisé dans les fcts get_employees et add_employees)
tab = ("<h2 style='text-align:center;'>Liste des employées</h2>"
         + "<table border='1' style='margin:auto;'>"
         + "<tr>"
         + "<th>ID</th>"
         + "<th>Nom</th>"
         + "<th>Age</th>"
         + "<th>Entreprise</th>"
         + "<th>Role</th>"
         + "</tr>")



# racine de l'API pour tester si le serveur fonctionne ... <>
@app.route('/')
def home():
    return ("<h1 style='text-align: center'> Bienvenue dans l'Api de gestion des employées !</h1>" +
            "<h3 style='text-align: center'> Pour Accéder à la liste des employées, cliquer sur le <a href='/employees'>lien</a> </h3>")



# activer mode debug pour voir les erreurs et recharger automatiquement le serveur
if __name__ == '__main__':
    app.run(debug=True)



#Endpoint pour lister tous les employées suivi d'une méthode HTTP GET qui permet de retourner la liste des employées sous forme d'une table
@app.route('/employees', methods=['GET'])
def get_employees():

    table = tab
    for emp in employees:
        table += ("<tr>"
                + "<td>" + str(emp['id']) + "</td>"
                + "<td>" + str(emp['name']) + "</td>"
                + "<td>" + str(emp['age']) + "</td>"
                + "<td>" + str(emp['company']) + "</td>"
                + "<td>" + str(emp['role']) + "</td>"
                + "</tr>"
                )
    table += "</table>"

    #lien pour revenir en arrière vers la page home
    retour = "<h4 style='text-align: center'> <a href='/'>Retour</a> </h4>"

    return table + retour



# Ajouter un employee (POST) avec la fct add_employees qui a bien fonctionnée après le test POST sur Postman
@app.route('/employees', methods=['POST'])
def add_employees():
    new_employee=request.get_json()      #Pour récupérer les données envoyé par le client
    new_employee['id']=len(employees)+1  #Attribuer un numéro de manière incrémentable
    employees.append(new_employee)

    table = tab
    for emp in employees:
        table += ("<tr>"
                + "<td>" + str(emp['id']) + "</td>"
                + "<td>" + str(emp['name']) + "</td>"
                + "<td>" + str(emp['age']) + "</td>"
                + "<td>" + str(emp['company']) + "</td>"
                + "<td>" + str(emp['role']) + "</td>"
                + "</tr>"
                )
    table += "</table>"

    #lien pour revenir en arrière vers la page home
    retour = "<h4 style='text-align: center'> <a href='/'>Retour</a> </h4>"

    return table + retour,201 #return new_employee, 201 #Le code 201 pour dire création réussie ...



#Afficher les employees par entreprise ....
@app.route('/employees/<company>', methods=['GET'])
def get_company(company):
    entreprise = [e for e in employees if e['company'] == company]
    if entreprise:

        table = tab
        for emp in entreprise:
            table += ("<tr>"
                      + "<td>" + str(emp['id']) + "</td>"
                      + "<td>" + str(emp['name']) + "</td>"
                      + "<td>" + str(emp['age']) + "</td>"
                      + "<td>" + str(emp['company']) + "</td>"
                      + "<td>" + str(emp['role']) + "</td>"
                      + "</tr>"
                      )
        table += "</table>"

        # lien pour revenir en arrière vers la page home
        retour = "<h4 style='text-align: center'> <a href='/'>Retour</a> </h4>"

        return table + retour
    return jsonify ({"erreur":"aucun employee ne travaille dans entreprise !"}), 404



# Mettre un jour un employee (PUT) avec une fct update_employee qui a fonctionné après le test sur Postman
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = next((e for e in employees if e['id']==id), None)
    if not employee:
        return jsonify({"message": "Etudiant non trouvé !"}), 404

    data = request.get_json()
    employee.update(data)  # Mise à jour des données

    table = tab
    for emp in employees:
        table += ("<tr>"
                  + "<td>" + str(emp['id']) + "</td>"
                  + "<td>" + str(emp['name']) + "</td>"
                  + "<td>" + str(emp['age']) + "</td>"
                  + "<td>" + str(emp['company']) + "</td>"
                  + "<td>" + str(emp['role']) + "</td>"
                  + "</tr>"
                  )
    table += "</table>"

    # lien pour revenir en arrière vers la page home
    retour = "<h4 style='text-align: center'> <a href='/'>Retour</a> </h4>"

    return table + retour



# Supprimer un employee (DELETE) et la fct delete
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employees = [e for e in employees if e['id']!=id]

    table = tab
    for emp in employees:
        table += ("<tr>"
                  + "<td>" + str(emp['id']) + "</td>"
                  + "<td>" + str(emp['name']) + "</td>"
                  + "<td>" + str(emp['age']) + "</td>"
                  + "<td>" + str(emp['company']) + "</td>"
                  + "<td>" + str(emp['role']) + "</td>"
                  + "</tr>"
                  )
    table += "</table>"

    # lien pour revenir en arrière vers la page home
    retour = "<h4 style='text-align: center'> <a href='/'>Retour</a> </h4>"

    return table + retour