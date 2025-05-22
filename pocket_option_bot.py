class PocketOptionBot:
    def __init__(self):
        self.mode = "demo"
        self.min_amount = 1.0

    def set_mode(self, mode):
        if mode in ["demo", "real"]:
            self.mode = mode
            return f"Mode de trading défini sur {mode}."
        return "Mode invalide."

    def set_min_amount(self, amount):
        self.min_amount = amount
        return f"Montant minimum défini à {amount} $."

    def get_profitable_assets(self):
        # Simulation, en pratique cette fonction devra utiliser une API ou un scraper
        return ["EURUSD", "USDJPY", "BTCUSD"]

    def place_trade(self, asset, direction):
        return f"Trade {'ACHAT' if direction == 'call' else 'VENTE'} sur {asset} en {self.mode} avec {self.min_amount}$."