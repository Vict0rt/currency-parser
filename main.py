from parser import privat_usd
from datetime import datetime
from itc_top_material import top_site_material

print("Привіт!\nКурс долара Приват банк: " + privat_usd(), ' ', datetime.now().strftime("%Y-%m-%d %H:%M"))
print("Топ матеріал на ITC.UA:")
print(*top_site_material(), sep='\n')