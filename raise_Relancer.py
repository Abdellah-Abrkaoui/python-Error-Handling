def action_risquee():
    try:
        raise ValueError("Erreur dans l'action risquée")
    except ValueError as e:
        print(f"Erreur capturée dans l'action : {e}")
        raise  # Relance l'exception pour la propager plus loin

try:
    action_risquee()
except ValueError as e:
    print(f"Erreur propagée au niveau principal : {e}")
