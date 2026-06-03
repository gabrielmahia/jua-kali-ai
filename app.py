import streamlit as st
import urllib.request, json
st.set_page_config(page_title="Jua Kali AI — Msaada wa Mafundi", page_icon="🔨", layout="centered")
st.markdown("""<style>.stApp{background:#0a0800;color:#fff8e1}
.j-card{background:#1a1200;border:1px solid #f57f17;border-radius:10px;padding:14px 18px;margin:8px 0}
.stButton>button{background:#e65100;color:#fff;border:none;border-radius:8px;padding:10px 24px;font-weight:700;width:100%}
</style>""", unsafe_allow_html=True)
API_KEY = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY","")
SYS = "Wewe ni mshauri wa uchumi wa Jua Kali Kenya. Jibu kwa Kiswahili. Saidia mafundi: usajili wa biashara, masoko, ushirika, cheti, na ukuaji wa biashara ndogo."
def ask(q):
    if not API_KEY: return "❌ API key not configured."
    url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    body={"contents":[{"role":"user","parts":[{"text":q}]}],"systemInstruction":{"parts":[{"text":SYS}]},"generationConfig":{"temperature":0.3,"maxOutputTokens":700}}
    try:
        req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={"Content-Type":"application/json"},method="POST")
        with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read())["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e: return f"❌ {e}"
st.markdown("# 🔨 Jua Kali AI"); st.markdown("**Msaada wa Mafundi wa Kenya — Kukua Biashara**")
st.info("Kenya ina wafanyakazi 3M+ wa Jua Kali — kizazi cha uchumi hasa nje ya ajira rasmi.")
tab1,tab2,tab3,tab4=st.tabs(["📋 Usajili","📈 Ukuaji","🤝 Ushirika","🏅 Vyeti"])
with tab1:
    trade=st.selectbox("Fundi wa nini:",["Useremala (Carpentry)","Uchomeleaji (Welding)","Umeme","Plumbing","Magari (Mechanics)","Ushonaji (Tailoring)","Ujenzi","Upigaji picha"])
    if st.button("📋 Usajili wa Biashara",key="jk1"):
        with st.spinner("..."): r=ask(f"Jinsi ya kusajili biashara ya {trade} Kenya kama Jua Kali artisan. Toa: KEBS, KIE (Kenya Industrial Estates), bodi ya Jua Kali ya kaunti, gharama, muda.")
        st.markdown(f'<div class="j-card">{r.replace(chr(10),"<br>")}</div>',unsafe_allow_html=True)
with tab2:
    challenge=st.selectbox("Changamoto yako:",["Kutafuta wateja zaidi","Kupata mtaji (capital)","Kupanua biashara","Kuajiri wafanyakazi","Kuweka bei sahihi","Masoko ya nje ya nchi"])
    if st.button("📈 Suluhisho",key="jk2"):
        with st.spinner("..."): r=ask(f"Mfundi wa Jua Kali ana changamoto ya: {challenge}. Toa suluhisho la vitendo la Kenya na rasilimali za KIE au KeNIA.")
        st.markdown(f'<div class="j-card">{r.replace(chr(10),"<br>")}</div>',unsafe_allow_html=True)
with tab3:
    if st.button("🤝 Jinsi ya Kuunda Ushirika wa Jua Kali",key="jk3"):
        with st.spinner("..."): r=ask("Hatua za kuunda ushirika (cooperative) wa Jua Kali Kenya. Toa: Usajili wa Cooperatives Societies Act, idadi ya wanachama, michango, faida za ushirika dhidi ya peke yangu.")
        st.markdown(f'<div class="j-card">{r.replace(chr(10),"<br>")}</div>',unsafe_allow_html=True)
with tab4:
    if st.button("🏅 Vyeti vya NITA na KEBS",key="jk4"):
        with st.spinner("..."): r=ask("Vyeti vinavyosaidia mafundi wa Jua Kali Kenya: NITA (National Industrial Training Authority), KEBS, TVET. Jinsi ya kupata, gharama, faida za mshahara na masoko.")
        st.markdown(f'<div class="j-card">{r.replace(chr(10),"<br>")}</div>',unsafe_allow_html=True)
st.markdown("---"); st.caption("🔨 Jua Kali AI v1.0 | KIE: kie.co.ke | NITA: nita.go.ke | CC BY-NC-ND 4.0")
