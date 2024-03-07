import random
import select
import csinsc

#**DIVISIONS**

#INFANTRY DIVISION TYPE: (1,2,3)
#1: LIGHT INFANTRY DIVISION (5000MP, 10SUP, 0ART, 500INFA)
#2: MEDIUM INFANTRY DIVISION (6000MP, 30SUP, 50ART, 840INFA)
#3: HEAVY INFANTRY DIVISION (12000MP, 70SUP, 100ART, 2000INFA)

#TANK DIVISION TYPE: (1,2,3)
#1: LIGHT TANK DIVISION (10000MP, 100SUP, 100ART, 300LTE)
#2: MEDIUM TANK DIVISION (10000MP, 200SUP, 200ART, 300MTE)
#3: HEAVY TANK DIVISION (10000MP, 700SUP, 400ART, 300HTE)

#**EQUIPMENT**

#MANPOWER MAXIMUM FOR COUNTRY (NUM)
#MANPOWER AVAILABLE (NUM) (CONSCRIPTION LAW TIMES MANPOWER MAXIMUM TIMES STABLITY AS A PERCENTAGE)
#SUPPORT EQUIPMENT (NUM)
#ARTILLERY EQUIPMENT (NUM)
#INFANTRY EQUIPMENT (NUM)
#LIGHT TANK EQUIPMENT (NUM)
#MEDIUM TANK EQUIPMENT (NUM)
#HEAVY TANK EQUIPMENT (NUM)
#FIGHTERS EQUIPMENT (NUM) - ASSIST IN EVERY BATTLE, IF You HAVE MORE FIGHTERS YOU GET 10% ADVANTAGE
#ANTIAIR EQUIPMENT (NUM) - ASSIST IN EVERY BATTLE, IF ANTIAIR > FIGHTERS FROM OTHER TEAM, THEIR FIGHTERS INFLICT NO DAMAGE
#PORT GUARDS (TRUE/FALSE) - PORT GUARDS ASSIST IN BATTLES IN THE CORNERS OF THE MAP. DEFENCE +10

#**FACTORIES**

#FACTORY USED AS CIVILIAN FACTORIES: (NUM)
#FACTORY USED AS MILITARY FACTORIES: (NUM)
#FACTORY COUNT EVERY MONTH: (ADDS ON BY WHAT?) (CONSCRIPTION LAW + STABILITY DETERMINES SPEED OF THIS)
#START: HALF ON INFANTRY EQUIPMENT, THIRD OF REST IS ARTILLERY, REST IS SUPPORT EQUIPMENT

#**DECISIONS**

#STABILITY: (NUM)
#CONSCRIPTION LAWS: (1,2,3,4,5) #(5%, 10%, 15%, 20%, 25%), STABILITY: (-0, -5, -10, -20, -50)
#CIV TO MIL CONVERSION: -20 CIVS +20 MILS BUT MANPOWER GOES DOWN BY 25% IN PROTEST, STABILITY -20
#WAR ECONOMY: (TRUE/FALSE) MANPOWER GOES DOWN BY 25% IN PROTEST, STABILITY -20 
#SAFE WORKPLACE: STABILITY +20, 10% OF MILS SHUT DOWN AND 10% OF FACTORIES BEING BUILT IS NOT DONE DUE TO BAD WORK PLACES
#INFRASTRUCTURE: STABLITY +10, 20% OF FACTORIES BEING BUILT IS NOT DONE TO MAKE INFRASTRUCTRE BETTER

#**SPIRITS**
#1 DISJOINTED GOVERNMENT
#2 BITTER LOSER 
#3 POLITICAL PARANOIA
#4 BRITISH STOICISM
#5 NEUTRALISM
#6 SICK MAN OF EUROPE
#7 FOR OUR SURVIVAL
#8 NEED FOR GREATNESS
#9 WE HAVE NOT YET LOST
#10 HUNGER AND MINORITIES
#11 CAUDILLO'S STRUGGLES
#12 FOREIGN COMPANIES
#13 MOUNTAIN COUNTRY
#14 REPUBLICAN UNREST

#MAJORS

FRA =   {"manpower_max": 45000000,
        "stability": 40,
        "conscription_law": 2,
        "civilian_factories": 10,
        "military_factories": 8,
        "port_guards": False,
        "support": 200,
        "artillery": 1000,
        "infantry": 30000,
        "light_tank": 1000,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 200,
        "antiair": False}
        
GER = {"manpower_max": 80000000,
        "stability": 20,
        "conscription_law": 1,
        "civilian_factories": 20,
        "military_factories": 3,
        "port_guards": False,
        "support": 150,
        "artillery": 500,
        "infantry": 15000,
        "light_tank": 0,
        "medium_tank": 700,
        "heavy_tank": 0,
        "fighters": 100,
        "antiair": False}
        
SOV = {"manpower_max": 170000000,
        "stability": 15,
        "conscription_law": 1,
        "civilian_factories": 25,
        "military_factories": 4,
        "port_guards": False,
        "support": 200,
        "artillery": 1000,
        "infantry": 30000,
        "light_tank": 700,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 100,
        "antiair": False}
        
ENG = {"manpower_max": 50000000,
        "stability": 60,
        "conscription_law": 1,
        "civilian_factories": 15,
        "military_factories": 4,
        "port_guards": False,
        "support": 200,
        "artillery": 1000,
        "infantry": 30000,
        "light_tank": 700,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 300,
        "antiair": True}

USA = {"manpower_max": 150000000,
        "stability": 70,
        "conscription_law": 1,
        "civilian_factories": 27,
        "military_factories": 4,
        "port_guards": False,
        "support": 100,
        "artillery": 500,
        "infantry": 10000,
        "light_tank": 500,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 400,
        "antiair": True}
        
ITA = {"manpower_max": 50000000,
        "stability": 40,
        "conscription_law": 2,
        "civilian_factories": 12,
        "military_factories": 3,
        "port_guards": False,
        "support": 300,
        "artillery": 500,
        "infantry": 20000,
        "light_tank": 500,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 100,
        "antiair": False}
        
JAP = {"manpower_max": 70000000,
        "stability": 15,
        "conscription_law": 1,
        "civilian_factories": 25,
        "military_factories": 4,
        "port_guards": False,
        "support": 200,
        "artillery": 1000,
        "infantry": 30000,
        "light_tank": 700,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 100,
        "antiair": False}
        
CHI = {"manpower_max": 270000000,
        "stability": 10,
        "conscription_law": 1,
        "civilian_factories": 8,
        "military_factories": 7,
        "port_guards": False,
        "support": 0,
        "artillery": 0,
        "infantry": 40000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 0,
        "antiair": 0}
        
#MINORS

POL = {"manpower_max": 35000000,
        "stability": 40,
        "conscription_law": 2,
        "civilian_factories": 7,
        "military_factories": 4,
        "port_guards": False,
        "support": 0,
        "artillery": 500,
        "infantry": 15000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 200,
        "antiair": False}
        
IND = {"manpower_max": 377000000,
        "stability": 20,
        "conscription_law": 1,
        "civilian_factories": 5,
        "military_factories": 5,
        "port_guards": False,
        "support": 150,
        "artillery": 500,
        "infantry": 20000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 100,
        "antiair": False}
        
MEX = {"manpower_max": 20000000,
        "stability": 30,
        "conscription_law": 1,
        "civilian_factories": 7,
        "military_factories": 4,
        "port_guards": False,
        "support": 200,
        "artillery": 1000,
        "infantry": 10000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 100,
        "antiair": False}
        
BRA = {"manpower_max": 40000000,
        "stability": 30,
        "conscription_law": 1,
        "civilian_factories": 9,
        "military_factories": 4,
        "port_guards": False,
        "support": 0,
        "artillery": 1000,
        "infantry": 15000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 300,
        "antiair": False}

SWI = {"manpower_max": 5000000,
        "stability": 70,
        "conscription_law": 1,
        "civilian_factories": 8,
        "military_factories": 5,
        "port_guards": False,
        "support": 100,
        "artillery": 5000,
        "infantry": 20000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 0,
        "antiair": True}
        
SPA = {"manpower_max": 25000000,
        "stability": 20,
        "conscription_law": 1,
        "civilian_factories": 5,
        "military_factories": 4,
        "port_guards": False,
        "support": 500,
        "artillery": 500,
        "infantry": 5000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 0,
        "antiair": False}

DUT = {"manpower_max": 80000000,
        "stability": 50,
        "conscription_law": 1,
        "civilian_factories": 6,
        "military_factories": 4,
        "port_guards": True,
        "support": 500,
        "artillery": 500,
        "infantry": 10000,
        "light_tank": 0,
        "medium_tank": 0,
        "heavy_tank": 0,
        "fighters": 100,
        "antiair": False}

BLANK = NOCOUNTRY

Countries = {"Player1": BLANK,
             "Player2": DUT)}

print(r'''
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        ''')
AskforCountry = True
while AskforCountry == True:
    Countryselected = input(f'''
       I Shall Return (temporary name for game)                        
-----------------------------------------------------
             Created by: James Spaven 
          Contributors: Mitchell Kennedy                 
-----------------------------------------------------
|                 Select a Country                  |
-----------------------------------------------------
|   + USA          + Germany        + Soviet Union  |  
|   + France       + Italy          + China         |
|   + UK           + Japan          +               |
|                  +                +               |
|---------------------------------------------------|
|   + Mexico       + Poland         + Switzerland   |
|   + Brazil       + Spain          + India         |  
|---------------------------------------------------|
|   + Player 1: Countries{Player1}                  |
|   + Player 2: Countries{Player2}                  |
-----------------------------------------------------                          
Write the country name to play that country. Ex. Player1.USA for player 1 to play with the USA.  
Write "Info.country" for info about the specific nation. DUT = the Dutch Empire (Always AI, cannot be selected for a human player.)           ''')
    def FRA(), GER(), SOV(), ENG(), USA(), ITA(), JAP(), CHI(), POL(), IND(), MEX(), BRA(), SWI(), SPA(), DUT():
        OtherPlayer = DUT
        if str(Player1) in Countryselected:
            if str(Countryselected) - str(Player1) = str(FRA) or str(GER) or str(SOV) or str(ENG) or str(USA) or str(ITA) or str(JAP) or str(CHI) or str(POL) or str(IND) or str(MEX) or str(BRA) or str(SWI) or str(SPA)
                Countries{Player1} = str(Countryselected) - str(Player1)
        elif str(Player2) in Countryselected:
            if str(Countryselected) - str(Player1) = str(FRA) or str(GER) or str(SOV) or str(ENG) or str(USA) or str(ITA) or str(JAP) or str(CHI) or str(POL) or str(IND) or str(MEX) or str(BRA) or str(SWI) or str(SPA)
                Countries{Player1} = str(Countryselected) - str(Player2)
        elif Countryselected = str(FRA) or str(GER) or str(SOV) or str(ENG) or str(USA) or str(ITA) or str(JAP) or str(CHI) or str(POL) or str(IND) or str(MEX) or str(BRA) or str(SWI) or str(SPA):
            if str(Countryselected) - str(Player1) = str(FRA) or str(GER) or str(SOV) or str(ENG) or str(USA) or str(ITA) or str(JAP) or str(CHI) or str(POL) or str(IND) or str(MEX) or str(BRA) or str(SWI) or str(SPA)
                Countries{Player1} = str(Countryselected) - str(Player1)
        elif Countryselected = str"Done":
            AskforCountry = False
        else None

Game = True
Player = 2
Gamestart = True
Keepgoing = True
Input = str("1")
while Game == True:
    userCountry = Countries{Player1}
    while Keepgoing == True:
        int(Player) = int(Player) + int(1) #Switches between Players
        if int(Player) = int(3)
            int(Player) = int(1) 
            userCountry = Countries{Player1}
        if int(Player) = int(2):
            userCountry = Countries{Player2}
        
        if Gamestart == True:
            Input = str(1)
        Gamestart = False
        print(r'''
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        ''')
        if Input == str("1"):
            Menu_on = 1
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| NEXT PLAYER 
|_____________________|_______________|
____________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ GOVERNMENT (5) \\
|___________|_______________|_______________|_______________|________________|

   +--------+--------+--------+--------+
   |  FRA   |  FRA   |  GER   |  GER   |
   |        |        |        |        |
   +--------+--------+--------+--------+
   |  FRA   |  FRA   |  GER   |  GER   |
   |        |        |        |        |
   +--------+--------+--------+--------+
   |  FRA   |  FRA   |  GER   |  GER   |
   |        |        |        |        |
   +--------+--------+--------+--------+
   |  FRA   |  FRA   |  GER   |  GER   |
   |        |        |        |        |
   +--------+--------+--------+--------+                                  '''.format(france_population, stability))

        if Input == str("2"):
            Menu_on = 2
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| NEXT PLAYER 
|_____________________|_______________|
____________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ GOVERNMENT (5) \\
|___________|_______________|_______________|_______________|________________|

   +---------------------------------------------------------+
   |                      DIVISIONS MENU                     |
   +---------------------------------------------------------+
   | Viewable Divisions                                      |
   |                                                         |
   | 1. Division 1                6. Division 6              |
   | 2. Division 2                7. Division 7              |
   | 3. Division 3                8. Division 8              |
   | 4. Division 4                9. Division 9              |
   | 5. Division 5                0. Division 10             |
   |                                                         |
   |  Add a division with '0'. Delete a division with '9'.   |
   +---------------------------------------------------------+            '''.format(france_population, stability))

        if Input == str("3"):
            Menu_on = 3
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| NEXT PLAYER 
|_____________________|_______________|
____________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ GOVERNMENT (5) \\
|___________|_______________|_______________|_______________|________________|

   +---------------------------------------------------------+
   |                    EQUIPMENT MENU                       |
   +---------------------------------------------------------+
   | Infantry Equipment: 500 units                           |
   | Artillery: 200 units                                    |
   | Support Equipment: 300 units                            |
   | Light Tanks: 100 units                                  |
   | Medium Tanks: 50 units                                  |
   | Heavy Tanks: 20 units                                   |
   | Fighters: 150 units                                     |
   | Anti-Air: 100 units                                     |
   |                                                         |
   +---------------------------------------------------------+            '''.format(france_population, stability))
            
        if Input == str("4"):
            Menu_on = 4
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| NEXT PLAYER 
|_____________________|_______________|
____________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ GOVERNMENT (5) \\
|___________|_______________|_______________|_______________|________________|

   +---------------------------------------------------------+
   |                       FACTORIES                         |
   +---------------------------------------------------------+
   | CIVILIAN FACTORIES: {}                                  |
   | MILITARY FACTORIES: {}                                  |
   |                                                         |
   | MILITARY PRODUCTION: {}%                                |
   |                                                         |
   | CURRENT FACTORY/IES BEING PRODUCED: {} (CIV/MIL)        |
   | RATE OF FACTORIES BEING MADE: {}                        |                       
   | FACTORY OUTPUT MENU (0)                                 |
   |                                                         |
   +---------------------------------------------------------+            '''.format(france_population, stability))
   if Input = str"0":
       Turn = Turn - 1 
            
        if Input == str("5")
            Menu_on = 5
            Input = input(f'''
_____________________________________
| {userCountry} ({userCountry.population})  |STABILITY {userCountry.stability}% \          >| NEXT PLAYER 
|_____________________|_______________|
____________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ GOVERNMENT (5) \\
|___________|_______________|_______________|_______________|________________|

   +---------------------------------------------------------+
   |                       GOVERNMENT                        |
   +---------------------------------------------------------+
   | SHOW NATIONAL SPIRIT FOR COUNTRY HERE                   |
   |                                                         |
   | DECISION TO REMOVE:                                      |
   | COST OF REMOVING:                                       |
   |                                                         |
   | OTHER DECISIONS:                                        |
   |                                                         |
   | MOBILIZATION LAW:  (< = O, > = P)                       |                       
   | WOMEN IN THE WORKFORCE                                  |
   | WAR ECONOMY                                             |
   | INFRASTRUCTURE                                          |
   | SAFE WORKPLACE                                          |
   +---------------------------------------------------------+            '''.format(france_population, stability))

        if Input == str("0") and Menu_on = 4:
            Menu_on = 6
            Input = input('''
_____________________________
| {userCountry} ({userCountry.population})  |STABILITY {userCountry.stability}% \          >| NEXT PLAYER 
|_____________________|_______________|
____________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ GOVERNMENT (5) \\
|___________|_______________|_______________|_______________|________________|

   +---------------------------------------------------------+
   |                     FACTORY OUTPUT                      |
   +----------------------------+----------------------------+
   | INFANTRY EQUIPMENT         |  0/16 Factories            |  
   | ARTILLERY EQUIPMENT        |  0/16 Factories            |
   | SUPPORT EQUIPMENT          |  0/16 Factories            |
   | ANTIAIR EQUIPMENT          |  0/16 Factories            |             
   | FIGHTER PLANES             |  0/16 Factories            |                     
   |                            |                            |
   | LIGHT TANKS                |  0/16 Factories            |
   | MEDIUM TANKS               |  0/16 Factories            |
   | HEAVY TANKS                |  0/16 Factories            |                       
   +---------------------------------------------------------+            '''.format(france_population, stability))
           
        if Input == str("0") and Menu_on = 2:
            Menu_on = 7
            Input = input('''
_____________________________________
| {userCountry} ({userCountry.population})  |STABILITY {userCountry.stability}% \          >| NEXT PLAYER 
|_____________________|_______________|
____________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ GOVERNMENT (5) \\
|___________|_______________|_______________|_______________|________________|

   +---------------------------------------------------------+
   |                       NEW DIVISION                      |
   +----------------------------+----------------------------+
   | LIGHT INFANTRY DIVISION    | CREATE: (LI)               |  
   | MEDIUM INFANTRY DIVISION   | CREATE: (MI)               | 
   | HEAVY INFANTRY DIVISION    | CREATE: (HI)               | 
   |                            |                            |       
   | LIGHT TANK DIVISION        | CREATE: (LT)               |                   
   | MEDIUM TANK DIVISION       | CREATE: (MT)               | 
   | HEAVY TANK DIVISION        | CREATE: (HT)               | 
   |                            |                            |                         
   +----------------------------+----------------------------+
   | DEPLOY IN CERTAIN REGION, USE (DV).(POSITION) e.g LI.A4 |                   
   +---------------------------------------------------------+            '''.format(france_population, stability))
