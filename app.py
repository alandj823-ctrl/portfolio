from flask import Flask, render_template

app = Flask(__name__)

# Prosjektdata
prosjekter = {
    "mitt-forste-prosjekt": {
        "tittel": "Min egen nettside",
        "dato": "2026",
        "beskrivelse": "Denne nettsiden er et personlig prosjekt utviklet fra bunnen av for å lære mer om webutvikling og samtidig bygge min egen digitale portefølje. Gjennom prosjektet har jeg jobbet med HTML og CSS for struktur og design, samt Python og Flask for backend og dynamisk innhold. Nettsiden videreutvikles fortløpende etter hvert som jeg lærer nye teknologier og bygger flere prosjekter.",
        "teknologi": ["HTML", "CSS", "Python","Flask","Git","CoPilot"],
        "lenke": None
    },
    "python-prosjekt": {
        "tittel": "Miljødataanalyseapplikasjon",
        "dato": "2025",
        "beskrivelse": "En applikasjon for å analysere og visualisere miljødata ved hjelp av Python og dataanalyseverktøy.",
        "teknologi": ["Python","Pandas","Matplotlib","Prophet","Git"],
        "lenke": None,
        "dataflyt": [
            {"navn": "API", "detalj": "Værdata hentes fra en ekstern tjeneste"},
            {"navn": "JSON", "detalj": "Responsen mottas som strukturerte data"},
            {"navn": "Python / Pandas", "detalj": "Dataene leses inn i en DataFrame"},
            {"navn": "Databehandling", "detalj": "Verdier ryddes, sorteres og klargjøres"},
            {"navn": "Analyse / prediksjon", "detalj": "Modeller og visualiseringer gir innsikt"}
        ],
        "api_kode": "import requests\nimport pandas as pd\n\nurl = \"https://api.met.no/weatherapi/locationforecast/2.0/compact\"\nparametere = {\n    \"lat\": 59.91,\n    \"lon\": 10.75\n}\nheaders = {\"User-Agent\": \"miljodataanalyse/1.0 kontakt@eksempel.no\"}\n\nrespons = requests.get(url, params=parametere, headers=headers, timeout=30)\nrespons.raise_for_status()\nvaerdata = respons.json()\n\nperioder = vaerdata[\"properties\"][\"timeseries\"]\ndata = pd.json_normalize(perioder)\ndata[\"tid\"] = pd.to_datetime(data[\"time\"])\ndata = data.sort_values(\"tid\").reset_index(drop=True)",
        "bilder": [
            {
                "fil": "Skjermbilde 2026-08-24 125227.jpg",
                "tittel": "Temperaturprognose",
                "beskrivelse": "Visualiseringen viser forventet temperatur over tid, med et usikkerhetsintervall rundt prognosen.",
                "kode": "from prophet import Prophet\nimport matplotlib.pyplot as plt\n\nmodel = Prophet()\nmodel.fit(temperaturdata.rename(columns={\"dato\": \"ds\", \"temperatur\": \"y\"}))\n\nframtid = model.make_future_dataframe(periods=365)\nprognose = model.predict(framtid)\nmodel.plot(prognose)\nplt.title(\"Predikert temperatur basert på nedbør per dag\")\nplt.show()"
            },
            {
                "fil": "Skjermbilde 2026-08-24 125301.jpg",
                "tittel": "Temperatur og breddegrad",
                "beskrivelse": "Scatterplottet undersøker forholdet mellom temperatur, breddegrad og registrert solskinnstid.",
                "kode": "import matplotlib.pyplot as plt\n\nplt.scatter(\n    data[\"temperatur\"],\n    data[\"lufttrykk\"],\n    c=data[\"solskinn_timer\"],\n    cmap=\"coolwarm\",\n    alpha=0.75\n)\nplt.xlabel(\"Temperatur\")\nplt.ylabel(\"Lufttrykk\")\nplt.colorbar(label=\"Solskinnstimer før regn\")\nplt.show()"
            },
            {
                "fil": "Skjermbilde 2026-08-24 125326.jpg",
                "tittel": "Nedbør og lufttrykk",
                "beskrivelse": "Her analyseres sammenhengen mellom nedbør og lufttrykk, der fargen viser solskinnstimer før regn.",
                "kode": "plt.scatter(\n    data[\"lufttrykk\"],\n    data[\"nedbor\"],\n    c=data[\"solskinn_timer\"],\n    cmap=\"coolwarm\",\n    alpha=0.75\n)\nplt.xlabel(\"Lufttrykk (hPa)\")\nplt.ylabel(\"Nedbør (mm)\")\nplt.colorbar(label=\"Solskinnstimer før regn\")\nplt.show()"
            },
            {
                "fil": "Skjermbilde 2026-08-24 125353.jpg",
                "tittel": "Gjennomsnittlig nedbør",
                "beskrivelse": "Stolpediagrammet viser gjennomsnittlig nedbør per dag og fremhever perioder med mer nedbør.",
                "kode": "daglig_nedbor = data.groupby(\"dato\")[\"nedbor\"].mean()\n\nax = daglig_nedbor.plot(\n    kind=\"bar\",\n    figsize=(14, 6),\n    color=\"skyblue\"\n)\nax.set_title(\"Gjennomsnittlig nedbør per dag\")\nax.set_xlabel(\"Dag\")\nax.set_ylabel(\"Nedbør (mm)\")\nplt.tight_layout()\nplt.show()"
            },
            {
                "fil": "Skjermbilde 2026-08-24 125519.jpg",
                "tittel": "Daglig temperatur",
                "beskrivelse": "Tidsserien viser hvordan den daglige temperaturen i Oslo Blindern varierer gjennom flere år.",
                "kode": "data[\"dato\"] = pd.to_datetime(data[\"dato\"])\ndata = data.sort_values(\"dato\")\n\nplt.figure(figsize=(14, 5))\nplt.plot(data[\"dato\"], data[\"temperatur\"], color=\"#dc2626\")\nplt.title(\"Daglig temperatur i Oslo Blindern\")\nplt.xlabel(\"Dato\")\nplt.ylabel(\"Temperatur (°C)\")\nplt.grid(True, alpha=0.3)\nplt.show()"
            }
        ]
    },
    "regulering-av-temperatur-i-reaktorkjerne": {
        "tittel": "Regulering av temperatur i reaktorkjerne",
        "dato": "2026",
        "beskrivelse": "Jeg utviklet og analyserte en matematisk modell for temperaturregulering i en reaktorkjerne i et tenkt fisjonskraftverk.",
        "teknologi": ["Python", "MatLab", "SimuLink"],
        "lenke": None,
        "rapport": "TTK4105_Rapport_69_endelig.pdf",
        "bilder": [
            {
                "fil": "Reg1.png",
                "tittel": "Reg1",
                "beskrivelse": "Oversikt over modellen for temperaturregulering i reaktorkjernen."
            },
            {
                "fil": "Reg2.png",
                "tittel": "Reg2",
                "beskrivelse": "Illustrasjon av hvordan temperatur og regulering utvikler seg i modellen."
            },
            {
                "fil": "Reg3.png",
                "tittel": "Reg3",
                "beskrivelse": "Resultat fra simuleringen av temperaturresponsen i reaktorkjernen."
            },
            {
                "fil": "Reg4.png",
                "tittel": "Reg4",
                "beskrivelse": "Visualisering av reguleringssystemets respons på endringer i modellen."
            },
            {
                "fil": "Reg5.png",
                "tittel": "Reg5",
                "beskrivelse": "Simuleringsresultat som viser modellens oppførsel over tid."
            },
            {
                "fil": "Reg6.png",
                "tittel": "Reg6",
                "beskrivelse": "Analysefigur fra arbeidet med temperaturregulering i reaktorkjernen."
            },
            {
                "fil": "Reg7.png",
                "tittel": "Reg7",
                "beskrivelse": "Sammenstilling av en sentral størrelse fra reguleringsmodellen."
            },
            {
                "fil": "Reg8.png",
                "tittel": "Reg8",
                "beskrivelse": "Avsluttende visualisering av resultatene fra simuleringen."
            }
        ]
    },
    "co2-fangst": {
        "tittel": "CO2 fangst",
        "dato": "2024",
        "beskrivelse": "Problemstillingen, ≪Har Norge potensiale for utvikling av CCS, og kan dette være en del av løsningen pa verdens CO2-utslipp? ˚ ≫, er sentral gjennom alle deloppgavene.",
        "mal": [
            {
                "tittel": "Problemstilling",
                "tekst": "Kan CCS være en realistisk og viktig del av løsningen for å redusere globale CO2-utslipp, og hva er Norges potensial for dette?"
            },
            {
                "tittel": "Om prosjektet",
                "tekst": "Dette prosjektet undersøkte muligheten for å utvikle CO2-fangst og lagring i Norge som en del av en større klimamålstrategi. Arbeidet fokuserte på teknologi, økonomi, politiske rammebetingelser og hvilke barrierer som må overvinnes for at løsningen skal bli praktisk gjennomførbar."
            },
            {
                "tittel": "Resultater",
                "tekst": "Prosjektet konkluderte med at Norge har gode forutsetninger for å bidra til CO2-fangst, spesielt gjennom eksisterende industri, geologiske lagringsmuligheter og teknologisk kompetanse. Samtidig viste analysen at løsningen krever stor investering, sterk politisk støtte og gode samarbeidsmodeller mellom offentlige og private aktører. CCS kan derfor være en viktig del av overgangsstrategien, men ikke alene er tilstrekkelig for å nå klimamålene."
            },
            {
                "tittel": "Mitt bidrag",
                "tekst": "Jeg bidro med analyse av løsningen, vurdering av forutsetningene for utvikling i Norge og strukturering av prosjektets hovedfunn. Jeg jobbet også med å sammenfatte hvordan CCS kan brukes som del av en bærekraftig og realistisk klimapolitikk."
            }
        ],
        "teknologi": [],
        "lenke": None,
        "presentasjon": "PBL2_uten_forste_slide.pdf"
    },
    "prosjektering-av-solkraftverk": {
        "tittel": "Prosjektering av solkraftverk",
        "dato": "2026",
        "beskrivelse": "Et prosjektarbeid med prosjektering og vurdering av et solkraftverk.",
        "mal": [
            {
                "tittel": "Problemstilling",
                "tekst": "Hvordan kan vi optimalisere prosjekteringen av et tenkt solkraftverk?≫."
            },
            {
                "tittel": "Om prosjektet",
                "tekst": "Denne oppgaven omhandler en tenkt prosjektering av et solkraftverk, og beregninger og analyser tilknyttet dette. Det blir diskutert hvilke solceller som er best a ta i bruk, og regnet på hvilken produksjon disse cellene vil kunne gi. Deretter vil det vises hvordan solcellepanelene koples og organiseres sammen, og avslutningsvis drøftes miljøkonsekvensene av solkraftverket."
            },
            {
                "tittel": "Resultater",
                "tekst": "I denne rapporten ble det laget et solkraftverk på et 5000 m² stort lagerbygningstak. Først ble forskjellige typer solcellepaneler undersøkt og sammenlignet, hvorav typen polykrystallinske skal brukes i dette solcellekraftverket. Deretter ble det gjort beregninger knyttet til installasjon og ytelse av solcellepanelene. Det ble funnet ut at det var plass til 2060 solcellepaneler på taket, som forventes å gi en årlig energiproduksjon på 618 MWh. Dette med en maksimal effekt på 721 kW. Solkraftverket har dessuten en total årlig energitetthet på 0,145 TWh/km². Panelene er organisert i serier og paralleller, hvor 8 elektriske grupper består av 225 paneler, og 2 elektriske grupper består av 130 paneler. Dette sikrer at parken er innenfor de gitte kapasitetsrammene, og dermed sikker drift og energiproduksjon. Miljøkonsekvensene av solcelleverket er minimale, da det utnytter eksisterende bygningsareal uten behov for ytterligere utbyggelse i naturen. Gjennom prosjektets beregninger kan det derfor konkluderes med at solkraftverk med polykrystallinske celler på lagerbygningstak, organisert i grupper på 225 og 130, er en av mange optimale prosjekteringer av en solcellepark som en effektiv og bærekraftig energiløsning."
            },
            {
                "tittel": "Mitt bidrag",
                "tekst": "Jeg bidro med analyse av forutsetningene for anlegget, dimensjonering av solcellemoduler og sammenstilling av resultatene. Jeg arbeidet også med å dokumentere vurderingene og presentere prosjektets tekniske løsning."
            }
        ],
        "bilder": [
            {
                "fil": "resultatpbl1.png",
                "tittel": "Resultatoversikt",
                "beskrivelse": "Oversikt over beregnet kapasitet, energiproduksjon og layout for solkraftverket."
            },
            {
                "fil": "resultat2pbl1.png",
                "tittel": "Produksjon og effekt",
                "beskrivelse": "Visualisering av forventet produksjon og dimensjonering av solcelleanlegget."
            },
            {
                "fil": "resultat3pbl1.png",
                "tittel": "Gruppering og kobling",
                "beskrivelse": "Illustrasjon av hvordan panelene er organisert i serier og parallellgrupper."
            },
            {
                "fil": "resultat4pbl1.png",
                "tittel": "Miljø- og konseptanalyse",
                "beskrivelse": "Konklusjon om bærekraft, byggemodul og nyttig utnyttelse av takareal."
            }
        ],
        "bilder_intro": "Et utvalg av de viktigste visualiseringene og beregningene som viser prosjektets resultater.",
        "teknologi": [],
        "lenke": None
    },
    "nullutslippsomrade-flyplassutvikling-bodo": {
        "tittel": "Nullutslippsområde, Flyplassutvikling, Bodø",
        "dato": "2024",
        "beskrivelse": "Oppgaven tar for seg den gamle flyplassen i Bodø, som skal utvikles til en ny bydel. Denne bydelen skal være et nullutslippsområde, som er et område der klimagassutslippene går mot null over en gitt periode. Rapporten diskuterer hvilke løsninger som kan være mulig for å oppnå målet om nullutslipputvikling.",
        "mal": [
            {
                "tittel": "Problemstilling",
                "tekst": "Hvordan kan en gammel flyplassområde i Bodø utvikles til et nullutslippsområde som samtidig skaper en bærekraftig og funksjonell bydel?"
            },
            {
                "tittel": "Om prosjektet",
                "tekst": "Prosjektet vurderte hvordan et tidligere flyplassområde kunne omformes til en moderne, klimavennlig bydel med fokus på energieffektivitet, transport, arealbruk og bærekraftige løsninger. Analysen tok utgangspunkt i konkrete byutviklingsmuligheter og undersøkte hvilke tiltak som ville være mest effektive for å nå nullutslippsmål."
            },
            {
                "tittel": "Resultater",
                "tekst": "Resultatet viste at et nullutslippsområde kan oppnås gjennom en kombinasjon av bærekraftige transportløsninger, energieffektive bygg, grønn infrastruktur, lokale energisystemer og strategisk arealplanlegging. I prosjektet ble det lagt vekt på hvordan utbygging kan skape verdi for både innbyggere og næringsliv samtidig som klimagassutslipp reduseres i takt med byens utvikling."
            },
            {
                "tittel": "Mitt bidrag",
                "tekst": "Jeg bidro med analysen av utviklingsmulighetene, vurdering av bærekraftige konsept og sammenstilling av prosjektets hovedfunn. Jeg jobbet også med å forklare hvordan nullutslippsmål kan omsettes til konkrete areal- og byutviklingsløsninger."
            }
        ],
        "teknologi": [],
        "lenke": None,
        "presentasjon": "PBL3_uten_forste_slide.pdf"
    }

}

@app.route("/")
def home():
    return render_template("app.html")

@app.route("/om-meg")
def om_meg():
    return render_template("om-meg.html")

@app.route("/prosjekt/<prosjekt_id>")
def prosjekt_detalj(prosjekt_id):
    prosjekt = prosjekter.get(prosjekt_id)
    if prosjekt:
        return render_template("prosjekt.html", prosjekt=prosjekt)
    else:
        return "Prosjektet ble ikke funnet", 404

if __name__ == "__main__":
    app.run(debug=True)
