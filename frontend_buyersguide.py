# Final Project - Ski finder web scraping quiz 
# Owein LaBarr and Colin Hodge
# CS021
# Project Description: This program will consist of a few questions for the user
# involving their gender, skill level, ski type, and desired profile of
# their prefered ski. The program will then use evo.com to generate a list of
# recommended skis available on the evo website.

#------------------------------------------
#ski_quiz_frontend.py built by Owein LaBarr
#------------------------------------------

#***Disclaimer: With the 4 questions/parameters we used, there are some combinations of answers in the ski quiz that do not return any skis because there are none on evo.com with those specifications***

# Dictinary of skis scpraped and formatted in the backend.
ski_dict = {'Male': {'Beginner-Intermediate': {
    'All Mountain': {
        'Camber': [('Volkl Bash 81 Skis 2021',
                   'https://www.evo.com/skis/volkl-bash-81'),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [('K2 Mindbender 85 Skis 2021',
                                 'https://www.evo.com/skis/k2-mindbender-85'
                                 ),(' ',' '),(' ',' '),(' ',' ')],
        },
    'Park & Pipe': {
        'Camber': [('Volkl Bash 81 Skis 2021',
                   'https://www.evo.com/skis/volkl-bash-81'),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        },
    'Powder': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        },
    'Alpine Touring': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        },
    }, 'Intermediate-Advanced': {
    'All Mountain': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [
            ('Line Skis Sakana Skis 2021',
             'https://www.evo.com/skis/line-sakana'),
            ('Armada Invictus 95 Skis',
             'https://www.evo.com/outlet/skis/armada-invictus-95'),
            ('Lib Tech Wreckreate 102 Skis 2021',
             'https://www.evo.com/skis/lib-tech-wreckreate-102'),
            ('Black Crows Vertis Skis 2021',
             'https://www.evo.com/skis/black-crows-vertis'),
            ('Lib Tech Wreckreate 92 Skis 2021',
             'https://www.evo.com/skis/lib-tech-wreckreate-92'),
            ('Atomic Backland 95 Skis 2021',
             'https://www.evo.com/skis/atomic-backland-95'),
            ('Atomic Vantage 86 C Skis 2021',
             'https://www.evo.com/skis/atomic-vantage-86-c-2021'),
            ('Lib Tech Wreckreate 84 Skis',
             'https://www.evo.com/outlet/skis/lib-tech-wreckreate-84'),
            ('DPS Cassiar F82 C2 Skis',
             'https://www.evo.com/outlet/skis/dps-cassiar-82-foundation'
             ),
            ('DPS Cassiar F87 C2 Skis',
             'https://www.evo.com/outlet/skis/dps-cassiar-87-foundation'
             ),
            ],
        'Rocker/Camber/Rocker': [
            ('Faction Candide 2.0 Skis 2021',
             'https://www.evo.com/skis/faction-candide-20'),
            ('Black Crows Atris Skis 2021',
             'https://www.evo.com/skis/black-crows-atris'),
            ('K2 Reckoner 102 Skis 2021',
             'https://www.evo.com/skis/k2-reckoner-102'),
            ('Black Crows Camox Skis 2021',
             'https://www.evo.com/skis/black-crows-camox'),
            ('Faction Prodigy 2.0 Skis 2021',
             'https://www.evo.com/skis/faction-prodigy-20'),
            ('Atomic Bent Chetler 100 Skis 2021',
             'https://www.evo.com/skis/atomic-bent-chetler-100'),
            ('Blizzard Zero G 105 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-105'),
            ('Line Skis Sir Francis Bacon Skis 2021',
             'https://www.evo.com/skis/line-sir-francis-bacon'),
            ('Line Skis Vision 98 Skis 2021',
             'https://www.evo.com/skis/line-vision-98'),
            ('Black Crows Navis Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-navis-freebird'),
            ('Black Crows Camox Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-camox-freebird'),
            ('Salomon QST 106 Skis 2021',
             'https://www.evo.com/skis/salomon-qst-106'),
            ('Salomon QST 99 Skis 2021',
             'https://www.evo.com/skis/salomon-qst-99'),
            ('Rossignol Black Ops Sender Skis 2021',
             'https://www.evo.com/skis/rossignol-black-ops-sender'),
            ('K2 Press Skis 2021', 'https://www.evo.com/skis/k2-press'
             ),
            ('Rossignol Black Ops Holy Shred Skis 2021',
             'https://www.evo.com/skis/rossignol-black-ops-holy-shred'
             ),
            ('Faction Prodigy 2.0 Skis',
             'https://www.evo.com/outlet/skis/faction-prodigy'),
            ('Atomic Vantage 97 Ti Skis',
             'https://www.evo.com/outlet/skis/atomic-vantage-97-ti-2020'
             ),
            ('Black Crows Atris Skis',
             'https://www.evo.com/outlet/skis/black-crows-atris-2020'),
            ('Black Crows Camox Skis',
             'https://www.evo.com/outlet/skis/black-crows-camox-2020'),
            ('Rossignol Sky 7 HD Skis',
             'https://www.evo.com/outlet/skis/rossignol-sky-7-hd'),
            ('Rossignol Soul 7 HD Skis',
             'https://www.evo.com/outlet/skis/rossignol-soul-7-hd'),
            ('Volkl Kendo 88 Skis',
             'https://www.evo.com/outlet/skis/volkl-kendo-88-2020'),
            ('Salomon QST 92 Skis',
             'https://www.evo.com/outlet/skis/salomon-qst-92-2020'),
            ('Faction Prodigy 1.0 Skis',
             'https://www.evo.com/outlet/skis/faction-prodigy-10'),
            ('Head Kore 93 Skis 2021',
             'https://www.evo.com/skis/head-kore-93'),
            ('Volkl Kanjo Skis',
             'https://www.evo.com/outlet/skis/volkl-kanjo'),
            ('K2 Poacher Skis',
             'https://www.evo.com/outlet/skis/k2-poacher-2020'),
            ('Blizzard Rustler 10 Skis',
             'https://www.evo.com/outlet/skis/blizzard-rustler-10-2020'
             ),
            ('Black Crows Captis Skis 2021',
             'https://www.evo.com/skis/black-crows-captis'),
            ('Faction Prodigy 3.0 Skis',
             'https://www.evo.com/outlet/skis/faction-prodigy-30-2020'
             ),
            ('Line Skis Sick Day 94 Skis',
             'https://www.evo.com/outlet/skis/line-sick-day-94-2020'),
            ('Line Skis Vision 98 Skis',
             'https://www.evo.com/outlet/skis/line-vision-98-2020'),
            ('Faction Chapter 1.0 Skis',
             'https://www.evo.com/outlet/skis/faction-chapter-10'),
            ('Armada Tracer 98 Skis',
             'https://www.evo.com/outlet/skis/armada-tracer-98-2020'),
            ('Black Crows Camox Skis - Blem',
             'https://www.evo.com/outlet/skis/black-crows-camox-blem'),
            ('Blizzard Brahma 82 Skis',
             'https://www.evo.com/outlet/skis/blizzard-brahma-82-2020'
             ),
            ('Faction Chapter 2.0 Skis 2020',
             'https://www.evo.com/skis/faction-chapter'),
            ('RMU Rippah 98 Skis 2021',
             'https://www.evo.com/skis/rmu-rippah-98'),
            ('ON3P Jeffrey 102 Skis 2021',
             'https://www.evo.com/skis/on3p-jeffrey-102'),
            ],
        },
    'Park & Pipe': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [
            ('K2 Press Skis 2021', 'https://www.evo.com/skis/k2-press'
             ),
            ('Faction Prodigy 1.0 Skis',
             'https://www.evo.com/outlet/skis/faction-prodigy-10'),
            ('K2 Poacher Skis',
             'https://www.evo.com/outlet/skis/k2-poacher-2020'),
            ('RMU Rippah 98 Skis 2021',
             'https://www.evo.com/skis/rmu-rippah-98'),
            ('ON3P Magnus 90 Skis 2021',
             'https://www.evo.com/skis/on3p-magnus-90'),
            ('Volkl Revolt 95 Skis 2021',
             'https://www.evo.com/skis/volkl-revolt-95'),
            ('Volkl Bash 86 Skis 2021',
             'https://www.evo.com/skis/volkl-bash-86'),
            ('Armada ARV 86 Skis 2021',
             'https://www.evo.com/skis/armada-arv-86'),
            ('K2 Poacher Skis 2021',
             'https://www.evo.com/skis/k2-poacher'),
            ('ON3P Magnus 102 Skis 2021',
             'https://www.evo.com/skis/on3p-magnus-102'),
            ('Line Skis Honey Badger Skis 2021',
             'https://www.evo.com/skis/line-honey-badger'),
            ('Line Skis Chronic Skis',
             'https://www.evo.com/outlet/skis/line-chronic-2020'),
            ('Icelantic Nomad 95 Skis 2021',
             'https://www.evo.com/skis/icelantic-nomad-95'),
            ('Line Skis Chronic Skis 2021',
             'https://www.evo.com/skis/line-chronic'),
            ('Line Skis Blend Skis 2021',
             'https://www.evo.com/skis/line-blend'),
            ('Armada ARV 96 Skis 2021',
             'https://www.evo.com/skis/armada-arv-96'),
            ('ON3P Jeffrey 96 Skis 2021',
             'https://www.evo.com/skis/on3p-jeffrey-96'),
            ('Armada Bdog Skis 2021',
             'https://www.evo.com/skis/armada-bdog'),
            ('Lib Tech Backwards Skis 2021',
             'https://www.evo.com/skis/lib-tech-backwards'),
            ('Armada Bdog Edgeless Skis 2021',
             'https://www.evo.com/skis/armada-bdog-edgeless'),
            ('Atomic Punx 5 Skis 2021',
             'https://www.evo.com/skis/atomic-punx-5'),
            ('Lib Tech UFO 95 Skis',
             'https://www.evo.com/outlet/skis/lib-tech-ufo-95'),
            ('Atomic Punx Five Skis',
             'https://www.evo.com/outlet/skis/atomic-punx-five'),
            ('Lib Tech Backwards Skis',
             'https://www.evo.com/outlet/skis/lib-tech-backwards-2020'
             ),
            ('K2 Poacher Skis - Used',
             'https://www.evo.com/outlet/used/skis/k2-poacher-2020'),
            ],
        },
    'Powder': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [('DPS Lotus F124 Skis 2021',
                                 'https://www.evo.com/skis/dps-lotus-f124-foundation'
                                 ), ('DPS Wailer F112 RP Skis 2021',
                                 'https://www.evo.com/skis/dps-wailer-f112-rp'
                                 ), ('DPS Wailer A112 RP Skis 2021',
                                 'https://www.evo.com/skis/dps-wailer-a112-rp'
                                 ), ('Blizzard Spur Skis 2021',
                                 'https://www.evo.com/skis/blizzard-spur'
                                 )],
        },
    'Alpine Touring': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [('WNDR Alpine Intention 110 Reverse Camber Skis 2021'
                   ,
                   'https://www.evo.com/skis/wndr-alpine-intention-110-reverse-camber'
                   ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [('Atomic Backland 78 Skis',
                          'https://www.evo.com/outlet/skis/atomic-backland-78'
                          ), ('Atomic Backland 95 Skis 2021',
                          'https://www.evo.com/skis/atomic-backland-95'
                          ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [
            ('Blizzard Zero G 105 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-105'),
            ('Line Skis Vision 98 Skis 2021',
             'https://www.evo.com/skis/line-vision-98'),
            ('Black Crows Navis Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-navis-freebird'),
            ('Black Crows Camox Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-camox-freebird'),
            ('Salomon QST 106 Skis 2021',
             'https://www.evo.com/skis/salomon-qst-106'),
            ('Salomon QST 99 Skis 2021',
             'https://www.evo.com/skis/salomon-qst-99'),
            ('Faction Agent 2.0 Skis',
             'https://www.evo.com/outlet/skis/faction-agent'),
            ('Head Kore 93 Skis 2021',
             'https://www.evo.com/skis/head-kore-93'),
            ('Line Skis Vision 98 Skis',
             'https://www.evo.com/outlet/skis/line-vision-98-2020'),
            ('Armada Tracer 98 Skis',
             'https://www.evo.com/outlet/skis/armada-tracer-98-2020'),
            ('Atomic Vantage 97 C Skis',
             'https://www.evo.com/outlet/skis/atomic-vantage-97-c-2020'
             ),
            ('Atomic Backland 107 Skis 2021',
             'https://www.evo.com/skis/atomic-backland-107'),
            ('Armada Tracer 98 Skis 2021',
             'https://www.evo.com/skis/armada-tracer-98'),
            ('Volkl Blaze 94 Skis 2021',
             'https://www.evo.com/skis/volkl-blaze-94'),
            ('WNDR Alpine Intention 110 Camber Skis 2021',
             'https://www.evo.com/skis/wndr-alpine-intention-110-camber'
             ),
            ('Black Crows Orb Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-orb-freebird'),
            ('Atomic Vantage 97 C Skis 2021',
             'https://www.evo.com/skis/atomic-vantage-97-c'),
            ('Head Kore 87 Skis 2021',
             'https://www.evo.com/skis/head-kore-87'),
            ('Faction Prime 2.0 Skis 2021',
             'https://www.evo.com/skis/faction-prime-20-2021'),
            ('Salomon QST 99 Skis - Used',
             'https://www.evo.com/outlet/used/skis/salomon-qst-99'),
            ('G3 SEEKr 100 Skis',
             'https://www.evo.com/outlet/skis/g3-seekr-100-2019'),
            ],
        },
    }, 'Advanced-Expert': {
    'All Mountain': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [('Black Crows Daemon Skis',
                   'https://www.evo.com/outlet/skis/black-crows-daemon'
                   ), ('WNDR Alpine Vital 100 Reverse Camber Skis 2021'
                   ,
                   'https://www.evo.com/skis/wndr-alpine-vital-100-reverse-camber'
                   ), ('Moment Meridian Skis 2020',
                   'https://www.evo.com/skis/moment-meridian')],
        'Rocker/Camber': [
            ('Armada Edollo Skis 2021',
             'https://www.evo.com/skis/armada-edollo'),
            ('Black Crows Orb Skis 2021',
             'https://www.evo.com/skis/black-crows-orb'),
            ('Atomic Vantage 90 Ti Skis',
             'https://www.evo.com/outlet/skis/atomic-vantage-90-ti'),
            ('Armada Invictus 99 Ti Skis',
             'https://www.evo.com/outlet/skis/armada-invictus-99-ti'),
            ('Line Skis Sakana Skis',
             'https://www.evo.com/outlet/skis/line-sakana-2020'),
            ('Rossignol Experience 94 Ti Skis',
             'https://www.evo.com/outlet/skis/rossignol-experience-94-ti'
             ),
            ('Black Crows Solis Skis 2021',
             'https://www.evo.com/skis/black-crows-solis'),
            ('Rossignol Experience 88 Ti Skis 2021',
             'https://www.evo.com/skis/rossignol-experience-88-ti'),
            ('Armada Invictus 89 Ti Skis',
             'https://www.evo.com/outlet/skis/armada-invictus-89-ti'),
            ('Black Crows Divus Skis 2021',
             'https://www.evo.com/skis/black-crows-divus'),
            ('Liberty evolv100 Skis 2021',
             'https://www.evo.com/skis/liberty-evolv100'),
            ('Liberty evolv90 Skis 2021',
             'https://www.evo.com/skis/liberty-evolv90'),
            ('Rossignol Experience 94 Ti Skis - Used',
             'https://www.evo.com/outlet/used/skis/rossignol-experience-94-ti'
             ),
            ('Liberty evolv100 Skis',
             'https://www.evo.com/outlet/skis/liberty-evolv100-2020'),
            ],
        'Rocker/Camber/Rocker': [
            ('Season Nexus Skis 2021',
             'https://www.evo.com/skis/season-nexus'),
            ('Salomon Stance 96 Skis 2021',
             'https://www.evo.com/skis/salomon-stance-96'),
            ('Faction Candide 3.0 Skis 2021',
             'https://www.evo.com/skis/faction-candide-30'),
            ('K2 Mindbender 99Ti Skis 2021',
             'https://www.evo.com/skis/k2-mindbender-99ti'),
            ('Black Crows Justis Skis 2021',
             'https://www.evo.com/skis/black-crows-justis'),
            ('Nordica Enforcer 100 Skis 2021',
             'https://www.evo.com/skis/nordica-enforcer-100'),
            ('Nordica Enforcer 94 Skis 2021',
             'https://www.evo.com/skis/nordica-enforcer-94'),
            ('Volkl M5 Mantra Skis 2021',
             'https://www.evo.com/skis/volkl-m5-mantra'),
            ('Blizzard Zero G 95 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-95'),
            ('Black Crows Corvus Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-corvus-freebird'),
            ('K2 Mindbender 108Ti Skis 2021',
             'https://www.evo.com/skis/k2-mindbender-108ti'),
            ('K2 Reckoner 112 Skis 2021',
             'https://www.evo.com/skis/k2-reckoner-112'),
            ('Volkl Revolt 104 Skis 2021',
             'https://www.evo.com/skis/volkl-revolt-104'),
            ('Line Skis Vision 108 Skis 2021',
             'https://www.evo.com/skis/line-vision-108'),
            ('Faction Dictator 3.0 Skis',
             'https://www.evo.com/outlet/skis/faction-dictator-30-2020'
             ),
            ('Head Kore 99 Skis',
             'https://www.evo.com/outlet/skis/head-kore-99-2020'),
            ('Nordica Enforcer 100 Skis',
             'https://www.evo.com/outlet/skis/nordica-enforcer-100-2020'
             ),
            ('Volkl M5 Mantra Skis',
             'https://www.evo.com/outlet/skis/volkl-m5-mantra-2020'),
            ('Nordica Enforcer 93 Skis',
             'https://www.evo.com/outlet/skis/nordica-enforcer-93'),
            ('Blizzard Bonafide Skis',
             'https://www.evo.com/outlet/skis/blizzard-bonafide'),
            ('Salomon Stance 90 Skis 2021',
             'https://www.evo.com/skis/salomon-stance-90'),
            ('Nordica Enforcer Free 104 Skis 2021',
             'https://www.evo.com/skis/nordica-enforcer-free-104'),
            ('Faction Dictator 2.0 Skis',
             'https://www.evo.com/outlet/skis/faction-dictator'),
            ('Blizzard Cochise Skis',
             'https://www.evo.com/outlet/skis/blizzard-cochise'),
            ('Volkl Kendo 92 Skis',
             'https://www.evo.com/outlet/skis/volkl-kendo-92'),
            ('Line Skis Blade Skis 2021',
             'https://www.evo.com/skis/line-blade'),
            ('Volkl Mantra 102 Skis 2021',
             'https://www.evo.com/skis/volkl-mantra-102'),
            ('Blizzard Bonafide 97 Skis 2021',
             'https://www.evo.com/skis/blizzard-bonafide-97'),
            ('Salomon Stance 102 Skis 2021',
             'https://www.evo.com/skis/salomon-stance-102'),
            ('Dynastar M-Free 108 Skis 2021',
             'https://www.evo.com/skis/dynastar-m-free-108'),
            ('Rossignol Black Ops Sender Ti Skis 2021',
             'https://www.evo.com/skis/rossignol-black-ops-sender-ti'),
            ('K2 Mindbender 99Ti Skis',
             'https://www.evo.com/outlet/skis/k2-mindbender-99ti-2020'
             ),
            ('Dynastar M-Pro 99 Skis 2021',
             'https://www.evo.com/skis/dynastar-m-pro-99'),
            ('ON3P Woodsman 108 Skis 2021',
             'https://www.evo.com/skis/on3p-woodsman-108'),
            ('Head Kore 105 Skis 2021',
             'https://www.evo.com/skis/head-kore-105'),
            ('Volkl Blaze 106 Skis 2021',
             'https://www.evo.com/skis/volkl-blaze-106'),
            ('Icelantic Nomad Lite Skis 2021',
             'https://www.evo.com/skis/icelantic-nomad-lite'),
            ('ON3P Jeffrey 108 Skis 2021',
             'https://www.evo.com/skis/on3p-jeffrey-108'),
            ('Armada Declivity 102 Ti Skis 2021',
             'https://www.evo.com/skis/armada-declivity-102-ti'),
            ('Moment Wildcat Tour 108 Skis 2021',
             'https://www.evo.com/skis/moment-wildcat-tour-108'),
            ],
        },
    'Park & Pipe': {
        'Camber': [('Volkl Revolt 87 Skis 2021',
                   'https://www.evo.com/skis/volkl-revolt-87'),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [('Armada Edollo Skis 2021',
                          'https://www.evo.com/skis/armada-edollo'),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [('Volkl Revolt 104 Skis 2021',
                                 'https://www.evo.com/skis/volkl-revolt-104'
                                 ),
                                 ('Line Skis Tom Wallisch Pro Skis 2021'
                                 ,
                                 'https://www.evo.com/skis/line-tom-wallisch-pro'
                                 ), ('K2 Sight Skis 2021',
                                 'https://www.evo.com/skis/k2-sight'),
                                 ('Atomic Punx 7 Skis',
                                 'https://www.evo.com/outlet/skis/atomic-punx-7'
                                 )],
        },
    'Powder': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [('Volkl V-Werks Katana Skis',
                   'https://www.evo.com/outlet/skis/volkl-v-werks-katana'
                   ), ('Black Crows Nocta Skis 2021',
                   'https://www.evo.com/skis/black-crows-nocta'),
                   ('Icelantic Saba 117 Skis 2021',
                   'https://www.evo.com/skis/icelantic-saba-117'),
                   ('Black Crows Nocta Skis',
                   'https://www.evo.com/outlet/skis/black-crows-nocta-2020'
                   ), ('Dynafit Beast 108 Skis - Used',
                   'https://www.evo.com/outlet/used/skis/dynafit-beast-108'
                   )],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [
            ('Season Forma Skis 2021',
             'https://www.evo.com/skis/season-forma'),
            ('Black Crows Anima Skis 2021',
             'https://www.evo.com/skis/black-crows-anima'),
            ('Atomic Bent Chetler 120 Skis 2021',
             'https://www.evo.com/skis/atomic-bent-chetler-120'),
            ('Armada Whitewalker Skis 2021',
             'https://www.evo.com/skis/armada-whitewalker'),
            ('Volkl Revolt 121 Skis 2021',
             'https://www.evo.com/skis/volkl-revolt-121'),
            ('Line Skis Outline Skis',
             'https://www.evo.com/outlet/skis/line-outline-2020'),
            ('K2 Mindbender 116 C Skis',
             'https://www.evo.com/outlet/skis/k2-mindbender-116-c-2020'
             ),
            ('Armada ARV 116 JJ Skis 2021',
             'https://www.evo.com/skis/armada-arv-116-jj'),
            ('Nordica Enforcer 110 Free Skis 2021',
             'https://www.evo.com/skis/nordica-enforcer-110-free'),
            ('Black Crows Ferox Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-ferox-freebird'),
            ('Dynastar M-Free 108 Skis 2021',
             'https://www.evo.com/skis/dynastar-m-free-108'),
            ('Faction Prodigy 4.0 Skis',
             'https://www.evo.com/outlet/skis/faction-prodigy-40'),
            ('Line Skis Outline Skis 2021',
             'https://www.evo.com/skis/line-outline'),
            ('Armada ARV 116 JJ UL Skis 2021',
             'https://www.evo.com/skis/armada-arv-116-jj-ul'),
            ('Armada Tracer 118 Skis 2021',
             'https://www.evo.com/skis/armada-tracer-118'),
            ('Rossignol Black Ops Gamer Skis 2021',
             'https://www.evo.com/skis/rossignol-black-ops-gamer'),
            ('Moment Wildcat Skis 2021',
             'https://www.evo.com/skis/moment-wildcat'),
            ('Dynastar M-Free 118 Skis 2021',
             'https://www.evo.com/skis/dynastar-m-free-118'),
            ('Armada Magic J Skis 2021',
             'https://www.evo.com/skis/armada-magic-j'),
            ('DPS Koala 119 Foundation Skis 2021',
             'https://www.evo.com/skis/dps-koala-119-foundation'),
            ('Blizzard Bodacious Skis 2021',
             'https://www.evo.com/skis/blizzard-bodacious'),
            ('K2 Reckoner 122 Skis 2021',
             'https://www.evo.com/skis/k2-reckoner-122'),
            ('Faction Prime 4.0 Skis 2021',
             'https://www.evo.com/skis/faction-prime-40'),
            ('Blizzard Rustler 11 Skis',
             'https://www.evo.com/outlet/skis/blizzard-rustler-11-2020'
             ),
            ('Moment Wildcat Tour Skis 2021',
             'https://www.evo.com/skis/moment-wildcat-tour'),
            ('DPS Pagoda Tour 112 RP Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-112-rp'),
            ('Line Skis Vision 118 Skis 2021',
             'https://www.evo.com/skis/line-vision-118'),
            ('K2 Mindbender 116 C Skis 2021',
             'https://www.evo.com/skis/k2-mindbender-116-c'),
            ('Line Skis Pescado Skis 2021',
             'https://www.evo.com/skis/line-pescado'),
            ('RMU YLE 110 Skis 2021',
             'https://www.evo.com/skis/rmu-yle-110'),
            ('Folsom Skis Powfish Skis 2021',
             'https://www.evo.com/skis/folsom-powfish'),
            ('Blizzard Rustler 11 Skis 2021',
             'https://www.evo.com/skis/blizzard-rustler-11'),
            ('RMU YLE 110 BM Skis 2021',
             'https://www.evo.com/skis/rmu-yle-110-bm'),
            ('G3 SEEKr 110 Skis 2021',
             'https://www.evo.com/skis/g3-seekr-110'),
            ('Icelantic Nomad 115 Skis 2021',
             'https://www.evo.com/skis/icelantic-nomad-115'),
            ('Moment Deathwish Skis 2021',
             'https://www.evo.com/skis/moment-deathwish'),
            ('Salomon QST 118 Skis 2021',
             'https://www.evo.com/skis/salomon-qst-118'),
            ('Black Crows Ferox Freebird Skis - Used',
             'https://www.evo.com/outlet/used/skis/black-crows-ferox-freebird'
             ),
            ('Nordica Enforcer 110 Free Skis',
             'https://www.evo.com/outlet/skis/nordica-enforcer-110-free-2020'
             ),
            ('DPS Wailer A110 C2 Skis 2021',
             'https://www.evo.com/skis/dps-wailer-a110-c2'),
            ],
        },
    'Alpine Touring': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [('Volkl V-Werks Katana Skis',
                   'https://www.evo.com/outlet/skis/volkl-v-werks-katana'
                   ), ('WNDR Alpine Vital 100 Reverse Camber Skis 2021'
                   ,
                   'https://www.evo.com/skis/wndr-alpine-vital-100-reverse-camber'
                   ), ('Dynafit Beast 108 Skis - Used',
                   'https://www.evo.com/outlet/used/skis/dynafit-beast-108'
                   )],
        'Rocker/Camber': [('Black Crows Solis Skis 2021',
                          'https://www.evo.com/skis/black-crows-solis'
                          ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [
            ('Blizzard Zero G 95 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-95'),
            ('Black Crows Corvus Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-corvus-freebird'),
            ('Line Skis Vision 108 Skis 2021',
             'https://www.evo.com/skis/line-vision-108'),
            ('Head Kore 99 Skis',
             'https://www.evo.com/outlet/skis/head-kore-99-2020'),
            ('Armada Tracer 108 Skis',
             'https://www.evo.com/outlet/skis/armada-tracer-108-2020'),
            ('Black Crows Ferox Freebird Skis 2021',
             'https://www.evo.com/skis/black-crows-ferox-freebird'),
            ('Atomic Backland 100 Skis 2021',
             'https://www.evo.com/skis/atomic-backland-100'),
            ('Armada ARV 116 JJ UL Skis 2021',
             'https://www.evo.com/skis/armada-arv-116-jj-ul'),
            ('Head Kore 105 Skis 2021',
             'https://www.evo.com/skis/head-kore-105'),
            ('Armada Tracer 118 Skis 2021',
             'https://www.evo.com/skis/armada-tracer-118'),
            ('Volkl Blaze 106 Skis 2021',
             'https://www.evo.com/skis/volkl-blaze-106'),
            ('Icelantic Nomad Lite Skis 2021',
             'https://www.evo.com/skis/icelantic-nomad-lite'),
            ('Moment Wildcat Tour 108 Skis 2021',
             'https://www.evo.com/skis/moment-wildcat-tour-108'),
            ('Armada Tracer 108 Skis 2021',
             'https://www.evo.com/skis/armada-tracer-108'),
            ('Blizzard Zero G 85 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-85'),
            ('WNDR Alpine Vital 100 Camber Skis 2021',
             'https://www.evo.com/skis/wndr-alpine-vital-100-camber'),
            ('Blizzard Zero G 95 Skis 2021',
             'https://www.evo.com/outlet/skis/blizzard-zero-g-95'),
            ('Moment Wildcat Tour Skis 2021',
             'https://www.evo.com/skis/moment-wildcat-tour'),
            ('DPS Pagoda Tour 112 RP Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-112-rp'),
            ('DPS Pagoda Tour 106 C2 Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-106-c2'),
            ('Line Skis Vision 118 Skis 2021',
             'https://www.evo.com/skis/line-vision-118'),
            ('Moment Deathwish Tour Skis 2021',
             'https://www.evo.com/skis/moment-deathwish-tour'),
            ('DPS Pagoda Tour 100 RP Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-100-rp'),
            ('G3 SEEKr 110 Skis 2021',
             'https://www.evo.com/skis/g3-seekr-110'),
            ('Dynastar M-Tour 99 Skis 2021',
             'https://www.evo.com/skis/dynastar-m-tour-99'),
            ('Black Diamond Helio Recon 105 Burkard Skis 2021',
             'https://www.evo.com/skis/black-diamond-helio-recon-105-burkard'
             ),
            ('Head Kore 99 Skis 2021',
             'https://www.evo.com/skis/head-kore-99'),
            ('Black Crows Ferox Freebird Skis - Used',
             'https://www.evo.com/outlet/used/skis/black-crows-ferox-freebird'
             ),
            ('Volkl Mantra V-Werks Skis 2021',
             'https://www.evo.com/skis/volkl-mantra-v-werks'),
            ('Armada Tracer 118 CHX Skis',
             'https://www.evo.com/outlet/skis/armada-tracer-118-chx'),
            ('Black Diamond Helio Carbon 104 Skis 2021',
             'https://www.evo.com/skis/black-diamond-helio-carbon-104'
             ),
            ('Black Diamond Helio Carbon 95 Skis 2021',
             'https://www.evo.com/skis/black-diamond-helio-carbon-95'),
            ('Black Diamond Helio Carbon 88 Skis 2021',
             'https://www.evo.com/skis/black-diamond-helio-carbon-88'),
            ('Faction Agent 3.0 Skis 2021',
             'https://www.evo.com/skis/faction-agent-30'),
            ('Faction Agent 2.0 Skis 2021',
             'https://www.evo.com/skis/faction-agent-20'),
            ('Black Diamond Helio Recon 105 Skis 2021',
             'https://www.evo.com/skis/black-diamond-helio-recon-105'),
            ('Black Diamond Helio Recon 95 Skis 2021',
             'https://www.evo.com/skis/black-diamond-helio-recon-95'),
            ('Faction Prime 2.0 Skis - Used',
             'https://www.evo.com/outlet/used/skis/faction-prime-20'),
            ('Black Diamond Helio 105 Skis - Used',
             'https://www.evo.com/outlet/used/skis/black-diamond-helio-105'
             ),
            ('Head Kore 99 Skis - Used',
             'https://www.evo.com/outlet/used/skis/head-kore-99-2020'),
            ],
        },
    }}, 'Female': {'Beginner-Intermediate': {
    'All Mountain': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [("Atomic Vantage 86 C W Skis - Women's",
                          'https://www.evo.com/outlet/skis/atomic-vantage-86-c-w-womens'
                          ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [("K2 Mindbender 85 Alliance Skis - Women's 2021"
                                 ,
                                 'https://www.evo.com/skis/k2-mindbender-85-alliance-womens'
                                 ),
                                 ("Blizzard Black Pearl 78 Skis - Women's 2021"
                                 ,
                                 'https://www.evo.com/skis/blizzard-black-pearl-78-womens'
                                 ),
                                 ("Blizzard Black Pearl 78 Skis - Women's"
                                 ,
                                 'https://www.evo.com/outlet/skis/blizzard-black-pearl-78-womens-2020'
                                 )],
        },
    'Park & Pipe': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        },
    'Powder': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        },
    'Alpine Touring': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        },
    }, 'Intermediate-Advanced': {
    'All Mountain': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [("Dynafit Beast 98 W Skis - Women's - Used",
                   'https://www.evo.com/outlet/used/skis/dynafit-beast-98-w-womens'
                   ), ("Dynafit Beast 98 W Skis - Women's",
                   'https://www.evo.com/outlet/skis/dynafit-beast-98-w-womens'
                   ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [
            ("Armada Victa 83 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-victa-83-womens'),
            ("Black Crows Vertis Birdie Skis - Women's 2021",
             'https://www.evo.com/skis/black-crows-vertis-birdie-womens'
             ),
            ("Armada Victa 93 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-victa-93-womens'),
            ("Armada Trace 88 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-trace-88-womens'),
            ("Volkl Kama Skis - Women's",
             'https://www.evo.com/outlet/skis/volkl-kama-womens'),
            ("Armada Victa 83 Skis - Women's",
             'https://www.evo.com/outlet/skis/armada-victa-83-womens-2020'
             ),
            ("Armada Trace 88 Skis - Women's",
             'https://www.evo.com/outlet/skis/armada-trace-88-womens-2019'
             ),
            ("DPS Uschi A82 C2 Skis - Women's",
             'https://www.evo.com/outlet/skis/dps-uschi-82-alchemist-womens'
             ),
            ("DPS Uschi A87 C2 Skis - Women's",
             'https://www.evo.com/outlet/skis/dps-uschi-87-alchemist-womens'
             ),
            ("Head Total Joy Skis - Women's",
             'https://www.evo.com/outlet/skis/head-total-joy-womens'),
            ],
        'Rocker/Camber/Rocker': [
            ("Line Skis Pandora 84 Skis - Women's 2021",
             'https://www.evo.com/skis/line-pandora-84-womens'),
            ("Black Crows Atris Birdie Skis - Women's 2021",
             'https://www.evo.com/skis/black-crows-atris-birdie-womens'
             ),
            ('Blizzard Zero G 105 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-105'),
            ("Salomon QST Lumen 99 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-qst-lumen-99-womens'),
            ("Blizzard Black Pearl 88 Skis - Women's 2021",
             'https://www.evo.com/skis/blizzard-black-pearl-88-womens'
             ),
            ("Line Skis Pandora 104 Skis - Women's 2021",
             'https://www.evo.com/skis/line-pandora-104-womens'),
            ("K2 Mindbender 90C Alliance Skis - Women's 2021",
             'https://www.evo.com/skis/k2-mindbender-90c-alliance-womens'
             ),
            ("Black Crows Camox Birdie Skis - Women's 2021",
             'https://www.evo.com/skis/black-crows-camox-birdie-womens'
             ),
            ("Salomon QST Lux 92 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-qst-lux-92-womens'),
            ("Faction Prodigy 2.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-prodigy-20x-womens'),
            ("Blizzard Black Pearl 82 Skis - Women's 2021",
             'https://www.evo.com/skis/blizzard-black-pearl-82-womens'
             ),
            ("Faction Candide 2.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-candide-20x-womens'),
            ("Atomic Vantage 97 C W Skis - Women's",
             'https://www.evo.com/outlet/skis/atomic-vantage-97-c-w-womens-2020'
             ),
            ("Blizzard Black Pearl 88 Skis - Women's",
             'https://www.evo.com/outlet/skis/blizzard-black-pearl-88-womens-2020'
             ),
            ("Rossignol Black Ops Stargazer Skis - Women's 2021",
             'https://www.evo.com/skis/rossignol-black-ops-stargazer-womens'
             ),
            ("Rossignol Black Ops Rallybird Skis - Women's 2021",
             'https://www.evo.com/skis/rossignol-black-ops-rallybird-womens'
             ),
            ("Black Crows Captis Birdie Skis - Women's 2021",
             'https://www.evo.com/skis/black-crows-captis-birdie-womens'
             ),
            ("Blizzard Black Pearl 97 Skis - Women's 2021",
             'https://www.evo.com/skis/blizzard-black-pearl-97-womens'
             ),
            ("Blizzard Sheeva 9 Skis - Women's 2021",
             'https://www.evo.com/skis/blizzard-sheeva-9-womens'),
            ("Volkl Kenja 88 Skis - Women's 2020 - Used",
             'https://www.evo.com/used/skis/volkl-kenja-88-womens-2020'
             ),
            ("Volkl Kenja 88 Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-kenja-88-womens'),
            ("K2 Empress Skis - Women's 2021",
             'https://www.evo.com/skis/k2-empress-womens'),
            ("Volkl Bash 86 W Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-bash-86-w-womens'),
            ("Volkl Blaze 94 W Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-blaze-94-w-womens'),
            ("Volkl Yumi 84 Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-yumi-84-womens'),
            ("Head Kore 93 W Skis - Women's 2021",
             'https://www.evo.com/skis/head-kore-93-w-womens'),
            ('Fischer Ranger 94 FR Skis 2021',
             'https://www.evo.com/skis/fischer-ranger-94-fr'),
            ("Rossignol Black Ops Blazer Skis - Women's 2021",
             'https://www.evo.com/skis/rossignol-black-ops-blazer-womens'
             ),
            ("Line Skis Pandora 94 Skis - Women's 2021",
             'https://www.evo.com/skis/line-pandora-94-womens'),
            ("Elan Ripstick 94 Skis - Women's 2021",
             'https://www.evo.com/skis/elan-ripstick-94-womens'),
            ("Folsom Skis Catwalk Skis - Women's 2021",
             'https://www.evo.com/skis/folsom-catwalk-womens'),
            ("Folsom Skis Cash 106 Skis - Women's 2021",
             'https://www.evo.com/skis/folsom-cash-106-womens'),
            ("Icelantic Maiden 91 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-maiden-91-womens'),
            ('DPS Pagoda Piste 100 C2 Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-piste-100-c2'),
            ("Salomon QST Myriad 85 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-qst-myriad-85-womens'),
            ("RMU Valhalla 97 Skis - Women's 2021",
             'https://www.evo.com/skis/rmu-valhalla-97-womens'),
            ("DPS Yvette F100 RP Skis - Women's 2021",
             'https://www.evo.com/skis/dps-yvette-f100-rp-womens'),
            ("Moment Sierra Skis - Women's 2021",
             'https://www.evo.com/skis/moment-sierra-womens'),
            ("Black Crows Camox Birdie Skis - Women's",
             'https://www.evo.com/outlet/skis/black-crows-camox-birdie-womens-2020'
             ),
            ("Nordica Santa Ana 88 Skis - Women's 2021",
             'https://www.evo.com/skis/nordica-santa-ana-88-womens'),
            ],
        },
    'Park & Pipe': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [
            ("Line Skis Honey Bee Skis - Women's 2021",
             'https://www.evo.com/skis/line-honey-bee-womens'),
            ("K2 Empress Skis - Women's 2021",
             'https://www.evo.com/skis/k2-empress-womens'),
            ("Volkl Bash 86 W Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-bash-86-w-womens'),
            ("Icelantic Maiden 91 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-maiden-91-womens'),
            ("Armada ARW 86 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-arw-86-womens'),
            ("Faction Prodigy 1.0X Skis - Women's",
             'https://www.evo.com/outlet/skis/faction-prodigy-10x-womens-2020'
             ),
            ("Faction Prodigy 1.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-prodigy-10x-womens'),
            ("Armada ARW 96 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-arw-96-womens'),
            ("Armada ARW 86 Skis - Women's",
             'https://www.evo.com/outlet/skis/armada-arw-86-womens-2020'
             ),
            ("Line Skis Honey Bee Skis - Women's",
             'https://www.evo.com/outlet/skis/line-honey-bee-womens-2020'
             ),
            ],
        },
    'Powder': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [("Coalition Snow Rafiki Skis - Women's 2021"
                                 ,
                                 'https://www.evo.com/skis/coalition-snow-rafiki-womens'
                                 ),
                                 ("DPS Yvette F112 RP Skis - Women's 2021"
                                 ,
                                 'https://www.evo.com/skis/dps-yvette-f112-rp-womens'
                                 ),
                                 ("DPS Yvette A112 RP Skis - Women's 2021"
                                 ,
                                 'https://www.evo.com/skis/dps-yvette-a112-rp-womens'
                                 ), ('Blizzard Spur Skis 2021',
                                 'https://www.evo.com/skis/blizzard-spur'
                                 ),
                                 ("Coalition Snow La Nieve Skis - Women's 2021"
                                 ,
                                 'https://www.evo.com/skis/coalition-snow-la-nieve-womens'
                                 )],
        },
    'Alpine Touring': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [('WNDR Alpine Intention 110 Reverse Camber Skis 2021'
                   ,
                   'https://www.evo.com/skis/wndr-alpine-intention-110-reverse-camber'
                   ), ("Dynafit Beast 98 W Skis - Women's - Used",
                   'https://www.evo.com/outlet/used/skis/dynafit-beast-98-w-womens'
                   ), ("Dynafit Beast 98 W Skis - Women's",
                   'https://www.evo.com/outlet/skis/dynafit-beast-98-w-womens'
                   )],
        'Rocker/Camber': [("Armada Trace 88 Skis - Women's 2021",
                          'https://www.evo.com/skis/armada-trace-88-womens'
                          ), ("Armada Trace 88 Skis - Women's",
                          'https://www.evo.com/outlet/skis/armada-trace-88-womens-2019'
                          ), ("DPS Uschi A82 C2 Skis - Women's",
                          'https://www.evo.com/outlet/skis/dps-uschi-82-alchemist-womens'
                          ), ("DPS Uschi A87 C2 Skis - Women's",
                          'https://www.evo.com/outlet/skis/dps-uschi-87-alchemist-womens'
                          )],
        'Rocker/Camber/Rocker': [
            ('Blizzard Zero G 105 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-105'),
            ("Salomon QST Lumen 99 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-qst-lumen-99-womens'),
            ("Volkl Blaze 94 W Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-blaze-94-w-womens'),
            ("Head Kore 93 W Skis - Women's 2021",
             'https://www.evo.com/skis/head-kore-93-w-womens'),
            ('WNDR Alpine Intention 110 Camber Skis 2021',
             'https://www.evo.com/skis/wndr-alpine-intention-110-camber'
             ),
            ("Armada Trace 98 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-trace-98-womens'),
            ("Faction Agent 2.0X Skis - Women's",
             'https://www.evo.com/outlet/skis/faction-agentx-womens'),
            ("Coalition Snow La Nieve Skis - Women's 2021",
             'https://www.evo.com/skis/coalition-snow-la-nieve-womens'
             ),
            ("Head Kore 87 W Skis - Women's 2021",
             'https://www.evo.com/skis/head-kore-87-w-womens'),
            ("Atomic Vantage 97 C W Skis - Women's 2021",
             'https://www.evo.com/skis/atomic-vantage-97-c-w-womens'),
            ("Salomon QST Lumen 99 Skis - Women's - Used",
             'https://www.evo.com/outlet/used/skis/salomon-qst-lumen-99-womens'
             ),
            ],
        },
    }, 'Advanced-Expert': {
    'All Mountain': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [('WNDR Alpine Vital 100 Reverse Camber Skis 2021',
                   'https://www.evo.com/skis/wndr-alpine-vital-100-reverse-camber'
                   ), ("Black Crows Daemon Birdie Skis - Women's",
                   'https://www.evo.com/outlet/skis/black-crows-daemon-birdie-womens'
                   ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [
            ("Black Crows Orb Birdie Skis - Women's 2021",
             'https://www.evo.com/skis/black-crows-orb-birdie-womens'),
            ("Rossignol Experience 88 Ti Skis - Women's 2021",
             'https://www.evo.com/skis/rossignol-experience-88-ti-womens'
             ),
            ("Liberty evolv90w Skis - Women's 2021",
             'https://www.evo.com/skis/liberty-evolv90w-womens'),
            ("Liberty evolv84w Skis - Women's 2021",
             'https://www.evo.com/skis/liberty-evolv84w-womens'),
            ("Atomic Vantage 90 Ti W Skis - Women's",
             'https://www.evo.com/outlet/skis/atomic-vantage-90-ti-w-womens'
             ),
            ("Atomic Vantage 90 Ti W Skis - Women's - Used",
             'https://www.evo.com/outlet/used/skis/atomic-vantage-90-ti-w-womens'
             ),
            ],
        'Rocker/Camber/Rocker': [
            ('Season Nexus Skis 2021',
             'https://www.evo.com/skis/season-nexus'),
            ('Blizzard Zero G 95 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-95'),
            ("Volkl Secret 92 Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-secret-92-womens'),
            ("Head Kore 99 W Skis - Women's",
             'https://www.evo.com/outlet/skis/head-kore-99-w-womens-2020'
             ),
            ("Volkl Secret 92 Skis - Women's",
             'https://www.evo.com/outlet/skis/volkl-secret-92-womens-2020'
             ),
            ("Blizzard Sheeva 10 Skis - Women's 2021",
             'https://www.evo.com/skis/blizzard-sheeva-10-womens'),
            ("Dynastar M-Pro 99 W Skis - Women's 2021",
             'https://www.evo.com/skis/dynastar-m-pro-99-w-womens'),
            ("Rossignol Black Ops Rallybird Ti Skis - Women's 2021",
             'https://www.evo.com/skis/rossignol-black-ops-rallybird-ti-womens'
             ),
            ("Volkl Blaze 106 W Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-blaze-106-w-womens'),
            ("Salomon Stance W 88 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-stance-w-88-womens'),
            ("Faction Dictator 2.0X Skis - Women's",
             'https://www.evo.com/outlet/skis/faction-dictatorx-womens'
             ),
            ("Icelantic Maiden Lite Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-maiden-lite-womens'),
            ('Fischer Ranger FR 102 Skis 2021',
             'https://www.evo.com/skis/fischer-ranger-fr-102'),
            ("Coalition Snow SOS Skis - Women's 2021",
             'https://www.evo.com/skis/coalition-snow-sos-womens'),
            ('WNDR Alpine Vital 100 Camber Skis 2021',
             'https://www.evo.com/skis/wndr-alpine-vital-100-camber'),
            ("K2 Mindbender 88Ti Alliance Skis - Women's 2021",
             'https://www.evo.com/skis/k2-mindbender-88ti-alliance-womens'
             ),
            ("K2 Missconduct Skis - Women's 2021",
             'https://www.evo.com/skis/k2-missconduct-womens'),
            ("Nordica Santa Ana 104 Free Skis - Women's 2021",
             'https://www.evo.com/skis/nordica-santa-ana-104-free-womens'
             ),
            ("Line Skis Blade W Skis - Women's 2021",
             'https://www.evo.com/skis/line-blade-w-womens'),
            ("Salomon Stance W 94 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-stance-w-94-womens'),
            ("Dynastar M-Pro 90 W Skis - Women's 2021",
             'https://www.evo.com/skis/dynastar-m-pro-90-w-womens'),
            ("Fischer Ranger 99 Ti Skis - Women's 2021",
             'https://www.evo.com/skis/fischer-ranger-99-ti-womens'),
            ('DPS Pagoda Tour 106 C2 Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-106-c2'),
            ("Icelantic Mystic 97 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-mystic-97-womens'),
            ("Faction Dictator 2.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-dictator-20x-womens'),
            ("Liberty Genesis 106 Skis - Women's 2021",
             'https://www.evo.com/skis/liberty-genesis-106-womens'),
            ("Faction Prodigy 3.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-prodigy-30x-womens'),
            ("Nordica Santa Ana 98 Skis - Women's 2021",
             'https://www.evo.com/skis/nordica-santa-ana-98-womens'),
            ("Moment Hot Mess Skis - Women's 2021",
             'https://www.evo.com/skis/moment-hot-mess-womens'),
            ("Icelantic Maiden 101 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-maiden-101-womens'),
            ("Faction Agent 2.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-agent-20x-womens'),
            ("K2 Mindbender 98Ti Alliance Skis - Women's 2021",
             'https://www.evo.com/skis/k2-mindbender-98ti-alliance-womens'
             ),
            ("Nordica Santa Ana 93 Skis - Women's 2021",
             'https://www.evo.com/skis/nordica-santa-ana-93-womens'),
            ("Head Kore 99 W Skis - Women's 2021",
             'https://www.evo.com/skis/head-kore-99-w-womens'),
            ('DPS Pagoda Piste 94 C2 Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-piste-94-c2'),
            ('DPS Pagoda Tour 100 RP Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-100-rp'),
            ("Volkl Secret 102 Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-secret-102-womens'),
            ("Moment Bella 108 Skis - Women's 2021",
             'https://www.evo.com/skis/moment-bella-108-womens'),
            ("Faction Dictator 3.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-dictator-30x-womens'),
            ("Elan Ripstick 102 Skis - Women's 2021",
             'https://www.evo.com/skis/elan-ripstick-102-womens'),
            ],
        },
    'Park & Pipe': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [("K2 Missconduct Skis - Women's 2021",
                                 'https://www.evo.com/skis/k2-missconduct-womens'
                                 ),
                                 ("Rossignol Black Ops 98W Skis - Women's"
                                 ,
                                 'https://www.evo.com/outlet/skis/rossignol-black-ops-98w-womens'
                                 ),(' ',' '),(' ',' '),(' ',' ')],
        },
    'Powder': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [("Icelantic Nia 105 Skis - Women's 2021",
                   'https://www.evo.com/skis/icelantic-nia-105-womens'
                   ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [
            ('Season Forma Skis 2021',
             'https://www.evo.com/skis/season-forma'),
            ("Rossignol Soul 7 HD W Skis - Women's",
             'https://www.evo.com/outlet/skis/rossignol-soul-7-hd-w-womens'
             ),
            ('Armada ARV 116 JJ UL Skis 2021',
             'https://www.evo.com/skis/armada-arv-116-jj-ul'),
            ("Faction Candide 3.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-candide-30x-womens'),
            ("Line Skis Pandora 110 Skis - Women's 2021",
             'https://www.evo.com/skis/line-pandora-110-womens'),
            ("Black Crows Anima Birdie Skis - Women's 2021",
             'https://www.evo.com/skis/black-crows-anima-birdie-womens'
             ),
            ("Salomon QST Stella 106 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-qst-stella-106-womens'),
            ("Blizzard Sheeva 11 Skis - Women's 2021",
             'https://www.evo.com/skis/blizzard-sheeva-11-womens'),
            ('DPS Pagoda Tour 112 RP Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-112-rp'),
            ("Nordica Santa Ana 110 Free Skis - Women's 2021",
             'https://www.evo.com/skis/nordica-santa-ana-110-free-womens'
             ),
            ("K2 Mindbender 115 C Alliance Skis - Women's 2021",
             'https://www.evo.com/skis/k2-mindbender-115-c-alliance-womens'
             ),
            ("Icelantic Maiden 111 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-maiden-111-womens'),
            ("Icelantic Mystic 107 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-mystic-107-womens'),
            ("Faction Dictator 3.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-dictator-30x-womens'),
            ("Armada ARW 116 VJJ UL Skis - Women's 2021",
             'https://www.evo.com/skis/armada-arw-116-vjj-ul-womens'),
            ("Black Crows Atris Birdie Skis - Women's",
             'https://www.evo.com/outlet/skis/black-crows-atris-birdie-womens-2020'
             ),
            ("RMU Valhalla 107 Skis - Women's 2021",
             'https://www.evo.com/skis/rmu-valhalla-107-womens'),
            ('KYE Shapes Numinous Skis 2021',
             'https://www.evo.com/skis/kye-shapes-numinous'),
            ("Moment Bella 116 Skis - Women's 2021",
             'https://www.evo.com/skis/moment-bella-116-womens'),
            ("Armada Trace 108 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-trace-108-womens'),
            ("Black Crows Atris Birdie Skis - Women's - Used",
             'https://www.evo.com/outlet/used/skis/black-crows-atris-birdie-womens-2020'
             ),
            ("Armada Trace 108 Skis - Women's",
             'https://www.evo.com/outlet/skis/armada-trace-108-womens-2020'
             ),
            ],
        },
    'Alpine Touring': {
        'Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker': [('WNDR Alpine Vital 100 Reverse Camber Skis 2021',
                   'https://www.evo.com/skis/wndr-alpine-vital-100-reverse-camber'
                   ),(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber': [(' ',' '),(' ',' '),(' ',' ')],
        'Rocker/Camber/Rocker': [
            ('Blizzard Zero G 95 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-95'),
            ("Head Kore 99 W Skis - Women's",
             'https://www.evo.com/outlet/skis/head-kore-99-w-womens-2020'
             ),
            ("Atomic Backland 107 W Skis - Women's 2021",
             'https://www.evo.com/skis/atomic-backland-107-w-womens'),
            ('Armada ARV 116 JJ UL Skis 2021',
             'https://www.evo.com/skis/armada-arv-116-jj-ul'),
            ("Atomic Backland 98 W Skis - Women's 2021",
             'https://www.evo.com/skis/atomic-backland-98-w-womens'),
            ("Volkl Blaze 106 W Skis - Women's 2021",
             'https://www.evo.com/skis/volkl-blaze-106-w-womens'),
            ('Blizzard Zero G 85 Skis 2021',
             'https://www.evo.com/skis/blizzard-zero-g-85'),
            ("Salomon QST Stella 106 Skis - Women's 2021",
             'https://www.evo.com/skis/salomon-qst-stella-106-womens'),
            ("Icelantic Maiden Lite Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-maiden-lite-womens'),
            ('WNDR Alpine Vital 100 Camber Skis 2021',
             'https://www.evo.com/skis/wndr-alpine-vital-100-camber'),
            ('DPS Pagoda Tour 112 RP Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-112-rp'),
            ('DPS Pagoda Tour 106 C2 Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-106-c2'),
            ("Icelantic Mystic 97 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-mystic-97-womens'),
            ("Faction Agent 2.0X Skis - Women's 2021",
             'https://www.evo.com/skis/faction-agent-20x-womens'),
            ("Head Kore 99 W Skis - Women's 2021",
             'https://www.evo.com/skis/head-kore-99-w-womens'),
            ('DPS Pagoda Tour 100 RP Skis 2021',
             'https://www.evo.com/skis/dps-pagoda-tour-100-rp'),
            ("Icelantic Mystic 107 Skis - Women's 2021",
             'https://www.evo.com/skis/icelantic-mystic-107-womens'),
            ("Armada ARW 116 VJJ UL Skis - Women's 2021",
             'https://www.evo.com/skis/armada-arw-116-vjj-ul-womens'),
            ("Armada Trace 108 Skis - Women's 2021",
             'https://www.evo.com/skis/armada-trace-108-womens'),
            ('Blizzard Zero G 95 Skis 2021',
             'https://www.evo.com/outlet/skis/blizzard-zero-g-95'),
            ("Armada Trace 108 Skis - Women's",
             'https://www.evo.com/outlet/skis/armada-trace-108-womens-2020'
             ),
            ],
        },
    }}}



# Define main_menu()    
def main_menu():
    """Displays title block for main menu, then provides a list of options for the user to choose from. When the user has chosen the function directs them to the appropriate guide. """
    # Display title block
    print("*********************")
    print("HodgBarr Buyers Guide")
    print("*********************")
    print()
    print("Welcome! Please type the number associated with your desired guide.")

    # Enumerated list of options
    menu_list = ["Ski Finder", "Boot Sizing", "Ski Sizing"]
    for c, value in enumerate(menu_list, 1):
            print(c, value)
    choice = input(">>> ")

    
    # While loop to for user choice and exception handling
    while choice == '1' or choice == '2' or choice == '3':
        if choice == '1':
            ski_guide()
            valid_choice = True
        elif choice == '2':
            boot_guide_gender()
            valid_choice = True
        elif choice == '3':
            size_guide()
            valid_choice = True
    print("Invalid option, try again")
    
            
    main_menu()
    
# Defining ski_guide()
def ski_guide():
    """The main function contains a set of dictionaries created using the backend program. This program will be submitted and will scrape evo's website for relevent data.
        The main function will also ask the user"""


    # Running each question function and assigning variables to returned values
    gender = gender_answer()
    level = skill_level()
    s_type = ski_type()
    pro_file = profile()

    # Creating a list of ski names and links using above key words to retrieve information in ski_dict
    ski_list = ski_dict[gender][level][s_type][pro_file]

    # Printing enumerated list of the first 3 results in ski_list
    answer = 'not main'
    while answer != 'main':
        print()
        print("Top 3 Recommended Skis for You!")
        print("-------------------------------")
        
        print("1. ",ski_list[0][0]," - ", ski_list[0][1])
        print("2. ",ski_list[1][0]," - ", ski_list[1][1])
        print("3. ",ski_list[2][0]," - ", ski_list[2][1])
        print()
        print("***If nothing appears, there are no skis on evo.com that match those specifications.***")
        print()
        print("When you would like to return to the main menu, type 'main'.")
        answer = input(">>> ")

    
        
    # Running main_menu again if user types 'main'
    main_menu()



def gender_answer():    
    """The first question is to ask the user if they are looking for mens or womens skis"""

    # Setting up boolean to ensure correct answer
    valid_gender = False
    
    # Print title block and ask question 
    print("------")
    print("Gender")
    print("------")
    print("Are you looking for Men's or Women's skis?")

    # While loop for exception handling and if statements to return matching key words in dictionary 
    while valid_gender == False:
        print("Please type 'M' for Men's or 'W' for Women's.")
        gender = input(">>> ")
        gender = gender.upper()
        if gender == "M":
            gender = 'Male'
            valid_gender = True
        elif gender == "W":
            gender = 'Women'
            valid_gender = True
        else:
            print("Please enter 'M' or 'W'")
            
    return gender

# Defining ski_level function
def skill_level():
    """Ask the user what experience level they beleive themselves to be"""
    print()
    
    # Printing enumerated list of skill levels
    skill_list = ["Beginner-Intermediate", "Intermediat-Advanced", "Advanced-Expert"]
    print("-----------")
    print("Skill Level")
    print("-----------")
    for c, value in enumerate(skill_list, 1):
            print(c, value)
    print()
    print("Out of the list above, what skill level do you see yourself in? Be Honest!")

    valid_level = False
    # While loop for exception handling and if statements to return matching key words in dictionary
    while valid_level == False:
        print("Please type the number associated with your ski level.")
        level = input(">>> ")
        if level == "1":
            level = 'Beginner-Intermediate'
            valid_level = True
        elif level == "2":
            level = 'Intermediate-Advanced'
            valid_level = True
        elif level == "3":
            level = 'Advanced-Expert'
            valid_level = True
        else:
            print("Invalid Selection, try again!")
    
    return level

# Defining ski_type() function
def ski_type():
    """Ask the user what ski type they prefer and returning the appropriate key word of selection"""

    print()
    print("---------")
    print("Ski Types")
    print("---------")

    # Printing enumerated list of ski types
    ski_type_list = ["All Mountain ", "Park/Pipe", "Powder", "Alpine Touring"]
    for c, value in enumerate(ski_type_list, 1):
            print(c, value)
    print()
    print("Above are a few of the most popular ski types.")

    valid_type = False
    # While loop for exception handling and if statements to return matching key words in dictionary
    while valid_type == False:
        print("Please type the number accociated with your desired ski type.")
        ski_type = input(">>> ")
        if ski_type == "1":
            ski_type = 'All Mountain'
            valid_type = True
        elif ski_type == "2":
            ski_type = 'Park & Pipe'
            valid_type = True
        elif ski_type == "3":
            ski_type = 'Powder'
            valid_type = True
        elif ski_type == "4":
            ski_type = 'Alpine Touring'
            valid_type = True
        else:
            print('Invalid selection, try again!')

    return ski_type

# Defining profile() function
"""Ask the user what profile they prefer and returning the appropriate key word of selection"""

# Print brief description of ski profile and the printing title block
def profile():
    print()
    print("A skis profile is very imprortant when considering your riding style/technique.")
    print("For a breif introduction on the the terms 'Camber', 'Rocker', and combination")
    print("of the two, visit this link to evo's buyers guide and find the section on profile")
    print("https://www.evo.com/guides/how-to-choose-skis-size-chart")
    print()
    print("------------")
    print("Ski Profiles")
    print("------------")
    print()

    # Printing enumerated list of ski profiles
    profile_list = ["Camber", "Rocker", "Rocker/Camber", "Rocker/Camber/Rocker"]
    for c, value in enumerate(profile_list, 1):
            print(c, value)
    print()
    valid_profile = False
    
    # While loop for exception handling and if statements to return matching key words in dictionary
    while valid_profile == False:
        print("From the list above, please select the number associated with the profile that best suits you.")
        profile = input(">>> ")
        if profile == '1':
            profile = 'Camber'
            valid_profile = True
        elif profile == '2':
            profile = 'Rocker'
            valid_profile = True
        elif profile == '3':
            profile = 'Rocker/Camber'
            valid_profile = True
        elif profile == '4':
            profile = 'Rocker/Camber/Rocker'
            valid_profile = True
        else:
            print("Invalid selection, try again!")
        
    return profile

# Defining boot_guide_gender() function
def boot_guide_gender():
    """This function asks the user if they would like to find their mens boot size or womens boot size and directs them to the specified boot_guide function"""

    print("Are you looking for Men's or Women's boot sizes? (M/W)")
    g = input(">>> ")

    while g == 'M' or g == 'W':
        try:
            if g == 'M':
                boot_guide_mens()
        
            elif g == 'W':
                boot_guide_womens()
        
        except:
            print("Invalid gender, please enter 'M' or 'W'")
            
    print("Invalid input, please try again!")
    boot_guide_gender()

    
# Defining boot_guide_mens function
def boot_guide_mens():
    """Prints title block and then takes in user shoe size and returns the comfort and performance fits"""
    print("------------------------------------")
    print("Wlecome to our Ski Boot Sizing Guide")
    print("------------------------------------")
    print()

    print("This program will return both comfort and performance fit sizes.")
    print("Typically the performance fit is a smaller boot size to decrease unwanted movement within the boot")
    
    
    
    # While loop with exception handling to determine the users boot size
    answer = 'y'
    while answer == 'y':
        try:
            print("Please enter your shoe size")
            shoe_size = float(input(">>> "))
        
            if shoe_size >=4 and shoe_size <= 14:
                boot_size = 18 + shoe_size
                print("Your Comfort Fit Boot Size is: ", boot_size)
                print("Your Performace Fit Boot Size is: ", boot_size - 1)
            else:
                print("Boot size must be between 4 and 14 in increments of 0.5.")
                
        except:
            print("Invalid answer, try again!")
            boot_guide_mens()
        answer = input("Would you like to calculate another boot size? (y/n)")

    print("Thanks for using our guide!")
    print()

    # Rerun main_menu() when user is done
    main_menu()
    
# Defining boot_guide_womens function
def boot_guide_womens():
    """Prints title block and then takes in user shoe size and returns the comfort and performance fits"""
    
    print("------------------------------------")
    print("Wlecome to our Ski Boot Sizing Guide")
    print("------------------------------------")
    print()

    print("This program will return both comfort and performance fit sizes.")
    print("Typically the performance fit is a smaller and less comfortable boot size to decrease unwanted movement within the boot.")
    
    
    
    # While loop with exception handling to determine the users boot size
    answer = 'y'
    while answer == 'y':
        try:
            print("Please enter your shoe size")
            shoe_size = float(input(">>> "))
            if shoe_size >=5 and shoe_size <= 12:
                boot_size = 17 + shoe_size
                print("Your Comfort Fit Boot Size is: ", boot_size)
                print("Your Performace Fit Boot Size is: ", boot_size - 1)
            else:
                print("Enter a shoe size between 5 and 12 in increments of 0.5")
        except:
            print("Invalid answer, try again!")
            boot_guide_womens()
        answer = input("Would you like to calculate another boot size? (y/n)")

    print("Thanks for using our guide!")
    print()

    # Rerun main_menu() when user is done
    main_menu()

# Defining size_guide() function
def size_guide():
    """Printing title block and providing the user with thier ski size range based on height input"""
    print("-------------------------------")
    print("Wlecome to our Ski Sizing Guide")
    print("-------------------------------")
    print()

    # While loop with exception handling to return the correst ski length based on height
    answer = 'y'
    while answer == 'y':
        try:
            print("Please enter your height in the format feet.inches (Please round to the nearest inch)")
            print("Example: 5.6 is 5ft 6in")
            h = input(">>> ")
            if h == '4.4' or h == '4.5' or h == '4.6':
                print("Your recomended ski size is 130-139cm")
            elif h == '4.8' or h == '4.9' or h == '4.10':
                print("Your recomended ski size is 140-149cm")
            elif h == '5.0' or h == '4.1' or h == '5.2':
                print("Your recomended ski size is 150-159cm")
            elif h == '5.4' or h == '5.5' or h == '5.6':
                print("Your recomended ski size is 160-169cm")
            elif h == '5.8' or h == '5.9' or h == '5.10':
                print("Your recomended ski size is 170-179cm")
            elif h == '6.0' or h == '6.1' or h == '6.2':
                print("Your recomended ski size is 180-189cm")
            elif h == '6.4' or h == '6.5' or h == '6.6':
                print("Your recomended ski size is >190cm")
            else:
                print("Invalid answer,try again!")
        except:
            print("Invalid answer, try again!")
            size_guide()
            
        answer = input("Would you like to calculate another ski size? (y/n)")
    print("Thanks for using our guide")
    print()

    # Rerun main_menu() when done
    main_menu()

    
              
# Running main_menu()
main_menu()
