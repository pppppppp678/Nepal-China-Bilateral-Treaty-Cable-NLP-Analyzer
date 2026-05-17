import streamlit as st
import pandas as pd
import plotly.express as px
import os
from diplomatic_analyzer import NepalChinaDiplomaticAnalyzer

# १. प्रिमियम एम्बेसी-ग्रेड डार्क थिम सेटअप
st.set_page_config(page_title="Nepal-China Diplomatic Intelligence", page_icon="📜", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #08070E; color: #E4E4E7; }
    .diplomat-title { font-size:32px !important; font-weight: 800 !important; color: #DC2626; letter-spacing: -0.5px; }
    .diplomat-sub { font-size:13px !important; color: #A1A1AA; margin-bottom: 25px; }
    .critical-card { background-color: #450A0A; border: 1px solid #991B1B; padding: 18px; border-radius: 6px; margin-bottom: 12px; }
    .tech-badge { font-family: 'Fira Code', monospace; background-color: #1E1B4B; color: #818CF8; padding: 2px 6px; border-radius: 4px; font-size:11px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="diplomat-title">📜 NEPAL-CHINA BILATERAL TREATY & CABLE NLP ANALYZER</p>', unsafe_allow_html=True)
st.markdown('<p class="diplomat-sub">Foreign Services Automation Matrix | Applied Semantic Risk Auditing Platform</p>', unsafe_allow_html=True)
st.divider()

# इन्जिन इनिसियलाइज गर्ने
analyzer = NepalChinaDiplomaticAnalyzer()

# साइडबार ब्रान्डिङ
st.sidebar.markdown("<h2 style='color:#DC2626; text-align:center;'>战略情报</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; font-size:12px; color:#A1A1AA;'>Strategic Intelligence Unit</p>", unsafe_allow_html=True)
st.sidebar.divider()
console_view = st.sidebar.radio("Select Intelligence Deck:", ["📂 Document Ingestion Fleet", "🦅 Legal Risk & Leverage Audit"])

# ==================== MODE 1: DOCUMENT INGESTION ====================
if console_view == "📂 Document Ingestion Fleet":
    st.markdown("### 📥 Structural Document Pipeline Gateway")
    st.write("नेपाल र चीनबीच भएका सम्झौताका पाठहरूलाई ब्याकइन्डमा पार्सिङ गर्न र शब्दहरूको सूचकाङ्क बनाउन तलको बटन थिच्नुहोस्।")
    
    if st.button("🔌 Execute Document Synchronization Pipeline"):
        with st.spinner("Processing legal syntax tensors..."):
            m1 = analyzer.simulate_treaty_ingestion()
            m2 = analyzer.execute_nlp_semantic_mining()
            st.success("Bilateral Data Lake Synchronized Successfully!")
            st.toast("Gold Layer Processed!")
            
    if os.path.exists(analyzer.silver_path):
        df = pd.read_csv(analyzer.silver_path)
        st.markdown("#### 📑 Active Transformed Metadata Registers")
        st.dataframe(df.tail(8), use_container_width=True, hide_index=True)
    else:
        st.info("Trigger the pipeline sync to process raw bilateral agreements text files.")

# ==================== MODE 2: RISK & LEVERAGE AUDIT ====================
else:
    st.markdown("### 🦅 Legal Sovereign Sovereignty & Threat Matrix Auditing")
    
    if os.path.exists(analyzer.silver_path):
        df = pd.read_csv(analyzer.silver_path)
        
        # म्याट्रिक्स गणनाहरू
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1: st.metric("Withdrawn Directives", len(df))
        with col_m2: st.metric("Critical Risk Flags", len(df[df["Strategic_Threat_Level"] == "CRITICAL"]))
        with col_m3: st.metric("Mean Risk Coefficient Score", f"{df['Risk_Index_Score'].mean():.2f}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ----- नयाँ फिचर: देशगत फाइदाहरूको भिजुअलाइजेशन -----
        st.markdown("### 🏛️ Geopolitical Benefit & Impact Distribution Matrix")
        
        # सिमुलेटेड फाइदाहरूको डेटाबेस
        benefit_data = pd.DataFrame({
            "Country": ["Nepal", "Nepal", "Nepal", "China", "China", "China"],
            "Sector": ["Infrastructure & Rail", "Trade & Energy Grid", "Agriculture Grants", "Strategic Border Security", "Transit Access Route", "Soft Power Influx"],
            "Impact_Score": [85, 72, 65, 88, 76, 82],
            "Funding_Type": ["60% Loan / 40% Grant", "Bilateral Investment", "100% Pure Grant", "Strategic Alignment", "Commercial Access", "Diplomatic Influence"]
        })
        
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.markdown("#### 🔹 Mutual Strategic Benefits by Sector")
            fig_bar = px.bar(
                benefit_data, 
                x="Country", 
                y="Impact_Score", 
                color="Sector", 
                barmode="group",
                text="Impact_Score",
                template="plotly_dark",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig_bar.update_traces(textposition='outside')
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with col_chart2:
            st.markdown("#### 🔹 Leverage Points & Resource Distribution")
            fig_pie = px.pie(
                benefit_data, 
                names="Funding_Type", 
                values="Impact_Score",
                template="plotly_dark",
                color_discrete_sequence=px.colors.sequential.Oranges_r
            )
            st.plotly_chart(fig_pie, use_container_width=True)
            
        st.divider()
        
        # पुराना रिस्क एनालिटिक्स ग्राफहरू
        col_g1, col_g2 = st.columns([6, 4])
        with col_g1:
            st.markdown("#### 📈 Document Risk Profile Distribution")
            fig1 = px.box(df, x="Category", y="Risk_Index_Score", color="Financial_Model", template="plotly_dark", color_discrete_sequence=px.colors.sequential.Reds_r)
            st.plotly_chart(fig1, use_container_width=True)
            
        with col_g2:
            st.markdown("#### 🎯 Threat Matrix Segment")
            fig2 = px.pie(df, names="Strategic_Threat_Level", template="plotly_dark", color_discrete_sequence=["#991B1B", "#D97706", "#047857"])
            st.plotly_chart(fig2, use_container_width=True)
            
        st.divider()
        st.markdown("#### ⚠️ High Risk Sovereign Exposure Alert (NLP Inference Triggered)")
        
        critical_items = df[df["Strategic_Threat_Level"] == "CRITICAL"].tail(2)
        if not critical_items.empty:
            for _, row in critical_items.iterrows():
                st.markdown(f"""
                <div class="critical-card">
                    <span class="tech-badge">RISK INDEX: {row['Risk_Index_Score']}</span>
                    <h4 style="margin: 8px 0 2px 0; color:#FCA5A5;">🛑 {row['Title']}</h4>
                    <p style="margin:0; font-size:12px; color:#F4F4F5;">Legal Category: <b>{row['Category']}</b> | Pipeline Flag: <b>{row['Financial_Model']}</b></p>
                    <p style="margin:4px 0 0 0; font-size:11px; color:#FDA4AF;">Jurisdiction Framework Notice: Clauses mention external jurisdiction dependencies (Beijing Courts/Radar).</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("Sovereignty Risk Matrix shows baseline safe configurations across current data streams.")
