import datetime


def verify_response(question, response):
    """ Verify the manager responses before save it in the dictionary """
    if question[2]:
        condition = question[2]
        if condition == int:
            try:
                int(response)
            except ValueError:
                print("Vous devez indiquer un nombre.")
                return False
            else:
                return True
        elif type(condition) == list:
            if response in condition:
                return True
            else:
                print("Vous devez choisir votre réponse dans la liste proposée.")
                return False
        elif condition == "date":
            date = response.split("-")
            try:
                date_test = datetime.date(int(date[2]), int(date[1]), int(date[1]))
            except ValueError:
                print("Vérifier que le nombre de mois est entre 1 et 12 et que le nombre de jours "
                      "est entre 1 et 31.")
                return False
            except TypeError:
                print("Les éléments de la date doivent être des chiffres séparés par un tiret.")
                return False
            except IndexError:
                print("Vous devez indiquez un jour(jj), un mois(mm) et une année(aaaa).")
                return False
            else:
                if datetime.date(1900, 1, 1) < date_test:
                    return True
                else:
                    print("L'année doit être composée de 4 chiffres.")
                    return False
        elif condition == "required":
            if response:
                return True
            else:
                print("Vous devez entrer une réponse.")
                return False
        else:
            pass
    else:
        return True


def check_float(number_to_test):
    """ Check if number_to_test is a float. """
    accept_scores = [0, 0.5, 1]
    try:
        float(number_to_test)
    except ValueError:
        print("Vous devez entrer un nombre.")
        return False
    else:
        if float(number_to_test) in accept_scores:
            return True
        else:
            print("Le score doit être 0, 1 ou 0.5 en cas de match nul")
            return False
