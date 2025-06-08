import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

from PIL import Image
import pandas as pd
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Sample Excel Template Download
from io import BytesIO





st.set_page_config(page_title="IFRS 17 CSM Calculator", layout="centered")


# 🌐 Multilingual Setup
translations = {
    "en": {
        "title": "📘 IFRS 17 Contractual Service Margin Calculator",
        "step1": "Step 1: Enter Assumptions",
        "step2": "Step 2: Calculate Contractual Service Margin",
        "upload": "Upload Excel File",
        "calculate": "Calculate Contractual Service Margin",
        "csm_release_title": "📊 Contractual Service Margin Movements",
        "ra_release_title": "📊 Risk Adjustment Release",
        "cashflow_title": "📊 Insurance Cash Flows",
        "projection_years": "Projection Years",
        "discount_rate": "Discount Rate (%)",
        "ra_percent": "Risk Adjustment (%)",
        "use_excel": "Use Excel Input",
        "manual_input": "Manual Input",
        "coverage_unit_option": "Coverage Unit Specification",
        "coverage_unit_default": "Default (Proportional)",
        "coverage_unit_excel": "From Excel Upload",
        "language_selector": "🌍 Choose Language",
        "input_premium": "Premiums (Comma separated)",
        "input_benefit": "Benefits (Comma separated)",
        "input_expense": "Expenses (Comma separated)",
        "input_coverage": "Coverage Units (Comma separated)",
        "excel_headers": {
            "Premium": "Premium",
            "Benefit": "Benefit",
            "Expense": "Expense",
            "CoverageUnits": "CoverageUnits"
        },
        "download_template": "📥 Download Sample Excel Template",
        "contact_us": "Contact Us",
        "your_name": "Your Name",
        "your_email": "Your Email",
        "your_message": "Your Message or Inquiry",
        "submit": "Submit",
        "form_success": "Thank you! We'll be in touch shortly.",
        "form_error": "Please fill in all fields.",
        "about": "About This App",
        "about_text": "This IFRS 17 CSM Calculator is intended for educational and illustrative purposes only. It simplifies the standard for easier understanding and is not meant for production-level actuarial valuation.",
        "disclaimer": "Disclaimer",
        "disclaimer_text": "Results are based on user-provided assumptions and inputs. Please consult a qualified actuary before making any financial or reporting decisions based on this tool.",
        "scenario_analysis": "Scenario Analysis (Optional)",
        "download_scenario_template": "📥 Download Scenario Excel Template",
        "scenario_upload_label": "Upload Scenario Excel File",
        "scenario_chart_title": "📊 CSM by Scenario"


    },
    "zh": {
        "title": "📘 IFRS 17 合同服务边际 计算器",
        "step1": "步骤一：输入假设",
        "step2": "步骤二：计算 合同服务边际",
        "upload": "上传 Excel 文件",
        "calculate": "计算 合同服务边际",
        "csm_release_title": "📊 合同服务边际 变动图",
        "ra_release_title": "📊 风险调整释放图",
        "cashflow_title": "📊 保单现金流图",
        "projection_years": "预测年数",
        "discount_rate": "贴现率 (%)",
        "ra_percent": "风险调整 (%)",
        "use_excel": "使用 Excel 输入",
        "manual_input": "手动输入",
        "coverage_unit_option": "服务期单位选项",
        "coverage_unit_default": "默认（按比例释放）",
        "coverage_unit_excel": "从 Excel 上传",
        "language_selector": "🌍 选择语言",
        "input_premium": "保费（用逗号分隔）",
        "input_benefit": "理赔（用逗号分隔）",
        "input_expense": "费用（用逗号分隔）",
        "input_coverage": "保障期限单位（用逗号分隔）",
        "excel_headers": {
            "Premium": "保费",
            "Benefit": "赔付",
            "Expense": "费用",
            "CoverageUnits": "服务期单位"
        },
        "download_template": "📥 下载示例 Excel 模板",
        "contact_us": "联系我们",
        "your_name": "您的姓名",
        "your_email": "您的邮箱",
        "your_message": "您的留言或咨询内容",
        "submit": "提交",
        "form_success": "感谢您的联系！我们会尽快回复您。",
        "form_error": "请填写所有字段。",
        "about": "关于本应用",
        "about_text": "本IFRS 17 合同服务边际计算器仅用于教育和说明用途。在过程中简化了标准以便于理解，并不用于正式精算评估。",
        "disclaimer": "免责声明",
        "disclaimer_text": "结果基于用户提供的假设和输入。在根据本工具做出任何财务或报告决策之前，请咨询符合资质的正精算师。",
        "scenario_analysis": "情景分析（可选）",
        "download_scenario_template": "📥 下载情景分析 Excel 模板",
        "scenario_upload_label": "上传情景分析文件",
        "scenario_chart_title": "📊 各情景下的 CSM 比较"

    },
    "fr": {
        "title": "📘 Calculateur de Marge de Service Contractuelle IFRS 17",
        "step1": "Étape 1 : Saisir les hypothèses",
        "step2": "Étape 2 : Calculer la Marge de Service Contractuelle",
        "upload": "Télécharger un fichier Excel",
        "calculate": "Calculer la Marge de Service Contractuelle",
        "csm_release_title": "📊 Mouvements de la Marge de Service Contractuelle",
        "ra_release_title": "📊 Libération de l'ajustement de risque",
        "cashflow_title": "📊 Flux de trésorerie d'assurance",
        "projection_years": "Années de projection",
        "discount_rate": "Taux d'actualisation (%)",
        "ra_percent": "Ajustement pour risque (%)",
        "use_excel": "Utiliser l'entrée Excel",
        "manual_input": "Saisie manuelle",
        "coverage_unit_option": "Spécification des unités de couverture",
        "coverage_unit_default": "Par défaut (proportionnel)",
        "coverage_unit_excel": "Depuis le fichier Excel",
        "language_selector": "🌍 Choisir la langue",
        "input_premium": "Primes (séparées par des virgules)",
        "input_benefit": "Prestations (séparées par des virgules)",
        "input_expense": "Frais (séparés par des virgules)",
        "input_coverage": "Unités de couverture (séparées par des virgules)",
        "excel_headers": {
            "Premium": "Prime",
            "Benefit": "Prestation",
            "Expense": "Frais",
            "CoverageUnits": "Unités de couverture"
        },
        "download_template": "📥 Télécharger un modèle Excel",
        "contact_us": "Nous contacter",
        "your_name": "Votre nom",
        "your_email": "Votre adresse e-mail",
        "your_message": "Votre message ou demande",
        "submit": "Envoyer",
        "form_success": "Merci ! Nous vous contacterons bientôt.",
        "form_error": "Veuillez remplir tous les champs.",
        "about": "À propos de cette application",
        "about_text": "Ce calculateur IFRS 17 CSM est destiné uniquement à des fins éducatives et illustratives. Il simplifie la norme pour en faciliter la compréhension et ne doit pas être utilisé pour des évaluations actuarielles en production.",
        "disclaimer": "Avertissement",
        "disclaimer_text": "Les résultats dépendent des hypothèses et données fournies par l'utilisateur. Veuillez consulter un actuaire qualifié avant toute décision financière ou comptable fondée sur cet outil.",
        "scenario_analysis": "Analyse de scénario (optionnelle)",
        "download_scenario_template": "📥 Télécharger le modèle Excel de scénario",
        "scenario_upload_label": "Téléverser un fichier de scénario",
        "scenario_chart_title": "📊 CSM par scénario"

    },
    "ar": {
        "title": "📘 حاسبة هامش الخدمة التعاقدية IFRS 17",
        "step1": "الخطوة 1: إدخال الافتراضات",
        "step2": "الخطوة 2: حساب هامش الخدمة التعاقدية",
        "upload": "تحميل ملف Excel",
        "calculate": "احسب هامش الخدمة التعاقدية",
        "csm_release_title": "📊 حركات هامش الخدمة التعاقدية",
        "ra_release_title": "📊 إصدار تعديل المخاطر",
        "cashflow_title": "📊 التدفقات النقدية التأمينية",
        "projection_years": "عدد سنوات التنبؤ",
        "discount_rate": "معدل الخصم (%)",
        "ra_percent": "نسبة تعديل المخاطر (%)",
        "use_excel": "استخدام إدخال Excel",
        "manual_input": "إدخال يدوي",
        "coverage_unit_option": "تحديد وحدات التغطية",
        "coverage_unit_default": "الافتراضي (نسبي)",
        "coverage_unit_excel": "من ملف Excel",
        "language_selector": "🌍 اختر اللغة",
        "input_premium": "الأقساط (مفصولة بفواصل)",
        "input_benefit": "المنافع (مفصولة بفواصل)",
        "input_expense": "النفقات (مفصولة بفواصل)",
        "input_coverage": "وحدات التغطية (مفصولة بفواصل)",
        "excel_headers": {
            "Premium": "القسط",
            "Benefit": "المنفعة",
            "Expense": "المصاريف",
            "CoverageUnits": "وحدات التغطية"
        },
        "download_template": "📥 تنزيل نموذج Excel",
        "contact_us": "اتصل بنا",
        "your_name": "اسمك",
        "your_email": "بريدك الإلكتروني",
        "your_message": "رسالتك أو استفسارك",
        "submit": "إرسال",
        "form_success": "شكرًا لك! سنتواصل معك قريبًا.",
        "form_error": "يرجى ملء جميع الحقول.",
        "about": "حول هذا التطبيق",
        "about_text": "هذا الحاسوب التوضيحي لمعيار IFRS 17 يهدف للأغراض التعليمية فقط. لقد تم تبسيط المعيار لتسهيل الفهم، ولا يُستخدم في التقييمات الاكتوارية الرسمية.",
        "disclaimer": "إخلاء المسؤولية",
        "disclaimer_text": "تعتمد النتائج على الافتراضات والمدخلات التي يوفرها المستخدم. يُرجى استشارة خبير اكتواري مؤهل قبل اتخاذ أي قرارات مالية أو محاسبية استنادًا إلى هذه الأداة.",
        "scenario_analysis": "تحليل السيناريو (اختياري)",
        "download_scenario_template": "📥 تنزيل قالب Excel للسيناريو",
        "scenario_upload_label": "تحميل ملف السيناريو",
        "scenario_chart_title": "📊 الهامش حسب السيناريو"

    }
}

# Language selection
lang = st.selectbox("🌍 Choose Language", options=["en", "zh", "fr", "ar"], format_func=lambda x: {"en": "🇬🇧 English", "zh": "🇨🇳 中文", "fr": "🇫🇷 Français", "ar": "🇸🇦 العربيةعربية"}[x])
t = translations[lang]

# Scenario template definition (multilingual support)
scenario_headers = {
    "en": {
        "Scenario Name": "Scenario Name",
        "Discount Rate (%)": "Discount Rate (%)",
        "Risk Adjustment (%)": "Risk Adjustment (%)",
        "Premiums": "Premiums",
        "Benefits": "Benefits",
        "Expenses": "Expenses",
        "Coverage Units": "Coverage Units"
    },
    "zh": {
        "Scenario Name": "情景名称",
        "Discount Rate (%)": "贴现率 (%)",
        "Risk Adjustment (%)": "风险调整 (%)",
        "Premiums": "保费",
        "Benefits": "理赔",
        "Expenses": "费用",
        "Coverage Units": "保障单位"
    },
    "fr": {
        "Scenario Name": "Nom du Scénario",
        "Discount Rate (%)": "Taux d'actualisation (%)",
        "Risk Adjustment (%)": "Ajustement pour risque (%)",
        "Premiums": "Primes",
        "Benefits": "Prestations",
        "Expenses": "Frais",
        "Coverage Units": "Unités de couverture"
    },
    "ar": {
        "Scenario Name": "اسم السيناريو",
        "Discount Rate (%)": "معدل الخصم (%)",
        "Risk Adjustment (%)": "تعديل المخاطر (%)",
        "Premiums": "الأقساط",
        "Benefits": "المنافع",
        "Expenses": "النفقات",
        "Coverage Units": "وحدات التغطية"
    }
}

headers = scenario_headers[lang]

scenario_df = pd.DataFrame({
    headers["Scenario Name"]: ["Base Case", "Optimistic", "Stressed"],
    headers["Discount Rate (%)"]: [5.0, 4.0, 6.0],
    headers["Risk Adjustment (%)"]: [5.0, 3.0, 7.0],
    headers["Premiums"]: ["100,100,100,100,100"] * 3,
    headers["Benefits"]: ["30,30,30,30,30"] * 3,
    headers["Expenses"]: ["10,10,10,10,10"] * 3,
    headers["Coverage Units"]: ["1,1,1,1,1"] * 3
})

scenario_buffer = BytesIO()
with pd.ExcelWriter(scenario_buffer, engine='openpyxl') as writer:
    scenario_df.to_excel(writer, sheet_name="Scenarios", index=False)
scenario_buffer.seek(0)

scenario_template = scenario_buffer


# --- Add Custom CSS Styling ---
st.markdown("""
    <style>
    .stButton > button {
        background-color: #007BFF;  /* Deep blue for buttons */
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
    .stTextInput input {
        border: 2px solid #007BFF;  /* Blue border for text input fields */
    }
    .stTextArea textarea {
        border: 2px solid #007BFF;  /* Blue border for text areas */
    }
    .email_button {
        background-color: #28a745;  /* Green background for Email Us button */
        color: white;
        border-radius: 5px;
        padding: 12px 25px;
        font-size: 16px;
        cursor: pointer;
    }
    .email_button:hover {
        background-color: #218838; /* Darker green on hover */
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to parse comma-separated strings into float lists
def parse_str_list(s):
    try:
        return [float(x.strip()) for x in str(s).split(",") if x.strip()]
    except:
        return []


logo = Image.open("Icon.png")
st.image(logo, width=160) 

st.title(t["title"])
st.markdown("---")

# --- Sample Excel Template Download
with st.expander(t["download_template"]):
    headers = t["excel_headers"]

    sample_df = pd.DataFrame({
        headers["Premium"]: [100] * 5,
        headers["Benefit"]: [30] * 5,
        headers["Expense"]: [10] * 5,
        headers["CoverageUnits"]: [1] * 5
    })

    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        sample_df.to_excel(writer, index=False)
    buffer.seek(0)

    st.download_button(
        label=t["download_template"],
        data=buffer,
        file_name="ifrs17_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# --- Scenario Excel Template Download
with st.expander(t["download_scenario_template"]):
    st.download_button(
        label=t["download_template"],
        data=scenario_template,
        file_name="ifrs17_scenario_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )




# --- Input Panel
st.header(t["step1"])
col1, col2 = st.columns(2)

with col1:
    num_years = st.number_input(t["projection_years"], min_value=1, max_value=100, value=5)
    discount_rate = st.number_input(t["discount_rate"], value=5.0) / 100
    ra_pct = st.number_input(t["ra_percent"], value=5.0) / 100
    use_excel = st.checkbox(t["upload"])

with col2:
    premiums = benefits = expenses = coverage_units = None
    if not use_excel:
        default_premium = st.text_input(t["input_premium"], "100,100,100,100,100")
        default_benefit = st.text_input(t["input_benefit"], "30,30,30,30,30")
        default_expense = st.text_input(t["input_expense"], "10,10,10,10,10")
        premiums = [float(x) for x in default_premium.split(",")]
        benefits = [float(x) for x in default_benefit.split(",")]
        expenses = [float(x) for x in default_expense.split(",")]
        coverage_units = [1] * len(premiums)
    else:
        uploaded_file = st.file_uploader(t["upload"], type=["xlsx"])

        if uploaded_file:
            try:
                df = pd.read_excel(uploaded_file)

                # 🔁 Step 1: Language-based reverse column mapping
                column_mapping = {
                    "zh": {
                        "保费": "Premium",
                        "赔付": "Benefit",
                        "费用": "Expense",
                        "服务期单位": "CoverageUnits"
                    },
                    "fr": {
                        "Prime": "Premium",
                        "Prestation": "Benefit",
                        "Frais": "Expense",
                        "Unités de couverture": "CoverageUnits"
                    },
                    "ar": {
                        "القسط": "Premium",
                        "المنفعة": "Benefit",
                        "المصاريف": "Expense",
                        "وحدات التغطية": "CoverageUnits"
                    },
                    "en": {
                        "Premium": "Premium",
                        "Benefit": "Benefit",
                        "Expense": "Expense",
                        "CoverageUnits": "CoverageUnits"
                    }
                }

                # 🔁 Step 2: Normalize column names
                df.rename(columns=column_mapping.get(lang, {}), inplace=True)

                # ✅ Step 3: Check for required columns
                required_cols = ["Scenario Name", "Premium", "Benefit", "Expense"]
                missing = [col for col in required_cols if col not in df.columns]
                if missing:
                    st.error(f"❌ Missing required column(s): {', '.join(missing)}")
                    st.stop()

                # ✅ Optional: preview
                st.write(t.get("preview_uploaded_file", "📄 Preview of uploaded file:"))
                st.dataframe(df)

            except Exception as e:
                st.error(f"⚠️ Error processing file: {str(e)}")
                st.stop()

# --- Scenario Analysis Section
st.subheader("📊 " + t["scenario_analysis"])

scenario_file = st.file_uploader(t["scenario_upload_label"], type=["xlsx"], key="scenario")
scenario_results = {}

if scenario_file:
    try:
        df_scenarios = pd.read_excel(scenario_file, sheet_name="Scenarios")

        st.write("🔍 Columns loaded:", df_scenarios.columns.tolist())

        st.dataframe(df_scenarios)

        for index, row in df_scenarios.iterrows():
            name = row["Scenario Name"]
            premiums = parse_str_list(row["Premiums"])
            benefits = parse_str_list(row["Benefits"])
            expenses = parse_str_list(row["Expenses"])
            coverage_units = [1] * len(premiums)
            dr = float(row["Discount Rate (%)"]) / 100
            ra = float(row["Risk Adjustment (%)"]) / 100

            pv_premiums = sum([p / ((1 + dr) ** i) for i, p in enumerate(premiums)])
            pv_benefits = sum([b / ((1 + dr) ** i) for i, b in enumerate(benefits)])
            pv_expenses = sum([e / ((1 + dr) ** i) for i, e in enumerate(expenses)])
            total_pv = pv_benefits + pv_expenses
            risk_adj = total_pv * ra
            csm = pv_premiums - total_pv - risk_adj

            scenario_results[name] = {
                "CSM": csm,
                "Risk Adjustment": risk_adj
            }

        # Chart of Scenario CSMs
        if scenario_results:
            scenario_names = list(scenario_results.keys())
            csm_values = [scenario_results[sc]["CSM"] for sc in scenario_names]

            st.subheader(t["scenario_chart_title"])
            fig, ax = plt.subplots(figsize=(10, 5))
            bars = ax.bar(scenario_names, csm_values)

            ax.set_xlabel("Scenario Name")
            ax.set_ylabel("CSM")
            ax.set_title(t["scenario_chart_title"])

            for bar, value in zip(bars, csm_values):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                        f"{value:,.2f}", ha='center', va='bottom')

            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Failed to process scenario file: {e}")



# --- CSM Calculation
st.header(t["step2"])
if st.button(t["calculate"]):
    if None in (premiums, benefits, expenses, coverage_units):
        st.error("Missing inputs. Please provide all required fields.")
    else:
        pv_premiums = sum([p / ((1 + discount_rate) ** i) for i, p in enumerate(premiums)])
        pv_benefits = sum([b / ((1 + discount_rate) ** i) for i, b in enumerate(benefits)])
        pv_expenses = sum([e / ((1 + discount_rate) ** i) for i, e in enumerate(expenses)])
        total_pv = pv_benefits + pv_expenses
        risk_adj = total_pv * ra_pct
        csm = pv_premiums - total_pv - risk_adj

        result = {
            "CSM at Initial Recognition": csm,
            "Risk Adjustment": risk_adj
        }

        st.success(f"✅ CSM at Initial Recognition: {csm:,.2f}")
        st.success(f"✅ Risk Adjustment: {risk_adj:,.2f}")

        # Show charts
        def calculate_csm_dynamic_release(csm_initial, discount_rate, coverage_units):
            num_years = len(coverage_units)
            csm_balance = []
            csm_release = []
            csm_start = csm_initial
            for t in range(num_years):
                interest = csm_start * discount_rate
                csm_available = csm_start + interest
                remaining_units = sum(coverage_units[t:])
                proportion = coverage_units[t] / remaining_units if remaining_units > 0 else 0
                release = csm_available * proportion
                csm_end = csm_available - release
                csm_release.append(release)
                csm_balance.append(csm_end)
                csm_start = csm_end
            return csm_release, csm_balance

        def show_csm_chart(csm_total, premiums, benefits, expenses, risk_adj, num_years, discount_rate, coverage_units):
            years = list(range(1, num_years + 1))
            if coverage_units is None:
                coverage_units = [1] * num_years

            csm_release, csm_balance = calculate_csm_dynamic_release(csm_total, discount_rate, coverage_units)
            total_units = sum(coverage_units)
            ra_release = [risk_adj * (u / total_units) for u in coverage_units]

            st.subheader(t["csm_release_title"])
            fig1, ax1 = plt.subplots(figsize=(10, 4))
            ax1.plot(years, csm_release, label="CSM Release", marker="o")
            ax1.plot(years, csm_balance, label="CSM Balance (EOP)", marker="o", linestyle="--")
            ax1.set_xlabel("Year")
            ax1.set_ylabel("Amount")
            ax1.set_title("CSM Release and Balance")
            ax1.legend()
            ax1.grid(True)
            st.pyplot(fig1)

            st.subheader(t["ra_release_title"])
            fig2, ax2 = plt.subplots(figsize=(10, 4))
            ax2.plot(years, ra_release, label="RA Release", marker="o", color="orange")
            ax2.set_xlabel("Year")
            ax2.set_ylabel("Amount")
            ax2.set_title("Risk Adjustment Release Pattern")
            ax2.legend()
            ax2.grid(True)
            st.pyplot(fig2)

            st.subheader(t["cashflow_title"])
            fig3, ax3 = plt.subplots(figsize=(10, 4))
            ax3.plot(years, premiums, label="Premiums", linestyle="--", marker=".")
            ax3.plot(years, benefits, label="Benefits", linestyle="--", marker=".")
            ax3.plot(years, expenses, label="Expenses", linestyle="--", marker=".")
            ax3.set_xlabel("Year")
            ax3.set_ylabel("Amount")
            ax3.set_title("Insurance Cash Flows")
            ax3.legend()
            ax3.grid(True)
            st.pyplot(fig3)

        show_csm_chart(
            result["CSM at Initial Recognition"],
            premiums,
            benefits,
            expenses,
            result["Risk Adjustment"],
            len(premiums),
            discount_rate,
            coverage_units
        )


# --- Email Us Button Instead of Contact Form ---
st.markdown("---")
st.header("📬 " + t["contact_us"])

# Email Us button with hover effect
st.markdown(
    """
    <a href="mailto:youremail@example.com?subject=Contact%20Us%20Form%20Submission&body=Please%20include%20your%20message%20here."
    target="_blank">
    <button class="email_button">
        Email Us
    </button>
    </a>
    """, unsafe_allow_html=True)


#For the About us and Disclaimers
st.markdown("---")
st.subheader("ℹ️ " + t["about"])
st.write(t["about_text"])

st.subheader("⚠️ " + t["disclaimer"])
st.write(t["disclaimer_text"])


#MVP on June 7th, 2025
# Footer
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; font-size: 0.8em; color: gray;'>"
    f"© 2025 XL Financial Group | Version v1.0.0 – Multilingual IFRS 17 CSM Calculator"
    f"</div>",
    unsafe_allow_html=True
)


st.info("📱 **Tip**: You can add this app to your phone's home screen for quicker access!")

if st.button("📖 How to do this?"):
    st.markdown("""
    **On iPhone (Safari):**
    1. Tap the **Share** icon
    2. Tap **Add to Home Screen**
    
    **On Android (Chrome):**
    1. Tap the **⋮ Menu** in top-right
    2. Tap **Add to Home screen**
    """)


