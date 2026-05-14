# CropSense — Treatment Advice Engine
# Bilingual: Hindi + English

TREATMENT_DATA = {

    "Tomato___Early_blight": {
        "name_en": "Early Blight",
        "name_hi": "अगेती झुलसा रोग",
        "crop_en": "Tomato",
        "crop_hi": "टमाटर",
        "cause_en": "Fungal infection (Alternaria solani). Spreads in warm, humid conditions.",
        "cause_hi": "फफूंद संक्रमण (अल्टरनेरिया सोलानी)। गर्म और नम मौसम में फैलता है।",
        "symptoms_en": "Dark brown spots with yellow rings on lower leaves.",
        "symptoms_hi": "निचली पत्तियों पर पीले छल्लों के साथ गहरे भूरे धब्बे।",
        "organic_en": "Spray neem oil (5ml/litre) every 7 days. Remove infected leaves immediately.",
        "organic_hi": "हर 7 दिन में नीम का तेल (5ml/लीटर) स्प्रे करें। संक्रमित पत्तियां तुरंत हटाएं।",
        "chemical_en": "Apply Mancozeb 75% WP (2g/litre) or Chlorothalonil spray.",
        "chemical_hi": "मैनकोज़ेब 75% WP (2g/लीटर) या क्लोरोथैलोनिल स्प्रे करें।",
        "prevention_en": "Crop rotation every season. Avoid overhead watering. Use resistant varieties.",
        "prevention_hi": "हर मौसम में फसल बदलें। ऊपर से पानी देने से बचें। प्रतिरोधी किस्में उगाएं।",
        "severity": "Medium",
        "yield_loss": "20-30%"
    },

    "Tomato___Late_blight": {
        "name_en": "Late Blight",
        "name_hi": "पछेती झुलसा रोग",
        "crop_en": "Tomato",
        "crop_hi": "टमाटर",
        "cause_en": "Water mold (Phytophthora infestans). Spreads rapidly in cool, wet weather.",
        "cause_hi": "जल फफूंद (फाइटोफ्थोरा इन्फेस्टैन्स)। ठंडे, गीले मौसम में तेजी से फैलता है।",
        "symptoms_en": "Water-soaked lesions on leaves, white mold on undersides, brown fruit rot.",
        "symptoms_hi": "पत्तियों पर पानी से भीगे धब्बे, नीचे की तरफ सफेद फफूंद, फल सड़न।",
        "organic_en": "Copper-based sprays (Bordeaux mixture). Remove and destroy infected plants.",
        "organic_hi": "तांबे आधारित स्प्रे (बोर्डो मिश्रण)। संक्रमित पौधे हटाकर नष्ट करें।",
        "chemical_en": "Apply Metalaxyl + Mancozeb (Ridomil Gold) at first sign of disease.",
        "chemical_hi": "रोग के पहले संकेत पर मेटालेक्सिल + मैनकोज़ेब (रिडोमिल गोल्ड) लगाएं।",
        "prevention_en": "Plant in well-drained soil. Maintain spacing. Avoid evening irrigation.",
        "prevention_hi": "अच्छी जल निकासी वाली मिट्टी में लगाएं। उचित दूरी रखें। शाम को सिंचाई न करें।",
        "severity": "High",
        "yield_loss": "50-80%"
    },

    "Tomato___healthy": {
        "name_en": "Healthy",
        "name_hi": "स्वस्थ",
        "crop_en": "Tomato",
        "crop_hi": "टमाटर",
        "cause_en": "No disease detected.",
        "cause_hi": "कोई रोग नहीं पाया गया।",
        "symptoms_en": "Plant appears healthy.",
        "symptoms_hi": "पौधा स्वस्थ दिखता है।",
        "organic_en": "Continue regular care. Water at base of plant. Use compost.",
        "organic_hi": "नियमित देखभाल जारी रखें। पौधे की जड़ में पानी दें। कम्पोस्ट का उपयोग करें।",
        "chemical_en": "No treatment needed. Preventive spraying optional.",
        "chemical_hi": "उपचार की आवश्यकता नहीं। वैकल्पिक रूप से निवारक छिड़काव करें।",
        "prevention_en": "Maintain good farming practices to keep plants healthy.",
        "prevention_hi": "पौधों को स्वस्थ रखने के लिए अच्छी कृषि पद्धतियां अपनाएं।",
        "severity": "None",
        "yield_loss": "0%"
    },

    "Potato___Early_blight": {
        "name_en": "Early Blight",
        "name_hi": "अगेती झुलसा रोग",
        "crop_en": "Potato",
        "crop_hi": "आलू",
        "cause_en": "Fungal infection (Alternaria solani).",
        "cause_hi": "फफूंद संक्रमण (अल्टरनेरिया सोलानी)।",
        "symptoms_en": "Circular brown spots with concentric rings on older leaves.",
        "symptoms_hi": "पुरानी पत्तियों पर गोलाकार भूरे धब्बे।",
        "organic_en": "Neem oil spray. Remove infected leaves. Maintain plant nutrition.",
        "organic_hi": "नीम तेल स्प्रे। संक्रमित पत्तियां हटाएं। पौधे का पोषण बनाए रखें।",
        "chemical_en": "Mancozeb 75% WP (2.5g/litre) spray every 10-15 days.",
        "chemical_hi": "हर 10-15 दिन में मैनकोज़ेब 75% WP (2.5g/लीटर) स्प्रे करें।",
        "prevention_en": "Use certified disease-free seed tubers. Proper crop rotation.",
        "prevention_hi": "प्रमाणित रोग मुक्त बीज कंद का उपयोग करें। उचित फसल चक्र अपनाएं।",
        "severity": "Medium",
        "yield_loss": "15-25%"
    },

    "Potato___Late_blight": {
        "name_en": "Late Blight",
        "name_hi": "पछेती झुलसा रोग",
        "crop_en": "Potato",
        "crop_hi": "आलू",
        "cause_en": "Water mold (Phytophthora infestans). Most destructive potato disease.",
        "cause_hi": "जल फफूंद। आलू की सबसे विनाशकारी बीमारी।",
        "symptoms_en": "Dark water-soaked spots on leaves. Rotting tubers with foul smell.",
        "symptoms_hi": "पत्तियों पर गहरे पानी से भीगे धब्बे। बदबूदार सड़े हुए कंद।",
        "organic_en": "Bordeaux mixture spray. Destroy infected plant material.",
        "organic_hi": "बोर्डो मिश्रण स्प्रे। संक्रमित पौधे सामग्री नष्ट करें।",
        "chemical_en": "Cymoxanil + Mancozeb spray. Harvest early if disease is severe.",
        "chemical_hi": "साइमोक्सेनिल + मैनकोज़ेब स्प्रे। रोग गंभीर हो तो जल्दी फसल काटें।",
        "prevention_en": "Resistant varieties. Good drainage. Hilling up soil around plants.",
        "prevention_hi": "प्रतिरोधी किस्में। अच्छी जल निकासी। पौधों के चारों ओर मिट्टी चढ़ाएं।",
        "severity": "High",
        "yield_loss": "40-70%"
    },

    "Corn_(maize)___Common_rust_": {
        "name_en": "Common Rust",
        "name_hi": "सामान्य रतुआ रोग",
        "crop_en": "Corn (Maize)",
        "crop_hi": "मक्का",
        "cause_en": "Fungal infection (Puccinia sorghi). Spreads through wind-borne spores.",
        "cause_hi": "फफूंद संक्रमण। हवा से फैलने वाले बीजाणुओं द्वारा फैलता है।",
        "symptoms_en": "Brick-red to brown pustules on both leaf surfaces.",
        "symptoms_hi": "दोनों पत्ती की सतहों पर ईंट-लाल से भूरे रंग के फुंसी।",
        "organic_en": "Remove heavily infected leaves. Improve air circulation.",
        "organic_hi": "अधिक संक्रमित पत्तियां हटाएं। वायु संचार सुधारें।",
        "chemical_en": "Propiconazole or Tebuconazole fungicide spray at early infection.",
        "chemical_hi": "प्रारंभिक संक्रमण पर प्रोपिकोनाज़ोल या टेबुकोनाज़ोल फफूंदनाशी स्प्रे।",
        "prevention_en": "Plant rust-resistant hybrids. Early planting to avoid peak spore season.",
        "prevention_hi": "रतुआ प्रतिरोधी संकर किस्में लगाएं। शिखर बीजाणु मौसम से बचने के लिए जल्दी बुवाई करें।",
        "severity": "Medium",
        "yield_loss": "10-20%"
    },

    "default": {
        "name_en": "Disease Detected",
        "name_hi": "रोग का पता चला",
        "crop_en": "Crop",
        "crop_hi": "फसल",
        "cause_en": "Fungal or bacterial infection detected.",
        "cause_hi": "फफूंद या बैक्टीरियल संक्रमण का पता चला।",
        "symptoms_en": "Visible disease symptoms on leaf.",
        "symptoms_hi": "पत्ती पर रोग के लक्षण दिखाई दे रहे हैं।",
        "organic_en": "Consult local agricultural extension officer. Apply neem oil as first step.",
        "organic_hi": "स्थानीय कृषि अधिकारी से सलाह लें। पहले कदम के रूप में नीम तेल लगाएं।",
        "chemical_en": "Contact your nearest Krishi Seva Kendra for specific fungicide recommendation.",
        "chemical_hi": "विशिष्ट फफूंदनाशी सिफारिश के लिए निकटतम कृषि सेवा केंद्र से संपर्क करें।",
        "prevention_en": "Maintain field hygiene. Crop rotation. Use certified seeds.",
        "prevention_hi": "खेत की स्वच्छता बनाए रखें। फसल चक्र अपनाएं। प्रमाणित बीज का उपयोग करें।",
        "severity": "Unknown",
        "yield_loss": "Variable"
    }
}


def get_treatment(class_name, language="both"):
    """
    Get treatment advice for a detected disease class.
    Returns bilingual treatment info.
    """
    # Try exact match first
    if class_name in TREATMENT_DATA:
        data = TREATMENT_DATA[class_name]
    else:
        # Try partial match
        matched = None
        for key in TREATMENT_DATA:
            if key.lower() in class_name.lower() or class_name.lower() in key.lower():
                matched = key
                break
        data = TREATMENT_DATA.get(matched, TREATMENT_DATA["default"])

    return data


def format_report(class_name, confidence):
    """
    Format a clean bilingual diagnosis report.
    """
    data = get_treatment(class_name)
    confidence_pct = f"{confidence*100:.1f}%"

    report = f"""
╔══════════════════════════════════════════╗
         🌿 CROPSENSE DIAGNOSIS REPORT
╚══════════════════════════════════════════╝

📊 Confidence: {confidence_pct}
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
💡 For expert advice: Call Kisan Call Centre 1800-180-1551 (Free)
💡 विशेषज्ञ सलाह के लिए: किसान कॉल सेंटर 1800-180-1551 (निशुल्क)
    """
    return report


# ── TEST IT ──
if __name__ == "__main__":
    print(format_report("Tomato___Early_blight", 0.94))
    print(format_report("Potato___Late_blight", 0.88))