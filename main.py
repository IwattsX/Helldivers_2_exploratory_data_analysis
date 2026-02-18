import json
from pprint import pprint
from collections import OrderedDict

file_name = "HD2_data.json"
planet_names = ["SUPER EARTH", "KLEN DAHTH II", "PATHFINDER V", "WIDOW'S HARBOR", "NEW HAVEN", "PILEN V", "HYDROFALL PRIME", "ZEA RUGOSIA", "DARROWPORT", "FORNSKOGUR II", "MIDASBURG", "CERBERUS IIIC", "PROSPERITY FALLS", "OKUL VI", "MARTYR'S BAY", "FREEDOM PEAK", "FORT UNION", "KELVINOR", "WRAITH", "IGLA", "NEW KIRUNA", "FORT JUSTICE", "ZEGEMA PARADISE", "PROVIDENCE", "PRIMORDIA", "SULFURA", "NUBLARIA I", "KRAKATWO", "VOLTERRA", "CRUCIBLE", "VEIL", "MARRE IV", "FORT SANCTUARY", "SEYSHEL BEACH", "HELLMIRE", "EFFLUVIA", "SOLGHAST", "DILUVIA", "VIRIDIA PRIME", "OBARI", "MYRADESH", "ATARAMA", "EMERIA", "BARABOS", "FENMIRE", "MASTIA", "SHALLUS", "KRAKABOS", "IRIDICA", "AZTERRA", "AZUR SECUNDUS", "IVIS", "SLIF", "CARAMOOR", "KHARST", "EUKORIA", "MYRIUM", "KERTH SECUNDUS", "PARSH", "REAF", "IRULTA", "EMORATH", "ILDUNA PRIME", "MAW", "BOREA", "CURIA", "TARSH", "SHELT", "IMBER", "BLISTICA", "RATCH", "JULHEIM", "VALGAARD", "ARKTURUS", "ESKER", "TERREK", "CIRRUS", "CRIMSICA", "HEETH", "VELD", "ALTA V", "URSICA XI", "INARI", "SKAASH", "MORADESH", "RASP", "BASHYR", "REGNUS", "MOG", "VALMOX", "IRO", "GRAFMERE", "NEW STOCKHOLM", "OASIS", "GENESIS PRIME", "OUTPOST 32", "CALYPSO", "ELYSIAN MEADOWS", "ALDERIDGE COVE", "TRANDOR", "EAST IRIDIUM TRADING BAY", "LIBERTY RIDGE", "BALDRICK PRIME", "THE WEIR", "KUPER", "OSLO STATION", "PÖPLI IX", "GUNVALD", "DOLPH", "BEKVAM III", "DUMA TYR", "VERNEN WELLS", "AESIR PASS", "AURORA BAY", "PENTA", "GAELLIVARE", "VOG-SOJOTH", "KIRRIK", "MORTAX PRIME", "WILFORD STATION", "PIONEER II", "ERSON SANDS", "SOCORRO III", "BORE ROCK", "FENRIR III", "TURING", "ANGEL'S VENTURE", "DARIUS II", "ACAMAR IV", "ACHERNAR SECUNDUS", "ACHIRD III", "ACRAB XI", "ACRUX IX", "ACUBENS PRIME", "ADHARA", "AFOYAY BAY", "AIN-5", "ALAIRT III", "ALAMAK VII", "ALARAPH", "ALATHFAR XI", "ANDAR", "ASPEROTH PRIME", "BELLATRIX", "BOTEIN", "OSUPSAM", "BRINK-2", "BUNDA SECUNDUS", "CANOPUS", "CAPH", "CASTOR", "DURGEN", "DRAUPNIR", "MORT", "INGMAR", "CHARBAL-VII", "CHARON PRIME", "CHOEPESSA IV", "CHOOHE", "CHORT BAY", "CLAORELL", "CLASA", "DEMIURG", "DENEB SECUNDUS", "ELECTRA BAY", "ENULIALE", "EPSILON PHOENCIS VI", "ERATA PRIME", "ESTANU", "FORI PRIME", "GACRUX", "GAR HAREN", "GATRIA", "GEMMA", "GRAND ERRANT", "HADAR", "HAKA", "HALDUS", "HALIES PORT", "HERTHON SECUNDUS", "HESOE PRIME", "HEZE BAY", "HORT", "HYDROBIUS", "KARLIA", "KEID", "KHANDARK", "KLAKA 5", "KNETH PORT", "KRAZ", "KUMA", "LASTOFE", "LENG SECUNDUS", "LESATH", "MAIA", "MALEVELON CREEK", "MANTES", "MARFARK", "MARTALE", "MATAR BAY", "MEISSA", "MEKBUDA", "MENKENT", "MERAK", "MERGA IV", "MINCHIR", "MINTORIA", "MORDIA 9", "NABATEA SECUNDUS", "NAVI VII", "NIVEL 43", "OSHAUNE", "OVERGOE PRIME", "PANDION-XXIV", "PARTION", "PEACOCK", "PHACT BAY", "PHERKAD SECUNDUS", "POLARIS PRIME", "POLLUX 31", "PRASA", "PROPUS", "RAS ALGETHI", "RD-4", "ROGUE 5", "RIRGA BAY", "SEASSE", "SENGE 23", "SETIA", "SHETE", "SIEMNOT", "SIRIUS", "SKAT BAY", "SPHERION", "STOR THA PRIME", "STOUT", "TERMADON", "TIBIT", "TIEN KWAN", "TROOST", "UBANEA", "USTOTU", "VANDALON IV", "VARYLIA 5", "WASAT", "VEGA BAY", "WEZEN", "VINDEMITARIX PRIME", "X-45", "YED PRIOR", "ZEFIA", "ZOSMA", "ZZANIAH PRIME", "SKITTER", "EUPHORIA III", "DIASPORA X", "GEMSTONE BLUFFS", "ZAGON PRIME", "OMICRON", "MARS"]

with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

planets_to_data = dict()
war_stats = data.get("warStats")
for stats in war_stats.get("planets_stats", []):
    planet_idx = stats.get('planetIndex', None)
    mission_success_rate = stats.get('missionSuccessRate', 0)
    mission_loss_rate = 100.0 - mission_success_rate
    # if planet_idx is None:
    #     continue
    # if mission_success_rate == 0 or mission_success_rate == 100:
    #     continue
    #
    if planet_idx >= 260 or planet_idx < 0:
        continue
    # print(planet_idx)
    planets_to_data[planet_idx] = {
        'mission_success_rate': round(mission_success_rate,1),
        'mission_loss_rate' : round(mission_loss_rate, 1),
        'planet_name' : planet_names[planet_idx]
    }


# pprint(planets_to_data)
res = OrderedDict(sorted(planets_to_data.items(), key=lambda item: item[1]['mission_success_rate']))
pprint(res)

# print(len(planet_names))
