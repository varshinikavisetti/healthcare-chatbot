# healthcare_data.py
# Expanded disease dictionary for Healthcare FAQ Chatbot
# NOTE: All text here is for demo/educational purposes only.
# Do NOT treat this as medical advice. Consult a doctor for diagnosis/treatment.

DISEASE_DB = {
    "diabetes": {
        "aliases": ["diabetes", "diabetes mellitus", "blood sugar"],
        "symptoms": "frequent urination, increased thirst, unexplained weight loss, fatigue, blurred vision, slow healing of wounds, numbness in feet",
        "medicines": "Common treatments include lifestyle changes and medicines such as metformin or insulin (prescription required).",
        "precautions": "Maintain blood sugar monitoring, diet control, exercise; follow doctor instructions.",
        "serious": True,
        "specialist": "Endocrinologist"
    },
   "viral infections": {
    "aliases": ["virus", "viral infection", "common viral fever", "viral"],
    "symptoms": "fever, fatigue, cough, sore throat, runny nose, muscle aches; may vary depending on the virus",
    "medicines": "Mostly supportive care: rest, hydration, and paracetamol for fever. Antivirals may be prescribed by a doctor for specific viral infections.",
    "precautions": "Maintain good hygiene, rest, drink fluids, and avoid close contact with others while symptomatic.",
    "serious": False,
    "specialist": "General Physician"
},

    "influenza": {
        "aliases": ["flu", "influenza"],
        "symptoms": "fever, chills, cough, sore throat, runny nose, muscle aches, fatigue",
        "medicines": "Rest, fluids, paracetamol/ibuprofen for fever. Antivirals (prescription) for high-risk patients.",
        "precautions": "Get seasonal vaccine if eligible; rest and hydrate.",
        "serious": False,
        "specialist": "General Physician"
    },
    "hypertension": {
        "aliases": ["high blood pressure", "hypertension"],
        "symptoms": "often no symptoms but may cause headaches, chest pain, vision problems in severe cases",
        "medicines": "Antihypertensives (e.g., ACE inhibitors, calcium channel blockers) — prescription only.",
        "precautions": "Diet (low salt), exercise, regular BP monitoring.",
        "serious": True,
        "specialist": "Cardiologist"
    },
    "anemia": {
        "aliases": ["anemia", "anaemia", "low hemoglobin"],
        "symptoms": "fatigue, pale skin, dizziness, shortness of breath, rapid heartbeat",
        "medicines": "Iron supplements, vitamin B12 or folic acid depending on cause (doctor to determine).",
        "precautions": "Dietary iron, confirm cause with blood tests.",
        "serious": True,
        "specialist": "Hematologist"
    },
    "migraine": {
        "aliases": ["migraine", "severe headache"],
        "symptoms": "severe headache often one-sided, nausea, sensitivity to light and sound",
        "medicines": "Over-the-counter painkillers (paracetamol/ibuprofen) or triptans (prescription).",
        "precautions": "Avoid triggers, rest in dark room; seek doctor if pattern changes.",
        "serious": False,
        "specialist": "Neurologist"
    },
    "asthma": {
        "aliases": ["asthma", "wheezing"],
        "symptoms": "shortness of breath, wheezing, chest tightness, coughing (worse at night/exercise)",
        "medicines": "Inhaled bronchodilators (relievers) and inhaled corticosteroids (preventers) — prescription required.",
        "precautions": "Avoid triggers, have inhaler action plan.",
        "serious": True,
        "specialist": "Pulmonologist"
    },
    "dengue": {
        "aliases": ["dengue", "dengue fever"],
        "symptoms": "high fever, severe headache, pain behind the eyes, joint/muscle pain, rash, nausea, vomiting",
        "medicines": "Supportive care (fluids, paracetamol). Avoid NSAIDs (ibuprofen/aspirin) if dengue is suspected — follow clinical guidance.",
        "precautions": "Seek immediate care for warning signs (abdominal pain, persistent vomiting, bleeding).",
        "serious": True,
        "specialist": "General Physician / Infectious Disease Specialist"
    },
    "malaria": {
        "aliases": ["malaria"],
        "symptoms": "fever, chills, headache, nausea, muscle aches, fatigue; can progress rapidly to severe illness",
        "medicines": "Antimalarials (prescription) — type depends on species and region.",
        "precautions": "Seek care quickly if malaria suspected (especially after travel to endemic areas).",
        "serious": True,
        "specialist": "Infectious Disease Specialist"
    },
    "pneumonia": {
        "aliases": ["pneumonia"],
        "symptoms": "cough, fever, shortness of breath, chest pain, fatigue",
        "medicines": "Antibiotics for bacterial pneumonia (prescription) and supportive care.",
        "precautions": "Seek medical attention for breathing difficulty or confusion.",
        "serious": True,
        "specialist": "Pulmonologist"
    },
    "tuberculosis": {
        "aliases": ["tuberculosis", "tb"],
        "symptoms": "persistent cough (2+ weeks), chest pain, coughing up blood, fever, night sweats, weight loss",
        "medicines": "Long-course combination antibiotics (prescription; supervised therapy).",
        "precautions": "TB is contagious—seek immediate medical evaluation and testing.",
        "serious": True,
        "specialist": "Infectious Disease Specialist / Pulmonologist"
    },
    "gastroenteritis": {
        "aliases": ["food poisoning", "stomach flu", "gastroenteritis"],
        "symptoms": "diarrhea, vomiting, abdominal pain, fever, dehydration",
        "medicines": "Oral rehydration, antiemetics or antidiarrheals as per doctor.",
        "precautions": "Maintain hydration; seek care for severe dehydration.",
        "serious": False,
        "specialist": "General Physician"
    },
    "urinary tract infection": {
        "aliases": ["uti", "urinary tract infection"],
        "symptoms": "burning urine, frequent urination, lower abdominal pain, cloudy or strong-smelling urine",
        "medicines": "Antibiotics (prescription) depending on culture results.",
        "precautions": "Seek medical evaluation; avoid self-prescribing antibiotics.",
        "serious": False,
        "specialist": "Urologist / General Physician"
    },
    "ear infection": {
        "aliases": ["ear infection", "otitis"],
        "symptoms": "ear pain, reduced hearing, fluid drainage, fever (in children)",
        "medicines": "Analgesics for pain; antibiotics if bacterial infection (doctor to decide).",
        "precautions": "See doctor if severe pain or hearing loss.",
        "serious": False,
        "specialist": "ENT Specialist"
    },
    "conjunctivitis": {
        "aliases": ["pink eye", "conjunctivitis"],
        "symptoms": "red eye, itching, discharge, tearing, gritty feeling",
        "medicines": "Antibiotic eye drops if bacterial; supportive care for viral/allergic types.",
        "precautions": "Contagious — maintain hygiene.",
        "serious": False,
        "specialist": "Ophthalmologist"
    },
    "arthritis": {
        "aliases": ["arthritis", "joint pain", "osteoarthritis", "rheumatoid arthritis"],
        "symptoms": "joint pain, stiffness, swelling, reduced range of motion",
        "medicines": "Pain relievers and disease-specific therapies (prescription).",
        "precautions": "Exercise, weight management, see rheumatologist for persistent symptoms.",
        "serious": False,
        "specialist": "Rheumatologist"
    },
    "depression": {
        "aliases": ["depression", "low mood", "mental health"],
        "symptoms": "persistent sadness, loss of interest, sleep/appetite changes, fatigue, suicidal thoughts (seek help immediately)",
        "medicines": "Therapy and antidepressants under medical supervision.",
        "precautions": "If suicidal or severe symptoms, seek immediate professional/mental health help.",
        "serious": True,
        "specialist": "Psychiatrist / Psychologist"
    },
    "chickenpox": {
        "aliases": ["chickenpox", "varicella"],
        "symptoms": "fever, itchy blister-like rash, tiredness",
        "medicines": "Antihistamines and calamine for itch; antivirals in some cases (doctor consult).",
        "precautions": "Contagious—avoid contact with vulnerable people.",
        "serious": False,
        "specialist": "General Physician"
    },
    "bronchitis": {
        "aliases": ["bronchitis"],
        "symptoms": "cough (sometimes with mucus), chest discomfort, fatigue, shortness of breath",
        "medicines": "Supportive care; antibiotics only if bacterial infection suspected.",
        "precautions": "See doctor if symptoms worsen or breathing difficulty occurs.",
        "serious": False,
        "specialist": "Pulmonologist / General Physician"
    }
}

# utility: build a simple keyword map for faster matching (optional)
def build_keyword_index(db):
    index = {}
    for name, info in db.items():
        tokens = set()
        tokens.update([w.strip() for w in name.split()])
        for a in info.get("aliases", []):
            tokens.update(a.split())
        tokens.update([w.strip() for w in info.get("symptoms", "").replace(",", " ").split()])
        index[name] = tokens
    return index

KEYWORD_INDEX = build_keyword_index(DISEASE_DB)
