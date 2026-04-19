# from dotenv import load_dotenv
# import os
# import openai

# openai.api_type = "azure"
# openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
# openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
# openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

# deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

# def classify_document(document_content):
#     """
#     Classifies the document layout as 'structured' or 'unstructured' based on text and table information.
#     """
#     text = document_content["text"]
#     tables = document_content["tables"]

#     # Prepare the prompt
# #     prompt = f"""
# # You are an AI assistant. Classify the following document layout as either 'structured' or 'unstructured'.

# # Structured documents typically contain tables, forms, or consistent layouts (e.g., insurance forms like ACORD). 
# # Unstructured documents contain free-form text, paragraphs, or inconsistent layouts (e.g., quote documents).

# # When classifying, ignore elements such as bullet points, headers, numbered sections, or indentation. Focus solely on the presence forms, or highly structured layouts.


# # Document Text:
# # {text[:2000]}

# # Tables:
# # {tables if tables else "No tables detected"}

# # Reply with only one word: structured or unstructured.
# # """


# #     prompt = f"""
# # You are an AI assistant. Classify the following document layout as either 'structured' or 'unstructured'.

# # Structured documents typically contain tables, forms, or consistent layouts. 
# # Unstructured documents contain free-form text, paragraphs, or inconsistent layouts.

# # When classifying, ignore formatting elements such as bullet points, headers, numbered sections, or indentation. Focus only on the presence of forms, or visually structured layouts.


# # Document Text:
# # {text[:2000]}

# # Tables:
# # {tables if tables else "No tables detected"}

# # Reply with only one word: structured or unstructured.
# # """



#     prompt = f"""
# You are an AI assistant. Classify the following document layout as either 'structured' or 'unstructured'.

# Structured documents contain tables, forms, or consistent visual layouts.
# Unstructured documents contain mostly free-form text, narrative content, or inconsistent layouts.

# Ignore formatting elements such as bullet points, headers, numbered sections, or indentation.
# Ignore business language, section titles, or document purpose. Focus only on the presence of tables, forms, or structured visual elements.

# Tables Detected: {len(tables)} table(s)

# Document Text Sample:
# {text[:1500]}

# Reply with only one word: structured or unstructured.
# """

#     response = openai.ChatCompletion.create(
#         engine=deployment_name,
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=4,
#         temperature=0.0  # Ensure deterministic responses
#     )
#     return response['choices'][0]['message']['content'].strip()











# # classifier.py

# from dotenv import load_dotenv

# import os

# from openai import AzureOpenAI

# # load env

# load_dotenv()

# # Required env vars (keep your existing names)

# AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

# AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

# AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

# if not (AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_VERSION and AZURE_OPENAI_API_KEY and AZURE_OPENAI_CHAT_DEPLOYMENT):

#     raise RuntimeError("Azure OpenAI env vars missing. Please set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_API_KEY and AZURE_OPENAI_CHAT_DEPLOYMENT")

# # Create new OpenAI client (v1+)

# client = AzureOpenAI(

#     api_key=AZURE_OPENAI_API_KEY,

#     api_base=AZURE_OPENAI_ENDPOINT,

#     api_type="azure",

#     api_version=AZURE_OPENAI_API_VERSION,

# )

# def classify_document(document_content):

#     """

#     Classifies the document layout as 'structured' or 'unstructured' based on text and table information.


#     """

#     text = document_content.get("text", "")

#     tables = document_content.get("tables", "")

# #     prompt = f"""

# # You are an AI assistant. Classify the following document layout as either 'structured' or 'unstructured'.

# # Structured documents typically contain tables, forms, or consistent layouts (e.g., insurance forms like ACORD). 

# # Unstructured documents contain free-form text, paragraphs, or inconsistent layouts (e.g., quote documents).

# # Document Text:

# # {text[:2000]}

# # Tables:

# # {tables if tables else "No tables detected"}

# # Reply with only one word: structured or unstructured.

# # """


#     prompt = f"""
# You are an expert in insurance documentation and intelligent document processing.

# Your task is to identify whether a given document is an ACORD insurance form or not.

# ACORD forms are standardized insurance documents published by the Association for Cooperative Operations Research and Development (ACORD).
# They include forms such as ACORD 25 (Certificate of Liability Insurance), ACORD 27 (Evidence of Property Insurance), ACORD 130 (Workers Compensation Application), etc.

# Classify the following document based on its content.
# Decide whether it is an ACORD Form or Non-ACORD Document.

# Definitions:

# ACORD Form:
# A standardized insurance form that typically includes the word “ACORD” followed by a form number (e.g., “ACORD 25 (2016/03)”),
# fields such as “Producer,” “Insured,” “Certificate Holder,” “Policy Number,” “Authorized Representative,” and often displays the ACORD logo or header.
# These documents summarize insurance coverage, liability, or property details.

# Non-ACORD Document:
# Any document that does not follow the ACORD format — e.g., invoices, contracts, letters, claims, proposals, or policy text.

# Document Content:
# {text[:2000]}

# Reply with only one word: ACORD or Non-ACORD.
# """


#     # For Azure OpenAI use model=<deployment name>

#     resp = client.chat.completions.create(

#         model=AZURE_OPENAI_CHAT_DEPLOYMENT,

#         messages=[{"role": "user", "content": prompt}],

#         max_tokens=4,

#         temperature=0.0

#     )

#     # response content: navigate to the assistant message

#     # The new client returns a structure where choices[0].message.content contains the assistant reply

#     choice = None

#     try:

#         choice = resp.choices[0].message["content"]

#     except Exception:

#         # fallback: try .choices[0].message.content (some versions expose attribute access)

#         choice = getattr(resp.choices[0].message, "content", "")

#     return choice.strip()
 


from dotenv import load_dotenv
import os
from openai import AzureOpenAI  #  Correct import for Azure OpenAI

# Load environment variables
load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

if not (AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_VERSION and AZURE_OPENAI_API_KEY and AZURE_OPENAI_CHAT_DEPLOYMENT):
    raise RuntimeError("Azure OpenAI env vars missing. Please set AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_API_KEY and AZURE_OPENAI_CHAT_DEPLOYMENT")

#  Create Azure OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)

# os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = phoenix_endpoint
# os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = phoenix_endpoint
# os.environ["PHOENIX_API_KEY"] = PHOENIX_API_KEY

def classify_document(document_content):
    text = document_content.get("text", "")
    print("this is my text : ", text)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:", document_content)
#     prompt = f"""
# You are an expert in insurance documentation and intelligent document processing.

# Your task is to identify whether a given document is an ACORD insurance form or not.

# ACORD forms are standardized insurance documents published by the Association for Cooperative Operations Research and Development (ACORD).
# They include forms such as ACORD 25 (Certificate of Liability Insurance), ACORD 27 (Evidence of Property Insurance), ACORD 130 (Workers Compensation Application), etc.

# Classify the following document based on its content.
# Decide whether it is an ACORD Form or Non-ACORD Document.

# Definitions:

# ACORD Form:
# A standardized insurance form that typically includes the word “ACORD” followed by a form number (e.g., “ACORD 25 (2016/03)”),
# fields such as “Producer,” “Insured,” “Certificate Holder,” “Policy Number,” “Authorized Representative,” and often displays the ACORD logo or header.
# These documents summarize insurance coverage, liability, or property details.

# Non-ACORD Document:
# Any document that does not follow the ACORD format — e.g., invoices, contracts, letters, claims, proposals, or policy text.

# Document Content:
# {text[:2000]}

# Reply with only one word: ACORD or Non-ACORD.
# """



#     prompt = f"""
# You are an expert in insurance documentation and intelligent document processing.
# Your task is to classify a given insurance-related document into ONE of the following categories:
# 1. ACORD
# 2. LOSS_RUN
# 3. NON_ACORD
# Definitions:
# ACORD:
# A standardized insurance form published by ACORD (Association for Cooperative Operations Research and Development).
# These documents usually:
# - Contain the word “ACORD” followed by a form number (e.g., ACORD 25, ACORD 27, ACORD 130)
# - Have structured fields such as Producer, Insured, Certificate Holder, Policy Number
# - Often display an ACORD header or logo
# - Are used for applications, certificates, or evidence of insurance
# LOSS_RUN:
# A Loss Run (Loss History) report summarizes historical insurance claims for one or more policies.
# These documents usually:
# - Contain phrases like “Loss Run Report”, “Claims History”, or “Valuation Date”
# - List multiple claims with dates of loss, claim numbers, descriptions, paid amounts, reserves, and total incurred losses
# - Cover a specific historical time period
# - Do NOT contain an ACORD form number or ACORD branding
# NON_ACORD:
# Any insurance-related or non-insurance document that is neither an ACORD form nor a Loss Run report.
# Examples include invoices, proposals, policy wording, endorsements, letters, emails, contracts, or internal reports.
# Document Content:
# {text[:2000]}
# Reply with ONLY ONE word from the following options:
# ACORD
# LOSS_RUN
# NON_ACORD
# """





#WORKING PROMPT - TESTED 
#     prompt = f"""
# You are an expert in insurance documentation and intelligent document processing.
# Your task is to classify a given insurance-related document into EXACTLY ONE of the following categories:
# 1. ACORD
# 2. SOV
# 3. LOSS_RUN
# 4. INSPECTION_REPORT
# 5. NON_ACORD
# Definitions:
# ACORD:
# A standardized insurance form published by ACORD (Association for Cooperative Operations Research and Development),
# used for applications, certificates, or evidence of insurance.
# These documents usually:
# - Have structured fields such as Producer, Insured, Certificate Holder, Policy Number
# - Summarize coverage or serve as an application or certificate
# SOV (Schedule / Statement of Values):
# A document that lists insured property values, usually in a tabular format.
# These documents usually:
# - Contain titles like “Schedule of Values” or “Statement of Values”
# - Include location-wise or building-wise property descriptions and values
# - Have columns such as Location, Building, Description, ACV, RC, 100% Values, Rates
# - May reference or be labeled as ACORD 139
# - Focus on property valuation, not coverage certification
# LOSS_RUN:
# A document that summarizes historical insurance claims.
# These documents usually:
# - Contain phrases like “Loss Run Report”, “Claims History”, or “Valuation Date”
# - List claim numbers, dates of loss, descriptions, paid amounts, reserves, and total incurred losses
# - Cover a historical time period
# - Do NOT function as applications or certificates
# INSPECTION_REPORT:
# A document created after a physical or on-site property inspection for underwriting or risk assessment.
# These documents usually:
# - Contain titles such as “Inspection Report” or similar
# - Include inspection dates, report IDs, broker or inspector details
# - Describe property condition, construction, occupancy, protection, and exposure (COPE)
# - Include sections on building systems, life safety, fire protection, security, utilities, roof, and operations
# - Provide observations, compliance notes, and risk improvement recommendations
# - Focus on current physical condition and risk characteristics of the property
# NON_ACORD:
# Any insurance-related document that is NOT an ACORD form, SOV, Loss Run, or Inspection Report.
# This includes:
# - Quote documents
# - Property detail reports
# - Underwriting summaries
# - Exposure analyses
# - Proposals, narratives, internal reports, or supporting documentation
# - Documents that reference ACORD forms but are not themselves ACORD forms
# Document Content:
# {text[:2000]}
# Reply with ONLY ONE word from the following options:
# ACORD
# SOV
# LOSS_RUN
# INSPECTION_REPORT
# NON_ACORD
# """



    prompt = f"""
You are an expert in insurance documentation and intelligent document processing.

Your task is to classify a given insurance-related document into EXACTLY ONE of the following categories:

1. ACORD
2. SOV
3. LOSS_RUN
4. INSPECTION_REPORT
5. Property_Detailed_Report
6. SUBMISSION_DOCUMENT
7. Submission_Report
8. Valuation_Report

Definitions:

ACORD:
A standardized insurance form published by ACORD (Association for Cooperative Operations Research and Development),
used for applications, certificates, or evidence of insurance.
These documents usually:
- Contain structured ACORD layouts and standardized fields
- Include sections such as Producer, Insured, Certificate Holder, Policy Number
- Serve as official insurance applications, certificates, or evidence forms

SOV (Schedule / Statement of Values):
A document that lists insured property values, primarily for property rating and underwriting.
These documents usually:
- Are titled “Schedule of Values” or “Statement of Values”
- Present location-wise or building-wise values in tabular format
- Include columns such as Location, Building, Description, ACV, RC, 100% Values, Rates
- May be labeled as ACORD 139
- Focus on valuation, not narrative underwriting analysis

LOSS_RUN:
A document that summarizes historical insurance claims experience.
These documents usually:
- Are titled “Loss Run Report” or similar
- Include claim numbers, dates of loss, paid amounts, reserves, and total incurred
- Cover prior policy periods
- Focus on loss history rather than current property condition

INSPECTION_REPORT:
A document created after a physical or on-site property inspection for underwriting or risk evaluation.
These documents usually:
- Are titled “Inspection Report” or similar
- Include inspection dates, report IDs, and inspector or broker details
- Describe observed property condition, construction, occupancy, protection, and exposure (COPE)
- Include sections on life safety, fire protection, security, utilities, roof, and operations
- Provide observations and risk improvement recommendations
- Focus on observed conditions at the time of inspection
A document that provides detailed descriptive information about the physical condition,
components, and systems of a property or building.
These documents usually:
- Organize information by building systems or structural components
 such as roof, exterior, structure, interior, plumbing, electrical,
 heating/cooling, ventilation, foundations, or site features
- Describe observed conditions, deterioration, damage, risks, or maintenance needs
- Provide commentary or explanations about property elements and how they function
- Include technical or informational descriptions of building materials,
 construction elements, or safety considerations
- Focus on documenting or explaining the condition and characteristics
 of a property and its building systems
These documents are informational assessments of property condition
rather than insurance forms, valuation schedules, claim histories,
or underwriting submission packages.


Property_Detailed_Report:
Any insurance-related document that is NOT an ACORD form, SOV, Loss Run, or Inspection Report.
This includes:
- Quote documents
- Property detail reports
- Underwriting summaries
- Exposure analyses
- Proposals, narratives, internal reports, or supporting documentation
- Documents that reference ACORD forms but are not themselves ACORD forms


SUBMISSION_DOCUMENT:
A structured underwriting document used in the Commercial Propoerty (LOB).
A document assembled to formally present a risk to an insurer for underwriting, quotation, or binding.
These documents usually:
- Are explicitly titled or framed as “Underwriting Submission” or similar
- Include broker details, producer codes, underwriting company information
- Present requested terms, program structure, limits, valuation, and effective dates
- Summarize the property, coverage intent, and underwriting rationale
- May reference or attach other documents such as SOVs, Loss Runs, Inspection Reports, or Property Detailed Reports
- Function as a submission package rather than a standalone property analysis


Submission_Report:
A structured underwriting report used in the Home Insurance line of business (LOB)
to present a residential property and its associated risk information to an insurer
for underwriting evaluation.
These documents are specifically prepared for Home Insurance underwriting and usually:
- Provide details about the homeowner or policyholder and the residential property
 being considered for insurance
- Describe property characteristics such as year built, construction type,
 roof material, cladding, foundation, storeys, floor area, and renovations
- Include insurance-related information relevant to Home Insurance such as
 rebuild sum insured, occupancy type, property usage, and coverage considerations
- Present risk information relevant to residential property underwriting including
 hazards such as earthquake, flood, coastal exposure, or land slip
- Describe security features, maintenance condition, or structural upgrades
 affecting Home Insurance risk evaluation
- May summarize claims history related to the residential property
- Often reference supporting documents such as inspection reports,
 engineering reports, weathertightness reports, rebuild estimates,
 LIM reports, photographs, or maintenance records
- Are intended to assist insurers in assessing and underwriting
 residential properties under Home Insurance policies
If the document presents residential property information for underwriting
evaluation in the Home Insurance LOB, it should be classified as Submission_Report.


Valuation_Report:
A professional report prepared to determine the insurance value of a property
or asset for insurance coverage purposes.
These documents are typically used in home insurance underwriting
to establish the appropriate insured value of buildings or assets.
These documents usually:
- Provide valuation estimates related to insurance coverage such as
 reinstatement cost, replacement cost, indemnity value, or functional replacement value
- Include valuation calculations or summaries used to determine the amount
 required to rebuild or replace the insured property
- Contain information about the property such as construction type,
 age, asset description, land characteristics, or building specifications
- Include provisions such as inflation allowances, demolition estimates,
 depreciation, or cost adjustments
- Are prepared by professional valuers, quantity surveyors, or valuation firms
- May include valuation dates, valuation methodology, or professional declarations
- Are specifically intended to establish insured values for insurance purposes
 rather than documenting inspection findings or underwriting submissions


Document Content:
{text[:2000]}

IMPORTANT OUTPUT RULES:
- You MUST reply with EXACTLY ONE value.
- The value MUST MATCH one of the following ENUMS EXACTLY (character-for-character).
- Do NOT shorten, modify, or partially return any label.
- If the document matches “Property Detailed Report”, you MUST return:
 "PROPERTY_DETAILED_REPORT" ONLY, so you should not miss REPORT word
Allowed outputs (EXACT ENUMS):
ACORD
SOV
LOSS_RUN
INSPECTION_REPORT
Property_Detailed_Report
Submission_Document
Submission_Report
Valuation_Report
Return ONLY the enum value. Do not add text, punctuation, or explanation.

"""



#     prompt = f"""
# You are an expert in insurance documentation and intelligent document processing.
# Your task is to classify a given insurance-related document into EXACTLY ONE of the following categories:
# 1. ACORD
# 2. SOV
# 3. LOSS_RUN
# 4. NON_ACORD
# Definitions:
# ACORD:
# A standardized insurance form published by ACORD (Association for Cooperative Operations Research and Development),
# used for applications, certificates, or evidence of insurance.
# These documents usually:
# - Contain “ACORD” followed by a form number (e.g., ACORD 25, ACORD 27, ACORD 125, ACORD 130)
# - Have structured fields such as Producer, Insured, Certificate Holder, Policy Number
# - Summarize coverage or serve as an application or certificate
# SOV (Schedule / Statement of Values):
# A document that lists insured property values, usually in a tabular format.
# These documents usually:
# - Contain titles like “Schedule of Values” or “Statement of Values”
# - Include location-wise or building-wise property descriptions and values
# - Have columns such as Location, Building, Description, ACV, RC, 100% Values, Rates
# - May reference or be labeled as ACORD 139
# - Focus on property valuation, not coverage certification
# LOSS_RUN:
# A document that summarizes historical insurance claims.
# These documents usually:
# - Contain phrases like “Loss Run Report”, “Claims History”, or “Valuation Date”
# - List claim numbers, dates of loss, descriptions, paid amounts, reserves, and total incurred losses
# - Cover a historical time period
# - Do NOT function as applications or certificates
# NON_ACORD:
# Any insurance-related document that is NOT an ACORD form, SOV, Loss Run, or Inspection Report.
# This includes:
# - Quote documents
# - Property detail reports
# - Underwriting summaries
# - Exposure analyses
# - Proposals, narratives, internal reports, or supporting documentation
# - Documents that reference ACORD forms but are not themselves ACORD forms
# Document Content:
# {text[:2000]}
# Reply with ONLY ONE word from the following options:
# ACORD
# SOV
# LOSS_RUN
# NON_ACORD
# """



    response = client.chat.completions.create(
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4,
        temperature=0.0
    )

    try:
        return response.choices[0].message.content.strip()
    except Exception:
        return getattr(response.choices[0].message, "content", "").strip()
