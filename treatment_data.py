# CropSense — Treatment Advice Engine
# Complete 38-class coverage · Bilingual: Hindi + English
# Keys match exactly: sorted(os.listdir("plantvillage dataset/color"))

TREATMENT_DATA = {

    # ─────────────────────────────────────────────────────
    # APPLE  (4 classes)
    # ─────────────────────────────────────────────────────

    "Apple___Apple_scab": {
        "name_en": "Apple Scab",
        "name_hi": "सेब खुरदरापन रोग",
        "crop_en": "Apple", "crop_hi": "सेब",
        "cause_en": "Fungal (Venturia inaequalis). Thrives in cool, wet spring. Spores from fallen infected leaves reinfect new growth.",
        "cause_hi": "फफूंद रोग। ठंडे, नम वसंत में पनपता है। गिरी पत्तियों के बीजाणु नई वृद्धि को संक्रमित करते हैं।",
        "symptoms_en": "Olive-green to brown velvety spots on leaves. Scabby, cracked lesions on fruit. Premature leaf drop.",
        "symptoms_hi": "पत्तियों पर जैतून-हरे से भूरे मखमली धब्बे। फल पर पपड़ीदार, फटे घाव। पत्तियाँ समय से पहले गिरना।",
        "organic_en": "Sulfur-based spray every 7–10 days during wet periods. Collect and destroy fallen leaves. Prune for airflow.",
        "organic_hi": "नम मौसम में हर 7-10 दिन सल्फर स्प्रे। गिरी पत्तियाँ नष्ट करें। वायु प्रवाह के लिए छंटाई करें।",
        "chemical_en": "Captan (2g/litre) or Myclobutanil (0.5ml/litre) at bud break, every 10 days. Rotate fungicides to prevent resistance.",
        "chemical_hi": "कली निकलते समय कैप्टान (2g/लीटर) या माइक्लोब्यूटेनिल (0.5ml/लीटर), हर 10 दिन। प्रतिरोध रोकने के लिए फफूंदनाशी बदलें।",
        "prevention_en": "Plant scab-resistant varieties (Gala, Fuji). Avoid overhead irrigation. Remove infected leaves in autumn.",
        "prevention_hi": "प्रतिरोधी किस्में लगाएं (गाला, फूजी)। ऊपर से सिंचाई न करें। शरद में संक्रमित पत्तियाँ हटाएं।",
        "severity": "Medium", "yield_loss": "20–40%"
    },

    "Apple___Black_rot": {
        "name_en": "Black Rot",
        "name_hi": "काला सड़न रोग",
        "crop_en": "Apple", "crop_hi": "सेब",
        "cause_en": "Fungal (Botryosphaeria obtusa). Enters through wounds or dead wood. Warm, humid conditions accelerate spread.",
        "cause_hi": "फफूंद रोग। घावों या मृत लकड़ी से प्रवेश करता है। गर्म, नम स्थितियों में तेजी से फैलता है।",
        "symptoms_en": "Purple spots on leaves enlarging to brown with yellow border. Fruit rots black and mummifies. Dark sunken cankers on branches.",
        "symptoms_hi": "पत्तियों पर बैंगनी धब्बे जो पीली सीमा के साथ भूरे हो जाते हैं। फल काला होकर ममीकृत हो जाता है। शाखाओं पर गहरे धंसे कैंकर।",
        "organic_en": "Prune and destroy all mummified fruit and dead wood. Apply Bordeaux mixture after pruning. Keep orchard floor clean.",
        "organic_hi": "ममीकृत फल और मृत लकड़ी छांटकर नष्ट करें। छंटाई के बाद बोर्डो मिश्रण लगाएं। बगीचा साफ रखें।",
        "chemical_en": "Captan or Thiophanate-methyl from petal fall at 10–14 day intervals. Remove infected wood promptly.",
        "chemical_hi": "पंखुड़ी गिरने से कैप्टान या थियोफेनेट-मेथिल, 10-14 दिन के अंतराल पर। संक्रमित लकड़ी तुरंत हटाएं।",
        "prevention_en": "Prune dead wood every winter. Avoid wounding bark. Burn all pruned material.",
        "prevention_hi": "हर सर्दी मृत लकड़ी छांटें। छाल को घायल करने से बचें। सभी छंटाई सामग्री जलाएं।",
        "severity": "High", "yield_loss": "30–60%"
    },

    "Apple___Cedar_apple_rust": {
        "name_en": "Cedar Apple Rust",
        "name_hi": "सेडर सेब रतुआ रोग",
        "crop_en": "Apple", "crop_hi": "सेब",
        "cause_en": "Fungal (Gymnosporangium juniperi-virginianae). Requires both apple and juniper/cedar trees to complete its lifecycle.",
        "cause_hi": "फफूंद रोग। जीवन चक्र के लिए सेब और जुनिपर/सीडर दोनों पेड़ों की जरूरत।",
        "symptoms_en": "Bright orange-yellow spots on upper leaf surface in spring. Tube-like structures on undersides. Deformed fruit.",
        "symptoms_hi": "वसंत में पत्ती की ऊपरी सतह पर चमकीले नारंगी-पीले धब्बे। निचली सतह पर नली जैसी संरचनाएं। विकृत फल।",
        "organic_en": "Remove nearby juniper trees if possible. Sulfur spray from pink bud stage through petal fall.",
        "organic_hi": "यदि संभव हो आसपास के जुनिपर पेड़ हटाएं। गुलाबी कली अवस्था से पंखुड़ी गिरने तक सल्फर स्प्रे।",
        "chemical_en": "Myclobutanil or Propiconazole spray starting at pink bud, 3–4 sprays at 7–10 day intervals. Critical timing — do not miss.",
        "chemical_hi": "गुलाबी कली से माइक्लोब्यूटेनिल या प्रोपिकोनाज़ोल, 7-10 दिन के अंतराल पर 3-4 स्प्रे। सही समय पर करना जरूरी।",
        "prevention_en": "Plant rust-resistant varieties. Avoid planting near junipers or red cedar trees.",
        "prevention_hi": "रतुआ प्रतिरोधी किस्में लगाएं। जुनिपर या लाल सीडर के पास न लगाएं।",
        "severity": "Medium", "yield_loss": "10–25%"
    },

    "Apple___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Apple", "crop_hi": "सेब",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Continue regular care. Compost mulch around base. Annual winter pruning for airflow.",
        "organic_hi": "नियमित देखभाल जारी रखें। आधार पर कम्पोस्ट मल्च। वार्षिक सर्दी छंटाई।",
        "chemical_en": "No treatment needed. Optional preventive copper spray before rainy season.",
        "chemical_hi": "उपचार की आवश्यकता नहीं। बारिश से पहले वैकल्पिक निवारक कॉपर स्प्रे।",
        "prevention_en": "Maintain sanitation. Remove fallen leaves and fruit promptly. Balanced fertilisation.",
        "prevention_hi": "स्वच्छता बनाए रखें। गिरी पत्तियाँ और फल तुरंत हटाएं। संतुलित उर्वरीकरण।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # BLUEBERRY  (1 class)
    # ─────────────────────────────────────────────────────

    "Blueberry___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Blueberry", "crop_hi": "ब्लूबेरी",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Maintain acidic soil (pH 4.5–5.5). Mulch with pine bark. Water at base only.",
        "organic_hi": "अम्लीय मिट्टी बनाए रखें (pH 4.5-5.5)। पाइन छाल से मल्चिंग। केवल आधार पर पानी।",
        "chemical_en": "No treatment needed. Test soil pH annually.",
        "chemical_hi": "उपचार की आवश्यकता नहीं। सालाना मिट्टी pH जांचें।",
        "prevention_en": "Ensure good drainage. Prune annually. Avoid waterlogging.",
        "prevention_hi": "अच्छी जल निकासी सुनिश्चित करें। सालाना छंटाई। जलजमाव से बचें।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # CHERRY  (2 classes)
    # ─────────────────────────────────────────────────────

    "Cherry_(including_sour)___Powdery_mildew": {
        "name_en": "Powdery Mildew",
        "name_hi": "चूर्णिल आसिता रोग",
        "crop_en": "Cherry", "crop_hi": "चेरी",
        "cause_en": "Fungal (Podosphaera clandestina). Warm days, cool nights. Does NOT need wet leaves — dry conditions actually favour it.",
        "cause_hi": "फफूंद रोग। गर्म दिन, ठंडी रात। गीली पत्तियों की जरूरत नहीं — शुष्क स्थितियों में पनपता है।",
        "symptoms_en": "White powdery coating on young leaves, shoots, and fruit. Infected leaves curl and distort. Stunted shoot growth.",
        "symptoms_hi": "छोटी पत्तियों और अंकुरों पर सफेद पाउडर परत। संक्रमित पत्तियाँ मुड़ती और विकृत होती हैं। अंकुर वृद्धि रुकना।",
        "organic_en": "Potassium bicarbonate or diluted neem oil (5ml/litre). Improve air circulation. Avoid excess nitrogen fertiliser.",
        "organic_hi": "पोटेशियम बाइकार्बोनेट या पतला नीम तेल (5ml/लीटर)। वायु संचार सुधारें। अत्यधिक नाइट्रोजन से बचें।",
        "chemical_en": "Myclobutanil, Tebuconazole, or sulfur at first white patches. Repeat every 14 days.",
        "chemical_hi": "सफेद धब्बों पर माइक्लोब्यूटेनिल, टेबुकोनाज़ोल या सल्फर। हर 14 दिन में दोहराएं।",
        "prevention_en": "Prune to open canopy. Plant resistant varieties. Avoid overhead irrigation.",
        "prevention_hi": "खुले चंदवे के लिए छंटाई। प्रतिरोधी किस्में लगाएं। ऊपर से सिंचाई न करें।",
        "severity": "Medium", "yield_loss": "10–30%"
    },

    "Cherry_(including_sour)___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Cherry", "crop_hi": "चेरी",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Regular pruning for airflow. Compost mulch. Monitor for aphids.",
        "organic_hi": "वायु प्रवाह के लिए नियमित छंटाई। कम्पोस्ट मल्च। एफिड की निगरानी।",
        "chemical_en": "No treatment needed.",
        "chemical_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Good canopy management. Remove mummified fruit. Balanced fertilisation.",
        "prevention_hi": "अच्छा चंदवा प्रबंधन। ममीकृत फल हटाएं। संतुलित उर्वरीकरण।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # CORN / MAIZE  (4 classes)
    # ─────────────────────────────────────────────────────

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "name_en": "Gray Leaf Spot",
        "name_hi": "ग्रे पत्ती धब्बा रोग",
        "crop_en": "Corn (Maize)", "crop_hi": "मक्का",
        "cause_en": "Fungal (Cercospora zeae-maydis). Warm, humid weather with heavy dew. Survives in crop residue over winter.",
        "cause_hi": "फफूंद रोग। गर्म, नम मौसम और भारी ओस। फसल अवशेषों में सर्दी भर जीवित रहता है।",
        "symptoms_en": "Long rectangular tan-to-grey lesions running parallel to leaf veins. Entire leaves can turn brown in severe cases.",
        "symptoms_hi": "पत्ती शिराओं के समानांतर लंबे आयताकार भूरे-से-धूसर घाव। गंभीर मामलों में पूरी पत्तियाँ भूरी।",
        "organic_en": "Plough crop residue under after harvest. Improve field drainage. Allow soil to dry between irrigations.",
        "organic_hi": "फसल के बाद जुताई कर फसल अवशेष दबाएं। खेत की जल निकासी सुधारें। सिंचाई के बीच मिट्टी सूखने दें।",
        "chemical_en": "Azoxystrobin or Propiconazole at early tasseling. One to two applications at 10–14 day intervals.",
        "chemical_hi": "तैसलिंग के शुरुआती चरण में एज़ोक्सीस्ट्रोबिन या प्रोपिकोनाज़ोल। 10-14 दिन के अंतराल पर 1-2 आवेदन।",
        "prevention_en": "Plant resistant hybrids. Rotate corn with soybean. Burn residue in severely affected fields.",
        "prevention_hi": "प्रतिरोधी संकर किस्में लगाएं। मक्का-सोयाबीन फसल चक्र। गंभीर खेतों में अवशेष जलाएं।",
        "severity": "Medium", "yield_loss": "10–30%"
    },

    "Corn_(maize)___Common_rust_": {
        "name_en": "Common Rust",
        "name_hi": "सामान्य रतुआ रोग",
        "crop_en": "Corn (Maize)", "crop_hi": "मक्का",
        "cause_en": "Fungal (Puccinia sorghi). Wind-borne spores. Favours cool temperatures (16–23°C) and high humidity.",
        "cause_hi": "फफूंद रोग। हवा से फैलने वाले बीजाणु। ठंडे तापमान (16-23°C) और उच्च आर्द्रता पसंद करता है।",
        "symptoms_en": "Brick-red to dark brown oval pustules on both leaf surfaces. Pustules release rusty powder when rubbed. Severely infected leaves turn yellow.",
        "symptoms_hi": "दोनों पत्ती सतहों पर ईंट-लाल से गहरे भूरे अंडाकार फुंसी। रगड़ने पर जंग जैसा पाउडर। गंभीर रूप से संक्रमित पत्तियाँ पीली।",
        "organic_en": "Remove heavily infected leaves. Improve spacing and air circulation. Avoid late planting.",
        "organic_hi": "अधिक संक्रमित पत्तियाँ हटाएं। दूरी और वायु संचार सुधारें। देर से बुवाई से बचें।",
        "chemical_en": "Propiconazole (Tilt 25 EC, 1ml/litre) or Tebuconazole at first pustule appearance. One early application usually sufficient.",
        "chemical_hi": "पहली फुंसी पर प्रोपिकोनाज़ोल (टिल्ट 25 EC, 1ml/लीटर) या टेबुकोनाज़ोल। समय पर एक आवेदन पर्याप्त।",
        "prevention_en": "Plant rust-resistant hybrids. Early planting to avoid peak spore season. Avoid excess nitrogen.",
        "prevention_hi": "रतुआ प्रतिरोधी संकर किस्में लगाएं। जल्दी बुवाई। नाइट्रोजन का अत्यधिक उपयोग न करें।",
        "severity": "Medium", "yield_loss": "10–20%"
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "name_en": "Northern Leaf Blight",
        "name_hi": "उत्तरी पत्ती झुलसा रोग",
        "crop_en": "Corn (Maize)", "crop_hi": "मक्का",
        "cause_en": "Fungal (Setosphaeria turcica). Moderate temperatures (18–27°C) with extended leaf wetness periods.",
        "cause_hi": "फफूंद रोग। मध्यम तापमान (18-27°C) और लंबे समय तक पत्ती की नमी।",
        "symptoms_en": "Long cigar-shaped grey-green to tan lesions (5–15 cm). Starts on lower leaves, moves upward. Dark spore masses in humid weather.",
        "symptoms_hi": "लंबे सिगार के आकार के धूसर-हरे से भूरे घाव (5-15 सेमी)। निचली पत्तियों से शुरू, ऊपर बढ़ता है।",
        "organic_en": "Plough crop residue under after harvest. Rotate with non-host crops. Avoid dense planting.",
        "organic_hi": "फसल के बाद फसल अवशेष जोतें। गैर-होस्ट फसलों के साथ चक्र। घनी बुवाई से बचें।",
        "chemical_en": "Azoxystrobin + Propiconazole or Pyraclostrobin at first sign of lesions on lower leaves. Protect upper canopy.",
        "chemical_hi": "निचली पत्तियों पर घाव के पहले संकेत पर एज़ोक्सीस्ट्रोबिन + प्रोपिकोनाज़ोल या पाइराक्लोस्ट्रोबिन।",
        "prevention_en": "Resistant hybrids are the most effective tool. Rotate crops. Balanced NPK fertilisation.",
        "prevention_hi": "प्रतिरोधी संकर किस्में सबसे प्रभावी। फसल चक्र। संतुलित NPK उर्वरीकरण।",
        "severity": "High", "yield_loss": "20–50%"
    },

    "Corn_(maize)___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Corn (Maize)", "crop_hi": "मक्का",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Maintain soil health with compost. Monitor regularly. Ensure proper spacing.",
        "organic_hi": "कम्पोस्ट से मिट्टी का स्वास्थ्य बनाए रखें। नियमित निगरानी। उचित दूरी।",
        "chemical_en": "No treatment needed.",
        "chemical_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Certified disease-free seeds. Balanced NPK. Crop rotation.",
        "prevention_hi": "प्रमाणित रोग मुक्त बीज। संतुलित NPK। फसल चक्र।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # GRAPE  (4 classes)
    # ─────────────────────────────────────────────────────

    "Grape___Black_rot": {
        "name_en": "Black Rot",
        "name_hi": "काला सड़न रोग",
        "crop_en": "Grape", "crop_hi": "अंगूर",
        "cause_en": "Fungal (Guignardia bidwellii). Warm (24–29°C), rainy weather. Mummified berries are the primary overwintering source.",
        "cause_hi": "फफूंद रोग। गर्म (24-29°C), बारिश के मौसम में तेजी से फैलता है। ममीकृत जामुन प्राथमिक स्रोत।",
        "symptoms_en": "Small tan spots with dark borders on leaves. Infected berries turn brown then black and mummify. Black pycnidia in lesion centres.",
        "symptoms_hi": "पत्तियों पर गहरे बॉर्डर के साथ छोटे भूरे धब्बे। संक्रमित जामुन भूरे फिर काले होकर ममीकृत।",
        "organic_en": "Remove ALL mummified berries every winter — primary infection source. Prune for air circulation. Copper spray at bud break.",
        "organic_hi": "हर सर्दी सभी ममीकृत जामुन हटाएं — प्राथमिक संक्रमण स्रोत। वायु संचार के लिए छंटाई। कली निकलते समय कॉपर स्प्रे।",
        "chemical_en": "Mancozeb or Myclobutanil starting at bud break. Critical sprays: pre-bloom, bloom, 2–3 weeks post-bloom. Do NOT miss bloom spray.",
        "chemical_hi": "कली निकलते समय से मैनकोज़ेब या माइक्लोब्यूटेनिल। महत्वपूर्ण: फूल से पहले, फूल के दौरान, फूल के 2-3 सप्ताह बाद।",
        "prevention_en": "Remove mummified fruit every winter. Thin canopy for airflow. Plant in well-drained sites.",
        "prevention_hi": "हर सर्दी ममीकृत फल हटाएं। वायु प्रवाह के लिए चंदवा पतला करें। अच्छी जल निकासी वाले स्थान पर लगाएं।",
        "severity": "High", "yield_loss": "50–100%"
    },

    "Grape___Esca_(Black_Measles)": {
        "name_en": "Esca (Black Measles)",
        "name_hi": "एस्का रोग (काली खसरा)",
        "crop_en": "Grape", "crop_hi": "अंगूर",
        "cause_en": "Wood-rotting fungal complex entering through pruning wounds. A chronic, progressive disease with no cure.",
        "cause_hi": "छंटाई के घावों से प्रवेश करने वाला लकड़ी सड़ाने वाला फफूंद समूह। कोई इलाज नहीं है।",
        "symptoms_en": "Interveinal leaf yellowing in 'tiger stripe' pattern. Berries develop dark spots and crack. Sudden vine collapse in severe cases.",
        "symptoms_hi": "शिराओं के बीच पत्ती का 'बाघ धारी' पैटर्न में पीलापन। जामुन पर गहरे धब्बे और दरारें। बेल का अचानक गिरना।",
        "organic_en": "No cure exists. Remove and destroy severely infected vines. Apply pruning wound sealant immediately after pruning. Delay pruning to late dormant season.",
        "organic_hi": "कोई इलाज नहीं। गंभीर रूप से संक्रमित बेल हटाकर नष्ट करें। छंटाई के तुरंत बाद घाव सीलेंट लगाएं।",
        "chemical_en": "No effective chemical cure. Consult your local agricultural officer for region-specific guidance.",
        "chemical_hi": "कोई प्रभावी रासायनिक इलाज नहीं। क्षेत्र-विशिष्ट मार्गदर्शन के लिए स्थानीय कृषि अधिकारी से संपर्क करें।",
        "prevention_en": "Seal pruning wounds with Bordeaux paste. Prune during dry weather. Use sterilised pruning tools.",
        "prevention_hi": "बोर्डो पेस्ट से छंटाई के घाव बंद करें। सूखे मौसम में छंटाई। नसबंदी किए उपकरण उपयोग करें।",
        "severity": "High", "yield_loss": "30–70%"
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "name_en": "Leaf Blight (Isariopsis Leaf Spot)",
        "name_hi": "पत्ती झुलसा रोग",
        "crop_en": "Grape", "crop_hi": "अंगूर",
        "cause_en": "Fungal (Pseudocercospora vitis). Warm, humid conditions late in the growing season.",
        "cause_hi": "फफूंद रोग। बढ़ते मौसम के अंत में गर्म, नम स्थितियों में।",
        "symptoms_en": "Dark brown to black angular spots bounded by leaf veins. White-grey powdery growth on undersides. Premature defoliation.",
        "symptoms_hi": "पत्ती शिराओं से घिरे गहरे भूरे से काले कोणीय धब्बे। निचली सतह पर सफेद-धूसर वृद्धि। समय से पहले पत्तियाँ झड़ना।",
        "organic_en": "Collect and destroy fallen leaves. Improve air circulation through canopy management. Copper spray at first sign.",
        "organic_hi": "गिरी पत्तियाँ इकट्ठी करके नष्ट करें। चंदवा प्रबंधन से वायु संचार सुधारें। पहले संकेत पर कॉपर स्प्रे।",
        "chemical_en": "Mancozeb 75% WP (2g/litre) or Carbendazim + Mancozeb spray at 10–14 day intervals.",
        "chemical_hi": "10-14 दिन के अंतराल पर मैनकोज़ेब 75% WP (2g/लीटर) या कार्बेंडाज़िम + मैनकोज़ेब स्प्रे।",
        "prevention_en": "Regular canopy thinning. Remove leaf litter. Avoid late-season irrigation that wets foliage.",
        "prevention_hi": "नियमित चंदवा पतलाई। पत्ती कूड़ा हटाएं। पत्तियाँ गीली करने वाली देर मौसम की सिंचाई से बचें।",
        "severity": "Medium", "yield_loss": "10–20%"
    },

    "Grape___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Grape", "crop_hi": "अंगूर",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Regular canopy management. Remove mummified fruit each season. Compost mulch.",
        "organic_hi": "नियमित चंदवा प्रबंधन। प्रत्येक मौसम में ममीकृत फल हटाएं। कम्पोस्ट मल्च।",
        "chemical_en": "No treatment needed. Preventive copper spray before rainy season optional.",
        "chemical_hi": "उपचार की आवश्यकता नहीं। बारिश से पहले निवारक कॉपर स्प्रे वैकल्पिक।",
        "prevention_en": "Seal pruning wounds. Maintain vine hygiene every season.",
        "prevention_hi": "छंटाई के घाव बंद करें। हर मौसम बेल की स्वच्छता बनाए रखें।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # ORANGE  (1 class)
    # ─────────────────────────────────────────────────────

    "Orange___Haunglongbing_(Citrus_greening)": {
        "name_en": "Citrus Greening (HLB / Huanglongbing)",
        "name_hi": "संतरा हरीताभ रोग (HLB)",
        "crop_en": "Orange", "crop_hi": "संतरा",
        "cause_en": "Bacterial (Candidatus Liberibacter asiaticus). Spread exclusively by Asian citrus psyllid insect. No cure exists — infected trees die within years.",
        "cause_hi": "जीवाणु रोग। केवल एशियाई साइट्रस सिला कीट द्वारा फैलता है। कोई इलाज नहीं — संक्रमित पेड़ वर्षों में मर जाते हैं।",
        "symptoms_en": "Asymmetric blotchy yellow mottling of leaves (unlike symmetric nutrient deficiency). Lopsided, small, bitter fruit. Stunted growth.",
        "symptoms_hi": "पत्तियों का असममित धब्बेदार पीलापन (पोषक कमी के विपरीत जो सममित होती है)। एकतरफा छोटे कड़वे फल। रुकी हुई वृद्धि।",
        "organic_en": "No cure. Remove and destroy infected trees immediately to prevent spread. Yellow sticky traps and neem oil to reduce psyllid populations.",
        "organic_hi": "कोई इलाज नहीं। फैलाव रोकने के लिए संक्रमित पेड़ तुरंत हटाकर नष्ट करें। पीले चिपचिपे जाल और नीम तेल से सिला नियंत्रित करें।",
        "chemical_en": "Imidacloprid or Thiamethoxam to control psyllid vector. Does NOT cure the disease. Notify your local agricultural officer immediately — this is a reportable disease.",
        "chemical_hi": "सिला वाहक नियंत्रण के लिए इमिडाक्लोप्रिड या थायमेथोक्सम। रोग ठीक नहीं होता। तुरंत स्थानीय कृषि अधिकारी को सूचित करें।",
        "prevention_en": "Certified disease-free nursery stock only. Install psyllid monitoring traps. Quarantine new plants for 3 months. Report suspected HLB immediately.",
        "prevention_hi": "केवल प्रमाणित रोग मुक्त नर्सरी पौधे। सिला निगरानी जाल। नए पौधों को 3 महीने क्वारंटाइन। संदिग्ध HLB तुरंत रिपोर्ट करें।",
        "severity": "High", "yield_loss": "100% (tree death within years)"
    },

    # ─────────────────────────────────────────────────────
    # PEACH  (2 classes)
    # ─────────────────────────────────────────────────────

    "Peach___Bacterial_spot": {
        "name_en": "Bacterial Spot",
        "name_hi": "जीवाणु धब्बा रोग",
        "crop_en": "Peach", "crop_hi": "आड़ू",
        "cause_en": "Bacterial (Xanthomonas arboricola pv. pruni). Rain splash, wind-driven rain, and contaminated tools. Warm, wet weather.",
        "cause_hi": "जीवाणु रोग। बारिश के छींटे, हवा से आई बारिश और दूषित उपकरण। गर्म, नम मौसम।",
        "symptoms_en": "Water-soaked lesions on leaves turning dark brown with yellow halo. Shot-hole appearance as centres fall out. Fruit cracking and gumming.",
        "symptoms_hi": "पत्तियों पर पानी से भीगे घाव जो पीले घेरे के साथ गहरे भूरे। केंद्र गिरने पर गोली के छेद जैसा। फल फटना और गोंद निकलना।",
        "organic_en": "Copper hydroxide spray during dormancy and at petal fall. Avoid working when leaves are wet. Sterilise pruning tools between trees.",
        "organic_hi": "निष्क्रियता और पंखुड़ी गिरने पर कॉपर हाइड्रॉक्साइड स्प्रे। पत्तियाँ गीली होने पर काम न करें। पेड़ों के बीच उपकरण नसबंदी करें।",
        "chemical_en": "Copper bactericide sprays from shuck split through harvest at 7–10 day intervals. Oxytetracycline where registered.",
        "chemical_hi": "शक स्प्लिट से फसल तक 7-10 दिन के अंतराल पर कॉपर बैक्टीरिसाइड स्प्रे।",
        "prevention_en": "Plant resistant varieties. Establish windbreaks. Drip irrigation. Avoid overhead watering.",
        "prevention_hi": "प्रतिरोधी किस्में लगाएं। पवन अवरोध लगाएं। ड्रिप सिंचाई। ऊपर से सिंचाई न करें।",
        "severity": "Medium", "yield_loss": "20–40%"
    },

    "Peach___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Peach", "crop_hi": "आड़ू",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Regular pruning for airflow. Compost around base. Remove fallen leaves promptly.",
        "organic_hi": "वायु प्रवाह के लिए नियमित छंटाई। आधार पर कम्पोस्ट। गिरी पत्तियाँ तुरंत हटाएं।",
        "chemical_en": "No treatment needed. Dormant copper spray optional.",
        "chemical_hi": "उपचार की आवश्यकता नहीं। निष्क्रिय कॉपर स्प्रे वैकल्पिक।",
        "prevention_en": "Balanced fertilisation. Drip irrigation preferred. Good canopy management.",
        "prevention_hi": "संतुलित उर्वरीकरण। ड्रिप सिंचाई बेहतर। अच्छा चंदवा प्रबंधन।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # BELL PEPPER  (2 classes)
    # ─────────────────────────────────────────────────────

    "Pepper,_bell___Bacterial_spot": {
        "name_en": "Bacterial Spot",
        "name_hi": "जीवाणु धब्बा रोग",
        "crop_en": "Bell Pepper", "crop_hi": "शिमला मिर्च",
        "cause_en": "Bacterial (Xanthomonas euvesicatoria). Rain splash, infected seed, contaminated tools. Warm, wet weather.",
        "cause_hi": "जीवाणु संक्रमण। बारिश के छींटे, संक्रमित बीज, दूषित उपकरण। गर्म, नम मौसम।",
        "symptoms_en": "Small water-soaked spots turning dark brown with yellow margins on leaves. Raised scabby spots on fruit. Defoliation in severe cases.",
        "symptoms_hi": "पत्तियों पर छोटे पानी से भीगे धब्बे, पीले हाशिये के साथ गहरे भूरे। फल पर उभरे पपड़ीदार धब्बे।",
        "organic_en": "Copper hydroxide spray (2g/litre) every 7 days in wet weather. Avoid field work when plants are wet. Use disease-free transplants.",
        "organic_hi": "नम मौसम में हर 7 दिन कॉपर हाइड्रॉक्साइड स्प्रे (2g/लीटर)। पौधे गीले होने पर खेत में काम न करें।",
        "chemical_en": "Copper bactericide + Mancozeb tank mix. Kasugamycin for severe outbreaks. Begin early — established infection cannot be eliminated.",
        "chemical_hi": "कॉपर बैक्टीरिसाइड + मैनकोज़ेब टैंक मिक्स। गंभीर प्रकोप में कासुगामाइसिन। जल्दी शुरू करें — स्थापित संक्रमण खत्म नहीं होता।",
        "prevention_en": "Certified disease-free seed. 3-year rotation with non-solanaceous crops. Drip irrigation. Stake plants.",
        "prevention_hi": "प्रमाणित रोग मुक्त बीज। गैर-सोलेनेसियस फसलों के साथ 3 साल का चक्र। ड्रिप सिंचाई।",
        "severity": "Medium", "yield_loss": "20–40%"
    },

    "Pepper,_bell___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Bell Pepper", "crop_hi": "शिमला मिर्च",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Mulch to retain moisture. Regular base watering. Compost side-dressing.",
        "organic_hi": "नमी के लिए मल्चिंग। नियमित जड़ में पानी। कम्पोस्ट साइड-ड्रेसिंग।",
        "chemical_en": "No treatment needed.",
        "chemical_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Rotate with non-solanaceous crops. Use disease-free transplants. Avoid overwatering.",
        "prevention_hi": "गैर-सोलेनेसियस फसलों के साथ चक्र। रोग मुक्त पौध। अत्यधिक पानी से बचें।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # POTATO  (3 classes)
    # ─────────────────────────────────────────────────────

    "Potato___Early_blight": {
        "name_en": "Early Blight",
        "name_hi": "अगेती झुलसा रोग",
        "crop_en": "Potato", "crop_hi": "आलू",
        "cause_en": "Fungal (Alternaria solani). Most damaging on nutritionally stressed plants. Airborne spores in warm (24–29°C), humid conditions.",
        "cause_hi": "फफूंद संक्रमण (अल्टरनेरिया सोलानी)। पोषण से कमजोर पौधों पर सबसे हानिकारक। गर्म (24-29°C), नम स्थितियों में हवाई बीजाणु।",
        "symptoms_en": "Circular brown spots with concentric rings (target board pattern) on older leaves first. Yellow tissue surrounds spots. Progresses upward.",
        "symptoms_hi": "पहले पुरानी पत्तियों पर संकेंद्रित छल्लों के साथ गोलाकार भूरे धब्बे (लक्ष्य बोर्ड पैटर्न)। धब्बों के आसपास पीला ऊतक।",
        "organic_en": "Neem oil spray (5ml/litre) every 7 days. Remove and destroy infected lower leaves. Adequate fertilisation reduces susceptibility.",
        "organic_hi": "हर 7 दिन नीम तेल स्प्रे (5ml/लीटर)। संक्रमित निचली पत्तियाँ हटाकर नष्ट करें। पर्याप्त उर्वरीकरण से संवेदनशीलता कम होती है।",
        "chemical_en": "Mancozeb 75% WP (2.5g/litre) every 10–15 days from first symptoms. Chlorothalonil (2g/litre) as alternative.",
        "chemical_hi": "पहले लक्षणों से हर 10-15 दिन मैनकोज़ेब 75% WP (2.5g/लीटर)। वैकल्पिक: क्लोरोथैलोनिल (2g/लीटर)।",
        "prevention_en": "Certified disease-free seed tubers. Minimum 3-year crop rotation. Balanced NPK. Avoid water stress.",
        "prevention_hi": "प्रमाणित रोग मुक्त बीज कंद। न्यूनतम 3 साल का फसल चक्र। संतुलित NPK। जल तनाव से बचें।",
        "severity": "Medium", "yield_loss": "15–25%"
    },

    "Potato___Late_blight": {
        "name_en": "Late Blight",
        "name_hi": "पछेती झुलसा रोग",
        "crop_en": "Potato", "crop_hi": "आलू",
        "cause_en": "Water mold (Phytophthora infestans). The pathogen behind the Irish Famine. Spreads explosively in cool (10–20°C), wet weather — can destroy a field in days.",
        "cause_hi": "जल फफूंद। आयरिश अकाल का कारण। ठंडे (10-20°C), नम मौसम में विस्फोटक रूप से फैलता है — कुछ दिनों में पूरा खेत नष्ट।",
        "symptoms_en": "Dark water-soaked lesions on leaves with white mold on undersides in humid conditions. Rapid tissue death. Brown foul-smelling tuber rot.",
        "symptoms_hi": "पत्तियों पर गहरे पानी से भीगे घाव, नम मौसम में नीचे सफेद फफूंद। तीव्र ऊतक मृत्यु। भूरे, बदबूदार कंद सड़न।",
        "organic_en": "Bordeaux mixture (1%) spray as preventive. Destroy crop residue — do not compost. Harvest tubers as soon as vines die.",
        "organic_hi": "निवारक के रूप में बोर्डो मिश्रण (1%) स्प्रे। फसल अवशेष नष्ट करें — खाद न बनाएं। बेल मरते ही कंद काट लें।",
        "chemical_en": "Metalaxyl + Mancozeb (Ridomil Gold MZ, 2.5g/litre) at first sign. Spray every 7 days in wet weather without exception. If severe: destroy foliage, harvest early.",
        "chemical_hi": "पहले संकेत पर मेटालेक्सिल + मैनकोज़ेब (रिडोमिल गोल्ड MZ, 2.5g/लीटर)। नम मौसम में बिना अपवाद हर 7 दिन स्प्रे। गंभीर: पत्तियाँ नष्ट करें, जल्दी फसल काटें।",
        "prevention_en": "Resistant varieties (Kufri Jyoti, Kufri Khyati). Good drainage essential. Hill soil around plants. Avoid late planting in cool, wet seasons.",
        "prevention_hi": "प्रतिरोधी किस्में (कुफरी ज्योति, कुफरी ख्याति)। अच्छी जल निकासी आवश्यक। पौधों के चारों ओर मिट्टी चढ़ाएं।",
        "severity": "High", "yield_loss": "40–100%"
    },

    "Potato___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Potato", "crop_hi": "आलू",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Hill soil at 2–3 week intervals. Maintain soil moisture. Compost side-dressing.",
        "organic_hi": "2-3 सप्ताह के अंतराल पर मिट्टी चढ़ाएं। मिट्टी की नमी बनाए रखें। कम्पोस्ट साइड-ड्रेसिंग।",
        "chemical_en": "No treatment needed. Preventive Mancozeb spray optional at high-risk periods.",
        "chemical_hi": "उपचार की आवश्यकता नहीं। उच्च जोखिम में निवारक मैनकोज़ेब वैकल्पिक।",
        "prevention_en": "Certified seed tubers. 3-year rotation. Balanced fertilisation with adequate potassium.",
        "prevention_hi": "प्रमाणित बीज कंद। 3 साल का चक्र। पर्याप्त पोटेशियम के साथ संतुलित उर्वरीकरण।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # RASPBERRY  (1 class)
    # ─────────────────────────────────────────────────────

    "Raspberry___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Raspberry", "crop_hi": "रसभरी",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Remove old fruiting canes after harvest. Heavy mulch. Maintain good air circulation.",
        "organic_hi": "फसल के बाद पुरानी फल वाली बेल हटाएं। भारी मल्च। अच्छा वायु संचार।",
        "chemical_en": "No treatment needed.",
        "chemical_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Remove old canes annually. Monitor for aphids and botrytis. Good drainage.",
        "prevention_hi": "सालाना पुरानी बेल हटाएं। एफिड और बोट्रीटिस की निगरानी। अच्छी जल निकासी।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # SOYBEAN  (1 class)
    # ─────────────────────────────────────────────────────

    "Soybean___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Soybean", "crop_hi": "सोयाबीन",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Inoculate seed with Rhizobium before sowing. Weed-free field. Adequate phosphorus and potassium.",
        "organic_hi": "बुवाई से पहले बीज को राइजोबियम से टीका लगाएं। खरपतवार मुक्त खेत। पर्याप्त फास्फोरस और पोटेशियम।",
        "chemical_en": "No treatment needed.",
        "chemical_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Rotate with corn or wheat. Certified seed. Monitor for rust during humid seasons.",
        "prevention_hi": "मक्का या गेहूँ के साथ चक्र। प्रमाणित बीज। नम मौसम में रतुआ की निगरानी।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # SQUASH  (1 class)
    # ─────────────────────────────────────────────────────

    "Squash___Powdery_mildew": {
        "name_en": "Powdery Mildew",
        "name_hi": "चूर्णिल आसिता रोग",
        "crop_en": "Squash", "crop_hi": "कद्दू/स्क्वैश",
        "cause_en": "Fungal (Podosphaera xanthii). Does NOT need wet leaves — thrives on warm, dry days with cool nights. Very common in cucurbits.",
        "cause_hi": "फफूंद रोग। गीली पत्तियों की जरूरत नहीं — गर्म, शुष्क दिन और ठंडी रात में पनपता है। कद्दू वर्गीय फसलों में बहुत आम।",
        "symptoms_en": "White powdery spots on upper leaf surfaces expanding to coat entire leaves. Infected leaves yellow and die. Fruit may be stunted.",
        "symptoms_hi": "पत्ती की ऊपरी सतह पर सफेद पाउडर धब्बे जो पूरी पत्तियों को ढक लेते हैं। संक्रमित पत्तियाँ पीली होकर मरती हैं।",
        "organic_en": "1 tbsp baking soda + 1 tsp soap in 1 litre water, spray weekly. Neem oil (5ml/litre). Remove infected leaves immediately.",
        "organic_hi": "1 लीटर पानी में 1 चम्मच बेकिंग सोडा + 1 चम्मच साबुन, साप्ताहिक स्प्रे। नीम तेल (5ml/लीटर)। संक्रमित पत्तियाँ तुरंत हटाएं।",
        "chemical_en": "Myclobutanil, Triadimefon, or sulfur at first white spots. Repeat every 10–14 days. Do NOT use sulfur above 32°C.",
        "chemical_hi": "पहले सफेद धब्बों पर माइक्लोब्यूटेनिल, ट्रायडिमेफोन या सल्फर। हर 10-14 दिन दोहराएं। 32°C से ऊपर सल्फर उपयोग न करें।",
        "prevention_en": "Plant resistant varieties. Adequate spacing for airflow. Avoid excess nitrogen. Grow in full sun.",
        "prevention_hi": "प्रतिरोधी किस्में लगाएं। वायु प्रवाह के लिए पर्याप्त दूरी। अत्यधिक नाइट्रोजन से बचें। पूर्ण धूप में उगाएं।",
        "severity": "Medium", "yield_loss": "20–40%"
    },

    # ─────────────────────────────────────────────────────
    # STRAWBERRY  (2 classes)
    # ─────────────────────────────────────────────────────

    "Strawberry___Leaf_scorch": {
        "name_en": "Leaf Scorch",
        "name_hi": "पत्ती झुलसान रोग",
        "crop_en": "Strawberry", "crop_hi": "स्ट्रॉबेरी",
        "cause_en": "Fungal (Diplocarpon earlianum). Rain splash and infected plant material. Warm (20–30°C), wet conditions.",
        "cause_hi": "फफूंद रोग। बारिश के छींटे और संक्रमित पौधे सामग्री। गर्म (20-30°C), नम स्थितियाँ।",
        "symptoms_en": "Irregular dark purple to reddish-purple spots on leaf surfaces. Leaves eventually appear scorched and die. No distinct grey centre unlike leaf spot.",
        "symptoms_hi": "पत्ती की सतह पर अनियमित गहरे बैंगनी से लालिमा-बैंगनी धब्बे। पत्तियाँ झुलसी दिखाई देती हैं और मरती हैं।",
        "organic_en": "Remove and destroy infected leaves. Avoid overhead irrigation. Mulch to prevent soil splash. Good air circulation.",
        "organic_hi": "संक्रमित पत्तियाँ हटाकर नष्ट करें। ऊपर से सिंचाई न करें। मिट्टी के छींटे रोकने के लिए मल्च।",
        "chemical_en": "Myclobutanil or Captan at first sign of spots. Repeat every 10–14 days in wet weather.",
        "chemical_hi": "धब्बों के पहले संकेत पर माइक्लोब्यूटेनिल या कैप्टान। नम मौसम में हर 10-14 दिन दोहराएं।",
        "prevention_en": "Certified disease-free transplants. Replace planting every 2–3 years. Avoid dense planting. Drip irrigation.",
        "prevention_hi": "रोग मुक्त प्रमाणित पौध। हर 2-3 साल में रोपण बदलें। घनी बुवाई से बचें। ड्रिप सिंचाई।",
        "severity": "Medium", "yield_loss": "15–30%"
    },

    "Strawberry___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Strawberry", "crop_hi": "स्ट्रॉबेरी",
        "cause_en": "No disease detected.", "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "No visible symptoms.", "symptoms_hi": "कोई दृश्य लक्षण नहीं।",
        "organic_en": "Straw mulch under plants. Remove old leaves after harvest. Drip irrigation preferred.",
        "organic_hi": "पौधों के नीचे पुआल मल्च। फसल के बाद पुरानी पत्तियाँ हटाएं। ड्रिप सिंचाई बेहतर।",
        "chemical_en": "No treatment needed.",
        "chemical_hi": "उपचार की आवश्यकता नहीं।",
        "prevention_en": "Replace runners every 2–3 years. Monitor for spider mites. Avoid waterlogging.",
        "prevention_hi": "हर 2-3 साल में रनर बदलें। स्पाइडर माइट की निगरानी। जलजमाव से बचें।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # TOMATO  (10 classes)
    # ─────────────────────────────────────────────────────

    "Tomato___Bacterial_spot": {
        "name_en": "Bacterial Spot",
        "name_hi": "जीवाणु धब्बा रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Bacterial (Xanthomonas vesicatoria group). Rain splash, wind-driven rain, infected seed, handling wet plants.",
        "cause_hi": "जीवाणु संक्रमण। बारिश के छींटे, हवा से आई बारिश, संक्रमित बीज, गीले पौधों को संभालना।",
        "symptoms_en": "Small water-soaked spots on leaves turning dark brown with yellow halo. Raised scab-like spots on fruit. Defoliation in severe cases.",
        "symptoms_hi": "पत्तियों पर छोटे पानी से भीगे धब्बे जो पीले घेरे के साथ गहरे भूरे। फल पर उभरे पपड़ी जैसे धब्बे।",
        "organic_en": "Copper hydroxide spray (2g/litre) every 7 days in wet weather. Do NOT work in field when foliage is wet.",
        "organic_hi": "नम मौसम में हर 7 दिन कॉपर हाइड्रॉक्साइड स्प्रे (2g/लीटर)। पत्ते गीले होने पर खेत में काम न करें।",
        "chemical_en": "Copper bactericide + Mancozeb tank mix. Streptomycin sulfate for severe cases. Early sprays critical — cannot eliminate established infection.",
        "chemical_hi": "कॉपर बैक्टीरिसाइड + मैनकोज़ेब टैंक मिक्स। गंभीर मामलों में स्ट्रेप्टोमाइसिन सल्फेट। जल्दी स्प्रे जरूरी।",
        "prevention_en": "Hot water seed treatment (50°C for 25 min). 3-year rotation. Drip irrigation. Stake plants.",
        "prevention_hi": "गर्म पानी बीज उपचार (50°C पर 25 मिनट)। 3 साल का चक्र। ड्रिप सिंचाई। पौधों को सहारा दें।",
        "severity": "Medium", "yield_loss": "20–50%"
    },

    "Tomato___Early_blight": {
        "name_en": "Early Blight",
        "name_hi": "अगेती झुलसा रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Fungal (Alternaria solani). Warm (24–29°C), humid conditions. Survives in soil and crop debris.",
        "cause_hi": "फफूंद संक्रमण (अल्टरनेरिया सोलानी)। गर्म (24-29°C) और नम मौसम में फैलता है। मिट्टी और फसल अवशेषों में जीवित रहता है।",
        "symptoms_en": "Dark brown spots with concentric yellow rings on lower leaves (target board pattern). Progresses upward. Stem lesions possible.",
        "symptoms_hi": "निचली पत्तियों पर पीले छल्लों के साथ गहरे भूरे धब्बे (लक्ष्य बोर्ड पैटर्न)। ऊपर की ओर बढ़ता है।",
        "organic_en": "Neem oil (5ml/litre) every 7 days. Remove infected leaves immediately. Mulch to prevent soil splash. Adequate fertilisation.",
        "organic_hi": "हर 7 दिन नीम तेल (5ml/लीटर)। संक्रमित पत्तियाँ तुरंत हटाएं। मिट्टी के छींटे रोकने के लिए मल्च।",
        "chemical_en": "Mancozeb 75% WP (2g/litre) or Chlorothalonil (2g/litre) every 7–10 days. Apply preventively at first sign of humidity.",
        "chemical_hi": "हर 7-10 दिन मैनकोज़ेब 75% WP (2g/लीटर) या क्लोरोथैलोनिल (2g/लीटर)। आर्द्रता के पहले संकेत पर निवारक रूप से लगाएं।",
        "prevention_en": "Crop rotation every season. Avoid overhead watering. Resistant varieties. Burn crop debris after harvest.",
        "prevention_hi": "हर मौसम फसल बदलें। ऊपर से पानी न दें। प्रतिरोधी किस्में। फसल के बाद अवशेष जलाएं।",
        "severity": "Medium", "yield_loss": "20–30%"
    },

    "Tomato___Late_blight": {
        "name_en": "Late Blight",
        "name_hi": "पछेती झुलसा रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Water mold (Phytophthora infestans). Spreads rapidly in cool (10–20°C), wet weather. Can destroy an entire field within 1–2 weeks.",
        "cause_hi": "जल फफूंद (फाइटोफ्थोरा इन्फेस्टैन्स)। ठंडे (10-20°C), गीले मौसम में तेजी से फैलता है। 1-2 सप्ताह में पूरा खेत नष्ट।",
        "symptoms_en": "Water-soaked grey-green lesions on leaves with white mold on undersides in humid weather. Brown rotting fruit. Entire plant collapses rapidly.",
        "symptoms_hi": "पत्तियों पर पानी से भीगे धूसर-हरे घाव, नम मौसम में नीचे सफेद फफूंद। भूरे सड़ते फल।",
        "organic_en": "Copper-based sprays (Bordeaux mixture 1%). Remove and destroy infected plants immediately. Do not compost infected material.",
        "organic_hi": "तांबे आधारित स्प्रे (बोर्डो मिश्रण 1%)। संक्रमित पौधे तुरंत हटाकर नष्ट करें। संक्रमित सामग्री की खाद न बनाएं।",
        "chemical_en": "Metalaxyl + Mancozeb (Ridomil Gold, 2.5g/litre) at first sign. Every 7 days in wet weather without exception. If severe: remove foliage, spray remaining stems.",
        "chemical_hi": "पहले संकेत पर मेटालेक्सिल + मैनकोज़ेब (रिडोमिल गोल्ड, 2.5g/लीटर)। बिना अपवाद नम मौसम में हर 7 दिन।",
        "prevention_en": "Well-drained soil. 60–90cm spacing. Avoid evening irrigation. Stake plants. Resistant varieties where available.",
        "prevention_hi": "अच्छी जल निकासी वाली मिट्टी। 60-90cm दूरी। शाम को सिंचाई न करें। पौधों को सहारा दें।",
        "severity": "High", "yield_loss": "50–100%"
    },

    "Tomato___Leaf_Mold": {
        "name_en": "Leaf Mold",
        "name_hi": "पत्ती फफूंद रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Fungal (Passalora fulva). Almost exclusively a greenhouse problem — favours high humidity (>85%) and poor ventilation.",
        "cause_hi": "फफूंद रोग। लगभग विशेष रूप से ग्रीनहाउस की समस्या — उच्च आर्द्रता (>85%) और खराब वेंटिलेशन।",
        "symptoms_en": "Yellow patches on upper leaf surface. Olive-green to brown velvety mold on undersides. Infected leaves curl upward and dry out.",
        "symptoms_hi": "पत्ती की ऊपरी सतह पर पीले धब्बे। निचली सतह पर जैतून-हरे से भूरे मखमली फफूंद। पत्तियाँ ऊपर मुड़ती और सूखती हैं।",
        "organic_en": "Increase ventilation first — chemicals are secondary. Improve spacing and prune leaves. Copper-based spray. Destroy infected leaves.",
        "organic_hi": "पहले वेंटिलेशन बढ़ाएं — रसायन गौण हैं। दूरी सुधारें और पत्तियाँ छांटें। तांबे आधारित स्प्रे।",
        "chemical_en": "Chlorothalonil or Mancozeb every 7 days. Tebuconazole for systemic control. Reduce humidity — this is the root cause.",
        "chemical_hi": "हर 7 दिन क्लोरोथैलोनिल या मैनकोज़ेब। प्रणालीगत नियंत्रण के लिए टेबुकोनाज़ोल। आर्द्रता कम करें — यही मूल कारण है।",
        "prevention_en": "Maintain humidity below 85%. Space plants adequately. Prune lower leaves for airflow. Avoid wetting foliage.",
        "prevention_hi": "आर्द्रता 85% से नीचे रखें। पर्याप्त दूरी। वायु प्रवाह के लिए निचली पत्तियाँ छांटें। पत्तियाँ गीली न होने दें।",
        "severity": "Medium", "yield_loss": "15–30%"
    },

    "Tomato___Septoria_leaf_spot": {
        "name_en": "Septoria Leaf Spot",
        "name_hi": "सेप्टोरिया पत्ती धब्बा रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Fungal (Septoria lycopersici). Rain splash. Most common after first fruit set in warm, wet weather.",
        "cause_hi": "फफूंद रोग। बारिश के छींटे। गर्म, नम मौसम में पहली फसल के बाद सबसे आम।",
        "symptoms_en": "Many small circular spots — dark brown border, grey-white centre — on lower leaves first. Tiny black pycnidia in centres. Severe defoliation.",
        "symptoms_hi": "पहले निचली पत्तियों पर कई छोटे गोलाकार धब्बे — गहरे भूरे बॉर्डर, धूसर-सफेद केंद्र। गंभीर पत्ती झड़ना।",
        "organic_en": "Remove and destroy infected lower leaves. Mulch to prevent soil splash. Copper spray every 7 days.",
        "organic_hi": "संक्रमित निचली पत्तियाँ हटाकर नष्ट करें। मिट्टी के छींटे रोकने के लिए मल्च। हर 7 दिन कॉपर स्प्रे।",
        "chemical_en": "Mancozeb 75% WP (2g/litre) or Chlorothalonil every 7–10 days. Azoxystrobin for severe cases.",
        "chemical_hi": "हर 7-10 दिन मैनकोज़ेब 75% WP (2g/लीटर) या क्लोरोथैलोनिल। गंभीर मामलों के लिए एज़ोक्सीस्ट्रोबिन।",
        "prevention_en": "3-year rotation. Remove infected debris after harvest. Stake plants off ground. Avoid overhead irrigation. Mulch beds.",
        "prevention_hi": "3 साल का चक्र। फसल के बाद संक्रमित अवशेष हटाएं। पौधों को जमीन से उठाकर सहारा दें। मल्च।",
        "severity": "Medium", "yield_loss": "20–35%"
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "name_en": "Spider Mites (Two-Spotted)",
        "name_hi": "मकड़ी घुन (द्विबिंदु)",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Pest infestation (Tetranychus urticae) — a mite, NOT a fungus. Hot, dry conditions. Reproduces from egg to adult in just 5 days at 30°C.",
        "cause_hi": "कीट संक्रमण — घुन, फफूंद नहीं। गर्म, शुष्क स्थितियाँ। 30°C पर 5 दिन में अंडे से वयस्क।",
        "symptoms_en": "Fine yellow stippling on upper leaf surface. Bronze or silver sheen. Fine webbing on undersides. Tiny moving dots visible with hand lens.",
        "symptoms_hi": "पत्ती की ऊपरी सतह पर महीन पीले बिंदु। कांस्य या चांदी की चमक। निचली सतह पर महीन जाला।",
        "organic_en": "Strong water jets on leaf undersides to dislodge mites. Neem oil spray (5ml/litre) every 5 days. Predatory mites in greenhouses.",
        "organic_hi": "घुन हटाने के लिए पत्ती की निचली सतह पर तेज पानी की धाराएं। हर 5 दिन नीम तेल स्प्रे (5ml/लीटर)।",
        "chemical_en": "Abamectin (0.5ml/litre) or Spiromesifen miticide. Rotate chemicals — mites develop resistance rapidly. NEVER use pyrethroids — they kill natural predators and worsen outbreaks.",
        "chemical_hi": "एबामेक्टिन (0.5ml/लीटर) या स्पाइरोमेसिफेन मिटीसाइड। रसायन बदलते रहें — घुन जल्दी प्रतिरोध विकसित करते हैं। पाइरेथ्रॉइड कभी न उपयोग करें।",
        "prevention_en": "Maintain soil moisture. Avoid dusty conditions. Inspect leaf undersides weekly. Remove weeds that harbour mites.",
        "prevention_hi": "पर्याप्त मिट्टी की नमी। धूल भरी स्थितियों से बचें। साप्ताहिक पत्ती की निचली सतह जांच। घुन पालने वाले खरपतवार हटाएं।",
        "severity": "High", "yield_loss": "30–50%"
    },

    "Tomato___Target_Spot": {
        "name_en": "Target Spot",
        "name_hi": "लक्ष्य धब्बा रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Fungal (Corynespora cassiicola). Warm (24–30°C), humid conditions. Affects leaves, stems, and fruit.",
        "cause_hi": "फफूंद रोग। गर्म (24-30°C), नम स्थितियाँ। पत्तियाँ, तने और फल प्रभावित।",
        "symptoms_en": "Brown spots with concentric rings and yellow halo — similar to Early Blight but larger and more irregular. Dark sunken lesions on fruit.",
        "symptoms_hi": "पीले घेरे के साथ संकेंद्रित छल्लों वाले भूरे धब्बे — अगेती झुलसा जैसे लेकिन बड़े और अनियमित। फल पर गहरे धंसे घाव।",
        "organic_en": "Copper spray every 7 days. Remove infected lower leaves. Improve spacing and airflow.",
        "organic_hi": "हर 7 दिन कॉपर स्प्रे। संक्रमित निचली पत्तियाँ हटाएं। दूरी और वायु प्रवाह सुधारें।",
        "chemical_en": "Azoxystrobin + Difenoconazole (Amistar Top) or Chlorothalonil. Begin sprays early in disease development.",
        "chemical_hi": "एज़ोक्सीस्ट्रोबिन + डाइफेनोकोनाज़ोल (अमिस्टार टॉप) या क्लोरोथैलोनिल। रोग के शुरुआती विकास में स्प्रे शुरू करें।",
        "prevention_en": "Crop rotation. Remove debris after harvest. Staking improves airflow. Drip irrigation preferred.",
        "prevention_hi": "फसल चक्र। फसल के बाद अवशेष हटाएं। सहारा देने से वायु प्रवाह सुधरता है। ड्रिप सिंचाई बेहतर।",
        "severity": "Medium", "yield_loss": "20–35%"
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "name_en": "Yellow Leaf Curl Virus (TYLCV)",
        "name_hi": "पीली पत्ती मुड़न विषाणु रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Viral disease (TYLCV). Transmitted ONLY by whitefly (Bemisia tabaci) — not by contact or tools. Infected plants cannot be cured.",
        "cause_hi": "विषाणु रोग। केवल सफेद मक्खी (बेमिसिया टबेसी) द्वारा फैलाया जाता है — संपर्क या उपकरणों से नहीं। संक्रमित पौधे ठीक नहीं हो सकते।",
        "symptoms_en": "Upward curling and yellowing of leaf margins and interveinal areas. Stunted, bushy plant growth. Flowers drop. Fruit set severely reduced or zero.",
        "symptoms_hi": "पत्ती के हाशिये और शिराओं के बीच ऊपर की ओर मुड़ना और पीला पड़ना। रुकी हुई, झाड़ीदार वृद्धि। फूल झड़ना। फल लगना बहुत कम या शून्य।",
        "organic_en": "Remove and destroy infected plants immediately — permanent virus reservoirs. Yellow sticky traps to monitor whitefly. Reflective silver mulch repels whiteflies.",
        "organic_hi": "संक्रमित पौधे तुरंत हटाकर नष्ट करें — स्थायी वायरस भंडार। सफेद मक्खी निगरानी के लिए पीले चिपचिपे जाल। चांदी परावर्तक मल्च।",
        "chemical_en": "Imidacloprid (0.5ml/litre) or Thiamethoxam to control whitefly vector. Does NOT cure the virus. Remove infected plants regardless.",
        "chemical_hi": "सफेद मक्खी नियंत्रण के लिए इमिडाक्लोप्रिड (0.5ml/लीटर) या थायमेथोक्सम। वायरस ठीक नहीं होता। फिर भी संक्रमित पौधे हटाएं।",
        "prevention_en": "TYLCV-resistant varieties (most effective). Insect-proof netting in nursery. Transplant in evenings. Remove infected plants within 24 hours of detection.",
        "prevention_hi": "TYLCV प्रतिरोधी किस्में (सबसे प्रभावी)। नर्सरी में कीट-प्रूफ जाल। शाम को रोपाई। पहचान के 24 घंटे के भीतर संक्रमित पौधे हटाएं।",
        "severity": "High", "yield_loss": "50–100%"
    },

    "Tomato___Tomato_mosaic_virus": {
        "name_en": "Tomato Mosaic Virus (ToMV)",
        "name_hi": "टमाटर मोजेक विषाणु रोग",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "Viral (Tomato Mosaic Virus). Extremely stable — survives on tools, hands, clothing, and soil for years. Spreads by TOUCH, not insects.",
        "cause_hi": "विषाणु रोग। अत्यंत स्थिर — उपकरणों, हाथों, कपड़ों और मिट्टी में वर्षों तक जीवित। स्पर्श से फैलता है, कीटों से नहीं।",
        "symptoms_en": "Mottled mosaic pattern of light and dark green on leaves. Leaf distortion, curling, blistering. Stunted growth. Fruit yellow blotches or internal browning.",
        "symptoms_hi": "पत्तियों पर हल्के और गहरे हरे रंग का मोज़ेक पैटर्न। पत्ती विकृति, मुड़ना, फफोले। रुकी हुई वृद्धि।",
        "organic_en": "No cure. Remove and destroy infected plants. Disinfect ALL tools with 10% bleach or 70% alcohol between plants. Wash hands thoroughly before handling.",
        "organic_hi": "कोई इलाज नहीं। संक्रमित पौधे हटाकर नष्ट करें। पौधों के बीच 10% ब्लीच या 70% अल्कोहल से सभी उपकरण कीटाणुरहित करें।",
        "chemical_en": "No chemical kills the virus. Disinfect tools with 1% sodium hypochlorite solution. Focus entirely on sanitation and resistant varieties.",
        "chemical_hi": "कोई रासायनिक उपचार वायरस नहीं मारता। 1% सोडियम हाइपोक्लोराइट से उपकरण कीटाणुरहित करें। पूरी तरह स्वच्छता और प्रतिरोध पर ध्यान दें।",
        "prevention_en": "TMV-resistant varieties. Disinfect tools between plants. Do NOT smoke near tomato plants (TMV survives in cured tobacco). Certified seed.",
        "prevention_hi": "TMV प्रतिरोधी किस्में। पौधों के बीच उपकरण कीटाणुरहित करें। टमाटर के पास तंबाकू न पिएं। प्रमाणित बीज।",
        "severity": "Medium", "yield_loss": "10–25%"
    },

    "Tomato___healthy": {
        "name_en": "Healthy", "name_hi": "स्वस्थ",
        "crop_en": "Tomato", "crop_hi": "टमाटर",
        "cause_en": "No disease detected. Plant appears healthy.",
        "cause_hi": "कोई रोग नहीं पाया गया। पौधा स्वस्थ दिखता है।",
        "symptoms_en": "No visible symptoms of disease.",
        "symptoms_hi": "रोग के कोई दृश्य लक्षण नहीं।",
        "organic_en": "Continue regular care. Water at base, not on leaves. Use compost. Weekly monitoring for early signs.",
        "organic_hi": "नियमित देखभाल जारी रखें। पत्तियों पर नहीं, जड़ में पानी दें। कम्पोस्ट उपयोग करें। साप्ताहिक निगरानी।",
        "chemical_en": "No treatment needed. Optional preventive Mancozeb spray at start of humid season.",
        "chemical_hi": "उपचार की आवश्यकता नहीं। नम मौसम की शुरुआत में वैकल्पिक निवारक मैनकोज़ेब स्प्रे।",
        "prevention_en": "Crop rotation. Certified seeds. Stake plants for airflow. Good farming practices.",
        "prevention_hi": "फसल चक्र। प्रमाणित बीज। वायु प्रवाह के लिए पौधों को सहारा दें।",
        "severity": "None", "yield_loss": "0%"
    },

    # ─────────────────────────────────────────────────────
    # DEFAULT FALLBACK
    # ─────────────────────────────────────────────────────

    "default": {
        "name_en": "Disease Detected",
        "name_hi": "रोग का पता चला",
        "crop_en": "Crop", "crop_hi": "फसल",
        "cause_en": "Fungal, bacterial, or viral infection detected. Exact pathogen requires field/laboratory confirmation.",
        "cause_hi": "फफूंद, जीवाणु या विषाणु संक्रमण। सटीक रोगज़नक़ के लिए क्षेत्र/प्रयोगशाला पुष्टि आवश्यक।",
        "symptoms_en": "Visible disease symptoms on leaf — spots, lesions, discolouration, or unusual growth.",
        "symptoms_hi": "पत्ती पर रोग के लक्षण — धब्बे, घाव, रंग परिवर्तन या असामान्य वृद्धि।",
        "organic_en": "Apply neem oil (5ml/litre) as first step. Remove visibly infected leaves. Avoid overhead irrigation. Consult local Krishi Vigyan Kendra (KVK).",
        "organic_hi": "पहले कदम के रूप में नीम तेल (5ml/लीटर) लगाएं। दृश्य रूप से संक्रमित पत्तियाँ हटाएं। स्थानीय KVK से सलाह लें।",
        "chemical_en": "Mancozeb 75% WP (2g/litre) as broad-spectrum preventive. Contact your nearest Krishi Seva Kendra for specific recommendation.",
        "chemical_hi": "मैनकोज़ेब 75% WP (2g/लीटर) व्यापक स्पेक्ट्रम निवारक। विशिष्ट सिफारिश के लिए निकटतम कृषि सेवा केंद्र से संपर्क करें।",
        "prevention_en": "Field hygiene. Crop rotation. Certified seeds. Balanced NPK. Remove and destroy crop debris after harvest.",
        "prevention_hi": "खेत की स्वच्छता। फसल चक्र। प्रमाणित बीज। संतुलित NPK। फसल के बाद अवशेष नष्ट करें।",
        "severity": "Unknown", "yield_loss": "Variable"
    }
}


# ─────────────────────────────────────────────────────────────────────────────
# LOOKUP FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def get_treatment(class_name, language="both"):
    """
    Get treatment data for a predicted class name.
    Exact match → partial match → default fallback.
    """
    if class_name in TREATMENT_DATA:
        return TREATMENT_DATA[class_name]
    for key in TREATMENT_DATA:
        if key == "default":
            continue
        if key.lower() in class_name.lower() or class_name.lower() in key.lower():
            return TREATMENT_DATA[key]
    return TREATMENT_DATA["default"]


def format_report(class_name, confidence):
    """Formatted bilingual CLI diagnosis report."""
    data = get_treatment(class_name)
    pct  = f"{confidence * 100:.1f}%"
    return f"""
╔══════════════════════════════════════════╗
         🌿 CROPSENSE DIAGNOSIS REPORT
╚══════════════════════════════════════════╝

📊 Confidence: {pct}
⚠️  Severity: {data['severity']} | Yield Loss Risk: {data['yield_loss']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 DISEASE / रोग
   EN: {data['name_en']} ({data['crop_en']})
   HI: {data['name_hi']} ({data['crop_hi']})

🔬 CAUSE / कारण
   EN: {data['cause_en']}
   HI: {data['cause_hi']}

🌱 ORGANIC TREATMENT / जैविक उपचार
   EN: {data['organic_en']}
   HI: {data['organic_hi']}

💊 CHEMICAL TREATMENT / रासायनिक उपचार
   EN: {data['chemical_en']}
   HI: {data['chemical_hi']}

🛡️  PREVENTION / रोकथाम
   EN: {data['prevention_en']}
   HI: {data['prevention_hi']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Kisan Call Centre: 1800-180-1551 (Free · 24/7 · Hindi available)
"""


# ─────────────────────────────────────────────────────────────────────────────
# SELF-TEST
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    EXPECTED = [
        "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
        "Blueberry___healthy",
        "Cherry_(including_sour)___Powdery_mildew", "Cherry_(including_sour)___healthy",
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn_(maize)___Common_rust_",
        "Corn_(maize)___Northern_Leaf_Blight", "Corn_(maize)___healthy",
        "Grape___Black_rot", "Grape___Esca_(Black_Measles)",
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
        "Orange___Haunglongbing_(Citrus_greening)",
        "Peach___Bacterial_spot", "Peach___healthy",
        "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy",
        "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
        "Raspberry___healthy", "Soybean___healthy", "Squash___Powdery_mildew",
        "Strawberry___Leaf_scorch", "Strawberry___healthy",
        "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight",
        "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
        "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Target_Spot",
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
        "Tomato___healthy",
    ]

    missing = [c for c in EXPECTED if c not in TREATMENT_DATA]
    extra   = [c for c in TREATMENT_DATA if c not in EXPECTED and c != "default"]

    print(f"Classes in TREATMENT_DATA : {len(TREATMENT_DATA) - 1}  (excl. default)")
    print(f"Expected (PlantVillage)   : {len(EXPECTED)}")
    print("Missing :", missing if missing else "None — all 38 covered ✅")
    print("Extra   :", extra   if extra   else "None ✅")
    print()
    print(format_report("Tomato___Early_blight", 0.94))
    print(format_report("Tomato___Spider_mites Two-spotted_spider_mite", 0.88))
    print(format_report("Orange___Haunglongbing_(Citrus_greening)", 0.76))
    print(format_report("Potato___Late_blight", 0.91))