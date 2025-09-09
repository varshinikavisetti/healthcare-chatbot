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
    },
    "sleepless_night": {
    "aliases": ["insomnia", "sleepless night", "cannot sleep"],
    "symptoms": "difficulty falling asleep, waking up during the night, feeling tired in the morning, irritability, poor concentration",
    "medicines": "Sleep hygiene practices, melatonin supplements, or prescription sleep aids as advised by a doctor.",
    "precautions": "Maintain a regular sleep schedule, avoid caffeine/alcohol before bed, create a relaxing bedtime routine.",
    "serious": False,
    "specialist": "Sleep Specialist / General Physician"
},
    

    "common cold": {
        "aliases": ["cold", "common cold", "runny nose"],
        "symptoms": "sneezing, runny nose, mild cough, sore throat, mild fatigue",
        "medicines": "Rest, fluids, paracetamol for fever, decongestants if needed",
        "precautions": "Wash hands frequently, avoid close contact with sick people",
        "serious": False,
        "specialist": "General Physician"
    },

    "eczema": {
        "aliases": ["eczema", "atopic dermatitis", "skin rash"],
        "symptoms": "dry, itchy, red skin, rashes, sometimes oozing",
        "medicines": "Moisturizers, topical corticosteroids, antihistamines",
        "precautions": "Avoid triggers, use gentle skincare products",
        "serious": False,
        "specialist": "Dermatologist"
    },

    "psoriasis": {
        "aliases": ["psoriasis", "skin scaling"],
        "symptoms": "thick red patches with silvery scales, itching, nail changes",
        "medicines": "Topical corticosteroids, phototherapy, systemic medications",
        "precautions": "Avoid stress, maintain skin hydration",
        "serious": False,
        "specialist": "Dermatologist"
    },

    "kidney stones": {
        "aliases": ["renal calculi", "kidney stones", "renal stone"],
        "symptoms": "severe flank pain, nausea, vomiting, blood in urine",
        "medicines": "Pain relief, hydration, sometimes lithotripsy or surgery",
        "precautions": "Drink plenty of fluids, reduce high-oxalate foods",
        "serious": True,
        "specialist": "Urologist"
    },

    "hepatitis b": {
        "aliases": ["hepatitis b", "hbv"],
        "symptoms": "jaundice, fatigue, nausea, abdominal pain, dark urine",
        "medicines": "Antiviral medications under doctor supervision",
        "precautions": "Vaccination, avoid alcohol, safe practices",
        "serious": True,
        "specialist": "Hepatologist / Infectious Disease Specialist"
    },

    "hepatitis c": {
        "aliases": ["hepatitis c", "hcv"],
        "symptoms": "fatigue, jaundice, abdominal pain, dark urine",
        "medicines": "Antiviral therapy prescribed by doctor",
        "precautions": "Avoid sharing needles, safe blood practices",
        "serious": True,
        "specialist": "Hepatologist / Infectious Disease Specialist"
    },

    "gout": {
        "aliases": ["gout", "arthritis", "uric acid"],
        "symptoms": "sudden severe joint pain, redness, swelling (often big toe)",
        "medicines": "NSAIDs, colchicine, lifestyle changes to reduce uric acid",
        "precautions": "Avoid alcohol and purine-rich foods",
        "serious": False,
        "specialist": "Rheumatologist"
    },

    "obesity": {
        "aliases": ["obesity", "overweight"],
        "symptoms": "excess body weight, fatigue, shortness of breath, joint pain",
        "medicines": "Diet, exercise, behavioral therapy, sometimes surgery",
        "precautions": "Maintain healthy lifestyle, monitor BMI",
        "serious": True,
        "specialist": "Endocrinologist / Dietitian"
    },

    "hypothyroidism": {
        "aliases": ["underactive thyroid", "hypothyroidism"],
        "symptoms": "fatigue, weight gain, cold intolerance, hair loss, constipation",
        "medicines": "Thyroid hormone replacement (levothyroxine)",
        "precautions": "Regular check-ups and medication adherence",
        "serious": True,
        "specialist": "Endocrinologist"
    },

    "hyperthyroidism": {
        "aliases": ["overactive thyroid", "hyperthyroidism", "graves disease"],
        "symptoms": "weight loss, palpitations, heat intolerance, anxiety, tremors",
        "medicines": "Anti-thyroid medications, beta-blockers, sometimes surgery",
        "precautions": "Regular monitoring, avoid excessive iodine intake",
        "serious": True,
        "specialist": "Endocrinologist"
    },

    "allergic rhinitis": {
        "aliases": ["hay fever", "allergic rhinitis", "nasal allergy"],
        "symptoms": "sneezing, runny nose, itchy eyes, congestion",
        "medicines": "Antihistamines, nasal corticosteroids, decongestants",
        "precautions": "Avoid allergens, keep environment clean",
        "serious": False,
        "specialist": "Allergist / ENT Specialist"
    },

    "otitis media": {
        "aliases": ["middle ear infection", "otitis media", "ear infection"],
        "symptoms": "ear pain, fever, irritability, hearing loss in children",
        "medicines": "Analgesics, antibiotics if bacterial, sometimes drainage",
        "precautions": "Treat colds promptly, avoid smoke exposure",
        "serious": False,
        "specialist": "ENT Specialist"
    },

    "sinusitis": {
        "aliases": ["sinus infection", "sinusitis"],
        "symptoms": "facial pain, nasal congestion, headache, fever, nasal discharge",
        "medicines": "Saline irrigation, decongestants, antibiotics if bacterial",
        "precautions": "Stay hydrated, treat allergies, avoid smoke",
        "serious": False,
        "specialist": "ENT Specialist"
    },

    "chronic kidney disease": {
        "aliases": ["ckd", "chronic kidney disease", "renal failure"],
        "symptoms": "fatigue, swelling, high blood pressure, changes in urination",
        "medicines": "Blood pressure control, dialysis, sometimes transplantation",
        "precautions": "Regular checkups, avoid nephrotoxic drugs",
        "serious": True,
        "specialist": "Nephrologist"
    },

    "heart attack": {
        "aliases": ["myocardial infarction", "heart attack", "mi"],
        "symptoms": "chest pain, shortness of breath, sweating, nausea",
        "medicines": "Emergency medical treatment, anticoagulants, surgery if needed",
        "precautions": "Control risk factors, healthy lifestyle, medications as prescribed",
        "serious": True,
        "specialist": "Cardiologist"
    },

    "stroke": {
        "aliases": ["stroke", "cerebrovascular accident", "cva"],
        "symptoms": "sudden weakness, numbness, difficulty speaking, vision problems",
        "medicines": "Emergency care, thrombolysis, rehabilitation",
        "precautions": "Control blood pressure, avoid smoking, healthy lifestyle",
        "serious": True,
        "specialist": "Neurologist"
    },

    "alzheimers disease": {
        "aliases": ["alzheimers", "dementia", "memory loss"],
        "symptoms": "memory loss, confusion, difficulty completing tasks, personality changes",
        "medicines": "Cognitive therapy, medications like cholinesterase inhibitors",
        "precautions": "Mental stimulation, safety measures at home",
        "serious": True,
        "specialist": "Neurologist / Geriatrician"
    },

    "parkinson's disease": {
        "aliases": ["parkinson", "parkinson's disease", "tremor disorder"],
        "symptoms": "tremor, stiffness, slow movement, balance issues",
        "medicines": "Levodopa, dopamine agonists, physiotherapy",
        "precautions": "Regular exercise, fall prevention strategies",
        "serious": True,
        "specialist": "Neurologist"
    },

    "epilepsy": {
        "aliases": ["epilepsy", "seizure disorder"],
        "symptoms": "recurrent seizures, temporary confusion, staring spells",
        "medicines": "Antiepileptic drugs, avoid seizure triggers",
        "precautions": "Avoid driving during seizures, adhere to medication",
        "serious": True,
        "specialist": "Neurologist"
    },

    "food allergies": {
        "aliases": ["food allergy", "allergic reaction"],
        "symptoms": "rash, itching, swelling, difficulty breathing, nausea",
        "medicines": "Antihistamines, epinephrine in severe cases",
        "precautions": "Avoid allergen, read labels carefully",
        "serious": True,
        "specialist": "Allergist"
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
