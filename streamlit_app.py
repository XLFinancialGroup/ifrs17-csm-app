import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

from PIL import Image
import pandas as pd
import os
import datetime

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Sample Excel Template Download
from io import BytesIO

# Step-by-step Integration: "Did You Know?" Insights Section with Multilingual Support
import random

import io
import xlsxwriter
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
        "scenario_chart_title": "📊 CSM by Scenario",
        "pricing_benchmark_title": "🧮 Pricing Benchmark Mode (Beta)",
        "product_a_title": "Product A (Your Product)",
        "product_b_title": "Benchmark Product B",
        "premium_input": "Premiums",
        "benefit_input": "Benefits",
        "expense_input": "Expenses",
        "discount_rate_input": "Discount Rate (%)",
        "risk_adj_input": "Risk Adjustment (%)",
        "compare_button": "Compare Products",
        "comparison_table_title": "📊 Comparison Table",
        "comparison_labels": [
            "Present Value of Premiums",
            "Total Present Value of Benefits + Expenses",
            "Risk Adjustment",
            "Resulting CSM"
        ],
        "mode_toggle_label": "🔀 Select Mode",
        "mode_toggle_options": {
            "csm": "📘 CSM Calculator Mode",
            "benchmark": "🧮 Pricing Benchmark Mode"
        },
        "did_you_know_title": "💡 Did You Know?",
        "tutorial_toggle": "❓ Enable Tutorial Mode",
        "model_repo_title": "Model Repository (Beta)",
        "model_repo_mode_label": "What would you like to do?",
        "model_repo_upload": "📤 Upload a Model",
        "model_repo_browse": "📁 Browse Models",
        "model_repo_upload_label": "Upload your IFRS 17 Model (.xlsx)",
        "model_repo_name_label": "Model Name / Description",
        "model_repo_success": "✅ Model uploaded successfully!",
        "model_repo_none": "📭 No models have been uploaded yet.",
        "download_excel_button": "Download IFRS 17 Scenario-based Excel Report",
        "scenario": "Scenario",
        "risk_adjustment": "Risk Adjustment",
        "job_board": "📌 Featured IFRS 17 Job Postings",
        "apply": "Apply",
        "tab_job_board": "Actuarial Job Board",
        "tab_ifrs17": "IFRS 17 CSM App"



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
        "scenario_chart_title": "📊 各情景下的 CSM 比较",
        "pricing_benchmark_title": "🧮 定价对比模式（测试版）",
        "product_a_title": "产品 A（您的产品）",
        "product_b_title": "基准产品 B",
        "premium_input": "保费",
        "benefit_input": "赔付",
        "expense_input": "费用",
        "discount_rate_input": "贴现率 (%)",
        "risk_adj_input": "风险调整 (%)",
        "compare_button": "比较产品",
        "comparison_table_title": "📊 对比表格",
        "comparison_labels": [
            "保费现值",
            "赔付和费用现值总和",
            "风险调整",
            "CSM 结果"
        ],
        "mode_toggle_label": "🔀 选择模式",
        "mode_toggle_options": {
            "csm": "📘 合同服务边际计算模式",
            "benchmark": "🧮 定价基准对比模式"
        },
        "did_you_know_title": "💡 你知道吗？",
        "tutorial_toggle": "❓ 启用教程模式",
        "model_repo_title": "模型库（测试版）",
        "model_repo_mode_label": "您希望执行的操作？",
        "model_repo_upload": "📤 上传模型",
        "model_repo_browse": "📁 浏览模型",
        "model_repo_upload_label": "上传您的 IFRS 17 模型（.xlsx）",
        "model_repo_name_label": "模型名称 / 描述",
        "model_repo_success": "✅ 模型上传成功！",
        "model_repo_none": "📭 当前没有上传的模型。",
        "download_excel_button": "下载 IFRS 17 情景分析 Excel 报告",
        "scenario": "情景",
        "risk_adjustment": "风险调整",
        "job_board": "📌 精选 IFRS 17 招聘信息",
        "apply": "申请",
        "tab_job_board": "精算职位看板",
        "tab_ifrs17": "IFRS 17 CSM 应用"

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
        "scenario_chart_title": "📊 CSM par scénario",
        "pricing_benchmark_title": "🧮 Mode de Référence de Tarification (Bêta)",
        "product_a_title": "Produit A (Votre produit)",
        "product_b_title": "Produit de référence B",
        "premium_input": "Primes",
        "benefit_input": "Prestations",
        "expense_input": "Frais",
        "discount_rate_input": "Taux d'actualisation (%)",
        "risk_adj_input": "Ajustement pour risque (%)",
        "compare_button": "Comparer les produits",
        "comparison_table_title": "📊 Tableau comparatif",
        "comparison_labels": [
            "Valeur actuelle des primes",
            "Valeur actuelle totale des prestations + frais",
            "Ajustement pour risque",
            "Marge de service contractuelle"
        ],
        "mode_toggle_label": "🔀 Sélectionner le mode",
        "mode_toggle_options": {
            "csm": "📘 Mode de calcul de la MSC",
            "benchmark": "🧮 Mode de comparaison des tarifs"
        },
        "did_you_know_title": "💡 Le Saviez-Vous ?",
        "tutorial_toggle": "❓ Activer le mode tutoriel",
        "model_repo_title": "Répertoire de Modèles (Bêta)",
        "model_repo_mode_label": "Que souhaitez-vous faire ?",
        "model_repo_upload": "📤 Télécharger un modèle",
        "model_repo_browse": "📁 Parcourir les modèles",
        "model_repo_upload_label": "Téléchargez votre modèle IFRS 17 (.xlsx)",
        "model_repo_name_label": "Nom / Description du modèle",
        "model_repo_success": "✅ Modèle téléchargé avec succès !",
        "model_repo_none": "📭 Aucun modèle n’a encore été téléchargé.",
        "download_excel_button": "Télécharger le rapport Excel basé sur des scénarios IFRS 17",
        "scenario": "Scénario",
        "risk_adjustment": "Ajustement pour risque",
        "job_board": "📌 Offres d'emploi IFRS 17 en vedette",
        "apply": "Postuler",
        "tab_job_board": "Tableau des Offres Actuarielles",
        "tab_ifrs17": "Application IFRS 17 CSM"


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
        "scenario_chart_title": "📊 الهامش حسب السيناريو",
        "pricing_benchmark_title": "🧮 وضع مقارنة الأسعار (تجريبي)",
        "product_a_title": "المنتج أ (منتجك)",
        "product_b_title": "المنتج ب المرجعي",
        "premium_input": "الأقساط",
        "benefit_input": "المنافع",
        "expense_input": "النفقات",
        "discount_rate_input": "معدل الخصم (%)",
        "risk_adj_input": "نسبة تعديل المخاطر (%)",
        "compare_button": "قارن المنتجات",
        "comparison_table_title": "📊 جدول المقارنة",
        "comparison_labels": [
            "القيمة الحالية للأقساط",
            "إجمالي القيمة الحالية للمنافع + النفقات",
            "تعديل المخاطر",
            "هامش الخدمة التعاقدية"
        ],
        "mode_toggle_label": "🔀 اختر الوضع",
        "mode_toggle_options": {
            "csm": "📘 وضع حساب هامش الخدمة التعاقدية",
            "benchmark": "🧮 وضع مقارنة الأسعار"
        },
        "did_you_know_title": "💡 هل كنت تعلم؟",
        "tutorial_toggle": "❓ تفعيل وضع الشرح",
        "model_repo_title": "مستودع النماذج (تجريبي)",
        "model_repo_mode_label": "ماذا ترغب أن تفعل؟",
        "model_repo_upload": "📤 تحميل نموذج",
        "model_repo_browse": "📁 استعراض النماذج",
        "model_repo_upload_label": "حمّل نموذج IFRS 17 الخاص بك (.xlsx)",
        "model_repo_name_label": "اسم / وصف النموذج",
        "model_repo_success": "✅ تم تحميل النموذج بنجاح!",
        "model_repo_none": "📭 لا توجد نماذج مرفوعة حالياً.",
        "download_excel_button": "تحميل تقرير Excel الخاص بسيناريوهات معيار IFRS 17",
        "scenario": "السيناريو",
        "risk_adjustment": "تعديل المخاطر",
        "job_board": "📌 وظائف IFRS 17 المميزة",
        "apply": "تقديم",
        "tab_job_board": "لوحة الوظائف الاكتوارية",
        "tab_ifrs17": "تطبيق IFRS 17 CSM"





    }
}

tutorial_text = {
    "en": {
        "intro": "Welcome to Tutorial Mode! This mode provides guidance at each step.",
        "step1": "Here you can input your assumptions manually or upload an Excel file.",
        "step2": "Click 'Calculate' to compute the Contractual Service Margin (CSM).",
        "scenario": "You can also upload a scenario file to perform CSM stress testing.",
        "charts": "Below, you'll see visual outputs of the CSM, RA release, and cash flows."
    },
    "zh": {
        "intro": "欢迎使用教程模式！我们会在每个步骤提供说明。",
        "step1": "在这里，您可以手动输入假设，或上传 Excel 文件。",
        "step2": "点击“计算”按钮，即可计算合同服务边际 (CSM)。",
        "scenario": "您还可以上传情景文件，进行压力测试。",
        "charts": "下方将展示 CSM、风险调整释放、及现金流的可视化图表。"
    },
    "fr": {
        "intro": "Bienvenue dans le mode tutoriel ! Ce mode vous guide étape par étape.",
        "step1": "Ici, vous pouvez saisir vos hypothèses manuellement ou télécharger un fichier Excel.",
        "step2": "Cliquez sur 'Calculer' pour obtenir la Marge de Service Contractuelle (MSC).",
        "scenario": "Vous pouvez également télécharger un fichier de scénario pour effectuer des tests de résistance.",
        "charts": "Ci-dessous, vous verrez des graphiques sur la MSC, la libération du RA et les flux de trésorerie."
    },
    "ar": {
        "intro": "مرحبًا بك في وضع الشرح! سنرشدك في كل خطوة.",
        "step1": "هنا يمكنك إدخال الفرضيات يدويًا أو تحميل ملف Excel.",
        "step2": "اضغط على 'احسب' لحساب هامش الخدمة التعاقدية (CSM).",
        "scenario": "يمكنك أيضًا تحميل ملف سيناريو لإجراء اختبار الضغط.",
        "charts": "في الأسفل، سترى رسومًا بيانية لـ CSM، إصدار RA، وتدفقات التأمين النقدية."
    }
}




# Language selection
lang = st.selectbox("🌍 Choose Language", options=["en", "zh", "fr", "ar"], format_func=lambda x: {"en": "🇬🇧 English", "zh": "🇨🇳 中文", "fr": "🇫🇷 Français", "ar": "🇸🇦 العربيةعربية"}[x])
t = translations[lang]

#Adding different tabs for different functions
tab1, tab2 = st.tabs([t["tab_ifrs17"], t["tab_job_board"]])

with tab1:
    # Mode toggle
    mode = st.radio(
        label=t["mode_toggle_label"],
        options=["csm", "benchmark"],
        format_func=lambda x: t["mode_toggle_options"][x]
    )

    show_tutorial = st.checkbox(t["tutorial_toggle"])
    if show_tutorial:
        st.info(tutorial_text[lang]["intro"])

    st.markdown("---")
    st.subheader("📂 " + t["model_repo_title"])

    repo_mode = st.radio(t["model_repo_mode_label"], [t["model_repo_upload"], t["model_repo_browse"]])

    if repo_mode == t["model_repo_upload"]:
        uploaded_model = st.file_uploader(t["model_repo_upload_label"], type=["xlsx"])
        model_name = st.text_input(t["model_repo_name_label"])

        if uploaded_model and model_name:
            save_path = os.path.join("repository", model_name + ".xlsx")
            os.makedirs("repository", exist_ok=True)

            with open(save_path, "wb") as f:
                f.write(uploaded_model.getbuffer())
            st.success(t["model_repo_success"])

    elif repo_mode == t["model_repo_browse"]:
        repo_dir = "repository"
        if os.path.exists(repo_dir) and os.listdir(repo_dir):
            for file in os.listdir(repo_dir):
                if file.endswith(".xlsx"):
                    with open(os.path.join(repo_dir, file), "rb") as f:
                        st.download_button(label=f"📥 Download {file}", data=f, file_name=file)
        else:
            st.info(t["model_repo_none"])





    # Scenario template definition (multilingual support)
    scenario_headers = {
        "en": {
            "Scenario Name": "Scenario Name",
            "Discount Rate (%)": "Discount Rate (%)",
            "Risk Adjustment (%)": "Risk Adjustment (%)",
            "Premiums": "Premiums",
            "Benefits": "Benefits",
            "Expenses": "Expenses",
            "Coverage Units": "Coverage Units",
        },
        "zh": {
            "Scenario Name": "情景名称",
            "Discount Rate (%)": "贴现率 (%)",
            "Risk Adjustment (%)": "风险调整 (%)",
            "Premiums": "保费",
            "Benefits": "理赔",
            "Expenses": "费用",
            "Coverage Units": "保障单位",
            "情景名称": "Scenario Name",
            "贴现率 (%)": "Discount Rate (%)",
            "风险调整 (%)": "Risk Adjustment (%)",
            "保费": "Premiums",
            "理赔": "Benefits",
            "费用": "Expenses",
            "保障单位": "CoverageUnits"
        },
        "fr": {
            "Scenario Name": "Nom du Scénario",
            "Discount Rate (%)": "Taux d'actualisation (%)",
            "Risk Adjustment (%)": "Ajustement pour risque (%)",
            "Premiums": "Primes",
            "Benefits": "Prestations",
            "Expenses": "Frais",
            "Coverage Units": "Unités de couverture",
            "Nom du scénario": "Scenario Name",
            "Taux d'actualisation (%)": "Discount Rate (%)",
            "Ajustement pour risque (%)": "Risk Adjustment (%)",
            "Primes": "Premiums",
            "Prestations": "Benefits",
            "Frais": "Expenses",
            "Unités de couverture": "CoverageUnits"
        },
        "ar": {
            "Scenario Name": "اسم السيناريو",
            "Discount Rate (%)": "معدل الخصم (%)",
            "Risk Adjustment (%)": "تعديل المخاطر (%)",
            "Premiums": "الأقساط",
            "Benefits": "المنافع",
            "Expenses": "النفقات",
            "Coverage Units": "وحدات التغطية",
            "اسم السيناريو": "Scenario Name",
            "معدل الخصم (%)": "Discount Rate (%)",
            "نسبة تعديل المخاطر (%)": "Risk Adjustment (%)",
            "الأقساط": "Premiums",
            "المنافع": "Benefits",
            "النفقات": "Expenses",
            "وحدات التغطية": "CoverageUnits"
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


    #Toggle between CSM calculator and Pricing Benchmark

    #CSM calculator mode
    if mode == "csm":

        # --- Input Panel
        st.header(t["step1"])
        col1, col2 = st.columns(2)
        if show_tutorial:
            st.info(tutorial_text[lang]["step1"])


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

    # --- Pricing Benchmark Mode ---
    elif mode == "benchmark":
        st.subheader(t["pricing_benchmark_title"])
        
        st.markdown("### " + t["product_a_title"])
        premium_a = st.text_input(f"{t['premium_input']} A", "100,100,100")
        benefit_a = st.text_input(f"{t['benefit_input']} A", "50,50,50")
        expense_a = st.text_input(f"{t['expense_input']} A", "10,10,10")
        discount_a = st.number_input(f"{t['discount_rate_input']} A", value=5.0) / 100
        ra_a = st.number_input(f"{t['risk_adj_input']} A", value=5.0) / 100

        st.markdown("### " + t["product_b_title"])
        premium_b = st.text_input(f"{t['premium_input']} B", "100,100,100")
        benefit_b = st.text_input(f"{t['benefit_input']} B", "60,60,60")
        expense_b = st.text_input(f"{t['expense_input']} B", "15,15,15")
        discount_b = st.number_input(f"{t['discount_rate_input']} B", value=4.0) / 100
        ra_b = st.number_input(f"{t['risk_adj_input']} B", value=4.0) / 100

        if st.button(t["compare_button"]):
            def compute_csm(prem, ben, exp, dsc, ra):
                prem_list = parse_str_list(prem)
                ben_list = parse_str_list(ben)
                exp_list = parse_str_list(exp)
                pv_prem = sum([p / ((1 + dsc) ** i) for i, p in enumerate(prem_list)])
                pv_benefits = sum([b / ((1 + dsc) ** i) for i, b in enumerate(ben_list)])
                pv_expenses = sum([e / ((1 + dsc) ** i) for i, e in enumerate(exp_list)])
                total_pv = pv_benefits + pv_expenses
                ra_val = total_pv * ra
                csm = pv_prem - total_pv - ra_val
                return pv_prem, total_pv, ra_val, csm

            result_a = compute_csm(premium_a, benefit_a, expense_a, discount_a, ra_a)
            result_b = compute_csm(premium_b, benefit_b, expense_b, discount_b, ra_b)

            df_compare = pd.DataFrame({
                "": t["comparison_labels"],
                t["product_a_title"]: result_a,
                t["product_b_title"]: result_b
            })

            st.subheader(t["comparison_table_title"])
            st.dataframe(df_compare)



    # --- Scenario Analysis Section
    st.subheader("📊 " + t["scenario_analysis"])
    if show_tutorial:
        st.info(tutorial_text[lang]["scenario"])


    scenario_file = st.file_uploader(t["scenario_upload_label"], type=["xlsx"], key="scenario")
    scenario_results = {}

    if scenario_file:
        try:
            df_scenarios = pd.read_excel(scenario_file, sheet_name="Scenarios")
            original_columns = df_scenarios.columns.tolist()
            st.write("🔍 Original Columns:", original_columns)

            # Normalize column names using language-aware mapping
            column_map = {
                scenario_headers[lang].get("Scenario Name", "Scenario Name"): "Scenario Name",
                scenario_headers[lang].get("Discount Rate (%)", "Discount Rate (%)"): "Discount Rate (%)",
                scenario_headers[lang].get("Risk Adjustment (%)", "Risk Adjustment (%)"): "Risk Adjustment (%)",
                scenario_headers[lang].get("Premiums", "Premiums"): "Premiums",
                scenario_headers[lang].get("Benefits", "Benefits"): "Benefits",
                scenario_headers[lang].get("Expenses", "Expenses"): "Expenses",
                scenario_headers[lang].get("Coverage Units", "Coverage Units"): "Coverage Units"
            }
            df_scenarios.rename(columns=column_map, inplace=True)
            normalized_columns = df_scenarios.columns.tolist()
            st.write("✅ Normalized Columns:", normalized_columns)

            st.dataframe(df_scenarios)

            for index, row in df_scenarios.iterrows():
                name = row["Scenario Name"]
                premiums = parse_str_list(row["Premiums"])
                benefits = parse_str_list(row["Benefits"])
                expenses = parse_str_list(row["Expenses"])
                coverage_units = parse_str_list(row["Coverage Units"]) if "Coverage Units" in row else [1] * len(premiums)

                discount_rate_scenario = float(row["Discount Rate (%)"]) / 100
                ra_pct_scenario = float(row["Risk Adjustment (%)"]) / 100

                # Compute CSM
                pv_premiums = sum([p / ((1 + discount_rate_scenario) ** i) for i, p in enumerate(premiums)])
                pv_benefits = sum([b / ((1 + discount_rate_scenario) ** i) for i, b in enumerate(benefits)])
                pv_expenses = sum([e / ((1 + discount_rate_scenario) ** i) for i, e in enumerate(expenses)])
                total_pv = pv_benefits + pv_expenses
                risk_adj = total_pv * ra_pct_scenario
                csm = pv_premiums - total_pv - risk_adj

                scenario_results[name] = {
                    "CSM": csm,
                    "Risk Adjustment": risk_adj,
                    "Discount Rate (%)": discount_rate * 100,
                    "RA (%)": ra_pct * 100
                }


            # Chart of Scenario CSMs
            if scenario_results:
                scenario_names = list(scenario_results.keys())
                csm_values = [scenario_results[sc]["CSM"] for sc in scenario_names]

                st.subheader(t["scenario_chart_title"])
                fig, ax = plt.subplots(figsize=(10, 5))
                colors = plt.cm.Set3(range(len(scenario_names)))  # Optional color palette
                bars = ax.bar(scenario_names, csm_values, color=colors)

                ax.set_xlabel("Scenario", fontsize=12)
                ax.set_ylabel("CSM", fontsize=12)
                ax.set_title(t["scenario_chart_title"], fontsize=14, weight='bold')
                ax.grid(True, axis='y', linestyle='--', alpha=0.6)
                ax.set_facecolor('#f8f9fa')
                fig.patch.set_facecolor('white')
                plt.xticks(rotation=30, ha='right')
                ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))

                for bar, value in zip(bars, csm_values):
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height(),
                        f"{value:,.0f}",
                        ha='center',
                        va='bottom',
                        fontsize=10,
                        fontweight='bold'
                    )

                st.pyplot(fig)

        except Exception as e:
            st.error(f"⚠️ Failed to process scenario file: {e}")



    # --- CSM Calculation
    st.header(t["step2"])
    if show_tutorial:
        st.info(tutorial_text[lang]["step2"])


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

            def show_csm_chart(csm_total, premiums, benefits, expenses, risk_adj, num_years, discount_rate, coverage_units, show_tutorial=False):
                years = list(range(1, num_years + 1))
                if coverage_units is None:
                    coverage_units = [1] * num_years

                csm_release, csm_balance = calculate_csm_dynamic_release(csm_total, discount_rate, coverage_units)
                total_units = sum(coverage_units)
                ra_release = [risk_adj * (u / total_units) for u in coverage_units]

                if show_tutorial:
                    st.info(tutorial_text[lang]["charts"])


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

    def generate_excel_report(scenario_results, lang):
        import io
        output = io.BytesIO()


        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            workbook = writer.book
            worksheet = workbook.add_worksheet("CSM Results")
            writer.sheets["CSM Results"] = worksheet

            # Define formats
            bold_format = workbook.add_format({'bold': True, 'font_color': 'black'})
            currency_format = workbook.add_format({'num_format': '#,##0.00', 'align': 'right'})

            # Write headers
            headers = ["Scenario", "CSM", "Risk Adjustment"]
            worksheet.write_row("A1", headers, bold_format)

            # Write data
            row_idx = 1
            for scenario, values in scenario_results.items():
                worksheet.write(row_idx, 0, scenario)
                worksheet.write_number(row_idx, 1, values["CSM"], currency_format)
                worksheet.write_number(row_idx, 2, values["Risk Adjustment"], currency_format)
                row_idx += 1

            # Only add chart if there are values
            if row_idx > 1:
                chart = workbook.add_chart({'type': 'column'})
                chart.add_series({
                    'name':       'CSM',
                    'categories': ['CSM Results', 1, 0, row_idx - 1, 0],
                    'values':     ['CSM Results', 1, 1, row_idx - 1, 1],
                })
                chart.set_title({'name': 'CSM by Scenario'})
                chart.set_x_axis({'name': 'Scenario'})
                chart.set_y_axis({'name': 'CSM Value'})
                worksheet.insert_chart('I2', chart)
            
            # Insert logo at the top-left corner (cell A1)
            logo_path = "Icon.png"  
            if os.path.exists(logo_path):
                worksheet.insert_image("A13", logo_path, {"x_scale": 0.5, "y_scale": 0.5})

            # Add timestamp and footer
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            footer_text = f"Generated by IFRS 17 CSM App from XL Financial Group on {now}"
            footer_row = row_idx + 2  # leave one empty row after the table
            worksheet.merge_range(footer_row, 0, footer_row, 8, footer_text)


        output.seek(0)
        return output.read()



    #Download button
    if st.button(t["download_excel_button"]):  
        
            excel_data = generate_excel_report(scenario_results, lang)
            st.download_button(
                label=t["download_excel_button"],
                data=excel_data,
                file_name="IFRS17_CSM_Report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )



    # --- Email Us Button Instead of Contact Form ---
    st.markdown("---")
    st.header("📬 " + t["contact_us"])

    # Email Us button with hover effect 
    st.markdown(
        """
        <a href="mailto:jamesxuwansi@gmail.com?subject=Contact%20Us%20Form%20Submission&body=Please%20include%20your%20message%20here."
        target="_blank">
        <button class="email_button">
            Email Us
        </button>
        </a>
        """, unsafe_allow_html=True)

    # Step 1: Define multilingual insights dictionary
    did_you_know_facts = {
        "en": [
            "Did you know? The Contractual Service Margin (CSM) cannot be negative. Any shortfall goes to the P&L immediately as a loss component.",
            "Did you know? Acquisition cash flows are included in the initial measurement of CSM and recognized over the coverage period.",
            "Did you know? Risk Adjustment reflects the compensation the entity requires for bearing non-financial risk.",
            "Did you know? Groups of insurance contracts must be segmented into at least three buckets: profitable, onerous, and no significant risk of becoming onerous.",
            "Did you know? IFRS 17 requires entities to reassess assumptions at each reporting date—making automation critical.",
            "Did you know? Under IFRS 17, insurance revenue is not equal to premiums received—it’s based on service provided.",
            "Did you know? The General Measurement Model (GMM) is the default approach under IFRS 17.",
            "Did you know? For contracts with direct participation features, the Variable Fee Approach (VFA) must be used."
        ],
        "zh": [
            "你知道吗？合同服务边际（CSM）不能为负，任何短缺将立即计入利润表为亏损部分。",
            "你知道吗？取得现金流包括在CSM初始计量中，并在保障期内分摊确认。",
            "你知道吗？风险调整反映公司因承担非财务风险而要求的补偿。",
            "你知道吗？保险合同组必须至少分为三类：盈利、亏损和无重大亏损风险。",
            "你知道吗？IFRS 17 要求在每个报告日重新评估假设，因此自动化尤为重要。",
            "你知道吗？根据 IFRS 17，保险收入不是等于收到的保费，而是基于已提供的服务确认。",
            "你知道吗？一般计量模型（GMM）是 IFRS 17 的默认计量方法。",
            "你知道吗？对于具有直接参与特征的合同，必须使用可变费用法（VFA）。"
        ],
        "fr": [
            "Le saviez-vous ? La Marge de Service Contractuelle (MSC) ne peut pas être négative. Tout déficit est imputé immédiatement au résultat.",
            "Le saviez-vous ? Les flux de trésorerie d'acquisition sont inclus dans la MSC initiale et reconnus sur la durée de couverture.",
            "Le saviez-vous ? L'ajustement pour risque reflète la compensation requise pour le risque non financier.",
            "Le saviez-vous ? Les groupes de contrats doivent être segmentés en trois catégories : profitables, déficitaires et à faible risque de devenir déficitaires.",
            "Le saviez-vous ? IFRS 17 exige la réévaluation des hypothèses à chaque date de reporting.",
            "Le saviez-vous ? En IFRS 17, les revenus d'assurance ne sont pas égaux aux primes reçues mais au service fourni.",
            "Le saviez-vous ? Le Modèle de Mesure Général (GMM) est l'approche par défaut selon IFRS 17.",
            "Le saviez-vous ? Les contrats avec participation directe doivent utiliser l'approche à frais variables (VFA)."
        ],
        "ar": [
            "هل تعلم؟ لا يمكن أن يكون هامش الخدمة التعاقدية (CSM) سالبًا. يتم تحويل أي عجز مباشرة إلى بيان الدخل كعنصر خسارة.",
            "هل تعلم؟ يتم تضمين التدفقات النقدية الخاصة بالاكتتاب في القياس الابتدائي لهامش CSM ويتم الاعتراف بها على مدى فترة التغطية.",
            "هل تعلم؟ يعكس تعديل المخاطر التعويض الذي تتطلبه الشركة لتحمل المخاطر غير المالية.",
            "هل تعلم؟ يجب تصنيف مجموعات عقود التأمين إلى ثلاث مجموعات: مربحة، خاسرة، وعديمة خطر الخسارة.",
            "هل تعلم؟ يتطلب معيار IFRS 17 إعادة تقييم الفرضيات في كل تاريخ تقرير، مما يجعل الأتمتة أمرًا حاسمًا.",
            "هل تعلم؟ بموجب IFRS 17، لا تساوي إيرادات التأمين الأقساط المستلمة بل تُحتسب على أساس الخدمة المقدمة.",
            "هل تعلم؟ يُعتبر النموذج العام للقياس (GMM) هو الأسلوب الافتراضي ضمن IFRS 17.",
            "هل تعلم؟ يجب استخدام طريقة الرسوم المتغيرة (VFA) للعقود ذات الميزات التشاركية المباشرة."
        ]
    }

    # Step 2: Display a random fact block under a new section
    st.markdown("---")
    st.subheader(t["did_you_know_title"])
    random_fact = random.choice(did_you_know_facts.get(lang, did_you_know_facts["en"]))
    st.info(random_fact)


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




#New section for the Job Board
job_listings = [
    {
        "title": "Senior IFRS Actuarial Analyst",
        "company": "Swiss Re",
        "location": "Zurich, Switzerland",
        "link": "https://www.swissre.com/careers/job/senior-ifrs-actuarial-analyst-hybrid-m-f-x-d-80-100-/1207913501"
    },
    {
        "title": "Senior Actuarial Analyst (Reporting Team)",
        "company": "Swiss Re",
        "location": "Hong Kong",
        "link": "https://www.actuarylist.com/actuarial-jobs/5654-swiss-re"
    },
    {
        "title": "Senior Actuarial Associate, IFRS17",
        "company": "Prudential Hong Kong",
        "location": "Hong Kong SAR",
        "link": "https://prudential.wd3.myworkdayjobs.com/ms-MY/prudential/job/Hong-Kong/Senior-Actuarial-Associate--IFRS17---Actuarial_25050263"
    }

]

with tab2:
    # --- Job Board Section ---
    st.markdown("---")
    st.subheader("💼 " + t["job_board"])
    st.caption("🔎 Last Verified: June 2025")

    for job in job_listings:
        with st.container():
            st.markdown(f"**🧑‍💼 {job['title']}**  \n"
                        f"🏢 {job['company']} | 📍 {job['location']}  \n"
                        f"[{t['apply']}]({job['link']})", unsafe_allow_html=True)
            st.markdown("---")

    #add custom CSS
    st.markdown("""
    <style>
    a {
        text-decoration: none;
        color: #0066cc;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)


