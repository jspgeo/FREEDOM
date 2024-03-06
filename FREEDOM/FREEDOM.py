
france_population = 7500000  
stability = 59 

#For All
import random
Hearts = True
Defence = 50
SoftAttack = 0
HardAttack = 0
Health = 0
Playing = True
Occupation = 5

#**DIVISIONS**

#INFANTRY DIVISION TYPE: (1,2,3)
#1: LIGHT INFANTRY DIVISION (5000MP, 10SUP, 0ART, 500INFA)
#2: MEDIUM INFANTRY DIVISION (6000MP, 30SUP, 50ART, 840INFA)
#3: HEAVY INFANTRY DIVISION (12000MP, 70SUP, 100ART, 2000INFA)

#INFANTRY DIVISIONS COUNT: (NUM)
#ANTIAIR IN DIVISIONS (TRUE/FALSE) #10% LESS ATTACK, 30 IN EACH DIV

#TANK DIVISION TYPE: (1,2,3)
#1: LIGHT TANK DIVISION (10000MP, 100SUP, 100ART, 300LTE)
#2: MEDIUM TANK DIVISION (10000MP, 200SUP, 200ART, 300MTE)
#3: HEAVY TANK DIVISION (10000MP, 700SUP, 400ART, 300HTE)

#TANK DIVISIONS COUNT: (NUM)
#ANTIAIR IN DIVISIONS (TRUE/FALSE) #10% LESS ATTACK, 500 IN EACH DIV

#**EQUIPMENT**

#MANPOWER MAXIMUM FOR COUNTRY (NUM)
#MANPOWER AVAILABLE (NUM) (CONSCRIPTION LAW TIMES MANPOWER MAXIMUM TIMES STABLITY AS A PERCENTAGE)
#SUPPORT EQUIPMENT (NUM)
#ARTILLERY EQUIPMENT (NUM)
#INFANTRY EQUIPMENT (NUM)
#LIGHT TANK EQUIPMENT (NUM)
#MEDIUM TANK EQUIPMENT (NUM)
#HEAVY TANK EQUIPMENT (NUM)
#FIGHTERS EQUIPMENT (NUM)
#ANTIAIR EQUIPMENT (NUM)
#PORT GUARDS (TRUE/FALSE)

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

"FRA" = ["manpower_max": 45.000.000,
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
        "antiair": False]
        
"GER" = ["manpower_max": 80.000.000,
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
        "antiair": False]
        
"SOV" = ["manpower_max": 170.000.000,
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
        "antiair": False]
        
"ENG" = ["manpower_max": 50.000.000,
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
        "antiair": True]

"USA" = ["manpower_max": 150.000.000,
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
        "antiair": True]
        
"ITA" = ["manpower_max": 50.000.000,
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
        "antiair": False]
        
"JAP" = ["manpower_max": 70.000.000,
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
        "antiair": False]
        
"CHI" = ["manpower_max": 270.000.000,
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
        "antiair": 0]
        
#MINORS

"POL" = ["manpower_max": 35.000.000,
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
        "antiair": False]
        
"IND" = ["manpower_max": 377.000.000,
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
        "antiair": False]
        
"MEX" = ["manpower_max": 20.000.000,
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
        "antiair": False]
        
"BRA" = ["manpower_max": 40.000.000,
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
        "antiair": False]

"SWI" = ["manpower_max": 5.000.000,
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
        "antiair": True]
        
"SPA" = ["manpower_max": 25.000.000,
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
        "antiair": False]

# def Fight(Country1, Country2):

# Fight = Input("r```







Game = True
Gamestart = True
Keepgoing = True
Input = str("1")
while Game == True:
    while Keepgoing == True:
        if Gamestart == True:
            Input = str(1)
        Gamestart = False
        print(r'''
            
            
            
            
            
            
            
            
            `
            
            
            
            
            
            
            
            
            
        ''')
        if Input == str("1"):
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| SKIP TO NEXT DAY
|_____________________|_______________|
___________________________________________________________________________
| MAP (1)  \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ DECISIONS (5) \
|___________|_______________|_______________|_______________|_______________|

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

        if str(Input) == str("2"):
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| SKIP TO NEXT DAY
|_____________________|_______________|
___________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ DECISIONS (5) \
|___________|_______________|_______________|_______________|_______________|

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
   | 0. Add New Division                                     |
   +---------------------------------------------------------+            '''.format(france_population, stability))

        if str(Input) == str("3"):
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| SKIP TO NEXT DAY
|_____________________|_______________|
___________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ DECISIONS (5) \
|___________|_______________|_______________|_______________|_______________|

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
            
        if str(Input) == str("4"):
            Input = input('''
_____________________________________
| FRANCE ({:,})  |STABILITY {}% \          >| SKIP TO NEXT DAY
|_____________________|_______________|
___________________________________________________________________________
| MAPS (1) \ DIVISIONS (2) \ EQUIPMENT (3) \ FACTORIES (4) \ DECISIONS (5) \
|___________|_______________|_______________|_______________|_______________|

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
   | CHANGE FACTORY PRODUCTION LINE (0)                      |
   |                                                         |
   | Anti-Air: 100 units                                     |
   |                                                         |
   +---------------------------------------------------------+            '''.format(france_population, stability))


