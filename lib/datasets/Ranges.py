
def Ranges():
    """
    Returns dictionaries with pre-defined ranges for various parameters used in the flights dataset analysis.

    Returns:
    price_ranges (dict): Dictionary with pre-defined price ranges.
    time_cols_dict (dict): Dictionary with pre-defined time of day ranges.
    cities_dict (dict): Dictionary mapping city names to their respective airport codes.
    price_ranges_air (dict): Dictionary with pre-defined Airbnb price ranges.
    beds_ranges (dict): Dictionary with pre-defined Airbnb bed count ranges.
    people_ranges (dict): Dictionary with pre-defined Airbnb guest count ranges.
    reviews_ranges (dict): Dictionary with pre-defined Airbnb review count ranges.
    """

    price_ranges = {'PriceLvl_1': [0, 100], 'PriceLvl_2': [100, 200], 'PriceLvl_3': [200, 300], 'PriceLvl_4': [300, 400], 
                'PriceLvl_5': [400, 500], 'PriceLvl_6': [500, 600], 'PriceLvl_7': [600, 700], 'PriceLvl_8': [700, 800], 
                'PriceLvl_9': [800, 900], 'PriceLvl_10': [900, 1000], 'PriceLvl_15': [1000, 1500], 
                'PriceLvl_20': [1500, 2000], 'PriceLvl_30': [2000, 3000], 'PriceLvl_40': [3000, 4000]}

    time_cols_dict = {
    'EarlyMorning': [4, 7],
    'Morning': [7, 12],
    'Noon': [12, 16],
    'Afternoon': [16, 19],
    'Evening': [19, 23],
    'Night': [0, 4]
}

    cities_dict = {'Tirana': 'TIA',
 'Graz': 'GRZ',
 'Innsbruck': 'INN',
 'Brussels': 'CRL',
 'Paphos': 'PFO',
 'Tallinn': 'TLL',
 'Helsinki': 'HEL',
 'Turku': 'TKU',
 'Lille': 'LIL',
 'Lyon': 'LYS',
 'Paris': 'ORY',
 'Kutaisi': 'KUT',
 'Dresden': 'DRS',
 'Leipzig': 'LEJ',
 'Munich': 'MUC',
 'Athens': 'ATH',
 'Chania': 'CHQ',
 'Santorini': 'JTR',
 'Thessaloniki': 'SKG',
 'Knock, County Mayo': 'NOC',
 'County Kerry': 'KIR',
 'Cagliari': 'CAG',
 'Catania': 'CTA',
 'Naples': 'NAP',
 'Olbia': 'OLB',
 'Trapani': 'TPS',
 'Venice': 'TSF',
 'Kaunas': 'KUN',
 'Vilnius': 'VNO',
 'Oslo': 'TRF',
 'Stavanger': 'SVG',
 'Warsaw': 'WMI',
 'Timișoara': 'TSR',
 'Niš': 'INI',
 'Málaga': 'AGP',
 'Alicante': 'ALC',
 'Almería': 'LEI',
 'Asturias': 'OVD',
 'Bilbao': 'BIO',
 'Barcelona': 'BCN',
 'Badajoz': 'BJZ',
 'Béziers': 'BZR',
 'Brindisi': 'BDS',
 'Donostia / San Sebastián': 'EAS',
 'Fuerteventura': 'FUE',
 'Girona': 'GRO',
 'Granada': 'GRX',
 'Ibiza': 'IBZ',
 'Jerez de la Frontera': 'XRY',
 'A Coruña': 'LCG',
 'Lanzarote': 'ACE',
 'Madrid': 'MAD',
 'Agadir': 'AGA',
 'Menorca': 'MAH',
 'Melilla': 'MLN',
 'Palma, Majorca': 'PMI',
 'Pamplona': 'PNA',
 'Santander': 'SDR',
 'Seville': 'SVQ',
 'Tenerife': 'TFS',
 'Valencia': 'VLC',
 'Valladolid': 'VLL',
 'Vigo': 'VGO',
 'Vitoria-Gasteiz': 'VIT',
 'Valverde': 'VDE',
 'Zaragoza': 'ZAZ',
 'Santiago de Compostela': 'SCQ'}
    price_ranges_air = {'PriceLvl_1_airbnb': [0, 100], 'PriceLvl_2_airbnb': [100, 200], 'PriceLvl_3_airbnb': [200, 300], 
                    'PriceLvl_4_airbnb': [300, 400], 'PriceLvl_5_airbnb': [400, 500], 'PriceLvl_6_airbnb': [500, 600], 
                    'PriceLvl_7_airbnb': [600, 700], 'PriceLvl_8_airbnb': [700, 800], 'PriceLvl_9_airbnb': [800, 900], 
                    'PriceLvl_10_airbnb': [900, 1000], 'PriceLvl_11_airbnb': [1000, 1100], 'PriceLvl_12_airbnb': [1100, 1200], 
                    'PriceLvl_13_airbnb': [1200, 1300], 'PriceLvl_14_airbnb': [1300, 1400], 'PriceLvl_15_airbnb': [1400, 1500], 
                    'PriceLvl_16_airbnb': [1500, 1600], 'PriceLvl_17_airbnb': [1600, 1700], 'PriceLvl_18_airbnb': [1700, 1800], 
                    'PriceLvl_19_airbnb': [1800, 1900], 'PriceLvl_20_airbnb': [1900, 2000]}

    beds_ranges = {'Beds_1_airbnb': [0, 1], 'Beds_2_airbnb': [1, 2], 'Beds_3_airbnb': [2, 3], 'Beds_4_airbnb': [3, 4], 
                'Beds_5_airbnb': [4, 5], 'Beds_6_airbnb': [5, 6], 'Beds_7_airbnb': [6, 7], 'Beds_8_airbnb': [7, 8], 
                'Beds_9_airbnb': [8, 9], 'Beds_10_airbnb': [9, 10]}

    people_ranges = {'People_1_airbnb': [0, 1], 'People_2_airbnb': [1, 2], 'People_3_airbnb': [2, 3], 'People_4_airbnb': [3, 4], 
                    'People_5_airbnb': [4, 5], 'People_6_airbnb': [5, 6], 'People_7_airbnb': [6, 7], 'People_8_airbnb': [7, 8], 
                    'People_9_airbnb': [8, 9], 'People_10_airbnb': [9, 10]}

    reviews_ranges = {'Reviews_1_airbnb': [0, 200], 'Reviews_2_airbnb': [200, 400], 'Reviews_3_airbnb': [400, 600], 
                    'Reviews_4_airbnb': [600, 800], 'Reviews_5_airbnb': [800, 1000]}



    return price_ranges, time_cols_dict, cities_dict, price_ranges_air, beds_ranges, people_ranges, reviews_ranges