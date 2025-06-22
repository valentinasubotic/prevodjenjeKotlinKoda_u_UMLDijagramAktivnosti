# Ovaj skript služi da uzme PlantUML kod (tekstualni opis dijagrama) i pomoću PlantUML alata (Java aplikacije)
# transformiše taj kod u grafički format (kao što su PNG, SVG, itd.).
#
# Koraci:
# 1. Uzima PlantUML kod (tekstualni opis dijagrama).
# 2. Pokreće PlantUML JAR koristeći Java da generiše sliku dijagrama (npr. PNG fajl).
# 3. Snima tu sliku na disk.
# Prije ovoga proverava da li je Java dostupna sistemu i da li postoji plantuml.jar fajl.

import os
import subprocess
import shutil

OUTPUT_FOLDER = "output"
PLANTUML_JAR = "plantuml.jar"

def generate_uml_image(plantuml_code: str, base_name: str):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    if not shutil.which("java"):
        print("[GREŠKA] Java nije instalirana ili nije dostupna u PATH-u.")
        return

    if not os.path.exists(PLANTUML_JAR):
        print(f"[GREŠKA] Ne postoji fajl: {PLANTUML_JAR}")
        return

    puml_path = os.path.join(OUTPUT_FOLDER, base_name + ".puml")
    with open(puml_path, "w", encoding="utf-8") as f:
        f.write("@startuml\n")
        f.write(plantuml_code)
        f.write("\n@enduml\n")

    subprocess.run(["java", "-jar", PLANTUML_JAR, puml_path])
    print(f"Dijagram generisan i sacuvan : {os.path.join(OUTPUT_FOLDER, base_name + '.png')}")
