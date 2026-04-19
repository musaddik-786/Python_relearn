



#Working code 

# test_scripts.py
import requests
import json

BASE_URL = "http://localhost:8667/api/v1/layout/layout_detection_mcp"

def run_test():
    payload = {
        #   "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/19BDB64178C5A9C8_attachment_Acord_125_High_tech_solution.pdf" , #Acord detected
        #   "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/19BDB4364822FBA8_attachment_Acord_125_Nexora_Systems.pdf"  #Acord detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/123DSAFAS_attachment_Loss_Run_Nexora.pdf"    #LOSSRUN detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/123DSAFAS_attachment_SOV - Nexora.pdf"   #SOV detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/1231312JBASF_attachment_Loss Run Sample 1.pdf"  #LOSSRUN detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/1231312JBASF_attachment_Loss Run Sample 2.pdf"  #LOSSRUN detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/1231312JBASF_attachment_Loss Run Sample 3.pdf"  #LOSSRUN detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/1231312JBASF_attachment_Loss Run Sample 3.pdf"    # #LOSSRUN detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/123213FSDFSDF_attachment_Request_for_Quote_Property_Detailed_Report.pdf"  #NONACORD detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/2131ASFASF_attachment_Acord_125_High_tech_solution.pdf" #ACORD DETECTED
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/2131ASFASF_attachment_Loss_Run_HighTech_Solution.pdf"   #LOSSRUN DETECTED
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/2131ASFASF_attachment_SOV.pdf" #SOV DETECTED
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/21312ASFDS_attachment_Acord_125_Greengen.pdf" #ACORD DETECTED
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/21312ASFDS_attachment_Loss_Run_GreenGen.pdf"  #lossrun detected
        # "attachment_url": "https://agenticai1.blob.core.windows.net/attachment-downloader/21312ASFDS_attachment_SOV.pdf"  #SOV Detected
        # "attachment_url" :"https://agenticai1.blob.core.windows.net/email-processed/Loss%20Run%20Sample%201%20NonTemp.pdf" #LOSSRUN DETECTED
        # "attachment_url" :"https://agenticai1.blob.core.windows.net/email-processed/Loss%20Run%20Sample%202%20NonTemp.pdf"  #LOSSRUNDETECTED
        # "attachment_url" :"https://agenticai1.blob.core.windows.net/email-processed/Loss%20Run%20Sample%203%20NonTemp.pdf"    #LOSSRUNDETECTED
        # "attachment_url" :"https://agenticai1.blob.core.windows.net/attachment-downloader/19BE070253C20666_attachment_SOV_Nexora_Systems_form.pdf" #SOVDETECTED
        # "attachment_url" :"https://agenticai1.blob.core.windows.net/attachment-downloader/123ASFJKANSF_attachment_Property%20Inspection%20Report%20-%20Nexora%20Systems%20-%20Jan%202026%201.pdf"  #SOVDETECTED
        # "attachment_url" :"https://agenticai1.blob.core.windows.net/attachment-downloader/123ASFJKANSF_attachment_Property%20Inspection%20Report%20GreenGen%20Realty%20-%20Jan%202026%201.pdf"     #SOVDETECTED
        # "attachment_url" :"https://agenticai1.blob.core.windows.net/attachment-downloader/123ASFJKANSF_attachment_Property%20Inspection%20Report%20HighTech%20Solutions%20-%20Jan%202026%201.pdf"    #SOVDETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/19BE070253C20666_attachment_Loss_Run_Nexora.pdf"    #LOSSRUN DETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/19BE070253C20666_attachment_SOV_Nexora_Systems_form.pdf"    #SOV DETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/213123SDFJKH_attachment_Loss Run Sample 1 NonTemp.pdf"        #LOSSRUN DETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/123ASDASF_attachment_Acord_139_Filled_V4%201.pdf"            #SOV DETECTED as it is ACORD 139
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/123DSAFAS_attachment_Loss_Run_Nexora.pdf"    #LOSSRUN DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/attachment-downloader/123DSAFAS_attachment_SOV%20-%20Nexora.pdf"   #----ACORD--which is wrong, after removing usually contains name acord form the prompt of ACORD now it is giving SOV
    
    
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123ASDASF_attachment_Acord_139_Filled_V4%201.pdf" #SOV DETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123DSAFAS_attachment_Loss_Run_Nexora.pdf"   #LOSS RUN DETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123DSAFAS_attachment_SOV - Nexora.pdf"        #SOV DETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/2131ASFASF_attachment_Acord_125_High_tech_solution.pdf"  #ACORD DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/2131ASFASF_attachment_Loss_Run_HighTech_Solution.pdf"    #LOSS RUN DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/2131ASFASF_attachment_SOV.pdf"  #SOV DETECTED
        # "attachment_url"  :   "https://agenticai1.blob.core.windows.net/quote-extraction-results/21312ASFDS_attachment_Acord_125_Greengen.pdf"   #ACORD DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/21312ASFDS_attachment_Loss_Run_GreenGen.pdf"   #LOSSRUN DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/21312ASFDS_attachment_SOV.pdf"   #SOV DETECTED
        # "attachment_url" :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/123213FSDFSDF_attachment_Request_for_Quote_Property_Detailed_Report.pdf"  #Property_Detailed_Report DETECTED
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/Loss Run Sample 1 NonTemp.pdf"  #LOSSRUN DETECTED
        # "attachment_url" :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/Loss Run Sample 1.pdf"  #LOSSRUN DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/Loss Run Sample 2 NonTemp.pdf"  ##LOSSRUN DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/Loss Run Sample 2.pdf"  #LOSSRUNDETECTED
        # "attachment_url"   :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/Loss Run Sample 3 NonTemp.pdf"  #LOSSRUNDETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/Loss Run Sample 3.pdf"   #LOSSRUNDETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/19BE070253C20666_attachment_Loss_Run_Nexora.pdf"   #LOSSRUNDETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/19BE070253C20666_attachment_SOV_Nexora_Systems_form.pdf"  #SOV DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/123ASFJKANSF_attachment_Property Inspection Report - Nexora Systems - Jan 2026 1.pdf"   #INSPECTION REPORT DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/123ASFJKANSF_attachment_Property Inspection Report GreenGen Realty - Jan 2026 1.pdf"  #INSPECTION REPORT DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/123ASFJKANSF_attachment_Property Inspection Report HighTech Solutions - Jan 2026 1.pdf"  #INSPECTION REPORT DETECTED
        # "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/213123SDFJKH_attachment_Loss Run Sample 1 NonTemp.pdf"      #LOSSRUNDETECTED
        # "attachment_url" :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/12312ASDJKB_attachment_Acord_140_Filled 2.pdf"  #ACORD DETECTED
    
    
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/12312213_attachment_ManufacturingFacility_SubmissionDocument.pdf"
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/12312213_attachment_SunflowerHotels_SubmissionDocument.pdf"
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/12312322_attachment_ManufacturingFacility_SubmissionDocument.pdf"
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/12312322_attachment_SunflowerHotels_Submission_Document_For_GW.pdf"
        "attachment_url"  :  "https://agenticai1.blob.core.windows.net/quote-extraction-results/123213FSDFSDF_attachment_Request_for_Property_Detailed_Report.pdf"

        # TESTING BY CHANGING NAME

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/12312322_attachment_ManufacturingFacility_ACORD.pdf"  #"Detected Submission_Document"
    
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/19BE070253C20666_attachment_SUBMISSION_DOCUMENT_Nexora_Systems_form.pdf"  #"SOV Detected"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123213FSDFSDF_attachment_Request_for_NONACORD.pdf" #Property_Detailed_Report

        #  "attachment_url": "https://agenticai1.blob.core.windows.net/quote-extraction-results/21312ASFDS_attachment_Greengen.pdf" #"ACORD DETECTED"

        #  "attachment_url":"https://agenticai1.blob.core.windows.net/quote-extraction-results/342SRDFS_attachment_Sample%20report%20-%20Inspected%20Residential%20NZ.pdf" #Sample_Report_Detected

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/3123SADASD_attachment_Tower%20Insurance%20-%20Home%20Submission%20Report.pdf"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/12321ASD_attachment_NZ%20Home%20Valuation%20Report.pdf"
 
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123123_attachment_NZ%20Home%20Valuation%20Report.docx"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123123_attachment_NZ%20Home%20Valuation%20Report_text.docx"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/231312_attachment_Hi%20I%20am%20unknwon%20developer%20from%20jarvis.docx"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123ASDASD_attachment_PDR.pdf"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/12312asf_attachment_SunflowerHotels.pdf"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/123123_attachment_NZ_Home_Valuation_Report.docx"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/3123SADASD_attachment_Tower_Insurance_-_Home_Submission_Report.pdf"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/19CDC8AB7BCC5E85_attachment_Tower_Insurance_-_Home_Submission_Report.pdf"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/quote-extraction-results/342SRDFS_attachment_Sample_report_-_Inspected_Residential_NZ.pdf"

        # "attachment_url": "https://agenticai1.blob.core.windows.net/quote-extraction-results/1231231_attachment_NZ_Home_Valuation_Report_edited.pdf"

        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/19CDC8AB7BCC5E85_attachment_SunflowerHotels_Submission_Document.pdf"
#     2. SOV
# 3. LOSS_RUN
# 4. INSPECTION_REPORT
# 5. Property_Detailed_Report
# 6. SUBMISSION_DOCUMENT
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/19C991EF83AE7D23_attachment_apex_submission_v2.pdf"
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/19CDC2E1EAD65B9A_attachment_crestview_submission.pdf"
        # "attachment_url" : "https://agenticai1.blob.core.windows.net/attachment-downloader/19CBDAC6A5B085AD_attachment_meridian_submission.pdf"
    }


    try:
        resp = requests.post(BASE_URL, json=payload, timeout=180)
        print("HTTP Status:", resp.status_code)
        try:
            data = resp.json()
            print(json.dumps(data, indent=4))
        except Exception:
            print("Response not JSON:", resp.text)
    except Exception as e:
        print("Error calling API:", str(e))

if __name__ == "__main__":
    print("Testing /layout_detection_mcp ...")
    run_test()