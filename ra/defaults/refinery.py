# ===== REFINERY DEFAULT REGISTER SOURCE =====
# Self-contained: nothing in this file is shared with or imported by any other business unit.
# Used only to (re)create the built-in default workbook if it is missing. Day-to-day edits are made in the Excel workbook
# and uploaded through the app's Register admin page.
ID_PREFIX = "REF"
# Row format: Tag|C|Hazard|L|Controls|R|Responsible|PPE;PPE
# C: J = Job Related Hazard, L = Job Location Related Hazard, E = Equipment and Material Related Hazard

COMMON_TAGS = [
 ("Posture/Movement", ["Climbing","Walking","Kneeling","Bending","Reaching Overhead","Ascending Stairs/Ladders","Descending Stairs/Ladders","Crawling"]),
 ("Manual Handling", ["Lifting","Carrying","Pushing","Pulling","Manual Handling of Loads","Repetitive Motion","Shoveling","Digging","Sweeping","Scraping","Team Lifting"]),
 ("Tool/Equipment Use", ["Hand Tool Use","Power Tool Use","Hammering","Mechanical Maintenance/Repair","Machining (Workshop Lathe/Mill)","Hydro-Jetting / High Pressure Cleaning","Bolt Torqueing / Tensioning","Compressor Overhaul"]),
 ("Hot Work", ["Welding","Cutting (Oxy-Acetylene)","Grinding","Hot Work (General)","Drilling","Sawing","Chiseling","Cold Cutting"]),
 ("Height/Access", ["Working at Height","Ladder Use","Scaffold Use","Rope Access","Working on Elevated Platform","Working Near Unprotected Edge","Man-lift/Aerial Platform Use","Scaffold Erection / Dismantling","Roof Work / Fragile Surface"]),
 ("Confined/Restricted", ["Confined Space Entry","Crawling in Restricted Space","Working in Trench/Excavation","Working Below Grade"]),
 ("Machinery/Equipment", ["Operating Mobile Equipment","Operating Fixed Machinery","Machine Guarding Removal/Replacement","Lockout-Tagout Application","Equipment Isolation","Rigging/Slinging Loads","Crane Operation","Signaling/Banksman Duties","Vehicle Driving","Reversing Vehicle","Use of Chain Block","Use of Forklift","Use of Overhead Crane","Tandem Lift","Lubrication/Greasing","Traffic Control/Flagging"]),
 ("Electrical", ["Live Electrical Work","De-energized Electrical Work","Cable Pulling","Electrical Panel Access","Battery / UPS Room Work","Transformer Oil Handling","Cable Jointing / Termination"]),
 ("Chemical/Material", ["Handling Hazardous Chemicals","Handling Flammable Materials","Handling Corrosive Substances","Spray Painting","Dust-Generating Activity","Handling Compressed Gas Cylinders","Waste Handling/Disposal","Fuel/Oil Transfer"]),
 ("Environmental Exposure", ["Working in Extreme Heat","Working in Noisy Environment","Working in Dusty Environment","Working Near Moving Machinery","Working Alone/Isolated","Night Shift Work","Working Outdoors in Weather","Working Near Water","Wet Work/Slippery Surface"]),
 ("Fluid/Pressure Systems", ["Pressure Washing","Hydraulic System Work","Pneumatic System Work"]),
 ("Inspection/Monitoring", ["Visual Inspection","Gas Testing/Atmospheric Monitoring","Sampling","Equipment Testing","Calibration","Vibration Analysis","Thermographic Survey","Non-Destructive Testing (NDT)","Radiographic Testing","Nucleonic Gauge Work (Radioactive Source)","Instrument Loop Checking"]),
 ("General Site Work", ["Housekeeping/Cleaning","Fire Watch Duty","Insulation / Lagging Work","Painting / Surface Coating","Civil / Foundation Work","Stores / Warehouse Handling","Emergency Response / Drill","Permit Issue / Area Handover","Contractor Supervision","Barricading/Signage Setup","First Aid Response Standby"]),
 ("Laboratory Operations", ["Sample Preparation (Laboratory)","Chemical/Reagent Handling (Laboratory)"]),
]

COMMON_AH = """
Climbing|J|Loss of grip or footing while climbing causing fall|H|Maintain three points of contact at all times; carry nothing by hand while climbing (use hoist line or tool bag); inspect rungs and steps before ascent|M|Area Supervisor|Grip gloves;Safety boots;Hard hat
Walking|J|Slip, trip, or fall on plant walkways, gratings, and pipe racks|M|Keep walkways clear and well lit; immediate spill clean-up; designated walking routes only; no mobile phone use while walking|L|Area Supervisor|Safety boots
Kneeling|J|Knee injury from prolonged kneeling on hard or uneven surfaces|L|Knee pads or kneeling mats; rotate posture regularly|N|Area Supervisor|Knee pads
Bending|J|Back strain from repeated or sustained bending|M|Raise the work to waist height where possible; rotate tasks; avoid bend-and-twist combinations|L|Area Supervisor|Task-appropriate PPE
Reaching Overhead|J|Shoulder strain and loss of balance when reaching overhead|M|Use a platform or step to bring work to chest height; limit sustained overhead work; rotate personnel|L|Area Supervisor|Task-appropriate PPE
Ascending Stairs/Ladders|L|Slip or trip on stairs or fixed ladder|M|Three points of contact; keep stairways clear of tools and material; adequate lighting on all access routes; handrail use mandatory|L|Area Supervisor|Safety boots
Descending Stairs/Ladders|L|Missed footing when descending, often while carrying items|M|Face the ladder when descending; carry nothing by hand; use hoist line for tools and parts|L|Area Supervisor|Safety boots;Safety gloves (general)
Crawling|J|Abrasion and knee injury while crawling in plant spaces|M|Knee and elbow protection; clear the route of sharp debris; lighting provided|L|Area Supervisor|Knee pads;Coveralls
Lifting|J|Back injury from lifting loads incorrectly or beyond individual capacity|M|Assess the load before lifting; use mechanical aids above 25 kg; bend the knees and keep the load close; team lift for awkward items|L|Area Supervisor|Safety gloves (general);Safety boots
Carrying|J|Strain or trip while carrying loads over uneven ground or stairs|M|Plan the route and clear obstructions; limit carry distance; use trolleys where possible; keep vision unobstructed|L|Area Supervisor|Safety gloves (general);Safety boots
Pushing|J|Strain from pushing heavy trolleys or loads|M|Maintain trolley wheels; use powered aids for heavy loads; avoid slopes and thresholds|L|Area Supervisor|Safety gloves (general);Safety boots
Pulling|J|Shoulder and back strain from pulling loads|M|Push in preference to pulling; use mechanical aids; avoid pulling on slopes or over thresholds|L|Area Supervisor|Safety gloves (general);Safety boots
Manual Handling of Loads|J|Musculoskeletal injury from manual handling of heavy or awkward loads|H|Manual handling assessment for loads over 25 kg; mechanical lifting aids; team lift with a nominated lead; rotate personnel on repetitive handling|M|Area Supervisor|Safety gloves (general);Safety boots
Manual Handling of Loads|E|Crushed fingers or feet when setting down loads|M|Plan the set-down point; use dunnage to keep fingers clear; safety boots with toe protection|L|Area Supervisor|Safety boots;Safety gloves (general)
Repetitive Motion|J|Upper limb disorder from sustained repetitive work|M|Job rotation and scheduled micro-breaks; ergonomic tool selection; report early symptoms for assessment|L|Area Supervisor|Anti-vibration gloves
Shoveling|J|Back strain and blistering from sustained shovelling|M|Correct shovel size for material density; rotate personnel; bend knees and avoid twisting; mechanical clearing where volume is high|L|Area Supervisor|Safety gloves (general);Safety boots
Digging|J|Strain and struck-by from manual digging near buried services|M|Hand-dig only where services may be present; permit to excavate; rotate personnel; maintain safe spacing between diggers|L|Area Supervisor|Safety gloves (general);Safety boots;Hard hat
Sweeping|J|Airborne dust generation from dry sweeping|M|Damp sweeping or industrial vacuum; RPE where dust cannot be suppressed|L|Area Supervisor|Dust mask (P2);Safety glasses
Scraping|J|Hand injury and residue release when scraping hardened deposits|M|Use long-handled tools to keep hands clear; cut-resistant gloves; confirm deposit is not pyrophoric or toxic before scraping|L|Area Supervisor|Cut-resistant gloves;Safety glasses
Team Lifting|J|Uncoordinated team lift causing sudden load transfer|M|Nominate one person to call the lift; brief the team on route and set-down point; matched heights where practicable|L|Area Supervisor|Safety gloves (general);Safety boots
Hand Tool Use|J|Injury from defective, worn, or incorrect hand tools|M|Pre-use inspection and removal of defective tools from service; correct tool for the task; non-sparking tools where a flammable atmosphere may exist; tool lanyards at height|L|Area Supervisor|Safety gloves (general);Safety glasses
Power Tool Use|E|Electric shock or entanglement from portable power tools|H|110 V or RCD protected supply; inspect leads and casing before use; no loose clothing near rotating tools; guards in place; hot work permit where the tool can ignite a flammable atmosphere|M|Area Supervisor|Safety glasses;Safety gloves (general)
Power Tool Use|J|Hand-arm vibration syndrome from prolonged power tool use|H|Limit trigger time per shift; anti-vibration tools and gloves; rotate operators|M|Area Supervisor|Anti-vibration gloves
Hammering|J|Struck-by flying fragments or misdirected blow injuring hand|M|Inspect hammer face and handle security; safety glasses mandatory; keep the holding hand clear; non-sparking hammer in classified areas|L|Workshop Technician|Safety glasses;Safety gloves (general)
Mechanical Maintenance/Repair|E|Crush injury from heavy components shifting or falling during removal|H|Assess component weight and plan the lift; certified lifting gear and purpose-built stands; never work under an unsupported load; exclusion zone during removal|M|Mechanical Maintenance Lead|Hard hat;Safety boots;Safety gloves (general)
Mechanical Maintenance/Repair|J|Hand injury from pinch points, sharp edges, and tool slip|M|Cut-resistant gloves; deburr edges; correct tool for the task; keep hands out of the line of force|L|Maintenance Technician|Cut-resistant gloves;Safety glasses
Machining (Workshop Lathe/Mill)|E|Entanglement in rotating chuck, workpiece, or swarf|E|No gloves, loose clothing, or jewellery near rotating machinery; chuck guard and interlock in place; chuck key removed before start; stop machine before clearing swarf|M|Workshop Supervisor|Safety glasses;No gloves (rotating machinery)
Hydro-Jetting / High Pressure Cleaning|E|Water jet injection injury or hose whip from ultra-high-pressure jetting|E|Trained and certified jetting crew; dead-man control on the gun; hose whip restraints; exclusion zone barricaded; never point the lance at any person|M|Maintenance Supervisor|Jetting suit;Face shield;Waterproof gloves;Waterproof / rain boots
Bolt Torqueing / Tensioning|E|Hydraulic tool failure or bolt failure releasing stored energy|H|Inspect hoses and fittings; stay out of the line of fire; use calibrated equipment within rated pressure; reaction arm positioned before applying pressure|M|Mechanical Maintenance Lead|Safety glasses;Safety gloves (general)
Compressor Overhaul|E|Stored gas and residual oil pressure during compressor strip-down|H|Isolate, depressurise, purge, and verify zero pressure at all receivers and lines; allow cool-down; drain oil to a controlled container|M|Maintenance Technician|Safety glasses;Safety gloves (general);Ear plugs
Welding|J|Arc eye and skin burns from UV radiation|H|Correct shade welding helmet; welding screens to protect passers-by; full skin coverage for welder and helper|L|Welding Supervisor|Welding helmet (correct shade);Flame-resistant (FR) coveralls;Leather welding gloves
Welding|J|Inhalation of welding fume including manganese and hexavalent chromium from stainless or alloy steels|H|Local exhaust ventilation at the arc; RPE appropriate to consumable and base metal; never weld in an unventilated confined space without airline supply|M|Welding Supervisor|Welding fume respirator;Welding helmet (correct shade)
Welding|E|Electric shock from welding return path or damaged cables|H|Inspect cables, holders, and return clamp before use; return clamp connected directly to the workpiece; insulating mat in damp conditions|M|Welding Supervisor|Leather welding gloves;Insulated boots
Cutting (Oxy-Acetylene)|E|Flashback or cylinder fire from oxy-fuel equipment|E|Flashback arrestors at regulator and torch; leak test before use; cylinders upright and secured; no oil or grease near oxygen fittings|M|Welding Supervisor|Flame-resistant (FR) coveralls;Leather welding gloves;Chemical goggles
Cutting (Oxy-Acetylene)|J|Falling cut section striking personnel|H|Plan and support the cut so the piece falls in a controlled direction; tag lines on heavy sections; exclusion zone beneath cutting at height|M|Maintenance Supervisor|Hard hat;Safety boots
Grinding|J|Abrasive wheel burst causing high-energy fragment injury|H|Check wheel rating exceeds machine speed; guard fitted at all times; correct wheel for the material; run new wheel free before use|M|Workshop Supervisor|Face shield;Safety glasses;Safety gloves (general)
Grinding|J|Eye injury from flying sparks and abrasive particles|H|Face shield over safety glasses; screens to protect adjacent workers; never grind toward walkways or open process drains|L|Workshop Supervisor|Face shield;Safety glasses
Hot Work (General)|L|Ignition of hydrocarbon vapour, combustible residue, or packaging causing fire or explosion|E|Hot work permit with continuous gas test (0% LEL at the work point); drains and openings within 15 m sealed; combustibles removed or covered; trained fire watch during work and for 60 minutes after; extinguisher and fire hose at the work face|M|Fire Watch / Maintenance Supervisor|Flame-resistant (FR) coveralls;Multi-gas detector;Face shield
Hot Work (General)|J|Burns from hot slag, sparks, or heated workpiece|H|Full FR clothing with no exposed skin; leather gauntlets and spats; allow parts to cool or handle with tongs; spatter screens|M|Maintenance Supervisor|Flame-resistant (FR) coveralls;Leather welding gloves;Welding spats
Drilling|E|Drill bit snatch or workpiece rotation causing hand and wrist injury|M|Clamp or vice the workpiece; no gloves on rotating spindle machines; correct speed and feed for the material|L|Workshop Supervisor|Safety glasses;No gloves (rotating machinery)
Sawing|E|Contact with saw blade or kickback of the workpiece|H|Blade guard in place; push stick and clamps used; stand out of the kickback line|M|Workshop Supervisor|Safety glasses;Safety gloves (general)
Chiseling|J|Flying chips and mushroomed chisel head fragments|M|Dress mushroomed heads before use; safety glasses mandatory; screens where others are nearby|L|Workshop Technician|Safety glasses;Safety gloves (general)
Cold Cutting|J|Sharp edges and stored stress release during cold cutting of pipe or plate|M|De-stress and support the section before the final cut; confirm line is drained and gas-free; deburr all cut edges|L|Maintenance Technician|Cut-resistant gloves;Safety glasses
Working at Height|L|Fall from height to lower level causing serious injury or fatality|E|Guardrails or edge protection in place; full body harness with double lanyard and 100% tie-off to certified anchor; permit to work at height; pre-use inspection of fall arrest equipment|M|Area Supervisor|Full body harness;Double lanyard;Hard hat with chin strap;Safety boots
Working at Height|L|Dropped tools or materials striking persons below|H|Barricade and sign the drop zone; tool lanyards on all hand tools; toe boards on platforms; no loose items in pockets at height|L|Area Supervisor|Hard hat;Tool lanyards
Working at Height|J|Rescue delay after a fall leaving worker in suspension trauma|E|Documented rescue plan before work starts; rescue equipment staged at the work face; never work at height alone; suspension trauma straps fitted|M|HSE Officer|Full body harness;Suspension trauma relief straps
Ladder Use|L|Ladder slipping, sliding, or toppling during use|H|Secure ladder at top and bottom; 4:1 angle rule; level firm footing; second person to foot the ladder where tying off is not possible|M|Area Supervisor|Safety boots;Safety gloves (general)
Scaffold Use|E|Scaffold collapse from incorrect erection or overloading|E|Scaffold erected and tagged by competent scaffolder only; green tag verified before each use; posted load limits observed; never modify without re-inspection|M|Scaffold Supervisor|Hard hat;Full body harness
Rope Access|J|Rope failure, abrasion, or incorrect rigging during descent|E|IRATA/SPRAT certified technicians only; twin-rope system with independent backup; edge protection at rub points; pre-use rope inspection logged|M|Rope Access Supervisor|Full body harness;Hard hat with chin strap;Descent / backup device
Working on Elevated Platform|L|Platform structural failure or guardrail defect|H|Inspect platform and guardrails before access; report and tag out any defect; observe posted load rating|M|Area Supervisor|Hard hat;Safety boots
Working Near Unprotected Edge|L|Fall over unguarded edge or through floor opening|E|Install temporary guardrail or cover all openings; harness tie-off where edge protection is not feasible; barricade and sign the area|M|Area Supervisor|Full body harness;Hard hat
Man-lift/Aerial Platform Use|E|Aerial platform tip-over or uncontrolled movement|E|Trained and authorised operators only; ground conditions assessed and outriggers deployed; harness clipped to basket anchor; never exceed basket load or reach limits|M|Area Supervisor|Full body harness;Hard hat
Scaffold Erection / Dismantling|J|Fall during erection or dismantling of scaffold|E|Competent scaffolders only; 100% tie-off during erection and dismantling; advance guardrail system; exclusion zone below|M|Scaffold Supervisor|Full body harness;Hard hat with chin strap;Safety boots
Scaffold Erection / Dismantling|J|Dropped components striking persons below|E|Full exclusion zone below with hard barriers and spotter; never throw components down; gin wheel or hoist; tool lanyards|M|Scaffold Supervisor|Hard hat;Safety gloves (general)
Roof Work / Fragile Surface|L|Fall through fragile roof sheeting or rooflight|E|Presume all roof sheets are fragile; crawl boards and edge protection; harness with running line; permit to access roof|H|Area Supervisor|Full body harness;Crawl boards;Hard hat
Confined Space Entry|L|Oxygen deficiency or enrichment inside the space|E|Confined space entry permit; pre-entry and continuous atmospheric testing (O2 19.5-23.5%); forced ventilation maintained; entry stopped immediately on alarm|M|HSE Officer / Confined Space Attendant|Multi-gas detector;Full body harness;Retrieval line
Confined Space Entry|L|Toxic or flammable gas in the space (H2S, CO, hydrocarbons) from residues or leaking isolations|E|Positive isolation by blinding or disconnection (valves alone not accepted); gas-free certificate; continuous LEL, H2S, CO and O2 monitoring; exit on any alarm|M|HSE Officer|Multi-gas detector;SCBA;Airline / air-fed respirator
Confined Space Entry|J|Would-be rescuer becoming a second casualty|E|Trained standby attendant at the entry at all times with no other duties; documented rescue plan and equipment staged before entry; strict no-unplanned-entry rule; entry log maintained|M|HSE Officer / Confined Space Attendant|Rescue harness;Retrieval winch and davit;SCBA
Confined Space Entry|E|Unexpected energisation or material flow into the occupied space|E|Full LOTO on all drives and inlets; blank or blind all connected pipework; independent verification of isolation before entry|M|Maintenance Supervisor|Lock and tag kit
Crawling in Restricted Space|J|Entrapment or inability to self-extract from a restricted opening|H|Assess opening size and egress route before entry; attendant maintains voice or visual contact; no entry alone; retrieval line where geometry permits|M|HSE Officer / Confined Space Attendant|Full body harness;Knee pads;Helmet with lamp
Working in Trench/Excavation|L|Trench wall collapse burying personnel|E|Shoring, benching, or sloping per soil assessment for any excavation over 1.2 m; spoil kept at least 1 m from edge; daily inspection by competent person; safe ladder access|M|Excavation Supervisor|Hard hat;Hi-vis vest;Safety boots
Working in Trench/Excavation|E|Striking buried services or live pipelines during excavation|E|Service drawings and locator survey before breaking ground; hand-dig trial pits to confirm; permit to excavate; pipeline owner present where crossing hydrocarbon lines|M|Excavation Supervisor|Insulated tools;Hard hat;Safety gloves (general)
Working Below Grade|L|Accumulation of heavier-than-air gases (H2S, hydrocarbon vapour, CO2) in pits and trenches|H|Gas test before and during entry; mechanical ventilation; attendant at grade level|M|HSE Officer|Multi-gas detector
Operating Mobile Equipment|J|Collision with pedestrians or other vehicles in shared traffic areas|E|Traffic management plan with segregated routes; reversing aids and alarms functional; speed limits enforced; spark arrestors on vehicles entering process areas|M|Plant/Fleet Supervisor|Hi-vis vest;Hard hat
Operating Fixed Machinery|E|Contact with moving parts during operation|H|Guards and interlocks in place; trained operators only; emergency stop tested; never bypass a safety device|M|Area Supervisor|Close-fitting clothing;Safety glasses
Machine Guarding Removal/Replacement|E|Operating equipment with guards removed or defeated|E|Guards removed only under LOTO; never operate with an interlock bypassed; guard refit verified and signed off before return to service|M|Maintenance Supervisor|Safety gloves (general);Safety glasses
Lockout-Tagout Application|E|Unexpected start-up or energisation during maintenance causing crush or amputation|E|Apply LOTO to every energy source on the isolation list; personal lock on a multi-lock hasp; try-out test to confirm zero energy; independent verification by a second competent person|M|Maintenance Supervisor|Lock and tag kit
Lockout-Tagout Application|E|Stored energy release after isolation (gravity, spring, hydraulic, pneumatic, process pressure)|E|Block suspended parts; bleed and vent pressure and verify at gauge; discharge capacitors; release spring tension under control|M|Maintenance Supervisor|Safety gloves (general);Face shield;Blocks / chocks
Equipment Isolation|E|Process fluid or gas entering the work area from connected plant through passing valves|E|Positive isolation (spade, blind, or spool removal) per isolation certificate; double block and bleed where blinding is not possible; isolation tags at every point; isolation register kept|M|Permit Issuing Authority|Safety gloves (general);Chemical goggles
Rigging/Slinging Loads|E|Load drop from failed or incorrectly rated rigging|E|Certified slings and shackles with current inspection tags; lift plan for all non-routine lifts; competent rigger; never stand under a suspended load|M|Rigging Supervisor|Hard hat;Safety gloves (general);Safety boots
Crane Operation|E|Crane overturning or structural failure during lift|E|Certified operator and crane; ground bearing assessed and outrigger mats used; lift plan within the load chart; wind speed limits observed|M|Lifting Engineer|Hard hat;Hi-vis vest
Crane Operation|L|Crane contact with overhead lines, pipe racks, or live process equipment|E|Lift plan identifies all obstructions; exclusion distance from power lines; banksman for all lifts near live plant|M|Lifting Engineer|Hard hat;Hi-vis vest
Signaling/Banksman Duties|J|Banksman struck by load or vehicle while directing|H|Banksman stays in the operator's sight and out of the load path; agreed hand or radio signals; hi-vis clothing|M|Rigging Supervisor|Hi-vis vest;Hard hat;Two-way radio
Vehicle Driving|J|Road traffic collision on plant or public roads|H|Licensed and authorised drivers only; speed limits enforced; seatbelt at all times; journey management for night and long-distance trips|M|Plant/Fleet Supervisor|Seatbelt;Hi-vis vest
Reversing Vehicle|J|Pedestrian struck by reversing vehicle|E|Reversing alarm and camera functional; banksman for reversing in congested areas; pedestrians stay out of the reversing zone|M|Plant/Fleet Supervisor|Hi-vis vest
Use of Chain Block|E|Chain block failure or load slip|H|Certified chain block within SWL; inspect chain and hook latch; secure to a rated anchor point; never stand under the load|M|Rigging Supervisor|Hard hat;Safety gloves (general)
Use of Forklift|J|Forklift overturn or pedestrian strike|E|Trained and authorised operators; load within rated capacity; segregated pedestrian routes; seatbelt worn|M|Stores Supervisor|Seatbelt;Hi-vis vest
Use of Overhead Crane|E|Load drop or collision during overhead crane travel|E|Pre-use checks of limits and brakes; trained operator; clear travel path; never pass loads over people|M|Rigging Supervisor|Hard hat;Safety boots
Tandem Lift|E|Load transfer and overload of one crane during a tandem lift|E|Engineered lift plan approved by lifting engineer; each crane derated per plan; single lift supervisor with radio control|H|Lifting Engineer|Hard hat;Two-way radio
Lubrication/Greasing|E|Entanglement when greasing near rotating equipment|H|Use remote greasing points; isolate where points are inside guards; no loose clothing|M|Lubrication Technician|Close-fitting clothing;Oil-resistant gloves
Traffic Control/Flagging|J|Flagger struck by passing vehicles|H|Hi-vis clothing; position flagger in a protected location; advance warning signage; stop/go board|M|Area Supervisor|Hi-vis vest;Stop/go board
Live Electrical Work|E|Electrocution from contact with live conductors|E|Live work only under a specific written permit where isolation is genuinely not feasible; authorised person only; insulated tools rated for the voltage; insulated matting; second person trained in rescue present|H|Licensed Electrician / Electrical Supervisor|Arc-rated suit and hood;Insulated electrical gloves;Face shield;Insulated mat
Live Electrical Work|E|Arc flash causing severe burns, blast injury, and hearing damage|E|Arc flash study and labelling; arc-rated PPE to the calculated rating; arc flash boundary maintained; remote switching where available|H|Electrical Supervisor|Arc-rated suit and hood;Ear plugs
De-energized Electrical Work|E|Working on apparatus assumed dead but still energised|E|Prove-test-prove with an approved voltage tester; apply earths where required; lock and tag at the isolation point; permit to work by authorised person|M|Licensed Electrician|Insulated electrical gloves;Voltage tester;Arc-rated suit and hood
Cable Pulling|J|Musculoskeletal injury and hand laceration during cable pulling|M|Cable rollers, winch, and lubricant rather than manual force; coordinate the pull with clear signals|L|Electrical Supervisor|Cut-resistant gloves;Safety boots
Electrical Panel Access|E|Arc flash or shock on opening a live panel door|E|Isolate before opening where practicable; arc-rated PPE and approach boundaries where live access is unavoidable; no unqualified persons inside the electrical room|H|Electrical Supervisor|Arc-rated suit and hood;Insulated electrical gloves;Face shield
Battery / UPS Room Work|E|Hydrogen accumulation and explosion risk in battery rooms|E|Ventilation verified; hydrogen detection; no smoking, hot work, or sparking tools; insulated tools only|H|Electrical Supervisor|Face shield;Chemical-resistant gloves;Chemical apron
Transformer Oil Handling|E|Oil fire and spill from transformer oil handling|H|No hot work near oil-filled equipment; bunded handling and spill kit; fire protection in service|M|Electrical Supervisor|Chemical-resistant gloves;Chemical goggles;Flame-resistant (FR) coveralls
Cable Jointing / Termination|E|Induced voltage or back-feed on an apparently dead cable|E|Positive cable identification; prove dead at the point of work; earth both ends; permit to work|H|Licensed Electrician|Insulated electrical gloves;Arc-rated suit and hood;Voltage tester
Handling Hazardous Chemicals|E|Skin or eye burns from chemical contact|H|Review SDS before use; chemical-resistant gloves, goggles and apron; eyewash and safety shower within 10 seconds travel; decant with spill tray|M|Area Supervisor|Chemical goggles;Chemical-resistant gloves;Chemical apron
Handling Hazardous Chemicals|J|Inhalation of vapours or mists causing respiratory harm|H|Use in a ventilated area; RPE selected against the specific substance; exposure monitoring where limits apply|M|HSE Officer|Organic vapour respirator;Chemical goggles
Handling Flammable Materials|E|Fire or explosion from flammable liquid vapour ignition|E|Eliminate ignition sources in the hazardous zone; bond and earth during transfer; approved flammables storage; extinguisher at the point of use|M|HSE Officer|Anti-static coveralls;Safety gloves (general)
Handling Corrosive Substances|E|Severe chemical burn from acid or alkali splash|E|Closed transfer systems where possible; full face shield over goggles; chemical suit for bulk handling; emergency shower tested weekly|M|HSE Officer|Face shield;Chemical suit;Chemical-resistant gloves;Waterproof / rain boots
Spray Painting|J|Solvent vapour inhalation and fire risk during spraying|H|Ventilated booth or well-ventilated area; air-fed or organic vapour respirator; eliminate ignition sources; earth equipment|M|Workshop Supervisor|Airline / air-fed respirator;Coveralls;Chemical goggles
Dust-Generating Activity|J|Inhalation of dust (catalyst fines, insulation, product dust)|H|Wet methods or local extraction; RPE (P3 minimum) where dust remains; restrict access to dusty zones|M|HSE Officer|P3 respirator;Sealed dust goggles;Coveralls
Handling Compressed Gas Cylinders|E|Cylinder falling, valve shear, or uncontrolled release|H|Cylinders upright and chained; valve caps fitted during transport; trolley for movement; never lift by the valve|M|Stores Supervisor|Safety boots;Safety gloves (general)
Waste Handling/Disposal|E|Exposure to unknown or mixed waste streams, oily sludge, and sharps|M|Segregate waste at source with clear labelling; never hand-sort mixed waste; licensed disposal contractor|L|HSE Officer|Puncture-resistant gloves;Chemical goggles;Coveralls
Fuel/Oil Transfer|E|Static ignition during fuel transfer|E|Bond and earth before transfer; no plastic containers for fuel; transfer stopped during electrical storms|M|Utilities Operator|Anti-static coveralls;Safety gloves (general)
Fuel/Oil Transfer|L|Spill to ground or drainage causing environmental harm and slip hazard|H|Bunded transfer area and drip trays; spill kit at point of transfer; attended transfer; drain valves kept closed|M|Utilities Operator|Safety gloves (general);Safety boots
Working in Extreme Heat|J|Heat stress, heat exhaustion, or heat stroke|H|Work/rest cycles matched to WBGT; cool rest area and hydration; acclimatisation for new workers; buddy system; heavy work rescheduled to cooler hours|M|Area Supervisor|Cooling vest;Drinking water
Working in Extreme Heat|J|Contact burns from hot surfaces, steam lines, and radiant heat|H|Lag or shield hot surfaces within reach; allow cool-down before maintenance; heat-resistant PPE; exclusion zones around hot points|M|Area Supervisor|Heat-resistant gauntlets;Face shield;Flame-resistant (FR) coveralls
Working in Noisy Environment|J|Noise-induced hearing loss from sustained exposure above 85 dB(A)|H|Engineering controls first; mandatory hearing protection in marked zones; limit exposure time; audiometric surveillance|M|HSE Officer|Ear plugs
Working in Noisy Environment|J|Failure to hear alarms, vehicles, or verbal warnings due to noise|H|Visual alarms in high-noise areas; radio communication; level-dependent hearing protection where awareness is critical|M|Area Supervisor|Level-dependent hearing protection;Two-way radio
Working in Dusty Environment|J|Respiratory irritation from prolonged dust exposure|H|Dust suppression and extraction at source; RPE with face-fit testing; rotation out of high-dust zones|M|HSE Officer|P3 respirator;Sealed dust goggles
Working Near Moving Machinery|E|Entanglement in unguarded or inadequately guarded moving parts|E|Fixed and interlocked guards maintained; emergency stops tested; no loose clothing, jewellery, or long hair; never reach past a guard|M|Area Supervisor|Close-fitting clothing;Safety gloves (general)
Working Alone/Isolated|J|Delayed discovery of injury, gas exposure, or incapacitation when working alone|H|Lone worker check-in schedule; personal gas monitor with man-down alarm where available; no lone working for high-risk tasks|M|Area Supervisor|Two-way radio;Multi-gas detector
Night Shift Work|J|Reduced alertness and impaired hazard perception on night shift|H|Adequate task lighting; fatigue management and shift rotation; limit high-risk work at night; buddy checks|M|Shift Supervisor|Hi-vis clothing (reflective);Intrinsically safe torch
Working Outdoors in Weather|L|Exposure to sun, rain, wind, and lightning|M|Stop outdoor and elevated work during electrical storms; sun protection and shade; wet weather gear; monitor forecast|L|Area Supervisor|Weather-appropriate clothing;Sun protection
Working Near Water|L|Drowning after fall into water, basin, or open tank|H|Edge protection and barriers; life buoy and throw line at the water edge; buoyancy aid where fall risk remains; never work alone near open water|M|Area Supervisor|Buoyancy aid;Full body harness
Wet Work/Slippery Surface|L|Slip on wet, oily, or product-covered surfaces|H|Immediate spill clean-up and drainage maintenance; anti-slip matting; slip-resistant footwear; signage while wet|M|Area Supervisor|Slip-resistant safety boots
Pressure Washing|E|Injection injury or eye injury from pressure washer spray|H|Trained operators; inspect hoses; never point at people; face shield and waterproof PPE|M|Area Supervisor|Face shield;Waterproof gloves;Waterproof / rain boots
Hydraulic System Work|E|Hydraulic fluid injection or sudden movement on pressure release|E|Lower or block loads; bleed pressure and verify at gauge; never search for leaks by hand; inspect hoses|M|Maintenance Technician|Safety glasses;Oil-resistant gloves
Pneumatic System Work|E|Hose whip or component ejection on air release|H|Isolate and bleed air; whip-checks on couplings; never point air at the body|M|Maintenance Technician|Safety glasses;Ear plugs
Visual Inspection|L|Exposure to live process hazards during inspection rounds|M|Area permit and briefing; personal gas monitor; stay on designated walkways; report leaks without intervening|L|Area Supervisor|Multi-gas detector;Hard hat;Safety glasses
Gas Testing/Atmospheric Monitoring|J|Incorrect gas test result due to uncalibrated detector or wrong sampling point|E|Bump test before use and calibration in date; test at multiple heights and points; authorised gas testers only; record results on the permit|M|Permit Issuing Authority|Multi-gas detector
Sampling|J|Exposure to process fluid during sampling|H|Closed-loop sample points where available; stand upwind; sample containers rated for the service; second person for toxic or H2S service|M|Process Operator|Chemical goggles;Chemical-resistant gloves;Multi-gas detector
Equipment Testing|E|Unexpected energisation or pressurisation during testing|H|Test procedure and permit; barricade the test area; communicate before energising; only authorised testers|M|Maintenance Supervisor|Safety glasses;Insulated electrical gloves
Calibration|J|Exposure to process connection or live instrument circuit during calibration|M|Isolate and vent impulse lines; confirm instrument is out of service with control room; intrinsically safe test equipment in classified areas|L|Instrumentation Technician|Safety glasses;Safety gloves (general)
Vibration Analysis|E|Contact with rotating equipment while taking readings|M|Use designated measurement points outside guards; no loose clothing; keep hands clear of rotating parts|L|Reliability Technician|Close-fitting clothing;Ear plugs
Thermographic Survey|J|Burns or electrical exposure while surveying hot or live equipment|M|Maintain approach boundaries; survey through IR windows where fitted; never open panels without electrical permit|L|Reliability Technician|Safety glasses;Insulated electrical gloves
Non-Destructive Testing (NDT)|J|Exposure to couplants, dyes, and UV light during NDT|M|SDS review; ventilation for dye penetrant work; UV-blocking eyewear|L|NDT Technician|Nitrile gloves;Safety glasses
Radiographic Testing|E|Ionising radiation exposure during radiography|E|Licensed radiography contractor only; controlled area barricaded and signed with monitoring at the boundary; work scheduled to minimise personnel nearby; dosimetry for all radiographers|H|Radiation Protection Supervisor|Dosimeter badge;Radiation survey meter
Nucleonic Gauge Work (Radioactive Source)|E|Ionising radiation exposure from an open or damaged source shutter|E|Shutter closed and padlocked before nearby work, verified with a survey meter; only licensed persons open source housings; dose monitoring; source register maintained|H|Radiation Protection Supervisor|Dosimeter badge;Radiation survey meter
Instrument Loop Checking|E|Unintended plant movement triggered by loop forcing or simulation|E|Loop check under permit with field and control room coordination; isolate final elements before forcing; log and reverse all forces|M|Instrumentation Technician|Two-way radio;Hi-vis vest
Housekeeping/Cleaning|L|Slips, trips, and cuts while cleaning plant areas|M|Clean as you go; correct tools; segregate waste; never clean near running machinery without isolation|L|Area Supervisor|Safety gloves (general);Safety boots
Fire Watch Duty|J|Fire watch unable to detect or respond to a fire|H|Trained fire watch with no other duties; extinguisher and radio at hand; remain for 60 minutes after hot work stops|M|Fire Watch|Fire extinguisher;Two-way radio;Flame-resistant (FR) coveralls
Insulation / Lagging Work|J|Exposure to insulation fibres and possible legacy asbestos|H|Survey for asbestos before disturbing legacy lagging; wet methods; RPE and disposable coveralls; bagged disposal|M|HSE Officer|P3 respirator;Disposable coveralls;Safety gloves (general)
Painting / Surface Coating|J|Solvent exposure and fire risk during coating work|H|Ventilation; organic vapour respirator; eliminate ignition sources; coating products approved for the area classification|M|Area Supervisor|Organic vapour respirator;Chemical-resistant gloves;Coveralls
Civil / Foundation Work|E|Excavation collapse and contact with buried services|E|Permit to excavate with service drawings and locator survey; shoring or battering per soil assessment; safe access and spoil setback|H|Civil Supervisor|Hard hat;Hi-vis vest;Safety boots
Stores / Warehouse Handling|E|Racking collapse or falling stock from height|H|Racking inspection and load limits displayed; no climbing on racking; mechanical aids for high-level retrieval|M|Stores Supervisor|Hard hat;Safety boots
Emergency Response / Drill|J|Responder injury during drill or real emergency response|H|Scene safety assessment before entry; never enter a gas-affected or confined space without correct PPE and rescue team; drills supervised with stop authority|M|HSE Officer|Task-appropriate PPE;SCBA
Permit Issue / Area Handover|J|Inadequate hazard communication at handover leading to work on live plant|E|Joint site inspection before issue; isolation certificate cross-referenced; gas test recorded; permit displayed at the work site; shift handover of all open permits|M|Permit Issuing Authority|Multi-gas detector;Hard hat
Contractor Supervision|J|Contractor unfamiliar with site hazards and rules|H|Site induction completed; contractor work pack and permit reviewed; competent supervisor present at all times|M|Contract Owner|Hi-vis vest;Hard hat
Barricading/Signage Setup|L|Struck by traffic or exposure to the hazard while setting up barriers|M|Set up barriers from the safe side; hi-vis; coordinate with traffic control|L|Area Supervisor|Hi-vis vest;Warning signage
First Aid Response Standby|J|Exposure to blood-borne pathogens and scene hazards|M|Universal precautions; gloves and resuscitation face shield; scene made safe before approach|L|First Aider|Nitrile gloves;Resuscitation face shield
Sample Preparation (Laboratory)|J|Cuts, burns, and dust exposure during sample preparation|M|Fume hood or extraction for volatile or dusty samples; heat-resistant gloves for ovens; sharps handling procedure|L|Laboratory Technician|Lab coat;Safety glasses;Nitrile gloves
Chemical/Reagent Handling (Laboratory)|E|Chemical splash or toxic vapour from reagents|H|Fume hood for volatile reagents; eyewash and safety shower tested; SDS accessible; no lone working with hazardous reagents|M|Laboratory Technician|Chemical goggles;Nitrile gloves;Lab coat
"""

COMMON_TOOLS = """
angle grinder|Hot Work|Grinding;Power Tool Use;Hot Work (General)
grinder|Hot Work|Grinding;Power Tool Use
welding machine|Hot Work|Welding;Hot Work (General);Fire Watch Duty
welder|Hot Work|Welding;Hot Work (General);Fire Watch Duty
welding set|Hot Work|Welding;Hot Work (General);Fire Watch Duty
cutting torch|Hot Work|Cutting (Oxy-Acetylene);Hot Work (General);Fire Watch Duty
oxy|Hot Work|Cutting (Oxy-Acetylene);Hot Work (General)
gas axe|Hot Work|Cutting (Oxy-Acetylene);Hot Work (General)
blow torch|Hot Work|Hot Work (General)
drill|Power Tools|Power Tool Use;Drilling
hammer|Hand Tools|Hammering;Hand Tool Use
chisel|Hand Tools|Chiseling;Hand Tool Use
spanner|Hand Tools|Hand Tool Use
wrench|Hand Tools|Hand Tool Use
torque wrench|Hand Tools|Bolt Torqueing / Tensioning;Hand Tool Use
hydraulic torque|Other|Bolt Torqueing / Tensioning;Hydraulic System Work
tensioner|Hand Tools|Bolt Torqueing / Tensioning
hacksaw|Hand Tools|Sawing;Hand Tool Use
shovel|Hand Tools|Shoveling;Manual Handling of Loads
scraper|Hand Tools|Scraping;Hand Tool Use
wire brush|Hand Tools|Hand Tool Use
chain block|Lifting & Rigging|Use of Chain Block;Rigging/Slinging Loads
chain hoist|Lifting & Rigging|Use of Chain Block;Rigging/Slinging Loads
crane|Lifting & Rigging|Crane Operation;Rigging/Slinging Loads;Signaling/Banksman Duties
overhead crane|Lifting & Rigging|Use of Overhead Crane;Rigging/Slinging Loads
mobile crane|Lifting & Rigging|Crane Operation;Rigging/Slinging Loads
sling|Lifting & Rigging|Rigging/Slinging Loads
shackle|Lifting & Rigging|Rigging/Slinging Loads
forklift|Mobile Plant|Use of Forklift;Operating Mobile Equipment
ladder|Access & Height|Ladder Use;Working at Height
scaffold|Access & Height|Scaffold Use;Working at Height
harness|Access & Height|Working at Height
man lift|Access & Height|Man-lift/Aerial Platform Use;Working at Height
cherry picker|Access & Height|Man-lift/Aerial Platform Use;Working at Height
scissor lift|Access & Height|Man-lift/Aerial Platform Use;Working at Height
excavator|Mobile Plant|Operating Mobile Equipment
lathe|Power Tools|Machining (Workshop Lathe/Mill)
milling machine|Power Tools|Machining (Workshop Lathe/Mill)
pressure washer|Fluid & Pressure|Pressure Washing;Wet Work/Slippery Surface
jetting|Fluid & Pressure|Hydro-Jetting / High Pressure Cleaning
hydro jet|Fluid & Pressure|Hydro-Jetting / High Pressure Cleaning
air hose|Fluid & Pressure|Pneumatic System Work
compressor|Fluid & Pressure|Pneumatic System Work
multimeter|Test & Measurement|Instrument Loop Checking;Equipment Testing
megger|Test & Measurement|De-energized Electrical Work;Equipment Testing
gas detector|Test & Measurement|Gas Testing/Atmospheric Monitoring
gas tester|Test & Measurement|Gas Testing/Atmospheric Monitoring
thermal camera|Test & Measurement|Thermographic Survey
vibration meter|Test & Measurement|Vibration Analysis
rope|Lifting & Rigging|Rope Access;Working at Height
winch|Lifting & Rigging|Rigging/Slinging Loads
trolley|Mobile Plant|Manual Handling of Loads
wheelbarrow|Mobile Plant|Manual Handling of Loads
"""

COMMON_RULES = [
 (r"\b(shut ?down|outage|isolat|locked? out|de-?energi[sz]ed|stopped)", ".", "shutdown / isolation", ["Lockout-Tagout Application","Equipment Isolation"]),
 (r"\b(tower|platform|gantry|roof|elevated|upper level|top of|scaffold|pipe ?rack)\b", ".", "elevated location", ["Working at Height","Climbing"]),
 (r"\b(hot|heat|thermal|residual heat|cool ?down|steam)\b", ".", "heat exposure", ["Working in Extreme Heat"]),
 (r"\b(dust|dusty|powder|fines)\b", ".", "dust", ["Dust-Generating Activity","Working in Dusty Environment"]),
 (r"\b(weld|cut|grind|torch|burn|spark|flame)", ".", "hot work", ["Hot Work (General)","Fire Watch Duty"]),
 (r"\b(lift|crane|hoist|sling|rig|chain block)", ".", "lifting", ["Rigging/Slinging Loads","Signaling/Banksman Duties"]),
 (r"\b(heavy|carry|move|haul|shift)", ".", "moving loads", ["Manual Handling of Loads"]),
 (r"\b(clean|clear|blockage|blocked|choke|jam|plugged)", ".", "cleaning / clearing", ["Housekeeping/Cleaning","Hand Tool Use"]),
 (r"\b(electric|cable|panel|motor|switchgear|mcc|transformer|fuse|wiring)", ".", "electrical work", ["De-energized Electrical Work","Electrical Panel Access","Lockout-Tagout Application"]),
 (r"\b(pump|bearing|gearbox|coupling|seal|valve|replace|repair|overhaul|service)", ".", "mechanical maintenance", ["Mechanical Maintenance/Repair","Hand Tool Use"]),
 (r"\b(truck|vehicle|loader|excavator|forklift|tipper|drive)", ".", "mobile plant", ["Operating Mobile Equipment","Vehicle Driving"]),
 (r"\b(night|dark|evening shift)\b", ".", "night work", ["Night Shift Work"]),
 (r"\b(alone|single person|by myself|one man)\b", ".", "lone working", ["Working Alone/Isolated"]),
 (r"\b(noise|noisy|loud)\b", ".", "noise", ["Working in Noisy Environment"]),
 (r"\b(chemical|acid|caustic|reagent|solvent)\b", ".", "chemicals", ["Handling Hazardous Chemicals"]),
 (r"\b(confined|restricted|tight space|manhole)\b", ".", "confined space", ["Confined Space Entry","Gas Testing/Atmospheric Monitoring"]),
]

COMMON_RESP = ["Area Supervisor","Maintenance Technician","Maintenance Supervisor","Mechanical Maintenance Lead","Workshop Supervisor","Workshop Technician",
 "Welding Supervisor","Fire Watch / Maintenance Supervisor","Fire Watch","HSE Officer","HSE Officer / Confined Space Attendant","Scaffold Supervisor",
 "Rope Access Supervisor","Excavation Supervisor","Plant/Fleet Supervisor","Permit Issuing Authority","Rigging Supervisor","Lifting Engineer",
 "Stores Supervisor","Lubrication Technician","Licensed Electrician","Licensed Electrician / Electrical Supervisor","Electrical Supervisor",
 "Utilities Operator","Shift Supervisor","Process Operator","Instrumentation Technician","Reliability Technician","NDT Technician",
 "Radiation Protection Supervisor","Civil Supervisor","Contract Owner","First Aider","Laboratory Technician"]

BU = dict(file="DANGOTE_REFINERY_Master_Workbook_v1.xlsx", title="DANGOTE PETROLEUM REFINERY — RISK REGISTER (MASTER WORKBOOK)",
          unit="Dangote Petroleum Refinery", company="DANGOTE PETROLEUM REFINERY")

LOCATIONS = [
 ("Crude Distillation Unit (CDU)","Process"),("Vacuum Distillation Unit (VDU)","Process"),
 ("Naphtha Hydrotreater","Process"),("Catalytic Reformer","Process"),("Diesel / Kerosene Hydrotreater","Process"),
 ("Fluid Catalytic Cracking Unit","Process"),("Alkylation Unit","Process"),("Hydrogen Generation Unit","Process"),
 ("Sulphur Recovery Unit","Process"),("Amine Regeneration Unit","Process"),("Sour Water Stripper","Process"),
 ("Polypropylene Plant","Process"),("Flare System","Process"),
 ("Crude Tank Farm","Utility"),("Product Tank Farm","Utility"),("LPG Storage (Spheres / Bullets)","Utility"),
 ("Captive Power Plant","Utility"),("Steam Generation / Boiler House","Utility"),("Cooling Water System","Utility"),
 ("Raw Water / Demineralisation Plant","Utility"),("Effluent Treatment Plant","Utility"),("Nitrogen / Instrument Air Plant","Utility"),
 ("Main Substation","Utility"),("Fire Water Pump House","Utility"),
 ("Truck Loading Gantry","Site"),("Marine Terminal / Jetty","Site"),("Pipe Racks and Pipeways","Site"),("Refinery Roads and Yard","Site"),
 ("Central Control Room","Building"),("Quality Control Laboratory","Building"),("Central Maintenance Workshop","Building"),
 ("Warehouse / Stores","Building"),("Fire Station","Building"),("Administrative Building","Building"),
 ("Other Area (User should Specify)","Other"),
]

EQUIPMENT_TYPES = ["Fired Heater / Furnace","Distillation Column","Pressure Vessel / Drum","Catalytic Reactor","Heat Exchanger","Air Cooler (Fin Fan)",
 "Centrifugal Pump","Process Compressor","Atmospheric Storage Tank","Pressurised Storage (LPG)","Flare Stack and KO Drum","Process Piping and Pipeline",
 "Loading Arm / Gantry","Marine Loading System","Steam Boiler","Gas Turbine / Generator","Cooling Tower","High Voltage Electrical Equipment",
 "Lifting Equipment","Mobile Plant","Laboratory Equipment","Scaffolding / Temporary Works","Radioactive Source Equipment","Fire Safety Equipment",
 "Workshop Machinery","Warehouse / Stores Equipment","Molten Sulphur System","Effluent / Oily Water System"]

PROC = "All process areas"
EQUIPMENT = [
 ("Crude Charge Heater","Fired Heater / Furnace","Listed areas only",["Crude Distillation Unit (CDU)"]),
 ("Vacuum Heater","Fired Heater / Furnace","Listed areas only",["Vacuum Distillation Unit (VDU)"]),
 ("Reformer Heaters","Fired Heater / Furnace","Listed areas only",["Catalytic Reformer"]),
 ("Hydrogen Plant Reformer Furnace","Fired Heater / Furnace","Listed areas only",["Hydrogen Generation Unit"]),
 ("Atmospheric Distillation Column","Distillation Column","Listed areas only",["Crude Distillation Unit (CDU)"]),
 ("Vacuum Column","Distillation Column","Listed areas only",["Vacuum Distillation Unit (VDU)"]),
 ("FCC Main Fractionator","Distillation Column","Listed areas only",["Fluid Catalytic Cracking Unit"]),
 ("Stripper / Stabiliser Column","Distillation Column","Listed areas only",["Naphtha Hydrotreater","Diesel / Kerosene Hydrotreater","Catalytic Reformer","Sour Water Stripper"]),
 ("Amine Regenerator","Distillation Column","Listed areas only",["Amine Regeneration Unit"]),
 ("Desalter","Pressure Vessel / Drum","Listed areas only",["Crude Distillation Unit (CDU)"]),
 ("Separator / Knock-out Drum","Pressure Vessel / Drum",PROC,[]),
 ("Reflux Drum","Pressure Vessel / Drum",PROC,[]),
 ("Hydrotreater Reactor","Catalytic Reactor","Listed areas only",["Naphtha Hydrotreater","Diesel / Kerosene Hydrotreater"]),
 ("Reformer Reactors","Catalytic Reactor","Listed areas only",["Catalytic Reformer"]),
 ("FCC Reactor / Regenerator","Catalytic Reactor","Listed areas only",["Fluid Catalytic Cracking Unit"]),
 ("Alkylation Reactor (Acid Service)","Catalytic Reactor","Listed areas only",["Alkylation Unit"]),
 ("Claus Reactor","Catalytic Reactor","Listed areas only",["Sulphur Recovery Unit"]),
 ("Polymerisation Reactor","Catalytic Reactor","Listed areas only",["Polypropylene Plant"]),
 ("Shell & Tube Heat Exchanger","Heat Exchanger",PROC,[]),
 ("Fin Fan Cooler","Air Cooler (Fin Fan)",PROC,[]),
 ("Process Pump","Centrifugal Pump",PROC,[]),
 ("Product Transfer Pump","Centrifugal Pump","Listed areas only",["Crude Tank Farm","Product Tank Farm","Truck Loading Gantry","Marine Terminal / Jetty"]),
 ("Wet Gas Compressor","Process Compressor","Listed areas only",["Fluid Catalytic Cracking Unit"]),
 ("Recycle Gas Compressor","Process Compressor","Listed areas only",["Naphtha Hydrotreater","Diesel / Kerosene Hydrotreater","Catalytic Reformer"]),
 ("Hydrogen Make-up Compressor","Process Compressor","Listed areas only",["Hydrogen Generation Unit","Diesel / Kerosene Hydrotreater"]),
 ("Air Compressor","Process Compressor","Listed areas only",["Nitrogen / Instrument Air Plant"]),
 ("Crude Storage Tank (Floating Roof)","Atmospheric Storage Tank","Listed areas only",["Crude Tank Farm"]),
 ("Product Storage Tank","Atmospheric Storage Tank","Listed areas only",["Product Tank Farm"]),
 ("LPG Sphere / Bullet","Pressurised Storage (LPG)","Listed areas only",["LPG Storage (Spheres / Bullets)"]),
 ("Flare Stack","Flare Stack and KO Drum","Listed areas only",["Flare System"]),
 ("Flare Knock-out Drum","Flare Stack and KO Drum","Listed areas only",["Flare System"]),
 ("Process Piping","Process Piping and Pipeline","All areas",[]),
 ("Pig Launcher / Receiver","Process Piping and Pipeline","Listed areas only",["Crude Tank Farm","Marine Terminal / Jetty","Pipe Racks and Pipeways"]),
 ("Truck Loading Arm","Loading Arm / Gantry","Listed areas only",["Truck Loading Gantry"]),
 ("Marine Loading Arm / Hose","Marine Loading System","Listed areas only",["Marine Terminal / Jetty"]),
 ("Steam Boiler","Steam Boiler","Listed areas only",["Steam Generation / Boiler House","Captive Power Plant"]),
 ("Gas Turbine Generator","Gas Turbine / Generator","Listed areas only",["Captive Power Plant"]),
 ("Steam Turbine Generator","Gas Turbine / Generator","Listed areas only",["Captive Power Plant"]),
 ("Cooling Tower Cell","Cooling Tower","Listed areas only",["Cooling Water System"]),
 ("Switchgear / MCC","High Voltage Electrical Equipment","All areas",[]),
 ("Power Transformer","High Voltage Electrical Equipment","Listed areas only",["Main Substation","Captive Power Plant"]),
 ("Overhead / Gantry Crane","Lifting Equipment","Listed areas only",["Central Maintenance Workshop","Captive Power Plant","Warehouse / Stores","Polypropylene Plant"]),
 ("Mobile Crane","Lifting Equipment","All areas",[]),
 ("Vacuum Truck","Mobile Plant","All areas",[]),
 ("Forklift / Telehandler","Mobile Plant","Listed areas only",["Warehouse / Stores","Polypropylene Plant","Central Maintenance Workshop","Refinery Roads and Yard"]),
 ("Laboratory Analysers and Fume Hoods","Laboratory Equipment","Listed areas only",["Quality Control Laboratory"]),
 ("Online Process Analyser Shelter","Laboratory Equipment",PROC,[]),
 ("Scaffolding (Temporary Works)","Scaffolding / Temporary Works","All areas",[]),
 ("Nucleonic Level / Density Gauge","Radioactive Source Equipment","Listed areas only",["Fluid Catalytic Cracking Unit","Polypropylene Plant","Vacuum Distillation Unit (VDU)"]),
 ("Fire Water Pump","Fire Safety Equipment","Listed areas only",["Fire Water Pump House"]),
 ("Deluge / Foam System","Fire Safety Equipment","Listed areas only",["Crude Tank Farm","Product Tank Farm","LPG Storage (Spheres / Bullets)","Truck Loading Gantry","Marine Terminal / Jetty"]),
 ("Workshop Machine Tools","Workshop Machinery","Listed areas only",["Central Maintenance Workshop"]),
 ("Warehouse Racking","Warehouse / Stores Equipment","Listed areas only",["Warehouse / Stores"]),
 ("Molten Sulphur Pit","Molten Sulphur System","Listed areas only",["Sulphur Recovery Unit"]),
 ("API / CPI Separator","Effluent / Oily Water System","Listed areas only",["Effluent Treatment Plant"]),
 ("Oily Water Sewer and Manholes","Effluent / Oily Water System","All areas",[]),
]

BU_TAGS = [
 ("Process Operations", ["Line Breaking / Opening Process Equipment","Blinding / De-blinding","Gas Freeing / Purging","Work in Nitrogen-Purged Equipment",
   "H2S Area Work","Hydrocarbon Sampling","Unit Start-up / Shutdown","Fired Heater Light-off / Operation","Valve Operation in Process Unit",
   "Flare System Work","Catalyst Loading / Unloading","Hot Tapping / Stoppling","Pigging Operations","Steam System Work",
   "Pressure Testing (Hydro / Pneumatic)","Amine / Caustic System Work","Molten Sulphur Handling","Work Near Benzene-Containing Streams"]),
 ("Tank Farm & Dispatch", ["Tank Gauging / Dipping","Tank Cleaning (Sludge Removal)","Product Loading (Truck Gantry)","Marine Loading / Unloading (Jetty)","Drain / Water Draw-off from Tanks"]),
]

BU_AH = """
Line Breaking / Opening Process Equipment|E|Release of hydrocarbon, H2S, or toxic fluid when breaking a line or opening equipment not fully drained, vented, or isolated|E|Line-break permit; positive isolation verified; drain, depressurise, flush or purge and confirm at bleed point; break the flange away from the body with bolts loosened on the far side first; second person standing by|M|Permit Issuing Authority|Chemical goggles;Face shield;Chemical-resistant gloves;Multi-gas detector
Line Breaking / Opening Process Equipment|L|Pyrophoric iron sulphide deposits igniting on exposure to air|H|Keep internals wet; open under controlled conditions with fire hose standing by; remove scale into water-filled containers|M|Process Operator|Flame-resistant (FR) coveralls;Face shield
Blinding / De-blinding|E|Spade or blind installed in the wrong location, wrong rating, or missed during reinstatement|E|Numbered blind list and register tied to the isolation certificate; rated blinds tagged and logged; walk-down verification before entry and before start-up|M|Permit Issuing Authority|Lock and tag kit;Safety gloves (general)
Blinding / De-blinding|E|Residual pressure or fluid release while spreading flanges|E|Depressurise and drain to closed system; confirm zero pressure at bleed; flange spreader used; stand clear of the line of fire|M|Mechanical Maintenance Lead|Face shield;Chemical-resistant gloves;Flame-resistant (FR) coveralls
Gas Freeing / Purging|E|Flammable mixture formed during steam-out or purging, or incomplete hydrocarbon removal|E|Approved purge procedure with target end-point concentrations; vent to flare or safe location; gas test before declaring gas-free; no hot work until certificate issued|M|Process Operator|Multi-gas detector;Flame-resistant (FR) coveralls
Gas Freeing / Purging|J|Burns from steam during steam-out|H|Steam hoses rated and secured with whip-checks; stand clear of vents and drains; hot-surface signage|M|Process Operator|Heat-resistant gauntlets;Face shield
Work in Nitrogen-Purged Equipment|L|Instant asphyxiation from nitrogen atmosphere at manways and vessel openings|E|Nitrogen warning signs and barriers at all openings; no head or body inside an opening without SCBA or airline; continuous O2 monitoring at the opening; specialist inert-entry contractor for any inert entry|H|HSE Officer / Confined Space Attendant|SCBA;Airline / air-fed respirator;Multi-gas detector
H2S Area Work|L|Hydrogen sulphide exposure causing loss of consciousness or death|E|Personal H2S monitor worn by every person; buddy system; escape set carried; work upwind; wind sock checked; H2S refuge and muster point known; evacuate on alarm|M|HSE Officer|H2S personal monitor;Escape breathing set;SCBA
Hydrocarbon Sampling|E|Exposure to toxic or flammable hydrocarbon vapour and liquid during sampling|H|Closed-loop samplers; stand upwind; sample bombs rated for pressure; second person for H2S service; bonding of containers|M|Process Operator|Chemical goggles;Chemical-resistant gloves;H2S personal monitor;Flame-resistant (FR) coveralls
Unit Start-up / Shutdown|J|Process upset, overpressure, or loss of containment during transient operations|E|Approved start-up/shutdown procedure with step sign-off; pre-start-up safety review; non-essential personnel cleared; control room and field communication by radio|M|Shift Supervisor|Flame-resistant (FR) coveralls;Two-way radio;H2S personal monitor
Fired Heater Light-off / Operation|E|Firebox explosion from fuel accumulation during light-off|E|Purge firebox for the required air changes; burner management system permissives verified; light one burner at a time; never relight without re-purge|H|Process Operator|Flame-resistant (FR) coveralls;Face shield;Heat-resistant gauntlets
Fired Heater Light-off / Operation|J|Flame flashback and radiant burns at peepholes and burner fronts|H|Use shaded viewing ports; stand to the side when opening; verify negative draught; aluminised PPE for close work|M|Process Operator|Face shield;Heat-resistant gauntlets;Flame-resistant (FR) coveralls
Valve Operation in Process Unit|J|Strain injury or valve-wheel kick when operating large or stiff valves|M|Use valve keys or actuators rather than cheater bars; check stem condition; position body out of line of the wheel|L|Process Operator|Safety gloves (general);Safety boots
Valve Operation in Process Unit|E|Wrong valve operated causing loss of containment|H|Valve tagging and line-up checklists; verify against P&ID; independent check for critical line-ups|M|Shift Supervisor|Two-way radio
Flare System Work|L|Thermal radiation, toxic gas, or sudden flaring while working near the flare|E|Work only during agreed flare-safe windows; radiation exposure limits; continuous gas monitoring; escape route planned; control room informed before access|H|Shift Supervisor|Flame-resistant (FR) coveralls;H2S personal monitor;SCBA
Catalyst Loading / Unloading|J|Exposure to catalyst dust, pyrophoric spent catalyst, and nickel or cobalt compounds|E|Unload spent catalyst under nitrogen blanket by specialist contractor; dust extraction; RPE (P3 or air-fed); keep spent catalyst wet or inerted in drums|H|HSE Officer|Airline / air-fed respirator;Disposable coveralls;Chemical goggles
Catalyst Loading / Unloading|L|Engulfment or asphyxiation inside reactor during catalyst handling|E|Inert entry only with specialist contractor and continuous breathing air; no entry while catalyst is flowing; standby rescue team|H|HSE Officer / Confined Space Attendant|Airline / air-fed respirator;Full body harness;Retrieval winch and davit
Hot Tapping / Stoppling|E|Burn-through or loss of containment while welding or tapping on a live line|E|Engineered hot-tap procedure with wall-thickness survey; qualified hot-tap contractor; flow and pressure within limits; fire watch and standby fire tender|H|Mechanical Maintenance Lead|Flame-resistant (FR) coveralls;Face shield;Multi-gas detector
Pigging Operations|E|Pressure release or projectile ejection when opening pig traps|E|Depressurise, drain, and verify zero pressure before opening the closure; interlock on closure where fitted; stand clear of the line of the barrel|M|Process Operator|Face shield;Chemical-resistant gloves;H2S personal monitor
Steam System Work|E|Scalding from steam or condensate release and water hammer|E|Isolate, depressurise, and drain; open drains slowly to avoid water hammer; never crack a flange on a live steam line|M|Utilities Supervisor|Heat-resistant gauntlets;Face shield;Coveralls
Pressure Testing (Hydro / Pneumatic)|E|Catastrophic failure releasing stored energy during pressure test|E|Test procedure with calculated test pressure and relief valve set; exclusion zone during pressurisation; pneumatic tests only with engineering approval; gauges calibrated|M|Inspection Engineer|Face shield;Hard hat;Safety boots
Amine / Caustic System Work|E|Chemical burns from amine or caustic and H2S release from rich amine|E|Drain and flush before opening; full chemical PPE; H2S monitoring; eyewash and safety shower at the work location|M|Process Operator|Chemical suit;Face shield;Chemical-resistant gloves;H2S personal monitor
Molten Sulphur Handling|E|Severe burns from molten sulphur at around 140 degrees C and sulphur fires|E|Heat-resistant PPE; steam-jacketed lines checked for leaks; fire hose with fog nozzle standing by; never use water jets on molten sulphur|M|Process Operator|Heat-resistant gauntlets;Face shield;Flame-resistant (FR) coveralls;Heat-resistant boots and gaiters
Molten Sulphur Handling|L|H2S and SO2 release from sulphur pits and loading points|E|Pit vent system operating; gas monitoring before approaching pit openings; work upwind; escape set carried|M|HSE Officer|H2S personal monitor;Escape breathing set
Work Near Benzene-Containing Streams|J|Benzene exposure (carcinogen) from reformate, aromatics, or gasoline streams|H|Identify benzene-containing streams on the permit; closed draining and sampling; benzene-specific monitoring; organic vapour RPE where exposure cannot be excluded; health surveillance|M|HSE Officer|Organic vapour respirator;Chemical-resistant gloves;Chemical goggles
Tank Gauging / Dipping|L|Exposure to hydrocarbon vapour and H2S at tank roof hatches|E|Use automatic gauging where available; stand upwind and open hatch slowly; personal H2S and LEL monitor; no tank roof access alone|M|Tank Farm Supervisor|H2S personal monitor;Multi-gas detector;Anti-static coveralls
Tank Gauging / Dipping|L|Fall from tank roof or through a floating roof|E|Fixed stairways and guarded platforms only; no access onto floating roofs without permit, gas test and harness; never walk on a fixed roof outside walkways|M|Tank Farm Supervisor|Full body harness;Hard hat
Tank Cleaning (Sludge Removal)|L|Toxic and flammable atmosphere and pyrophoric deposits inside tank|E|Specialist tank-cleaning contractor; mechanical sludge removal where possible; positive isolation and gas-free certificate; continuous monitoring; breathing air for entry|H|Tank Farm Supervisor|Airline / air-fed respirator;Chemical suit;Multi-gas detector;Full body harness
Product Loading (Truck Gantry)|E|Fire or explosion from static discharge or overfill during truck loading|E|Earth and overfill protection system interlocked with loading; bottom loading where available; driver stays at the gantry; no mobile phones; emergency stop accessible|M|Dispatch Supervisor|Anti-static coveralls;Safety gloves (general);Hi-vis vest
Product Loading (Truck Gantry)|L|Fall from truck top during top loading|E|Gantry access platform with folding guardrail; harness where platform is not available; never walk on tanker tops unprotected|M|Dispatch Supervisor|Full body harness;Hard hat
Marine Loading / Unloading (Jetty)|E|Hose or loading-arm failure, surge, or emergency disconnection causing a hydrocarbon spill or fire|E|Ship-shore safety checklist; loading arm envelope monitored with ERC tested; agreed loading rates; spill containment and boom on standby; fire monitors ready|H|Marine Terminal Supervisor|Flame-resistant (FR) coveralls;Buoyancy aid;H2S personal monitor
Marine Loading / Unloading (Jetty)|L|Fall into water from jetty or gangway|E|Edge protection and life rings along the jetty; lifejacket at the vessel edge; controlled gangway access only; never work alone at the waterside|H|Marine Terminal Supervisor|Buoyancy aid;Hi-vis vest
Drain / Water Draw-off from Tanks|E|Hydrocarbon release when draining water from tank bottoms unattended|H|Draining always attended; close valve before leaving; H2S and LEL monitoring at the drain; drain to closed system|M|Tank Farm Supervisor|H2S personal monitor;Chemical-resistant gloves;Chemical goggles
"""

EH = """
Fired Heater / Furnace|E|Firebox explosion or tube rupture leading to fire|E|Burner management system with flame failure protection; tube skin temperature monitoring; emergency shutdown and snuffing steam tested; no manual override of trips|H|Process Operator|Flame-resistant (FR) coveralls;Face shield|Any|Operational
Fired Heater / Furnace|L|Confined space entry into firebox with residual heat and refractory dust|E|Positive isolation of all fuel lines by blinding; cool-down verified; confined space permit and gas test; refractory dust RPE|M|HSE Officer / Confined Space Attendant|P3 respirator;Full body harness;Multi-gas detector|Any|Shutdown/Isolated
Fired Heater / Furnace|J|Burns from hot surfaces, flue gas leaks, and peepholes|H|Hot-surface lagging and signage; shaded viewing ports; draught confirmed negative before opening doors|M|Process Operator|Heat-resistant gauntlets;Face shield|Any|Operational
Distillation Column|L|Fall from height on column platforms and ladders|E|Caged ladders and guarded platforms maintained; 100% tie-off outside protection; tool lanyards|M|Area Supervisor|Full body harness;Hard hat with chin strap|Any|Any
Distillation Column|L|Toxic or pyrophoric atmosphere inside column during entry|E|Steam-out and water wash; positive isolation; gas-free certificate; pyrophoric deposits kept wet; continuous monitoring and standby|M|HSE Officer / Confined Space Attendant|Multi-gas detector;SCBA;Full body harness|Any|Shutdown/Isolated
Distillation Column|E|Loss of containment of hydrocarbon at flanges, drains, and instruments|H|Leak detection and repair programme; flange management; gas detection in the unit; respond to leaks only with isolation and authorisation|M|Process Operator|H2S personal monitor;Flame-resistant (FR) coveralls|Any|Operational
Pressure Vessel / Drum|E|Overpressure and vessel rupture|E|Relief valves inspected and certified; never isolate a relief device without engineering authorisation; level and pressure alarms maintained|H|Inspection Engineer|Hard hat;Face shield|Any|Any
Pressure Vessel / Drum|L|Confined space hazards on vessel entry (toxic, flammable, inert)|E|Positive isolation and blinding; purge and gas-free certificate; continuous monitoring; standby attendant and rescue plan|M|HSE Officer / Confined Space Attendant|Multi-gas detector;SCBA;Full body harness|Any|Shutdown/Isolated
Catalytic Reactor|E|High-pressure hydrogen leak causing invisible flame or explosion|E|Hydrogen leak detection; flange management with controlled bolting; flame detectors; approach suspected leaks with a broom or thermal camera, never by hand|H|Process Operator|Flame-resistant (FR) coveralls;Face shield|Any|Operational
Catalytic Reactor|L|Inert (nitrogen) atmosphere and pyrophoric catalyst inside reactor|E|Inert entry only by specialist contractor with breathing air; strict control of manways; nitrogen warning barriers|H|HSE Officer / Confined Space Attendant|Airline / air-fed respirator;Full body harness|Any|Shutdown/Isolated
Catalytic Reactor|J|Hydrofluoric or sulphuric acid exposure in alkylation service|E|Acid-area entry procedure; full acid PPE and buddy system; acid-neutralising first aid and emergency showers; acid leak detection|H|Process Operator|Acid suit;Face shield;Chemical-resistant gloves|Any|Any
Heat Exchanger|E|Tube bundle drop or shifting during extraction|E|Engineered bundle extractor or puller; lift plan; exclusion zone; bundle supported before work beneath|M|Rigging Supervisor|Hard hat;Safety boots|Any|Shutdown/Isolated
Heat Exchanger|E|Release of process fluid when opening channel head|E|Drain and depressurise both shell and tube sides; confirm at bleeds; line-break precautions|M|Mechanical Maintenance Lead|Face shield;Chemical-resistant gloves;H2S personal monitor|Any|Shutdown/Isolated
Air Cooler (Fin Fan)|E|Contact with rotating fan blades during maintenance|E|LOTO on fan motor and lock the fan against windmilling; guards refitted before restart|M|Mechanical Maintenance Lead|Lock and tag kit;Safety gloves (general)|Any|Shutdown/Isolated
Air Cooler (Fin Fan)|L|Fall from fin fan deck|H|Guardrails on decks; harness outside protection; inspect gratings|M|Area Supervisor|Full body harness;Hard hat|Any|Any
Centrifugal Pump|E|Seal failure releasing hot or toxic hydrocarbon and fire|E|Seal monitoring and leak detection; emergency isolation valves accessible; fire protection at pump rows; respond only with isolation|H|Process Operator|Flame-resistant (FR) coveralls;Face shield;H2S personal monitor|Running|Operational
Centrifugal Pump|E|Pump started or pressurised during maintenance|E|Electrical LOTO and suction/discharge isolation with vent and drain verified; try-start test|M|Maintenance Supervisor|Lock and tag kit;Safety gloves (general)|Any|Shutdown/Isolated
Process Compressor|E|Gas release and fire from compressor seals or piping vibration failure|E|Seal gas system monitored; vibration protection and trips; gas detection in compressor house; emergency shutdown tested|H|Process Operator|Flame-resistant (FR) coveralls;Ear plugs plus ear muffs|Running|Operational
Process Compressor|E|Unexpected rotation or pressurisation during overhaul|E|Isolate, depressurise, purge; lock turning gear and drivers; verify zero speed and pressure|M|Mechanical Maintenance Lead|Lock and tag kit;Face shield|Any|Shutdown/Isolated
Atmospheric Storage Tank|E|Tank fire or rim-seal fire|E|Rim-seal fire detection and foam system tested; lightning protection and shunts maintained; hot work prohibited without certificate|H|Tank Farm Supervisor|Flame-resistant (FR) coveralls|Any|Any
Atmospheric Storage Tank|E|Tank overfill causing vapour cloud and spill|E|Independent high-high level alarm and overfill protection tested; transfers attended; bund drain valves closed|H|Tank Farm Supervisor|Multi-gas detector|Any|Operational
Atmospheric Storage Tank|L|Fall from tank roof or stairway|H|Guarded stairways and roof walkways; no access outside walkways; harness for roof edge work|M|Tank Farm Supervisor|Full body harness;Hard hat|Any|Any
Pressurised Storage (LPG)|E|LPG release forming vapour cloud with risk of explosion or BLEVE|E|Water deluge and gas detection tested; remote-operated isolation valves; never drain unattended; ignition control within the storage area|H|Tank Farm Supervisor|Flame-resistant (FR) coveralls;Multi-gas detector|Any|Any
Pressurised Storage (LPG)|J|Cold burns from LPG liquid release|H|Closed draining; cryogenic-rated gloves and face shield for draining and sampling|M|Process Operator|Cold-insulated gloves;Face shield|Any|Any
Flare Stack and KO Drum|L|Thermal radiation and toxic gas exposure near flare|E|Restricted zone; flare-safe work windows; gas monitoring; control room clearance before entry|H|Shift Supervisor|Flame-resistant (FR) coveralls;H2S personal monitor|Any|Operational
Flare Stack and KO Drum|E|Liquid carry-over or flashback in the flare system|E|KO drum level control and alarms; purge gas flow maintained; water seal level monitored|H|Process Operator|Flame-resistant (FR) coveralls|Any|Operational
Process Piping and Pipeline|E|Loss of containment from corroded or damaged piping|E|Risk-based inspection programme; corrosion monitoring; leaks isolated and reported; temporary clamps only under engineering approval|H|Inspection Engineer|H2S personal monitor;Flame-resistant (FR) coveralls|Any|Any
Process Piping and Pipeline|E|Trapped pressure between closed valves|H|Bleed points used to depressurise every isolated section; verify zero at bleed before opening|M|Process Operator|Face shield;Chemical-resistant gloves|Any|Shutdown/Isolated
Loading Arm / Gantry|E|Static ignition or overfill during loading|E|Earth verification and overfill interlocks; emergency stop; no loading during electrical storms|M|Dispatch Supervisor|Anti-static coveralls|Any|Operational
Loading Arm / Gantry|L|Vehicle collision at the gantry|H|Gantry traffic management; speed limits; wheel chocks; driver training|M|Dispatch Supervisor|Hi-vis vest|Any|Any
Marine Loading System|E|Hose or arm rupture causing spill to water|E|Hoses tested and certified; arm envelope alarms and ERC; spill response equipment ready|H|Marine Terminal Supervisor|Buoyancy aid;Flame-resistant (FR) coveralls|Any|Operational
Marine Loading System|L|Fall into water during connection and disconnection|E|Lifejackets; edge protection; work from designated platforms|H|Marine Terminal Supervisor|Buoyancy aid;Hard hat|Any|Any
Steam Boiler|E|Boiler explosion or tube failure|E|Water level and burner management trips tested; statutory inspection current; water chemistry control|H|Utilities Supervisor|Face shield;Heat-resistant gauntlets|Any|Operational
Steam Boiler|J|Burns from steam leaks and hot surfaces|H|Lagging maintained; leaks reported and isolated; never approach a high-pressure steam leak (invisible jet)|M|Utilities Operator|Heat-resistant gauntlets;Face shield|Any|Any
Gas Turbine / Generator|E|Fuel gas leak and fire in turbine enclosure|E|Enclosure gas detection and fire suppression tested; enclosure entry only with suppression inhibited and permit|H|Utilities Supervisor|Ear plugs plus ear muffs;Flame-resistant (FR) coveralls|Any|Any
Gas Turbine / Generator|E|Back-feed or unexpected start during maintenance|E|Electrical and mechanical isolation of generator and starting system; turning gear locked; verify zero voltage|M|Electrical Supervisor|Lock and tag kit;Voltage tester|Any|Shutdown/Isolated
Cooling Tower|E|Fan blade contact or unexpected start|E|LOTO on fan drive and lock rotor; guards refitted before restart|M|Mechanical Maintenance Lead|Lock and tag kit|Any|Shutdown/Isolated
Cooling Tower|J|Legionella and treatment chemical exposure|H|Water treatment programme; RPE near drift during operation; chemical PPE for dosing|M|HSE Officer|P3 respirator;Chemical goggles|Any|Any
High Voltage Electrical Equipment|E|Electrocution from contact with high voltage conductors|E|Isolate, lock, prove dead, and earth before work; authorised HV person and permit; approach distances maintained|H|HV Authorised Person|Arc-rated suit and hood;Insulated electrical gloves;Voltage tester|Any|Any
High Voltage Electrical Equipment|E|Arc flash during switching or racking|E|Arc flash study and labelling; remote racking; arc-rated PPE to rating|H|Electrical Supervisor|Arc-rated suit and hood;Ear plugs|Any|Any
Lifting Equipment|E|Load drop from equipment failure or overload|E|Thorough examination current; pre-use checks; SWL never exceeded; lift plan|M|Lifting Engineer|Hard hat;Safety boots|Any|Any
Lifting Equipment|L|Crane contact with live process plant or pipe racks|E|Lift plan with exclusion zones; banksman; process isolation of plant under the lift path where required|M|Lifting Engineer|Hard hat;Hi-vis vest|Any|Any
Mobile Plant|E|Ignition source from vehicles entering classified process areas|E|Vehicle entry permit for process areas; spark arrestors; engine off when not required; gas test before entry|M|Plant/Fleet Supervisor|Hi-vis vest|Any|Any
Mobile Plant|J|Collision with pedestrians or plant|E|Traffic management plan; speed limits; reversing aids; banksman in congested areas|M|Plant/Fleet Supervisor|Hi-vis vest;Hard hat|Any|Any
Laboratory Equipment|J|Exposure to hydrocarbon samples, H2S, and reagents|H|Fume hoods; closed sample handling; H2S monitoring in the sample receiving area|M|Laboratory Technician|Chemical goggles;Nitrile gloves;Lab coat|Any|Any
Laboratory Equipment|E|Fire from flammable samples and solvents|H|Flammables cabinets; minimal quantities on bench; extinguishers and fire blanket|M|Laboratory Technician|Lab coat;Safety glasses|Any|Any
Scaffolding / Temporary Works|E|Scaffold collapse or unauthorised modification|E|Competent scaffolders only; tag system; load limits; re-inspection after modification|H|Scaffold Supervisor|Hard hat;Full body harness|Any|Any
Scaffolding / Temporary Works|J|Dropped components from scaffold levels|H|Toe boards and debris netting; exclusion zone below; tool lanyards|M|Scaffold Supervisor|Hard hat|Any|Any
Radioactive Source Equipment|E|Ionising radiation exposure from source with open or damaged shutter|E|Shutter closed and locked before nearby work, verified with survey meter; licensed persons only; source register|H|Radiation Protection Supervisor|Dosimeter badge;Radiation survey meter|Any|Any
Fire Safety Equipment|E|Fire system impaired when needed|E|Impairment permit and compensatory measures; scheduled testing; restore and verify after work|M|Fire Safety Officer|Task-appropriate PPE|Any|Any
Fire Safety Equipment|E|Unexpected deluge or foam release during maintenance|H|Isolate deluge valves and inform control room; warning signage|M|Fire Safety Officer|Waterproof / rain boots|Any|Shutdown/Isolated
Workshop Machinery|E|Entanglement in lathes, mills, and drills|E|Guards and interlocks; no gloves or loose clothing at rotating machinery; trained operators|M|Workshop Supervisor|Safety glasses;Close-fitting clothing|Any|Any
Warehouse / Stores Equipment|E|Racking collapse or falling stock|H|Load limits displayed; racking inspection; no climbing on racking|M|Stores Supervisor|Hard hat;Safety boots|Any|Any
Molten Sulphur System|E|Molten sulphur burns and sulphur fires|E|Steam jacketing checked; heat-resistant PPE; fog nozzle hose standing by|M|Process Operator|Heat-resistant gauntlets;Face shield;Flame-resistant (FR) coveralls|Any|Any
Molten Sulphur System|L|H2S accumulation in sulphur pit headspace|E|Pit sweep and vent system running; gas test before opening covers; no entry without confined space permit|M|HSE Officer|H2S personal monitor;SCBA|Any|Any
Effluent / Oily Water System|L|Flammable vapour and H2S at manholes, separators, and sewers|E|Sealed drain covers maintained; gas test before work near openings; no hot work within 15 m of open drains without sealing|M|HSE Officer|H2S personal monitor;Multi-gas detector|Any|Any
Effluent / Oily Water System|L|Drowning or engulfment in open separators and basins|H|Guardrails and covers; harness and line for work over open liquid; never work alone|M|Area Supervisor|Buoyancy aid;Full body harness|Any|Any
"""

PRESETS = [
 ("Pump seal replacement","Mechanical","Replace mechanical seal on a process pump after isolation, draining and flushing",
  ["Line Breaking / Opening Process Equipment","Equipment Isolation","Lockout-Tagout Application","Mechanical Maintenance/Repair","Hand Tool Use","H2S Area Work"],
  "Centrifugal Pump","Static","Shutdown/Isolated","Process Pump",""),
 ("Heat exchanger bundle pull","Mechanical","Open channel head and extract tube bundle for cleaning during shutdown",
  ["Line Breaking / Opening Process Equipment","Blinding / De-blinding","Rigging/Slinging Loads","Crane Operation","Hydro-Jetting / High Pressure Cleaning","Equipment Isolation"],
  "Heat Exchanger","Static","Shutdown/Isolated","Shell & Tube Heat Exchanger",""),
 ("Vessel entry for inspection","Inspection","Enter a drum or column for internal inspection after steam-out and blinding",
  ["Confined Space Entry","Gas Freeing / Purging","Blinding / De-blinding","Gas Testing/Atmospheric Monitoring","Visual Inspection","Lockout-Tagout Application"],
  "Pressure Vessel / Drum","Static","Shutdown/Isolated","Separator / Knock-out Drum",""),
 ("Tank roof gauging / sampling","Operations","Manual dip and sample of a product tank from the roof platform",
  ["Tank Gauging / Dipping","Hydrocarbon Sampling","Climbing","Working at Height","H2S Area Work"],
  "Atmospheric Storage Tank","Static","Operational","Product Storage Tank","Product Tank Farm"),
 ("Tank water draw-off","Operations","Drain water from crude tank bottom to the oily water system",
  ["Drain / Water Draw-off from Tanks","H2S Area Work","Hydrocarbon Sampling"],
  "Atmospheric Storage Tank","Static","Operational","Crude Storage Tank (Floating Roof)","Crude Tank Farm"),
 ("Truck loading at gantry","Dispatch","Load product into road tanker at the loading gantry",
  ["Product Loading (Truck Gantry)","Handling Flammable Materials","Traffic Control/Flagging","Working at Height"],
  "Loading Arm / Gantry","Static","Operational","Truck Loading Arm","Truck Loading Gantry"),
 ("Ship loading at jetty","Dispatch","Connect loading arm and load product to vessel at the marine terminal",
  ["Marine Loading / Unloading (Jetty)","Working Near Water","Handling Flammable Materials","H2S Area Work"],
  "Marine Loading System","Static","Operational","Marine Loading Arm / Hose","Marine Terminal / Jetty"),
 ("Fired heater light-off","Operations","Purge and light burners on a fired heater during unit start-up",
  ["Fired Heater Light-off / Operation","Unit Start-up / Shutdown","Working in Extreme Heat","Valve Operation in Process Unit"],
  "Fired Heater / Furnace","Static","Operational","Crude Charge Heater","Crude Distillation Unit (CDU)"),
 ("Reactor catalyst change-out","Turnaround","Unload spent catalyst and reload fresh catalyst in a hydrotreater reactor",
  ["Catalyst Loading / Unloading","Work in Nitrogen-Purged Equipment","Confined Space Entry","Rigging/Slinging Loads","Dust-Generating Activity"],
  "Catalytic Reactor","Static","Shutdown/Isolated","Hydrotreater Reactor",""),
 ("Hot work in process unit","Mechanical","Welding repair on piping support inside a live process unit",
  ["Welding","Hot Work (General)","Fire Watch Duty","Gas Testing/Atmospheric Monitoring","Working at Height"],
  "Process Piping and Pipeline","Static","Operational","Process Piping",""),
 ("HV switching","Electrical","Switch and rack out a breaker for maintenance isolation",
  ["Electrical Panel Access","De-energized Electrical Work","Lockout-Tagout Application"],
  "High Voltage Electrical Equipment","Static","Operational","Switchgear / MCC","Main Substation"),
 ("Pig launching","Operations","Load and launch a cleaning pig on the crude transfer line",
  ["Pigging Operations","Line Breaking / Opening Process Equipment","H2S Area Work","Valve Operation in Process Unit"],
  "Process Piping and Pipeline","Static","Operational","Pig Launcher / Receiver","Crude Tank Farm"),
]

TOOLS = """
blind|Process Isolation|Blinding / De-blinding
spade|Process Isolation|Blinding / De-blinding
flange spreader|Process Isolation|Blinding / De-blinding;Line Breaking / Opening Process Equipment
hot tap machine|Process Isolation|Hot Tapping / Stoppling
pig|Process Isolation|Pigging Operations
dip tape|Test & Measurement|Tank Gauging / Dipping
sample bomb|Test & Measurement|Hydrocarbon Sampling
h2s monitor|Test & Measurement|H2S Area Work
breathing apparatus|Access & Height|Confined Space Entry
scba|Access & Height|Confined Space Entry
vacuum truck|Mobile Plant|Operating Mobile Equipment
"""

RULES = [
 (r"\b(enter|entering|entry|inside|internal|go into|get into|climb into|within)", r"\b(column|drum|vessel|tank|reactor|heater|furnace|exchanger|sphere|bullet|separator|regenerator|stack|pit)\b", "entry into a vessel", ["Confined Space Entry","Gas Testing/Atmospheric Monitoring","Lockout-Tagout Application"]),
 (r"\b(h2s|sour|hydrogen sulphide|hydrogen sulfide)\b", ".", "H2S service", ["H2S Area Work"]),
 (r"\b(line ?break|break(ing)? (the |a )?(line|flange|containment)|open(ing)? (the |a )?(line|flange|pump|exchanger|vessel))", ".", "breaking containment", ["Line Breaking / Opening Process Equipment","Equipment Isolation"]),
 (r"\b(blind|blinding|spade|spading|spectacle)\b", ".", "positive isolation", ["Blinding / De-blinding"]),
 (r"\b(steam ?out|purg|gas ?free|degas)", ".", "purging / gas-freeing", ["Gas Freeing / Purging"]),
 (r"\b(nitrogen|inert|n2)\b", ".", "nitrogen atmosphere", ["Work in Nitrogen-Purged Equipment"]),
 (r"\b(crude|naphtha|gasoline|petrol|diesel|kerosene|jet|lpg|hydrocarbon|condensate|fuel)\b", ".", "hydrocarbon service", ["Handling Flammable Materials"]),
 (r"\b(reformate|benzene|aromatic|gasoline|petrol)\b", ".", "benzene-containing stream", ["Work Near Benzene-Containing Streams"]),
 (r"\b(catalyst)\b", ".", "catalyst handling", ["Catalyst Loading / Unloading","Dust-Generating Activity"]),
 (r"\b(sulphur|sulfur)\b", ".", "sulphur handling", ["Molten Sulphur Handling"]),
 (r"\b(amine|caustic)\b", ".", "amine / caustic", ["Amine / Caustic System Work"]),
 (r"\b(flare)\b", ".", "flare", ["Flare System Work"]),
 (r"\b(heater|furnace|burner|light[- ]?off)\b", ".", "fired heater", ["Fired Heater Light-off / Operation"]),
 (r"\b(dip|gaug)", r"\b(tank)\b", "tank gauging", ["Tank Gauging / Dipping"]),
 (r"\b(gantry|tanker|truck loading)\b", ".", "truck loading", ["Product Loading (Truck Gantry)"]),
 (r"\b(jetty|vessel loading|ship|marine|spm|barge)\b", ".", "marine loading", ["Marine Loading / Unloading (Jetty)","Working Near Water"]),
 (r"\b(hydro ?test|pressure test|pneumatic test|leak test)\b", ".", "pressure testing", ["Pressure Testing (Hydro / Pneumatic)"]),
 (r"\b(start[- ]?up|starting up|shutting down|commission|bring(ing)? (the )?(unit|plant|train) (up|down))", r"\b(unit|plant|train|column|heater)\b", "unit transient", ["Unit Start-up / Shutdown"]),
]

RESP = ["Permit Issuing Authority","Shift Supervisor","Tank Farm Supervisor","Dispatch Supervisor","Marine Terminal Supervisor","Inspection Engineer",
 "Utilities Supervisor","HV Authorised Person","Fire Safety Officer","Workshop Supervisor"]

ERP = ["Stop work, raise the alarm and go to the nearest upwind muster point.",
       "Refinery emergency numbers: [TO BE CONFIRMED BY REFINERY HSE]",
       "Fire & Rescue: [TO BE CONFIRMED]   Security: [TO BE CONFIRMED]   Medical: [TO BE CONFIRMED]"]

SYNONYMS = """
confined space|Confined Space Entry
enclosed space|Confined Space Entry
height|Working at Height
climb|Climbing
ladder|Ladder Use
scaffold|Scaffold Use
weld|Welding
torch|Cutting (Oxy-Acetylene)
grind|Grinding
hot work|Hot Work (General)
crane|Crane Operation
lifting|Rigging/Slinging Loads
hoist|Use of Chain Block
lockout|Lockout-Tagout Application
loto|Lockout-Tagout Application
isolat|Equipment Isolation
inspect|Visual Inspection
clean|Housekeeping/Cleaning
sample|Hydrocarbon Sampling
chemical|Handling Hazardous Chemicals
panel|Electrical Panel Access
forklift|Use of Forklift
trench|Working in Trench/Excavation
manual handling|Manual Handling of Loads
repair|Mechanical Maintenance/Repair
replace|Mechanical Maintenance/Repair
fire watch|Fire Watch Duty
gas test|Gas Testing/Atmospheric Monitoring
h2s|H2S Area Work
sour|H2S Area Work
blind|Blinding / De-blinding
spade|Blinding / De-blinding
purge|Gas Freeing / Purging
steam out|Gas Freeing / Purging
pig|Pigging Operations
flare|Flare System Work
catalyst|Catalyst Loading / Unloading
hot tap|Hot Tapping / Stoppling
benzene|Work Near Benzene-Containing Streams
dip|Tank Gauging / Dipping
tanker|Product Loading (Truck Gantry)
jetty|Marine Loading / Unloading (Jetty)
"""
