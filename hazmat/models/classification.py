from odoo import models, fields, api

class ClassificationMatrix(models.Model):
    _name = 'classification.matrix'
    
    classification = fields.Selection([
                        ('acid_w_w', 'Acid W/W'),
                        ('acid_sludge', 'Acid sludge'),
                        ('acids', 'Acids'),
                        ('alkyl_w_W', 'Alkyl W/W'),
                        ('amine_waste', 'Amine Waste'),
                        ('ammonia_w_w', 'Ammonia W/W'),
                        ('asbestos', 'Asbestos'),
                        ('batteries', 'Batteries'),
                        ('catalysts_etc', 'Catalysts etc'),
                        ('caustic_soda', 'Caustic Soda'),
                        ('chemical_sludge', 'Chemical Sludge'),
                        ('chemical_waste', 'Chemical Waste'),
                        ('chemical_w_w', 'Chemical W/W'),
                        ('chemicals', 'Chemicals'),
                        ('clay_waste', 'Clay Waste'),
                        ('diesel_w_w', 'Diesel W/W'),
                        ('drums_empty', 'Drums Empty'),
                        ('drums_full', 'Drums Full'),
                        ('fly_ash', 'Fly Ash'),
                        ('ibcs', 'IBCs'),
                        ('lime_waste', 'Lime Waste'),
                        ('oil_waste', 'Oil (Waste)'),
                        ('oily_sludge', 'Oily Sludge'),
                        ('oily_sludge_sol', 'Oily Sludge (Sol)'),
                        ('oily_w_w', 'Oily W/W'),
                        ('petrochemical_w_w', 'Petrochemical W/W'),
                        ('sewage', 'Sewage'),
                        ('soot_ash', 'Soot/Ash'),
                        ('spent_caustic_w_w', 'Spent Caustic W/W'),
                        ('sludge_to_landfill', 'Sludge to Landfill'),
                        ('solids_to_landfill', 'Solids to Landfill'),
                        ('sulphur_waste', 'Sulphur Waste'),
                        ('waste_to_landfill', 'Waste to Landfill'),
                    ])
    treatment_path = fields.Selection([
                        ('chemical', 'Chemical'),
                        ('asbestos', 'Asbestos'),
                        ('other', 'Other'),
                        ('catalyst', 'Catalyst'),
                        ('solids', 'Solids'),
                        ('oil', 'Oil'),
                        ('fly_ash_ash', 'Fly Ash/Ash'),
                        ('petrochemical', 'Petrochemical'),
                        ('sewage', 'Sewage'),
                        ('spent_caustic', 'Spent Caustic'),
                        ('landfill', 'Landfill'),
                    ])
    market_size = fields.Selection([
                            ('market', 'Market'),
                            ('non_market', 'Non Market'),
                        ])