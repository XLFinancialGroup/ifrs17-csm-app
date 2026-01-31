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
        "tab_ifrs17": "IFRS 17 CSM App",
        "pnl_statement_title": "📈 Projected IFRS 17 Profit & Loss Statement",
        "tab_pnl_statement": "IFRS 17 Profit & Loss Statement",
        "insurance_revenue": "Insurance Revenue",
        "insurance_expense": "Insurance Expense",
        "net_insurance_result": "Net Insurance Result",
        "csm_release": "CSM Release",
        "ra_release": "RA Release",
        "expected_benefit": "Expected Benefits",
        "expected_expense": "Expected Expenses",
        "year": "Year",
        "actual_claims": "Actual Claims",
        "actual_expenses": "Actual Expenses",
        "actual_premiums": "Actual Premiums",
        "actual_inputs_expander": "Enter Actual Cash Flows (per year)",
        "balance_sheet_tab": "📊 Balance Sheet",
        "balance_sheet_title": "Balance Sheet",
        "csm_balance": "CSM Balance",
        "ra_balance": "RA Balance",
        "cash_balance": "Cash Balance",
        "total_liabilities": "Total Liabilities",
        "retained_earnings": "Retained Earnings",
        "total_equity": "Total Equity",
        "assets_liabilities_check": "Assets = Liabilities + Equity?",
        "total_assets": "Total Assets",
        "total_liab_equity": "Total Liabilities + Equities",
        "pv_future_cf": "PV of Future Cash Flows",
        "retained_earnings": "Retained Earnings",
        "total_equity": "Total Equity",
        "total_assets": "Total Assets",
        "total_liabilities_equity": "Total Liabilities + Equities",
        "asset_liability_check": "Asset – (Liab + Equity)",
        "insurance_finance_expense": "Insurance Finance Income and Expenses",
        "current_discount_rate": "Current Discount Rate (%)",
        "news_tab_title": "📰 IFRS 17 & Actuarial News",
        "loss_component_init": "Loss Component at Initial Recognition",
        "loss_component_release": "Loss Component Release",
        "loss_component_balance": "Loss Component Balance",
        "initial_lc_expense": "Initial Loss Component",
        "assump_change_expander": "Assumption update (prospective)",
        "assump_change_start":    "Apply changes from Year …",
        "benefit_change_pct":     "Δ Expected Benefits (%)",
        "expense_change_pct":     "Δ Expected Expenses (%)",
        "ra_new_pct":             "New Risk-Adjustment (%)",
        "assump_change_loss":     "Loss-component increase",
        "assump_change_gain":     "Loss-component release",
        "tab_paa": "PAA (Simplified)",
        "paa_title": "📘 IFRS 17 PAA Calculator",
        "coverage_period": "Coverage period (years)",
        "total_gwp": "Total written premium",
        "earned_premium_pattern": "Revenue pattern",
        "pattern_even": "Even (straight-line)",
        "pattern_front": "Front-loaded",
        "pattern_back": "Back-loaded",
        "expected_claim_ratio": "Ultimate loss ratio (%)",
        "onerous_check": "Run onerous test?",
        "lrc_init": "Initial LRC",
        "lic_init": "Initial LIC (zero → no incurred claims)",
        "revenue": "Insurance revenue",
        "claims_incurred": "Claims incurred",
        "exp_recognised": "Insurance service expenses",
        "net_result": "Insurance service result"





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
        "tab_ifrs17": "IFRS 17 CSM 应用",
        "pnl_statement_title": "📈 预计 IFRS 17 损益表",
        "tab_pnl_statement": "IFRS 17 损益表",
        "insurance_revenue": "保险收入",
        "insurance_expense": "保险支出",
        "net_insurance_result": "保险净结果",
        "csm_release": "CSM 释放",
        "ra_release": "风险调整释放",
        "expected_benefit": "预期赔付",
        "expected_expense": "预期费用",
        "year": "年度",
        "actual_claims": "实际赔付",
        "actual_expenses": "实际费用",
        "actual_premiums": "实际保费",
        "actual_inputs_expander": "请提供实际现金流数据",
        "balance_sheet_tab": "📊 资产负债表",
        "balance_sheet_title": "资产负债表",
        "csm_balance": "CSM余额",
        "ra_balance": "风险调整余额",
        "cash_balance": "现金余额",
        "total_liabilities": "总负债",
        "retained_earnings": "留存收益",
        "total_equity": "所有者权益总计",
        "assets_liabilities_check": "资产 = 负债 + 权益 校验",
        "total_assets": "资产总计",
        "total_liab_equity": "负债和权益总计",
        "pv_future_cf": "未来现金流现值",
        "retained_earnings": "留存收益",
        "total_equity": "总权益",
        "total_assets": "资产总额",
        "total_liabilities_equity": "负债与权益总额",
        "asset_liability_check": "资产 - (负债 + 权益)",
        "insurance_finance_expense": "保险财务收入与费用",
        "current_discount_rate": "当前贴现率（%）",
        "news_tab_title": "📰 IFRS 17 与 精算 新闻",
        "loss_component_init": "初始确认时损失组成部分",
        "loss_component_release": "损失组成部分摊销",
        "loss_component_balance": "损失组成部分余额",
        "initial_lc_expense": "初始确认时损失组成部分",
        "assump_change_expander": "假设更新（未来情景）",
        "assump_change_start":    "从第几年开始应用变动",
        "benefit_change_pct":     "预期赔付变化 (%)",
        "expense_change_pct":     "预期费用变化 (%)",
        "ra_new_pct":             "新的风险调整 (%)",
        "assump_change_loss":     "损失组成部分增加",
        "assump_change_gain":     "损失组成部分释放",
        "tab_paa": "PAA（简化法）",
        "paa_title": "📘 IFRS 17 PAA 计算器",
        "coverage_period": "保障期限（年）",
        "total_gwp": "总签单保费",
        "earned_premium_pattern": "收入摊销模式",
        "pattern_even": "平均（直线法）",
        "pattern_front": "前端加速",
        "pattern_back": "后端加速",
        "expected_claim_ratio": "预计赔付率 (%)",
        "onerous_check": "执行亏损测试？",
        "lrc_init": "期初 LRC",
        "lic_init": "期初 LIC（0＝无已发生赔付）",
        "revenue": "保险收入",
        "claims_incurred": "已发生赔款",
        "exp_recognised": "保险服务支出",
        "net_result": "保险服务结果"


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
        "tab_ifrs17": "Application IFRS 17 CSM",
        "pnl_statement_title": "📈 Compte de résultat IFRS 17 projeté",
        "tab_pnl_statement": "Compte de résultat IFRS 17 projeté",
        "insurance_revenue": "Revenus d'assurance",
        "insurance_expense": "Dépenses d'assurance",
        "net_insurance_result": "Résultat net d'assurance",
        "csm_release": "Libération du CSM",
        "ra_release": "Libération de l'Ajustement pour Risque",
        "expected_benefit": "Prestations prévues",
        "expected_expense": "Dépenses prévues",
        "year": "Année",
        "actual_claims": "Sinistres Réels",
        "actual_expenses": "Dépenses Réelles",
        "actual_premiums": "primes effectives",
        "actual_inputs_expander": "saisir les flux de trésorerie réels (par an)",
        "balance_sheet_tab": "📊 Bilan",
        "balance_sheet_title": "Bilan",
        "csm_balance": "Solde du CSM",
        "ra_balance": "Solde de l'ajustement pour risque",
        "cash_balance": "Solde de trésorerie",
        "total_liabilities": "Total du passif",
        "retained_earnings": "Résultats non distribués",
        "total_equity": "Total des capitaux propres",
        "assets_liabilities_check": "Vérification : Actif = Passif + Capitaux propres",
        "total_assets": "Total de l’actif",
        "total_liab_equity": "Total des passifs et capitaux propres",
        "pv_future_cf": "VAN des flux de trésorerie futurs",
        "retained_earnings": "Résultats non distribués",
        "total_equity": "Total des capitaux propres",
        "total_assets": "Total de l’actif",
        "total_liabilities_equity": "Total passif + capitaux propres",
        "asset_liability_check": "Actif – (Passif + Capitaux propres)",
        "insurance_finance_expense": "Produits et charges financiers d'assurance",
        "current_discount_rate": "Taux d'actualisation courant (%)",
        "news_tab_title": "📰 Actualités IFRS 17 & Actuariat",
        "loss_component_init": "Composant de perte à la reconnaissance initiale",
        "loss_component_release": "Libération du composant de perte",
        "loss_component_balance": "Solde du composant de perte",
        "initial_lc_expense": "Composante de perte initiale",
        "assump_change_expander": "Mise à jour des hypothèses (prospective)",
        "assump_change_start":    "Appliquer les changements à partir de l’année …",
        "benefit_change_pct":     "Δ Prestations prévues (%)",
        "expense_change_pct":     "Δ Dépenses prévues (%)",
        "ra_new_pct":             "Nouvel ajustement pour risque (%)",
        "assump_change_loss":     "Augmentation du composant de perte",
        "assump_change_gain":     "Libération du composant de perte",
        "tab_paa": "PAA (Simplifié)",
        "paa_title": "📘 Calculateur PAA IFRS 17",
        "coverage_period": "Période de couverture (années)",
        "total_gwp": "Prime émise totale",
        "earned_premium_pattern": "Profil de reconnaissance du revenu",
        "pattern_even": "Linéaire",
        "pattern_front": "Chargé en début",
        "pattern_back": "Chargé en fin",
        "expected_claim_ratio": "Taux de sinistralité ultime (%)",
        "onerous_check": "Effectuer le test d’onérosité ?",
        "lrc_init": "LRC initiale",
        "lic_init": "LIC initiale (zéro → aucun sinistre encouru)",
        "revenue": "Revenus d’assurance",
        "claims_incurred": "Sinistres encourus",
        "exp_recognised": "Dépenses de service d’assurance",
        "net_result": "Résultat du service d’assurance"



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
        "tab_ifrs17": "تطبيق IFRS 17 CSM",
        "pnl_statement_title": "📈 بيان الأرباح والخسائر المتوقع لـ IFRS 17",
        "tab_pnl_statement": "بيان الأرباح والخسائر IFRS 17",
        "insurance_revenue": "إيرادات التأمين",
        "insurance_expense": "مصاريف التأمين",
        "net_insurance_result": "صافي نتائج التأمين",
        "csm_release": "تحرير هامش الخدمة التعاقدي",
        "ra_release": "تحرير تعديل المخاطر",
        "expected_benefit": "المدفوعات المتوقعة",
        "expected_expense": "المصروفات المتوقعة",
        "year": "السنة",
        "actual_claims": "المطالبات الفعلية",
        "actual_expenses": "المصروفات الفعلية",
        "actual_premiums": "الأقساط الفعلية",
        "actual_inputs_expander": "أدخل التدفقات النقدية الفعلية (سنويًا)",
        "balance_sheet_tab": "📊 الميزانية العمومية",
        "balance_sheet_title": "الميزانية العمومية",
        "csm_balance": "رصيد هامش الخدمة التعاقدية",
        "ra_balance": "رصيد التعديل للمخاطر",
        "cash_balance": "رصيد النقدية",
        "total_liabilities": "إجمالي الالتزامات",
        "retained_earnings": "الأرباح المحتجزة",
        "total_equity": "إجمالي حقوق الملكية",
        "assets_liabilities_check": "التحقق: الأصول = الالتزامات + حقوق الملكية",
        "total_assets": "إجمالي الأصول",
        "total_liab_equity": "إجمالي الالتزامات وحقوق الملكية",
        "pv_future_cf": "القيمة الحالية للتدفقات النقدية المستقبلية",
        "retained_earnings": "الأرباح المحتجزة",
        "total_equity": "إجمالي حقوق الملكية",
        "total_assets": "إجمالي الأصول",
        "total_liabilities_equity": "إجمالي الخصوم وحقوق الملكية",
        "asset_liability_check": "الأصول - (الخصوم + حقوق الملكية)",
        "insurance_finance_expense": "دخل ومصروف التمويل التأميني",
        "current_discount_rate": "معدل الخصم الحالي (%)",
        "news_tab_title": "📰 أخبار IFRS 17 والخبرة الاكتوارية",
        "loss_component_init": "مكوّن الخسارة عند الاعتراف الأولي",
        "loss_component_release": "إطلاق مكوّن الخسارة",
        "loss_component_balance": "رصيد مكوّن الخسارة",
        "initial_lc_expense": "مكون الخسارة الأولي",
        "assump_change_expander": "تحديث الفرضيات (مستقبلي)",
        "assump_change_start":    "تطبيق التغييرات ابتداءً من السنة …",
        "benefit_change_pct":     "تغيّر المنافع المتوقعة (%)",
        "expense_change_pct":     "تغيّر المصروفات المتوقعة (%)",
        "ra_new_pct":             "نسبة تعديل المخاطر الجديدة (%)",
        "assump_change_loss":     "زيادة مكوّن الخسارة",
        "assump_change_gain":     "تحرير مكوّن الخسارة",
        "tab_paa": "طريقة PAA (المبسطة)",
        "paa_title": "📘 حاسبة PAA لمعيار IFRS 17",
        "coverage_period": "فترة التغطية (بالسنوات)",
        "total_gwp": "إجمالي الأقساط المكتتبة",
        "earned_premium_pattern": "نمط الاعتراف بالإيراد",
        "pattern_even": "مستقيم (متساوٍ)",
        "pattern_front": "محمل مقدماً",
        "pattern_back": "محمل مؤخراً",
        "expected_claim_ratio": "نسبة الخسارة المتوقعة (%)",
        "onerous_check": "تنفيذ اختبار العجز؟",
        "lrc_init": "رصيد LRC الافتتاحي",
        "lic_init": "رصيد LIC الافتتاحي (صفر = لا مطالبات متكبدة)",
        "revenue": "إيرادات التأمين",
        "claims_incurred": "المطالبات المتكبدة",
        "exp_recognised": "مصاريف خدمة التأمين",
        "net_result": "نتيجة خدمة التأمين"






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
tab1, tab2, tab5 = st.tabs([t["tab_ifrs17"], t["tab_pnl_statement"], t["tab_paa"]])

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
                #input actual cash flows
                # Actual Premiums Input
                st.markdown("### " + t["actual_inputs_expander"])

                # Create a DataFrame for user to enter Actuals
                projection_years = len(premiums)
                default_actuals = {
                    t["year"]: list(range(1, projection_years + 1)),
                    t["actual_premiums"]: [100] * projection_years,
                    t["actual_claims"]: [30] * projection_years,
                    t["actual_expenses"]: [10] * projection_years
                }

                actuals_df = pd.DataFrame(default_actuals)

                edited_df = st.data_editor(actuals_df, use_container_width=True, num_rows="dynamic")
                # Extract actual cash flow inputs from edited_df
                actual_premiums = edited_df[t["actual_premiums"]].tolist()
                actual_claims = edited_df[t["actual_claims"]].tolist()
                actual_expenses = edited_df[t["actual_expenses"]].tolist()

                # Included another section to introduce assumption changes on non-financial assumptions    
                with st.expander("🛠️  " + t["assump_change_expander"]):
                    change_year = st.number_input(
                        t["assump_change_start"], min_value=1,
                        max_value=len(premiums), value=len(premiums)//2
                    )

                    benefit_factor = st.number_input(
                        t["benefit_change_pct"], value=0.0, step=0.01
                    ) / 100

                    expense_factor = st.number_input(
                        t["expense_change_pct"], value=0.0, step=0.01
                    ) / 100

                    ra_new_pct = st.number_input(
                        t["ra_new_pct"], value=ra_pct*100, step=0.1
                    ) / 100

                with st.expander("📉 Enter Current Discount Rates (for IFIE calculation)"):
                    projection_years = len(premiums)  

                    # Default: use initial discount rate
                    default_discount_rates = {
                        t["year"]: list(range(1, projection_years + 1)),
                        t["current_discount_rate"]: [discount_rate * 100] * projection_years  # As %
                    }

                    discount_rate_df = pd.DataFrame(default_discount_rates)
                    edited_discount_rate_df = st.data_editor(discount_rate_df, use_container_width=True, num_rows="fixed")
                    
                    # Convert to decimal for calculation
                    current_discount_rates = [r / 100 for r in edited_discount_rate_df[t["current_discount_rate"]].tolist()]




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

    result = {}

    # --- inside Tab-1, just after you build `result = {...}` and show the success messages
    st.session_state["csm_ready"] = True        # <-- add this single line

    if st.button(t["calculate"]):
        if None in (premiums, benefits, expenses, coverage_units):
            st.error("Missing inputs. Please provide all required fields.")
        else:
            pv_premiums = sum([p / ((1 + discount_rate) ** i) for i, p in enumerate(premiums)])
            pv_benefits = sum([b / ((1 + discount_rate) ** i) for i, b in enumerate(benefits)])
            pv_expenses = sum([e / ((1 + discount_rate) ** i) for i, e in enumerate(expenses)])
            total_pv = pv_benefits + pv_expenses
            risk_adj = total_pv * ra_pct
            csm =  pv_premiums - total_pv - risk_adj

            # ---------- LOSS COMPONENT CHECK ----------
            if csm < 0:                     # group is onerous
                loss_component_init = -csm  # positive number carried in liabilities
                csm = 0.0                   # CSM cannot be negative
            else:
                loss_component_init = 0.0


            result = {
                "CSM at Initial Recognition": csm,
                "Risk Adjustment": risk_adj,
                "Loss Component": loss_component_init
            }

            st.success(f"✅ CSM at Initial Recognition: {csm:,.2f}")
            st.success(f"✅ Risk Adjustment: {risk_adj:,.2f}")
            st.success(f"✅ Loss Component: {loss_component_init:,.2f}")

            # Calculate the impact of change in non-financial assumptions
            def recalc_delta_future_cf(i_start):
                """
                Change in PV of future benefits+expenses and RA from year i_start onward,
                using the user-entered assumption shifts.
                """
                ben_new = benefits.copy()
                exp_new = expenses.copy()

                for j in range(i_start, len(benefits)):
                    ben_new[j] *= (1 + benefit_factor)
                    exp_new[j] *= (1 + expense_factor)

                def pv(arr):
                    return sum(x / ((1 + discount_rate) ** k)
                            for k, x in enumerate(arr[i_start:], start=0))

                pv_old = pv([benefits[k] + expenses[k] for k in range(i_start, len(benefits))])
                pv_new = pv([ben_new[k] + exp_new[k]   for k in range(i_start, len(benefits))])

                delta_pv = pv_new - pv_old
                delta_ra = delta_pv * ra_new_pct - pv_old * ra_pct
                return delta_pv, delta_ra, ben_new, exp_new

            # ---------------------------------------------------------------
            
            # --------------------------------------------------------------------
            #  Build “new” assumption arrays directly from the user-entered shifts
            # --------------------------------------------------------------------
            projection_years = len(benefits)

            # 2-a  Benefits & Expenses after the change _____________
            new_benefits = [b * (1 + benefit_factor) if benefit_factor else b
                            for b in benefits]
            new_expenses = [e * (1 + expense_factor) if expense_factor else e
                            for e in expenses]

            # 2-b  Risk-adjustment percentage after the change ______
            new_ra_pct   = [ra_new_pct] * projection_years      # same % each year
            
            #  Δ-tables coming from the user
            benefit_deltas   = [new_benefits[i]  - benefits[i]  for i in range(projection_years)]
            expense_deltas   = [new_expenses[i]  - expenses[i]  for i in range(projection_years)]
            ra_pct_deltas    = [new_ra_pct[i]    - ra_pct       for i in range(projection_years)]

            # Convert the RA-% change into a *currency* amount that affects CSM
            ra_future        = risk_adj                            # opening RA (future service)
            ra_delta_amounts = []
            for i in range(projection_years):
                # Adjust RA for the changed % (simplified – same base all years)
                new_ra_amt      = ra_future * (1 + ra_pct_deltas[i])
                delta_ra_amt    = new_ra_amt - ra_future
                ra_delta_amounts.append(delta_ra_amt)
                ra_future       = new_ra_amt                       # roll forward

            # FINAL list consumed by the CSM engine
            assump_deltas = [
                    -(benefit_deltas[i] + expense_deltas[i])      # PV of CF change (opposite sign)
                    - ra_delta_amounts[i]                         # RA change for future service
                    for i in range(projection_years)
            ]
            # ---------------------------------------------------------------

            #For the chart
            # -----------------------------------------------------------------
            def calculate_csm_from_pl(csm_opening,
                                    discount_rate,
                                    coverage_units,
                                    premiums,
                                    actual_premiums,
                                    assump_deltas):
                """
                Returns two equal-length lists:
                    csm_release[i]   – amount recognised in year i+1
                    csm_balance[i]   – closing balance at end of year i+1
                It mirrors the logic used in Tab 2 (P&L).
                """
                num_years   = len(coverage_units)
                rel, bal    = [], []
                csm_start   = csm_opening

                for i in range(num_years):
                    interest        = csm_start * discount_rate
                    delta_premium   = actual_premiums[i] - premiums[i]
                    delta_assump    = assump_deltas[i]          # ← NEW piece
                    csm_available   = csm_start + interest + delta_premium + delta_assump

                    remaining_units = sum(coverage_units[i:])
                    share           = coverage_units[i] / remaining_units if remaining_units else 0
                    release         = csm_available * share

                    csm_end         = csm_available - release

                    rel.append(release)
                    bal.append(csm_end)
                    csm_start       = csm_end

                return rel, bal
            # -----------------------------------------------------------------

            # ----------------------------------------------------------------------
            def apply_future_assumption_shifts(start_i: int,
                                            ben: list[float],
                                            exp: list[float],
                                            ra_init: float) -> tuple[list[float],
                                                                        list[float],
                                                                        float]:
                """
                Return (benefits_adj, expenses_adj, ra_adj) *after* applying
                user-specified % shocks from index start_i onward (0-based).
                """
                # clone so we don't mutate originals
                ben_new = ben.copy()
                exp_new = exp.copy()

                for j in range(start_i, len(ben)):
                    ben_new[j] *= (1 + benefit_factor)
                    exp_new[j] *= (1 + expense_factor)

                # RA at initial recognition was 'ra_init' (= total_pv * ra_pct)
                total_pv_old = sum(b + e for b, e in zip(ben, exp))
                total_pv_new = sum(b + e for b, e in zip(ben_new, exp_new))
                ra_new_full  = total_pv_new * ra_new_pct

                return ben_new, exp_new, ra_new_full
            # ----------------------------------------------------------------------


            # ----------------------------------------------------------------------

            # Show charts
            # don't need this anymore
            #def calculate_csm_dynamic_release(csm_initial, discount_rate, coverage_units, premiums, actual_premiums, assump_deltas):
            #    num_years = len(coverage_units)
            #    csm_balance = []
            #    csm_release = []
            #    csm_start = csm_initial
            #    for i in range(num_years):
            #        interest = csm_start * discount_rate
            #        delta_premium = actual_premiums[i] - premiums[i]
            #        delta_assump = assump_deltas[i]
            #        csm_available = csm_start + interest + delta_premium + delta_assump
            #        remaining_units = sum(coverage_units[i:])
            #        proportion = coverage_units[i] / remaining_units if remaining_units > 0 else 0
            #        release = csm_available * proportion
            #        csm_end = csm_available - release
            #        csm_release.append(release)
            #        csm_balance.append(csm_end)
            #        csm_start = csm_end
            #    return csm_release, csm_balance

            # ----- non-financial assumption change year -------------------------
            assump_change_year = st.number_input(
                "Year in which new assumptions start (1 = first projection year)",
                min_value=1,
                max_value=len(premiums),
                value=1,
                step=1
            )


            def show_csm_chart(csm_total, premiums, benefits, expenses, risk_adj, num_years, discount_rate, coverage_units, assump_change_year, benefit_factor, expense_factor, ra_new_pct, loss_component_init, show_tutorial=False):
                years = list(range(1, num_years + 1))
                if coverage_units is None:
                    coverage_units = [1] * num_years

                # ❶ Apply assumption change from the chosen year (1-based → 0-based index)
                idx_change   = assump_change_year - 1
                benefits_adj, expenses_adj, ra_adj = apply_future_assumption_shifts(
                    idx_change, benefits, expenses, risk_adj)

                # ❷ Re-compute CSM *prospectively* at the change date
                pv_ben_old = sum( benefits[i] / ((1+discount_rate)**i) for i in range(idx_change, num_years) )
                pv_exp_old = sum( expenses[i] / ((1+discount_rate)**i) for i in range(idx_change, num_years) )
                pv_ben_new = sum( benefits_adj[i] / ((1+discount_rate)**i) for i in range(idx_change, num_years) )
                pv_exp_new = sum( expenses_adj[i] / ((1+discount_rate)**i) for i in range(idx_change, num_years) )

                delta_pv   = (pv_ben_new + pv_exp_new) - (pv_ben_old + pv_exp_old)
                delta_ra   = ra_adj - risk_adj        # positive if RA% increased

                csm_total  = csm_total - delta_pv - delta_ra   # IFRS 17 para B96(b)

                # ❸ Now run the *existing* dynamic-release engine on the adjusted inputs
                csm_release, csm_balance = calculate_csm_from_pl(
                    csm_total, discount_rate, coverage_units, premiums, actual_premiums, assump_deltas
                )
                total_units = sum(coverage_units)
                # RA release with accretion at current rate
                ra_release = []
                ra_balance_csm = []
                ra_start = result["Risk Adjustment"]

                for i in range(len(coverage_units)):
                    ra_interest = ra_start * current_discount_rates[i]  # current rate accretion
                    ra_start += ra_interest

                    lc_alloc = 1 - loss_component_init / (total_pv)
                    portion = coverage_units[i] / total_units if total_units > 0 else 0
                    release = result["Risk Adjustment"] * portion
                    ra_release.append(release)

                    ra_end = ra_start - release
                    ra_balance_csm.append(ra_end)
                    ra_start = ra_end  # update for next period


                if show_tutorial:
                    st.info(tutorial_text[lang]["charts"])


                st.subheader(t["csm_release_title"])
                fig1, ax1 = plt.subplots(figsize=(10, 4))
                ax1.plot(years, csm_release, label="CSM Release", marker="o")
                ax1.plot(years, csm_balance, label="CSM Balance (EOP)", marker="o", linestyle="--")
                for x, y in zip(years, csm_balance):
                    ax1.annotate(f"{y:,.0f}", xy=(x, y), xytext=(0, 8),
                                textcoords="offset points", ha="center", fontsize=9)
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

            assump_deltas = [0.0] * len(premiums)

            show_csm_chart(
                result["CSM at Initial Recognition"],
                premiums,
                benefits,
                expenses,
                result["Risk Adjustment"],
                len(premiums),
                discount_rate,
                coverage_units,
                assump_change_year,     
                benefit_factor,
                expense_factor,
                ra_new_pct,
                loss_component_init
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

with tab2:

    if not st.session_state.get("csm_ready"):
        st.info("↖️ Run the calculation in the CSM tab first, then come back here.")
        st.stop()          # nothing below will execute until the flag is set

    # --- IFRS 17-Compliant P&L Statement ---
    st.subheader("📈 " + t["pnl_statement_title"])

    # Total units for proportional allocation
    total_units = sum(coverage_units)

    projection_years = len(premiums)
    pv_premiums = sum([p / ((1 + discount_rate) ** i) for i, p in enumerate(premiums)])
    pv_benefits = sum([b / ((1 + discount_rate) ** i) for i, b in enumerate(benefits)])
    pv_expenses = sum([e / ((1 + discount_rate) ** i) for i, e in enumerate(expenses)])
    total_pv = pv_benefits + pv_expenses
    risk_adj = total_pv * ra_pct
    csm = pv_premiums - total_pv - risk_adj
    
    # ---------- LOSS COMPONENT CHECK ----------
    if csm < 0:                     # group is onerous
        loss_component_init = -csm  # positive number carried in liabilities
        csm = 0.0                   # CSM cannot be negative
    else:
        loss_component_init = 0.0
    
    lc_alloc = 1 - loss_component_init / (total_pv) 
    ra_release = [risk_adj / projection_years] * projection_years 

    # --- RA Accretion and Balance using Current Discount Rates ---
    ra_start = risk_adj
    ra_accretion = []
    ra_balance = []

    for i in range(projection_years):
        current_rate = current_discount_rates[i]
        accrete_interest = ra_start * current_rate
        ra_start += accrete_interest
        ra_release_amt = ra_start * (coverage_units[i] / total_units)
        ra_end = ra_start - ra_release_amt

        ra_accretion.append(accrete_interest)
        ra_balance.append(ra_end)
        ra_start = ra_end

    # --- PVFCF Accretion ---
    pvfcf_balance = []
    pv_benefits_expenses = [benefits[i] + expenses[i] for i in range(projection_years)]
    pvfcf = sum([cf / ((1 + discount_rate) ** i) for i, cf in enumerate(pv_benefits_expenses)])

    for i in range(projection_years):
        current_rate = current_discount_rates[i]
        accrete_interest = pvfcf * current_rate
        pvfcf += accrete_interest - pv_benefits_expenses[i]
        pvfcf_balance.append(pvfcf)

    pl_data = []
    csm_start = csm
    lc_start  = max(-csm_start, 0)        # initial Loss Component (if onerous)
    lc_balance = lc_start

    for i in range(projection_years):
        # ---- 3·1  Interest on opening CSM
        csm_int = csm_start * discount_rate

        # ---- 3·2  Premium variance already in your code
        delta_prem = actual_premiums[i] - premiums[i]

        # ---- 3·3  Assumption change kicks in?
        if i + 1 == change_year:
            Δpv, Δra, benefits, expenses = recalc_delta_future_cf(i)
            ra_pct = ra_new_pct                    # store new % for future years
        else:
            Δpv = Δra = 0

        # ---- 3·4  Absorb Δ’s into CSM or Loss Component
        adjust_CSM = -(Δpv + Δra)                 # sign convention
        if csm_start + csm_int + delta_prem >= adjust_CSM >= 0:
            csm_after_adj = csm_start + csm_int + delta_prem - adjust_CSM
            lc_release = 0
            lc_increase = 0
        else:
            # insufficient CSM – create / add to Loss Component
            deficiency = adjust_CSM - (csm_start + csm_int + delta_prem)
            csm_after_adj = 0
            lc_increase   = deficiency
            lc_release    = 0

        # if CSM > 0 and LC exists, favourable Δ first reverses LC
        if lc_balance > 0 and adjust_CSM < 0:
            reversal = min(lc_balance, -adjust_CSM)
            lc_release = reversal          # treated as negative expense
            lc_balance -= reversal
            adjust_CSM += reversal         # remainder (if any) to CSM
            csm_after_adj = csm_start + csm_int + delta_prem - adjust_CSM

        lc_balance += lc_increase

        # ---- 3·5  Coverage-units release
        remaining_units = sum(coverage_units[i:])
        release_prop   = coverage_units[i] / remaining_units if remaining_units else 0
        csm_rel        = csm_after_adj * release_prop
        csm_end        = csm_after_adj - csm_rel

        # ---- 3·6  RA paths (your new accretion code stays as-is)
        ra_rel   = ra_release[i]           # already computed earlier
        ra_int   = ra_accretion[i]
        ra_end   = ra_balance[i]

        # ---- 3·7  IFRS-17 lines for year i+1
        exp_ben_exp = benefits[i] + expenses[i]
        insurance_revenue = csm_rel + ra_rel + exp_ben_exp
        insurance_expense = actual_claims[i] + actual_expenses[i] \
                            + lc_increase - lc_release            # LC inc (+) or release (–)
        ifie = -csm_int + ra_int + pvfcf_balance[i]*current_discount_rates[i]

        net_result = insurance_revenue - insurance_expense + ifie

        # ---- 3·8  Store row for table
        pl_data.append({
            t["csm_release"]:      round(csm_rel,2),
            t["ra_release"]:       round(ra_rel,2),
            t["expected_benefit"]: round(benefits[i],2),
            t["expected_expense"]: round(expenses[i],2),
            t["insurance_revenue"]: round(insurance_revenue,2),
            t["actual_claims"]:     round(actual_claims[i],2),
            t["actual_expenses"]:   round(actual_expenses[i],2),
            t["insurance_expense"]: round(insurance_expense,2),
            t["assump_change_loss"]: round(lc_increase,2) if lc_increase else "",
            t["assump_change_gain"]: round(-lc_release,2) if lc_release  else "",
            t["insurance_finance_expense"]: round(ifie,2),
            t["net_insurance_result"]:      round(net_result,2),
        })

        # ---- 3·9  roll forward CSM & RA
        csm_start = csm_end
        #  (ra_balance[i] already holds closing RA)



    pl_df = pd.DataFrame(pl_data).T
    # Build Markdown table manually
    markdown_table = "| " + " | ".join(["**" + str(col) + "**" for col in pl_df.columns.insert(0, "Year")]) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * (len(pl_df.columns) + 1)) + " |\n"

    for idx, (row_label, row_data) in enumerate(pl_df.iterrows()):
        is_important = row_label in [
            t["insurance_revenue"],
            t["insurance_expense"],
            t["insurance_finance_expense"],
            t["net_insurance_result"]
        ]
        
        # Insert horizontal lines BEFORE the important rows
        if row_label == t["insurance_revenue"] or row_label == t["insurance_expense"] or row_label == t["insurance_finance_expense"]:
            markdown_table += "|---" + "|---" * projection_years + "|\n"
        elif row_label == t["net_insurance_result"]:
            markdown_table += "|===" + "|===" * projection_years + "|\n"

        display_label = f"**{row_label}**" if is_important else row_label
        def _fmt(val: object, important: bool) -> str:
            """Return a nicely-formatted string; bold if important."""
            try:
                # works for int, float, numpy numbers, pd NA with float coercion
                txt = f"{float(val):,.2f}"
            except (TypeError, ValueError):
                # leave non-numeric values (or real NaNs) unchanged
                txt = str(val)
            return f"**{txt}**" if important else txt

        values = [_fmt(v, is_important) for v in row_data]
        row_str = "| " + display_label + " | " + " | ".join(values) + " |\n"
        markdown_table += row_str

    # Display the markdown table
    st.markdown(markdown_table)



#New section for the Job Board - updated on 06/21/2025
job_listings = [
    {
        "title": "IFRS 17 Lead Actuary",
        "company": "Allianz SE",
        "location": "Munich, Germany",
        "date": "2025-06-12",
        "link": "https://careers.allianz.com/job/ifrs17-lead-actuary"
    },
    {
        "title": "Senior Actuarial Analyst – IFRS 17",
        "company": "AIA Group",
        "location": "Hong Kong",
        "date": "2025-06-10",
        "link": "https://careers.aia.com/job/ifrs17-analyst-hk"
    },
    {
        "title": "IFRS 17 Reporting Manager",
        "company": "Qatar Insurance",
        "location": "Doha, Qatar",
        "date": "2025-06-09",
        "link": "https://qic.qa/careers/ifrs17-reporting-manager"
    },
    {
        "title": "Actuarial Consultant – IFRS 17 / LDTI",
        "company": "PwC Middle East",
        "location": "Dubai, UAE",
        "date": "2025-06-11",
        "link": "https://www.pwc.com/me/jobs/ifrs17-consultant"
    },
    {
        "title": "Group Finance Analyst (IFRS 17)",
        "company": "Ping An Insurance",
        "location": "Shenzhen, China",
        "date": "2025-06-08",
        "link": "https://talent.pingan.cn/job/43321"
    },
    {
        "title": "IFRS 17 Implementation Lead",
        "company": "Zurich Insurance",
        "location": "Singapore",
        "date": "2025-06-07",
        "link": "https://www.zurich.com/en/careers/jobs/ifrs17-lead-sg"
    },
    {
        "title": "Valuation Actuary – IFRS 17",
        "company": "AXA Gulf",
        "location": "Bahrain",
        "date": "2025-06-06",
        "link": "https://gulf.axa-careers.com/job/valuation-actuary-ifrs17"
    },
    {
        "title": "IFRS 17 Technical Specialist",
        "company": "Swiss Re",
        "location": "Zurich, Switzerland",
        "date": "2025-06-05",
        "link": "https://www.swissre.com/careers/job/ifrs17-tech-specialist"
    }
]

# with tab3:
    # --- Job Board Section ---
#    st.markdown("---")
#    st.subheader("💼 " + t["job_board"])
#    st.caption("🔎 Last Verified: June 2025")
#
#    for job in job_listings:
#        with st.container():
#            st.markdown(f"**🧑‍💼 {job['title']}**  \n"
#                        f"🏢 {job['company']} | 📍 {job['location']}  \n"
#                        f"[{t['apply']}]({job['link']})", unsafe_allow_html=True)
#            st.markdown("---")
#
#    #add custom CSS
#    st.markdown("""
#    <style>
#    a {
#        text-decoration: none;
#        color: #0066cc;
#    }
#    a:hover {
#        text-decoration: underline;
#    }
#    </style>
#    """, unsafe_allow_html=True)



# Curated articles
news_items = [
    {
        "title_en": "IASB issues June 2025 IFRS 17 implementation update",
        "title_zh": "IASB 发布 2025 年 6 月 IFRS 17 实施更新",
        "title_fr": "L'IASB publie la mise à jour de juin 2025 sur l’application d’IFRS 17",
        "title_ar": "مجلس معايير المحاسبة الدولية يصدر تحديث يونيو 2025 لتطبيق المعيار IFRS 17",
        "url": "https://www.ifrs.org/news/2025/06/iasb-ifrs17-update/",
        "date": "2025-06-11"
    },
    {
        "title_en": "Dubai FSA reminds insurers of July IFRS 17 filing deadline",
        "title_zh": "迪拜金融监管局提醒保险公司 7 月 IFRS 17 申报截止",
        "title_fr": "La DFSA rappelle aux assureurs la date limite de dépôt IFRS 17 en juillet",
        "title_ar": "سلطة دبي للخدمات المالية تُذَكِّر شركات التأمين بموعد تقديم تقارير IFRS 17 في يوليو",
        "url": "https://dfsa.ae/news/ifrs17-filing-deadline",
        "date": "2025-06-10"
    },
    {
        "title_en": "KPMG survey: 68 % of Asia insurers adjust CSM after first-year experience",
        "title_zh": "毕马威调查：68% 亚洲保险公司首年后调整 CSM",
        "title_fr": "Étude KPMG : 68 % des assureurs asiatiques ajustent la MSC après la première année",
        "title_ar": "استطلاع KPMG: ‎%68 من شركات التأمين الآسيوية تعدّل هامش الخدمة التعاقدية بعد العام الأول",
        "url": "https://home.kpmg/xx/en/home/insights/2025/06/asia-ifrs17-survey.html",
        "date": "2025-06-09"
    },
    {
        "title_en": "Saudi CMA publishes IFRS 17 Q&A for cooperative insurers",
        "title_zh": "沙特 CMA 发布合作保险公司 IFRS 17 问答",
        "title_fr": "L’Autorité des marchés saoudienne publie une FAQ IFRS 17 pour les assureurs coopératifs",
        "title_ar": "هيئة السوق المالية السعودية تصدر أسئلة وأجوبة حول المعيار IFRS 17 لشركات التأمين التعاونية",
        "url": "https://cma.org.sa/en/IFRS17-FAQ",
        "date": "2025-06-09"
    },
    {
        "title_en": "Munich Re Q1-25 results: first IFRS 17 balance shows €1.9 bn CSM",
        "title_zh": "慕再 2025 年一季度 IFRS 17 报表首次显示 19 亿欧元 CSM",
        "title_fr": "Résultats T1-25 de Munich Re : premier bilan IFRS 17 affiche 1,9 Md € de MSC",
        "title_ar": "نتائج ميونخ ري للربع الأول 2025: أول ميزانية وفق IFRS 17 تُظهر هامش خدمة بـ1.9 مليار €",
        "url": "https://www.munichre.com/en/company/investors/results/q1-2025.html",
        "date": "2025-06-07"
    },
    {
        "title_en": "PwC tool benchmarks IFRS 17 RA calibration trends across EMEA",
        "title_zh": "普华永道工具对比 EMEA 地区 IFRS 17 风险调整校准趋势",
        "title_fr": "Un outil PwC compare les tendances d’étalonnage de l’ajustement pour risque IFRS 17 en EMEA",
        "title_ar": "أداة PwC تقارن اتجاهات معايرة تعديل المخاطر (IFRS 17) عبر أوروبا والشرق الأوسط وإفريقيا",
        "url": "https://www.pwc.com/ifrs17/ra-benchmark-2025",
        "date": "2025-06-06"
    },
    {
        "title_en": "MAS issues guidance on OCI vs P&L option under IFRS 17",
        "title_zh": "新加坡金管局发布 IFRS 17 其它综合收益与损益选项指引",
        "title_fr": "La MAS publie des directives sur l’option OCI vs résultat selon IFRS 17",
        "title_ar": "سلطة النقد السنغافورية تصدر إرشادات حول خيار الدخل الشامل الآخر مقابل الربح والخسارة في IFRS 17",
        "url": "https://www.mas.gov.sg/regulation/notices/ifrs17-oci",
        "date": "2025-06-05"
    },
    {
        "title_en": "EY white-paper: modelling loss-component release paths",
        "title_zh": "安永白皮书：损失组件释放路径建模",
        "title_fr": "Livre blanc EY : modélisation de la libération du composant de perte",
        "title_ar": "ورقة عمل EY: نمذجة مسار تحرير مكوّن الخسارة",
        "url": "https://www.ey.com/en_gl/insurance/ifrs17-loss-component-release",
        "date": "2025-06-05"
    },
    {
        "title_en": "APRA warns on data-quality gaps in Australian IFRS 17 submissions",
        "title_zh": "澳洲审慎监管局警示 IFRS 17 报送数据缺口",
        "title_fr": "L’APRA alerte sur les lacunes de qualité des données dans les dossiers IFRS 17 australiens",
        "title_ar": "هيئة الرقابة المالية الأسترالية تحذر من فجوات جودة البيانات في تقارير IFRS 17",
        "url": "https://www.apra.gov.au/news/media-release-ifrs17-data-quality",
        "date": "2025-06-04"
    },
    {
        "title_en": "Willis Towers Watson launches cloud CSM engine for ME insurers",
        "title_zh": "韦莱将推出面向中东保险公司的云端 CSM 引擎",
        "title_fr": "WTW lance un moteur MSC cloud pour les assureurs du Moyen-Orient",
        "title_ar": "ويليس تاورز واتسون تطلق محرك CSM سحابي لشركات التأمين في الشرق الأوسط",
        "url": "https://www.wtwco.com/en/news/2025/06/wtw-cloud-csm-engine",
        "date": "2025-06-03"
    }
]
 


# with tab4:
#    st.subheader("📰 " + t["news_tab_title"])
#
#    for article in news_items:
#        localized_title = article.get(f"title_{lang}", article["title_en"])
#        st.markdown(f"- [{localized_title}]({article['url']}) — {article['date']}")
#
#
#
#    st.markdown("***")
#    st.markdown({
#    "en":"*Disclaimer: Headlines © their respective publishers. "
#         "Links open external sites; XL Financial Group is not responsible for the content. "
#         "Links may stop working—please run a fresh search if needed.*",
#    "zh":"*免责声明：标题版权归原出版方所有。点击链接将跳转至外部网站，"
#         "XL Financial Group 不对其内容承担责任。链接可能失效，如有需要请重新搜索。*",
#    "fr":"*Avertissement : Titres © leurs éditeurs respectifs. Les liens ouvrent des sites externes ;"
#         "XL Financial Group n’est pas responsable du contenu; "
#         "Les liens peuvent devenir inactifs ; effectuez une nouvelle recherche si nécessaire.*",
#    "ar":"*إخلاء مسؤولية: المحتوى لأغراض المعلومات فقط ولا يعد نصيحة مهنية"
#         "عناوين الأخبار © للناشرين الأصليين. الروابط تفتح مواقع خارجية؛ ."
#         "لا تتحمّل ‎XL Financial Group مسؤولية المحتوى."
#         "قد تتوقف الروابط عن العمل — يُنصح المستخدم بالبحث من جديد إذا لزم الأمر.*"
#    }[lang])


#Simplified PAA tab
with tab5:
    st.subheader(t["paa_title"])
    st.markdown("---")

    # ----- BASIC INPUTS ---------------------------------------------------
    col_a, col_b = st.columns(2)
    with col_a:
        cov_years = st.number_input(t["coverage_period"], 1, 20, 1)
        gwp       = st.number_input(t["total_gwp"], value=1_000_000.0, step=10_000.0)

    with col_b:
        loss_ratio = st.number_input(t["expected_claim_ratio"], value=70.0, step=1.0)/100
        pattern    = st.selectbox(t["earned_premium_pattern"],
                                  [t["pattern_even"], t["pattern_front"], t["pattern_back"]])
        run_urtest = st.checkbox(t["onerous_check"], value=False)

    # ----- RECOGNITION PATTERN -------------------------------------------
    yrs = list(range(1, cov_years+1))
    if pattern == t["pattern_even"]:
        earn_factor = [1/cov_years]*cov_years
    elif pattern == t["pattern_front"]:
        earn_factor = [2/(cov_years*(cov_years+1))*(cov_years-i+1) for i in yrs]
    else:  # back-loaded
        earn_factor = [2/(cov_years*(cov_years+1))*i for i in yrs]

    earned_prem = [gwp * f for f in earn_factor]
    cum_earned  = [sum(earned_prem[:i]) for i in yrs]
    unearned    = [gwp - ce for ce in cum_earned]

    # ----- INITIAL BALANCES ----------------------------------------------
    lrc_open = gwp                      # simplest: acquisition CF = 0
    lic_open = 0.0                     # assume no incurred claims initially

    # ----- TABLE CALC -----------------------------------------------------
    rows = []
    onerous_now = False
    for i, yr in enumerate(yrs, start=0):
        revenue = earned_prem[i]
        claims  = revenue * loss_ratio

        # service expense = claims (no RA / no exp here)
        service_exp = claims
        result_srv  = revenue - service_exp

        # update LRC & LIC
        lrc_close = unearned[i]
        lic_close = lic_open + claims   # still no payments modelled

        if run_urtest:
            onerous_now = lrc_close < 0

        rows.append({
            t["year"]: yr,
            t["revenue"]: revenue,
            t["claims_incurred"]: claims,
            t["exp_recognised"]: service_exp,
            t["net_result"]: result_srv,
            t["lrc_init"] if i==0 else "": lrc_open if i==0 else "",
            t["lic_init"] if i==0 else "": lic_open if i==0 else "",
            "LRC close": lrc_close,
            "LIC close": lic_close,
            "Onerous?": "⚠️" if onerous_now else "✅"
        })

        # roll forward openings
        lrc_open = lrc_close
        lic_open = lic_close

    # --- build DataFrame and apply number-only formatting -------------------
    df = pd.DataFrame(rows).set_index(t["year"])

    # choose only numeric columns for formatting
    num_cols = df.select_dtypes("number").columns
    fmt_dict = {col: "{:,.0f}" for col in num_cols}

    st.dataframe(df.style.format(fmt_dict), use_container_width=True)



