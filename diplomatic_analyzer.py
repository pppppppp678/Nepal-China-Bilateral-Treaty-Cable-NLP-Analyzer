import pandas as pd
import numpy as np
import json
import os
import re
from datetime import datetime

class NepalChinaDiplomaticAnalyzer:
    def __init__(self):
        self.bronze_dir = "diplomatic_intelligence/bronze_treaties"
        self.silver_path = "diplomatic_intelligence/silver_analyzed_cables.csv"
        os.makedirs(self.bronze_dir, exist_ok=True)
        
    def simulate_treaty_ingestion(self):
        """
        १. BRONZE LAYER: नेपाल-चीन सम्झौता र कूटनीतिक केबल्सको वास्तविक जस्तै पाठ सिमुलेट गर्ने
        """
        mock_documents = [
            {
                "doc_id": "TREATY_2026_01",
                "title": "Framework Agreement on Cross-Border Railway Connectivity",
                "type": "Bilateral Treaty",
                "text": "The Ministry of Infrastructure of Nepal and the National Railway Administration of China agree to construct a rail link connecting Keyrung to Kathmandu. China provides a 60% loan component and 40% grant. Legal disputes will be arbitrated exclusively under Chinese maritime and trade laws in Beijing courts.",
                "signatories": ["MoID Nepal", "NRA China"],
                "date": "2026-01-15"
            },
            {
                "doc_id": "CABLE_2026_A",
                "title": "Confidential Briefing on Northern Border Security Infrastructure",
                "type": "Diplomatic Cable",
                "text": "Diplomatic communication signals strong Chinese insistence on installing advanced communication radar arrays along the northern checkpoints of Mustang and Tatopani to monitor regional movements. Financial assistance offered is $15 Million USD.",
                "signatories": ["Ministry of Foreign Affairs China", "MoFA Nepal"],
                "date": "2026-03-10"
            },
            {
                "doc_id": "TREATY_2026_02",
                "title": "MoU on Agricultural Technology and Food Security Cooperation",
                "type": "MoU",
                "text": "China agrees to supply eco-friendly hybrid seeds and technical training programs to Nepali cooperative banking unions and farmers. This is a 100% grant-based initiative with zero bilateral financial interest or sovereign guarantees required.",
                "signatories": ["Ministry of Agriculture Nepal", "MOFCOM China"],
                "date": "2026-04-05"
            }
        ]
        
        # ५० वटा र्यान्डम कूटनीतिक रेकर्डहरू जेनेरेट गर्ने (Data Stream Simulation)
        extended_fleet = []
        for i in range(45):
            selected = np.random.choice(mock_documents)
            copied = selected.copy()
            copied["doc_id"] = f"{selected['type'].split()[0].upper()}_{1000 + i}"
            copied["date"] = f"2026-05-{np.random.randint(1, 17):02d}"
            extended_fleet.append(copied)
            
        with open(os.path.join(self.bronze_dir, "raw_treaty_dump.json"), "w") as f:
            json.dump(extended_fleet, f, indent=4)
        return f"Successfully Ingested {len(extended_fleet)} Geopolitical Treaty Blocks into Bronze Storage."

    def execute_nlp_semantic_mining(self):
        """
        २. SILVER & GOLD LAYER: कानुनी जोखिम र सफ्ट पावर सूचकहरू गणना गर्ने NLP इन्जिन
        """
        raw_file = os.path.join(self.bronze_dir, "raw_treaty_dump.json")
        if not os.path.exists(raw_file):
            return "Error: Ingestion payload not detected."
            
        with open(raw_file, "r") as f:
            docs = json.load(f)
            
        processed_data = []
        
        for doc in docs:
            text_lower = doc["text"].lower()
            
            # NLP Rule-Based Feature Extraction (सिनियर आर्किटेक्चर प्याटर्न)
            # क) वित्तीय प्रकृति पत्ता लगाउने (Financial Nature)
            if "loan" in text_lower:
                finance_type = "Loan Dominated (Debt Exposure)"
                base_risk = 0.55
            elif "grant" in text_lower and "loan" not in text_lower:
                finance_type = "Pure Grant (Soft Power Influx)"
                base_risk = 0.10
            else:
                finance_type = "Bilateral Cooperation"
                base_risk = 0.25
                
            # ख) सार्वभौम वा कानुनी जोखिम मापन (Sovereign Risk Matrix)
            risk_score = base_risk
            if "arbitrated" in text_lower or "beijing courts" in text_lower:
                risk_score += 0.35 # बाह्य अदालतको अधिकार क्षेत्र हुँदा जोखिम बढ्छ
            if "radar" in text_lower or "security" in text_lower or "monitor" in text_lower:
                risk_score += 0.25 # सुरक्षा सम्बन्धी विषयमा उच्च संवेदनशीलता
                
            # ग) डलर वा रकम पार्सिङ (Regex Metadata Mining)
            monetary_match = re.search(r'\$?(\d+)\s*(?:Million|Billion)?\s*(?:USD|%|NPR)?', doc["text"])
            extracted_metric = monetary_match.group(0) if monetary_match else "Unspecified Value"

            processed_data.append({
                "Document_ID": doc["doc_id"],
                "Title": doc["title"],
                "Category": doc["type"],
                "Financial_Model": finance_type,
                "Extracted_Metric": extracted_metric,
                "Risk_Index_Score": round(risk_score, 2),
                "Strategic_Threat_Level": "CRITICAL" if risk_score >= 0.70 else "MODERATE" if risk_score >= 0.40 else "LOW",
                "Analysis_Date": doc["date"]
            })
            
        df = pd.DataFrame(processed_data)
        df.to_csv(self.silver_path, index=False)
        return f"NLP Intelligence Suite execution completed. Silver layer structured matrix generated."
