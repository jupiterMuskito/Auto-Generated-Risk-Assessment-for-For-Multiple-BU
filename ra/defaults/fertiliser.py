# ===== FERTILISER DEFAULT REGISTER SOURCE =====
# Self-contained: nothing in this file is shared with or imported by any other business unit.
# Used only to (re)create the built-in default workbook if it is missing. Day-to-day edits are made in the Excel workbook
# and uploaded through the app's Register admin page.
ID_PREFIX = "FER"
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

BU = dict(file="DANGOTE_FERTILISER_Master_Workbook_v1.xlsx", title="DANGOTE FERTILISER — RISK REGISTER (MASTER WORKBOOK)",
          unit="Dangote Fertiliser", company="DANGOTE FERTILISER LIMITED")

LOCATIONS = [
 ("Natural Gas Receiving and Metering Station","Process"),("Desulphurisation Unit","Process"),("Primary Reformer","Process"),
 ("Secondary Reformer","Process"),("CO Shift Conversion","Process"),("CO2 Removal Unit","Process"),("Methanation Unit","Process"),
 ("Syngas Compression","Process"),("Ammonia Synthesis Loop","Process"),("Ammonia Refrigeration Unit","Process"),
 ("Urea Synthesis (HP Section)","Process"),("Urea Recirculation and Evaporation","Process"),("Urea Granulation Unit","Process"),
 ("Urea Product Conveying","Process"),("Flare System","Process"),
 ("Ammonia Storage Tanks","Utility"),("Urea Bulk Storage Hall","Utility"),("Steam Generation / HRSG","Utility"),("Power Generation (GTG / STG)","Utility"),
 ("Cooling Water System","Utility"),("Demineralised Water Plant","Utility"),("Nitrogen / Instrument Air Plant","Utility"),
 ("Effluent Treatment Plant","Utility"),("Main Substation","Utility"),("Fire Water Pump House","Utility"),
 ("Bagging Plant","Site"),("Truck Loading Bay","Site"),("Jetty / Export Terminal","Site"),("Pipe Racks and Pipeways","Site"),("Plant Roads and Yard","Site"),
 ("Central Control Room","Building"),("Quality Control Laboratory","Building"),("Central Maintenance Workshop","Building"),
 ("Warehouse / Stores","Building"),("Fire Station","Building"),("Administrative Building","Building"),
 ("Other Area (User should Specify)","Other"),
]

EQUIPMENT_TYPES = ["Reformer Furnace","High Pressure Reactor / Converter","Pressure Vessel / Drum","Heat Exchanger / Waste Heat Boiler",
 "Process Compressor","Centrifugal Pump","Ammonia Refrigeration System","Refrigerated Ammonia Storage Tank","Urea HP Equipment (Reactor / Stripper / Condenser)",
 "Granulator and Fluid Bed Cooler","Bulk Conveyor / Bucket Elevator","Product Storage and Reclaimer","Bagging Machine","Natural Gas Metering Skid",
 "Process Piping and Pipeline","Flare Stack and KO Drum","Steam Boiler / HRSG","Gas Turbine / Generator","Cooling Tower",
 "High Voltage Electrical Equipment","Lifting Equipment","Mobile Plant","Laboratory Equipment","Scaffolding / Temporary Works",
 "Radioactive Source Equipment","Fire Safety Equipment","Workshop Machinery","Warehouse / Stores Equipment"]

PROC = "All process areas"
EQUIPMENT = [
 ("Primary Reformer Furnace","Reformer Furnace","Listed areas only",["Primary Reformer"]),
 ("Secondary Reformer","High Pressure Reactor / Converter","Listed areas only",["Secondary Reformer"]),
 ("Desulphuriser Vessels","High Pressure Reactor / Converter","Listed areas only",["Desulphurisation Unit"]),
 ("HT / LT Shift Converters","High Pressure Reactor / Converter","Listed areas only",["CO Shift Conversion"]),
 ("Methanator","High Pressure Reactor / Converter","Listed areas only",["Methanation Unit"]),
 ("Ammonia Converter","High Pressure Reactor / Converter","Listed areas only",["Ammonia Synthesis Loop"]),
 ("CO2 Absorber / Stripper","Pressure Vessel / Drum","Listed areas only",["CO2 Removal Unit"]),
 ("Separator / Knock-out Drum","Pressure Vessel / Drum",PROC,[]),
 ("Process Gas Waste Heat Boiler","Heat Exchanger / Waste Heat Boiler","Listed areas only",["Secondary Reformer","Ammonia Synthesis Loop"]),
 ("Shell & Tube Heat Exchanger","Heat Exchanger / Waste Heat Boiler",PROC,[]),
 ("Syngas Compressor","Process Compressor","Listed areas only",["Syngas Compression"]),
 ("Process Air Compressor","Process Compressor","Listed areas only",["Secondary Reformer","Syngas Compression"]),
 ("Ammonia Refrigeration Compressor","Process Compressor","Listed areas only",["Ammonia Refrigeration Unit"]),
 ("CO2 Compressor","Process Compressor","Listed areas only",["Urea Synthesis (HP Section)"]),
 ("Process Pump","Centrifugal Pump",PROC,[]),
 ("HP Ammonia / Carbamate Pump","Centrifugal Pump","Listed areas only",["Urea Synthesis (HP Section)","Urea Recirculation and Evaporation"]),
 ("Ammonia Chiller / Flash Drums","Ammonia Refrigeration System","Listed areas only",["Ammonia Refrigeration Unit","Ammonia Synthesis Loop"]),
 ("Refrigerated Ammonia Tank","Refrigerated Ammonia Storage Tank","Listed areas only",["Ammonia Storage Tanks"]),
 ("Urea Reactor","Urea HP Equipment (Reactor / Stripper / Condenser)","Listed areas only",["Urea Synthesis (HP Section)"]),
 ("HP Stripper","Urea HP Equipment (Reactor / Stripper / Condenser)","Listed areas only",["Urea Synthesis (HP Section)"]),
 ("HP Carbamate Condenser","Urea HP Equipment (Reactor / Stripper / Condenser)","Listed areas only",["Urea Synthesis (HP Section)"]),
 ("Urea Granulator","Granulator and Fluid Bed Cooler","Listed areas only",["Urea Granulation Unit"]),
 ("Fluid Bed Cooler","Granulator and Fluid Bed Cooler","Listed areas only",["Urea Granulation Unit"]),
 ("Granulation Scrubber","Pressure Vessel / Drum","Listed areas only",["Urea Granulation Unit"]),
 ("Product Belt Conveyor","Bulk Conveyor / Bucket Elevator","Listed areas only",["Urea Product Conveying","Urea Bulk Storage Hall","Bagging Plant","Jetty / Export Terminal","Urea Granulation Unit"]),
 ("Bucket Elevator","Bulk Conveyor / Bucket Elevator","Listed areas only",["Urea Granulation Unit","Urea Product Conveying"]),
 ("Portal Scraper Reclaimer","Product Storage and Reclaimer","Listed areas only",["Urea Bulk Storage Hall"]),
 ("Stacker / Tripper","Product Storage and Reclaimer","Listed areas only",["Urea Bulk Storage Hall"]),
 ("Bagging and Stitching Line","Bagging Machine","Listed areas only",["Bagging Plant"]),
 ("Ship Loader","Bulk Conveyor / Bucket Elevator","Listed areas only",["Jetty / Export Terminal"]),
 ("Gas Metering Skid / Pressure Reduction","Natural Gas Metering Skid","Listed areas only",["Natural Gas Receiving and Metering Station"]),
 ("Process Piping","Process Piping and Pipeline","All areas",[]),
 ("Flare Stack","Flare Stack and KO Drum","Listed areas only",["Flare System"]),
 ("Auxiliary Boiler / HRSG","Steam Boiler / HRSG","Listed areas only",["Steam Generation / HRSG","Power Generation (GTG / STG)"]),
 ("Gas Turbine Generator","Gas Turbine / Generator","Listed areas only",["Power Generation (GTG / STG)"]),
 ("Cooling Tower Cell","Cooling Tower","Listed areas only",["Cooling Water System"]),
 ("Switchgear / MCC","High Voltage Electrical Equipment","All areas",[]),
 ("Power Transformer","High Voltage Electrical Equipment","Listed areas only",["Main Substation","Power Generation (GTG / STG)"]),
 ("Overhead / Gantry Crane","Lifting Equipment","Listed areas only",["Central Maintenance Workshop","Syngas Compression","Power Generation (GTG / STG)","Warehouse / Stores"]),
 ("Mobile Crane","Lifting Equipment","All areas",[]),
 ("Front-end Loader / Bulldozer","Mobile Plant","Listed areas only",["Urea Bulk Storage Hall","Plant Roads and Yard"]),
 ("Forklift","Mobile Plant","Listed areas only",["Bagging Plant","Warehouse / Stores","Central Maintenance Workshop"]),
 ("Laboratory Analysers and Fume Hoods","Laboratory Equipment","Listed areas only",["Quality Control Laboratory"]),
 ("Scaffolding (Temporary Works)","Scaffolding / Temporary Works","All areas",[]),
 ("Nucleonic Level Gauge","Radioactive Source Equipment","Listed areas only",["Urea Synthesis (HP Section)","Urea Granulation Unit"]),
 ("Fire Water Pump","Fire Safety Equipment","Listed areas only",["Fire Water Pump House"]),
 ("Ammonia Water Curtain / Deluge","Fire Safety Equipment","Listed areas only",["Ammonia Storage Tanks","Ammonia Refrigeration Unit"]),
 ("Workshop Machine Tools","Workshop Machinery","Listed areas only",["Central Maintenance Workshop"]),
 ("Warehouse Racking","Warehouse / Stores Equipment","Listed areas only",["Warehouse / Stores"]),
]

BU_TAGS = [
 ("Process Operations", ["Ammonia Handling / Transfer","Ammonia Line Draining / Breaking","Urea HP Section Work","Carbamate Line Clearing / Flushing",
   "Line Breaking / Opening Process Equipment","Gas Freeing / Purging","Work in Nitrogen-Purged Equipment","Reformer Furnace Operation / Inspection",
   "Catalyst Loading / Unloading","Syngas / Hydrogen System Work","Natural Gas Pipeline / Metering Work","CO2 Removal / Amine System Work",
   "Steam System Work","Unit Start-up / Shutdown","Pressure Testing (Hydro / Pneumatic)","Urea-Formaldehyde (UF) Additive Handling"]),
 ("Product Handling & Dispatch", ["Granulator / Fluid Bed Operation","Urea Bulk Storage & Reclaim Work","Bagging / Bag Stacking","Product Dispatch Loading (Truck / Ship)"]),
]

BU_AH = """
Ammonia Handling / Transfer|L|Toxic ammonia release causing severe respiratory injury or death|E|Ammonia detectors with alarm; escape respirator carried in ammonia areas; work upwind; emergency showers and eyewash at hand; evacuate crosswind on alarm|M|HSE Officer|Ammonia escape respirator;Chemical goggles;Chemical-resistant gloves;NH3 personal monitor
Ammonia Handling / Transfer|J|Cold burns (frostbite) from liquid ammonia contact|E|Closed transfer; cryogenic-rated gloves and face shield for any liquid service; never touch frosted lines|M|Process Operator|Cold-insulated gloves;Face shield;Chemical suit
Ammonia Line Draining / Breaking|E|Liquid ammonia flashing to vapour when opening or draining lines|E|Line-break permit; depressurise, drain to closed system, and purge with nitrogen; confirm at bleed; full ammonia suit and SCBA for first break; water curtain or hose ready|M|Permit Issuing Authority|Ammonia-protective suit;SCBA;Cold-insulated gloves
Urea HP Section Work|E|High-pressure release of hot carbamate and ammonia at around 140 bar|E|Full isolation, depressurisation, and flushing of HP loop before work; leak detection on HP equipment; never tighten flanges on a pressurised HP system|H|Process Operator|Chemical suit;Face shield;Ammonia escape respirator;Heat-resistant gauntlets
Urea HP Section Work|E|Failure of corroded HP equipment due to loss of passivation air|E|Passivation oxygen monitored; leak detection system on reactor and stripper liners; inspection programme for HP equipment|H|Inspection Engineer|Ammonia escape respirator
Carbamate Line Clearing / Flushing|E|Blockage release spraying hot carbamate and ammonia|E|Clear using steam or condensate flushing from a remote point; never hammer or heat blocked carbamate lines locally; face shield and chemical suit|M|Process Operator|Chemical suit;Face shield;Ammonia escape respirator
Line Breaking / Opening Process Equipment|E|Release of syngas, ammonia, or process fluid when breaking containment|E|Line-break permit; positive isolation verified; depressurise, drain, purge and confirm at bleed; loosen far-side bolts first; standby person|M|Permit Issuing Authority|Chemical goggles;Face shield;Chemical-resistant gloves;Multi-gas detector
Gas Freeing / Purging|E|Flammable syngas or hydrogen mixture formed during purging|E|Approved purge procedure with end-point gas analysis; vent to flare or safe location; no hot work until gas-free certificate|M|Process Operator|Multi-gas detector;Flame-resistant (FR) coveralls
Work in Nitrogen-Purged Equipment|L|Instant asphyxiation from nitrogen atmosphere at openings|E|Nitrogen warning barriers at all openings; no head or body inside an opening without breathing air; continuous O2 monitoring; specialist inert-entry contractor only|H|HSE Officer / Confined Space Attendant|SCBA;Airline / air-fed respirator;Multi-gas detector
Reformer Furnace Operation / Inspection|E|Firebox explosion on light-off or tube rupture|E|Burner management permissives and purge; tube wall temperature monitoring; light burners one at a time; never relight without re-purge|H|Process Operator|Flame-resistant (FR) coveralls;Face shield;Heat-resistant gauntlets
Reformer Furnace Operation / Inspection|J|Radiant heat and flame exposure at peepholes|H|Shaded viewing; stand to the side when opening ports; verify negative draught; heat stress management|M|Process Operator|Face shield;Heat-resistant gauntlets;Flame-resistant (FR) coveralls
Catalyst Loading / Unloading|J|Exposure to catalyst dust and pyrophoric reduced catalyst (nickel, iron, copper)|E|Unload reduced catalyst under nitrogen or after controlled oxidation; specialist contractor; dust extraction; P3 or air-fed RPE; keep spent catalyst wet or inerted|H|HSE Officer|Airline / air-fed respirator;Disposable coveralls;Chemical goggles
Catalyst Loading / Unloading|L|Asphyxiation or engulfment inside reactor during catalyst work|E|Inert entry only with breathing air; no entry while catalyst is flowing; standby rescue team|H|HSE Officer / Confined Space Attendant|Airline / air-fed respirator;Full body harness;Retrieval winch and davit
Syngas / Hydrogen System Work|E|Hydrogen or syngas leak causing invisible flame, explosion, or CO poisoning|E|Fixed hydrogen, CO and flame detection; flange management; personal CO monitor; approach suspected leaks with thermal camera or broom, never by hand|H|Process Operator|Flame-resistant (FR) coveralls;CO detector;Face shield
Natural Gas Pipeline / Metering Work|E|Natural gas release and fire at the metering station|E|Isolation and depressurisation by gas operator; gas detection; hazardous area-rated tools; no ignition sources; pipeline owner permit where applicable|H|Process Operator|Flame-resistant (FR) coveralls;Multi-gas detector
CO2 Removal / Amine System Work|E|Chemical burns from amine or carbonate solution and CO2 asphyxiation|E|Drain and flush before opening; chemical PPE; O2 and CO2 monitoring in low areas; eyewash and shower at hand|M|Process Operator|Chemical suit;Face shield;Chemical-resistant gloves;Multi-gas detector
Steam System Work|E|Scalding from steam or condensate release and water hammer|E|Isolate, depressurise, and drain; open drains slowly; never crack a flange on a live steam line|M|Utilities Supervisor|Heat-resistant gauntlets;Face shield;Coveralls
Unit Start-up / Shutdown|J|Process upset, overpressure, or ammonia release during transient operations|E|Approved start-up/shutdown procedure with step sign-off; pre-start-up safety review; non-essential personnel cleared; radio communication with control room|M|Shift Supervisor|Flame-resistant (FR) coveralls;Two-way radio;Ammonia escape respirator
Pressure Testing (Hydro / Pneumatic)|E|Catastrophic failure releasing stored energy during pressure test|E|Test procedure with calculated test pressure and relief set; exclusion zone during pressurisation; pneumatic tests only with engineering approval|M|Inspection Engineer|Face shield;Hard hat;Safety boots
Urea-Formaldehyde (UF) Additive Handling|J|Formaldehyde vapour exposure (sensitiser and carcinogen)|H|Closed transfer and dosing; ventilation at the dosing point; organic vapour RPE for line breaks; eyewash and shower nearby|M|Process Operator|Organic vapour respirator;Chemical-resistant gloves;Chemical goggles
Granulator / Fluid Bed Operation|E|Contact with hot urea melt and granules|H|Heat-resistant PPE; isolate melt supply before opening spray headers; allow cool-down before entry|M|Process Operator|Heat-resistant gauntlets;Face shield;Coveralls
Granulator / Fluid Bed Operation|J|Urea dust and ammonia exposure at granulator and scrubber|M|Scrubber and dust extraction operating; RPE in dusty areas; ammonia monitoring|L|Process Operator|Dust mask (P2);Sealed dust goggles;NH3 personal monitor
Urea Bulk Storage & Reclaim Work|L|Engulfment by collapsing urea pile or caked face|E|Never stand on or below a steep or caked face; break cake mechanically from a safe position; no entry on the pile without permit, harness and lifeline|H|Area Supervisor|Full body harness;Retrieval line;Dust mask (P2)
Urea Bulk Storage & Reclaim Work|E|Struck by reclaimer, stacker, or loader in the storage hall|E|Exclusion zones around moving machines; radio contact with operators; pedestrian access only with machines stopped or under traffic control|M|Area Supervisor|Hi-vis vest;Two-way radio
Bagging / Bag Stacking|E|Entanglement or crush at bagging, stitching, and stacking machines|E|Interlocked guarding; isolate before clearing jams; never reach into a running machine|M|Packing Plant Supervisor|Close-fitting clothing;Safety gloves (general);Ear plugs
Bagging / Bag Stacking|J|Musculoskeletal injury from manual bag handling and falling bags|M|Mechanical handling of bags; stack within height limits; rotate personnel|L|Packing Plant Supervisor|Safety gloves (general);Safety boots;Dust mask (P2)
Product Dispatch Loading (Truck / Ship)|L|Struck by trucks or falling from truck beds during loading|H|Traffic management with marked pedestrian routes; drivers in safe zone; no climbing on loads without fall protection|M|Dispatch Supervisor|Hi-vis vest;Hard hat;Safety boots
Product Dispatch Loading (Truck / Ship)|L|Fall into water or hold during ship loading|E|Edge protection and lifejackets on the jetty; no access to the hold during loading; ship loader exclusion zone|H|Marine Terminal Supervisor|Buoyancy aid;Hi-vis vest
"""

EH = """
Reformer Furnace|E|Firebox explosion or reformer tube rupture|E|Burner management with flame failure protection; tube wall temperature surveys; emergency shutdown tested|H|Process Operator|Flame-resistant (FR) coveralls;Face shield|Any|Operational
Reformer Furnace|L|Confined space entry into firebox or tunnels with residual heat and refractory dust|E|Positive fuel isolation by blinding; cool-down verified; confined space permit and gas test; refractory dust RPE|M|HSE Officer / Confined Space Attendant|P3 respirator;Full body harness;Multi-gas detector|Any|Shutdown/Isolated
Reformer Furnace|L|Fall from height on furnace platforms, penthouse, and pigtails area|H|Guarded platforms; harness outside protection; heat stress controls|M|Area Supervisor|Full body harness;Hard hat|Any|Any
High Pressure Reactor / Converter|E|High-pressure hydrogen or syngas leak causing fire, explosion, or toxic exposure|E|Flange management; hydrogen and CO detection; flame detection; isolate before any intervention|H|Process Operator|Flame-resistant (FR) coveralls;CO detector|Any|Operational
High Pressure Reactor / Converter|L|Inert atmosphere and pyrophoric catalyst during entry|E|Inert entry by specialist contractor with breathing air; nitrogen warning barriers; standby rescue|H|HSE Officer / Confined Space Attendant|Airline / air-fed respirator;Full body harness|Any|Shutdown/Isolated
Pressure Vessel / Drum|E|Overpressure and vessel rupture|E|Relief valves inspected and certified; never isolate a relief device without authorisation; alarms maintained|H|Inspection Engineer|Hard hat;Face shield|Any|Any
Pressure Vessel / Drum|L|Confined space hazards on vessel entry (toxic, inert, flammable)|E|Positive isolation and blinding; purge and gas-free certificate; continuous monitoring; standby and rescue plan|M|HSE Officer / Confined Space Attendant|Multi-gas detector;SCBA;Full body harness|Any|Shutdown/Isolated
Heat Exchanger / Waste Heat Boiler|E|Steam or process gas release from tube failure|E|Water chemistry control; inspection programme; isolate and depressurise both sides before opening|H|Utilities Supervisor|Heat-resistant gauntlets;Face shield|Any|Any
Heat Exchanger / Waste Heat Boiler|E|Tube bundle drop during extraction|E|Engineered bundle extractor; lift plan; exclusion zone|M|Rigging Supervisor|Hard hat;Safety boots|Any|Shutdown/Isolated
Process Compressor|E|Gas release and fire from seals or piping vibration failure|E|Seal gas and vibration monitoring; trips tested; gas detection in compressor house|H|Process Operator|Flame-resistant (FR) coveralls;Ear plugs plus ear muffs|Running|Operational
Process Compressor|E|Unexpected rotation or pressurisation during overhaul|E|Isolate, depressurise, purge; lock turning gear and drivers; verify zero speed and pressure|M|Mechanical Maintenance Lead|Lock and tag kit;Face shield|Any|Shutdown/Isolated
Centrifugal Pump|E|Seal failure releasing ammonia, carbamate, or hot process fluid|E|Seal monitoring; remote isolation valves; ammonia detection at pump rows; respond only with isolation|H|Process Operator|Ammonia escape respirator;Face shield;Chemical-resistant gloves|Running|Operational
Centrifugal Pump|E|Pump started or pressurised during maintenance|E|Electrical LOTO and process isolation with vent and drain verified; try-start test|M|Maintenance Supervisor|Lock and tag kit;Safety gloves (general)|Any|Shutdown/Isolated
Ammonia Refrigeration System|E|Large liquid ammonia release forming a toxic cloud|E|Ammonia detection and alarms; emergency isolation valves; water curtain; escape respirators and wind socks; emergency response plan drilled|H|Process Operator|Ammonia escape respirator;NH3 personal monitor|Any|Any
Ammonia Refrigeration System|J|Frostbite from cold ammonia lines and drains|H|Never touch frosted lines; cryogenic gloves and face shield for draining|M|Process Operator|Cold-insulated gloves;Face shield|Any|Any
Refrigerated Ammonia Storage Tank|E|Tank overpressure, roll-over, or containment failure releasing ammonia|E|Pressure control and relief systems tested; boil-off compressors maintained; level and temperature monitoring; restricted access|H|Process Operator|Ammonia escape respirator;NH3 personal monitor|Any|Any
Refrigerated Ammonia Storage Tank|L|Fall from tank roof or stairway|H|Guarded stairways and roof walkways; harness for edge work|M|Area Supervisor|Full body harness;Hard hat|Any|Any
Urea HP Equipment (Reactor / Stripper / Condenser)|E|HP equipment rupture or liner leak releasing hot carbamate and ammonia|E|Liner leak detection system monitored; passivation air maintained; HP equipment inspection programme; full depressurisation and flushing before work|H|Inspection Engineer|Chemical suit;Ammonia escape respirator;Face shield|Any|Any
Urea HP Equipment (Reactor / Stripper / Condenser)|L|Confined space entry into reactor with ammonia residue and heat|E|Flush, depressurise, and ventilate; positive isolation; continuous NH3 and O2 monitoring; standby and rescue|M|HSE Officer / Confined Space Attendant|SCBA;Full body harness;NH3 personal monitor|Any|Shutdown/Isolated
Granulator and Fluid Bed Cooler|E|Contact with moving parts or hot product during entry or cleaning|E|LOTO on fans, scrapers, and melt supply; cool-down verified; confined space permit for internal work|M|Mechanical Maintenance Lead|Lock and tag kit;Heat-resistant gauntlets;Dust mask (P2)|Any|Shutdown/Isolated
Granulator and Fluid Bed Cooler|J|Dust and ammonia exposure around the granulator|M|Scrubber operating; RPE in dusty areas; ammonia monitoring|L|Process Operator|Dust mask (P2);NH3 personal monitor|Any|Operational
Bulk Conveyor / Bucket Elevator|E|Entanglement at belt nip points, idlers, and drive drums|E|Fixed nip guards; pull-cord tested; never clear material on a running belt|M|Area Supervisor|Close-fitting clothing;Safety gloves (general)|Any|Operational
Bulk Conveyor / Bucket Elevator|E|Stored belt tension or counterweight release during maintenance|E|LOTO on drive; chock or land counterweight before releasing tension|M|Mechanical Maintenance Lead|Hard hat;Safety gloves (general)|Any|Shutdown/Isolated
Product Storage and Reclaimer|E|Struck by or caught in reclaimer, scraper, or stacker|E|Exclusion zones; interlocked access; LOTO before maintenance; radio contact with operator|M|Area Supervisor|Hi-vis vest;Two-way radio|Any|Any
Product Storage and Reclaimer|L|Engulfment by collapsing product face|E|No access beneath steep or caked faces; mechanical breaking from a safe position; permit for pile access|H|Area Supervisor|Full body harness;Retrieval line|Any|Any
Bagging Machine|E|Entanglement or crush at bagging, stitching, and palletising mechanisms|E|Interlocked guards; isolate before clearing jams; reset only from outside the guarded area|M|Packing Plant Supervisor|Close-fitting clothing;Ear plugs|Any|Any
Natural Gas Metering Skid|E|Natural gas release and fire|E|Gas detection and emergency shutdown valves tested; hazardous area-rated equipment; isolation and depressurisation before work|H|Process Operator|Flame-resistant (FR) coveralls;Multi-gas detector|Any|Any
Process Piping and Pipeline|E|Loss of containment from corroded or damaged piping|E|Risk-based inspection; leaks isolated and reported; temporary clamps only under engineering approval|H|Inspection Engineer|Ammonia escape respirator;Flame-resistant (FR) coveralls|Any|Any
Process Piping and Pipeline|E|Trapped pressure between closed valves|H|Use bleed points to depressurise isolated sections; verify zero before opening|M|Process Operator|Face shield;Chemical-resistant gloves|Any|Shutdown/Isolated
Flare Stack and KO Drum|L|Thermal radiation and toxic gas near flare|E|Restricted zone; flare-safe work windows; control room clearance before entry|H|Shift Supervisor|Flame-resistant (FR) coveralls;Ammonia escape respirator|Any|Operational
Steam Boiler / HRSG|E|Boiler explosion or tube failure|E|Water level and burner management trips tested; statutory inspection current; water chemistry control|H|Utilities Supervisor|Face shield;Heat-resistant gauntlets|Any|Operational
Gas Turbine / Generator|E|Fuel gas leak and fire in turbine enclosure|E|Enclosure gas detection and suppression tested; entry only with suppression inhibited and permit|H|Utilities Supervisor|Ear plugs plus ear muffs;Flame-resistant (FR) coveralls|Any|Any
Gas Turbine / Generator|E|Back-feed or unexpected start during maintenance|E|Electrical and mechanical isolation; turning gear locked; verify zero voltage|M|Electrical Supervisor|Lock and tag kit;Voltage tester|Any|Shutdown/Isolated
Cooling Tower|E|Fan blade contact or unexpected start|E|LOTO on fan drive and lock rotor; guards refitted before restart|M|Mechanical Maintenance Lead|Lock and tag kit|Any|Shutdown/Isolated
Cooling Tower|J|Legionella and treatment chemical exposure|H|Water treatment programme; RPE near drift; chemical PPE for dosing|M|HSE Officer|P3 respirator;Chemical goggles|Any|Any
High Voltage Electrical Equipment|E|Electrocution from contact with high voltage conductors|E|Isolate, lock, prove dead, and earth before work; authorised HV person and permit|H|HV Authorised Person|Arc-rated suit and hood;Insulated electrical gloves;Voltage tester|Any|Any
High Voltage Electrical Equipment|E|Arc flash during switching or racking|E|Arc flash study and labelling; remote racking; arc-rated PPE to rating|H|Electrical Supervisor|Arc-rated suit and hood;Ear plugs|Any|Any
Lifting Equipment|E|Load drop from equipment failure or overload|E|Thorough examination current; pre-use checks; SWL never exceeded; lift plan|M|Lifting Engineer|Hard hat;Safety boots|Any|Any
Lifting Equipment|L|Crane contact with live process plant or pipe racks|E|Lift plan with exclusion zones; banksman; isolate plant under the lift path where required|M|Lifting Engineer|Hard hat;Hi-vis vest|Any|Any
Mobile Plant|J|Collision with pedestrians or plant|E|Traffic management; speed limits; reversing aids; banksman in congested areas|M|Plant/Fleet Supervisor|Hi-vis vest;Hard hat|Any|Any
Mobile Plant|E|Ignition source from vehicles entering classified process areas|E|Vehicle entry permit for process areas; spark arrestors; gas test before entry|M|Plant/Fleet Supervisor|Hi-vis vest|Any|Any
Laboratory Equipment|J|Exposure to ammonia, urea solutions, and reagents|H|Fume hoods; closed sample handling; eyewash and shower tested|M|Laboratory Technician|Chemical goggles;Nitrile gloves;Lab coat|Any|Any
Scaffolding / Temporary Works|E|Scaffold collapse or unauthorised modification|E|Competent scaffolders only; tag system; load limits; re-inspection after modification|H|Scaffold Supervisor|Hard hat;Full body harness|Any|Any
Radioactive Source Equipment|E|Ionising radiation exposure from source with open or damaged shutter|E|Shutter closed and locked before nearby work, verified with survey meter; licensed persons only; source register|H|Radiation Protection Supervisor|Dosimeter badge;Radiation survey meter|Any|Any
Fire Safety Equipment|E|Fire or ammonia water curtain impaired when needed|E|Impairment permit and compensatory measures; scheduled testing; restore and verify after work|M|Fire Safety Officer|Task-appropriate PPE|Any|Any
Workshop Machinery|E|Entanglement in lathes, mills, and drills|E|Guards and interlocks; no gloves or loose clothing at rotating machinery; trained operators|M|Workshop Supervisor|Safety glasses;Close-fitting clothing|Any|Any
Warehouse / Stores Equipment|E|Racking collapse or falling stock|H|Load limits displayed; racking inspection; no climbing on racking|M|Stores Supervisor|Hard hat;Safety boots|Any|Any
"""

PRESETS = [
 ("Ammonia pump seal replacement","Mechanical","Replace seal on an ammonia pump after draining, nitrogen purging and isolation",
  ["Ammonia Line Draining / Breaking","Line Breaking / Opening Process Equipment","Equipment Isolation","Lockout-Tagout Application","Mechanical Maintenance/Repair","Ammonia Handling / Transfer"],
  "Centrifugal Pump","Static","Shutdown/Isolated","Process Pump",""),
 ("Reformer tube inspection","Inspection","Inspect reformer tubes through peepholes and survey tube wall temperatures",
  ["Reformer Furnace Operation / Inspection","Working in Extreme Heat","Thermographic Survey","Working on Elevated Platform"],
  "Reformer Furnace","Static","Operational","Primary Reformer Furnace","Primary Reformer"),
 ("Converter catalyst change-out","Turnaround","Unload spent catalyst and reload fresh catalyst in a shift converter",
  ["Catalyst Loading / Unloading","Work in Nitrogen-Purged Equipment","Confined Space Entry","Rigging/Slinging Loads","Dust-Generating Activity"],
  "High Pressure Reactor / Converter","Static","Shutdown/Isolated","HT / LT Shift Converters","CO Shift Conversion"),
 ("Carbamate line flushing","Operations","Flush a blocked carbamate line with steam condensate from a remote point",
  ["Carbamate Line Clearing / Flushing","Urea HP Section Work","Steam System Work","Ammonia Handling / Transfer"],
  "Urea HP Equipment (Reactor / Stripper / Condenser)","Static","Operational","HP Carbamate Condenser","Urea Synthesis (HP Section)"),
 ("Urea reactor internal inspection","Inspection","Enter the urea reactor for liner inspection after flushing and isolation",
  ["Confined Space Entry","Urea HP Section Work","Equipment Isolation","Gas Testing/Atmospheric Monitoring","Visual Inspection","Non-Destructive Testing (NDT)"],
  "Urea HP Equipment (Reactor / Stripper / Condenser)","Static","Shutdown/Isolated","Urea Reactor","Urea Synthesis (HP Section)"),
 ("Granulator cleaning","Operations","Clean caked urea from granulator internals during shutdown",
  ["Granulator / Fluid Bed Operation","Confined Space Entry","Housekeeping/Cleaning","Lockout-Tagout Application","Dust-Generating Activity"],
  "Granulator and Fluid Bed Cooler","Static","Shutdown/Isolated","Urea Granulator","Urea Granulation Unit"),
 ("Breaking caked urea in storage","Operations","Break and reclaim caked urea face in the bulk storage hall",
  ["Urea Bulk Storage & Reclaim Work","Operating Mobile Equipment","Dust-Generating Activity"],
  "Product Storage and Reclaimer","Static","Operational","Portal Scraper Reclaimer","Urea Bulk Storage Hall"),
 ("Bagging line jam clearing","Operations","Clear a bag jam on the bagging and stitching line",
  ["Bagging / Bag Stacking","Lockout-Tagout Application","Working Near Moving Machinery"],
  "Bagging Machine","Static","Shutdown/Isolated","Bagging and Stitching Line","Bagging Plant"),
 ("Truck loading of bagged urea","Dispatch","Load bagged urea onto trucks at the loading bay",
  ["Product Dispatch Loading (Truck / Ship)","Use of Forklift","Traffic Control/Flagging","Manual Handling of Loads"],
  "Mobile Plant","Static","Operational","Forklift","Bagging Plant"),
 ("Conveyor belt repair","Mechanical","Repair damaged product conveyor belt and replace idlers",
  ["Mechanical Maintenance/Repair","Lockout-Tagout Application","Hand Tool Use","Manual Handling of Loads"],
  "Bulk Conveyor / Bucket Elevator","Static","Shutdown/Isolated","Product Belt Conveyor",""),
 ("HV switching","Electrical","Switch and rack out a breaker for maintenance isolation",
  ["Electrical Panel Access","De-energized Electrical Work","Lockout-Tagout Application"],
  "High Voltage Electrical Equipment","Static","Operational","Switchgear / MCC","Main Substation"),
]

TOOLS = """
blind|Process Isolation|Line Breaking / Opening Process Equipment
flange spreader|Process Isolation|Line Breaking / Opening Process Equipment
nh3 monitor|Test & Measurement|Ammonia Handling / Transfer
ammonia detector|Test & Measurement|Ammonia Handling / Transfer
breathing apparatus|Access & Height|Confined Space Entry
scba|Access & Height|Confined Space Entry
loader|Mobile Plant|Operating Mobile Equipment
bulldozer|Mobile Plant|Operating Mobile Equipment
"""

RULES = [
 (r"\b(enter|entering|entry|inside|internal|go into|get into|climb into|within)", r"\b(reactor|converter|vessel|drum|tank|furnace|reformer|stripper|absorber|granulator|boiler|silo|hopper|scrubber)\b", "entry into a vessel", ["Confined Space Entry","Gas Testing/Atmospheric Monitoring","Lockout-Tagout Application"]),
 (r"\b(ammonia|nh3)\b", ".", "ammonia service", ["Ammonia Handling / Transfer"]),
 (r"\b(ammonia|nh3)\b", r"\b(drain|break|open|flange|line|seal|pump)", "ammonia containment break", ["Ammonia Line Draining / Breaking"]),
 (r"\b(carbamate)\b", ".", "carbamate", ["Carbamate Line Clearing / Flushing","Urea HP Section Work"]),
 (r"\b(urea reactor|hp stripper|hp section|high pressure|hp loop|carbamate condenser)\b", ".", "urea HP section", ["Urea HP Section Work"]),
 (r"\b(line ?break|break(ing)? (the |a )?(line|flange|containment)|open(ing)? (the |a )?(line|flange|pump|exchanger|vessel))", ".", "breaking containment", ["Line Breaking / Opening Process Equipment","Equipment Isolation"]),
 (r"\b(purg|gas ?free|steam ?out)", ".", "purging", ["Gas Freeing / Purging"]),
 (r"\b(nitrogen|inert|n2)\b", ".", "nitrogen atmosphere", ["Work in Nitrogen-Purged Equipment"]),
 (r"\b(reformer|furnace|burner|peephole|tube wall)\b", ".", "reformer furnace", ["Reformer Furnace Operation / Inspection"]),
 (r"\b(catalyst)\b", ".", "catalyst handling", ["Catalyst Loading / Unloading","Dust-Generating Activity"]),
 (r"\b(syngas|synthesis gas|hydrogen|h2)\b", ".", "syngas / hydrogen", ["Syngas / Hydrogen System Work"]),
 (r"\b(natural gas|metering|gas skid|pressure reduction)\b", ".", "natural gas", ["Natural Gas Pipeline / Metering Work"]),
 (r"\b(amine|benfield|carbonate|co2 removal|absorber)\b", ".", "CO2 removal", ["CO2 Removal / Amine System Work"]),
 (r"\b(formaldehyde|uf85|uf-85|uf additive)\b", ".", "UF additive", ["Urea-Formaldehyde (UF) Additive Handling"]),
 (r"\b(granulat|fluid bed|prill)", ".", "granulation", ["Granulator / Fluid Bed Operation"]),
 (r"\b(storage hall|reclaim|stockpile|caked|pile)\b", ".", "bulk storage", ["Urea Bulk Storage & Reclaim Work"]),
 (r"\b(bag|bagging|stitch|palleti)", ".", "bagging", ["Bagging / Bag Stacking"]),
 (r"\b(dispatch|truck loading|ship loading|ship loader|jetty)\b", ".", "dispatch", ["Product Dispatch Loading (Truck / Ship)"]),
 (r"\b(hydro ?test|pressure test|pneumatic test|leak test)\b", ".", "pressure testing", ["Pressure Testing (Hydro / Pneumatic)"]),
 (r"\b(start[- ]?up|starting up|shutting down|commission|bring(ing)? (the )?(unit|plant|train) (up|down))", r"\b(unit|plant|train|loop|reformer)\b", "unit transient", ["Unit Start-up / Shutdown"]),
]

RESP = ["Permit Issuing Authority","Shift Supervisor","Packing Plant Supervisor","Dispatch Supervisor","Marine Terminal Supervisor","Inspection Engineer",
 "Utilities Supervisor","HV Authorised Person","Fire Safety Officer","Workshop Supervisor"]

ERP = ["Stop work, raise the alarm and move crosswind / upwind to the nearest ammonia-safe muster point.",
       "Fertiliser plant emergency numbers: [TO BE CONFIRMED BY FERTILISER HSE]",
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
sample|Sampling
chemical|Handling Hazardous Chemicals
panel|Electrical Panel Access
forklift|Use of Forklift
trench|Working in Trench/Excavation
manual handling|Manual Handling of Loads
repair|Mechanical Maintenance/Repair
replace|Mechanical Maintenance/Repair
fire watch|Fire Watch Duty
gas test|Gas Testing/Atmospheric Monitoring
ammonia|Ammonia Handling / Transfer
nh3|Ammonia Handling / Transfer
carbamate|Carbamate Line Clearing / Flushing
urea reactor|Urea HP Section Work
purge|Gas Freeing / Purging
catalyst|Catalyst Loading / Unloading
reformer|Reformer Furnace Operation / Inspection
syngas|Syngas / Hydrogen System Work
granulator|Granulator / Fluid Bed Operation
bagging|Bagging / Bag Stacking
caked|Urea Bulk Storage & Reclaim Work
formaldehyde|Urea-Formaldehyde (UF) Additive Handling
"""
