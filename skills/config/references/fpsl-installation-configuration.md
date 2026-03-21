Classification: official-source-derived
Source basis: FPSL_ADMINGUIDE_EN.pdf, pages 23-40
Trust usage: installation sequence, pre-install checks, post-install tasks, business content
Do not use for: specific landscape details without adaptation
Topics covered: installation, client setup, business content, BC sets, configuration sequence, pre-checks

# Installation, Setup, and Client Configuration
3.3.1 Communication Destinations

This section shows an overview of the communication destinations used by SAP S/4HANA for financial
products subledger.


 Destination                    Delivered                      Type          User, Authorizations     Description


 FPSL system                    No                             RFC           Dialog User with         The usage is optional.
                                                                             authorizations for
                                                                             RDL-Result Viewer        The destination is used
                                                                             (F_BAHW_RES) or          for the drill-through
                                                                             Source Data (con-        from the FI-GL docu-
                                                                             tracts F_BAF1_AUG,
                                                                                                      ment back to the FPSL
                                                                             business transactions
                                                                                                      subledger documents
                                                                             F_BAF2_BTC), Ac-
                                                                             counting Authoriza-      in the RDL Results
                                                                             tions F_BABR_BAS         Viewer.
                                                                             and the GL connector
                                                                             F_BABR_GLC

 FI-GL system                   No                             SOAP          Technical System         The usage is optional.
                                                                             user, business author-
                                                                             izations required for    The destination is used
                                                                             creating ledger docu-    for sending prepared
                                                                             ments in FI-GL.          general ledger docu-
                                                                                                      ments from the FS-
                                                                                                      FPS system to the
                                                                                                      FI-GL system. Serv-
                                                                                                      ice Consumer is Finan-
                                                                                                      cialInstrumentsAnaly-
                                                                                                      ticalAccountingDocu-
                                                                                                      mentPreparationAc-
                                                                                                      countingDocumentNo-
                                                                                                      tificationOut,
                                                                                                      (SWC S4FPSL,
                                                                                                      http://sap.com/xi/BA/
                                                                                                      Global ), service pro-
                                                                                                      vider is Accounting-
                                                                                                      DocumentERPBulkNo-
                                                                                                      tification_In (SWC
                                                                                                      S4CORE, http://
                                                                                                      sap.com/xi/APPL/SE/
                                                                                                      Global)




3.4           Internet Communication Framework Security

This section describes how SAP S/4HANA for financial products subledger uses Internet Communication
Framework (ICF) services.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                            PUBLIC        23

Only activate services that are needed for the applications running in your system.

For the Workplace for Financial Accountants and Actuaries, the following ICF services are required:

•     /default_host/sap/bc/ui5_ui5/ba1/acd
•     /default_host/sap/bc/ui5_ui5/ba1/cil
•     /default_host/sap/opu/odata/sap/fps_assg_chg_drvrs_srv
•     /default_host/sap/opu/odata/sap/fps_chg_ins_liab_srv

Use transaction SICF to activate these services.

If your firewall(s) use URL filtering, also note the URLs used for the services and adjust your firewall settings
accordingly.

For more information, see the user assistance for SAP NetWeaver. To find the relevant documents, go to SAP
Help Portal at https://help.sap.com/nw and open the product page for your SAP NetWeaver release. Search for
"activating and deactivating ICF services" and "ICF security".




3.5          Data Protection and Privacy
This section provides information about how SAP S/4HANA for financial products subledger complies with
data protection requirements.

You can find an overview of the system landscape and the architecture components in section System
Architecture for SAP S/4HANA for Financial Products Subledger [page 7].




3.5.1 Introduction

Data protection is associated with numerous legal requirements and privacy concerns. In addition to
compliance with general data protection and privacy acts, it is necessary to consider compliance with industry-
specific legislation in different countries. SAP provides specific features and functions to support compliance
with regard to relevant legal requirements, including data protection, which are documented in these templates
along with the assumptions that have been guiding the implementation in the software. By nature of legal
requirements the conclusion whether these features are covering customer specific demands as well as the
conclusion whether additional measures have to be taken is solely with the customer.

      Note

     SAP does not provide legal advice in any form. SAP software supports data protection compliance by
     providing security features and specific data protection-relevant functions, such as simplified blocking and
     deletion of personal data. In many cases, compliance with applicable data protection and privacy laws will
     not be covered by a product feature. Definitions and other terms used in this document are not taken from
     a particular legal source.


      Caution

     The extent to which data protection is supported by technical means depends on secure system operation.
     Network security, security note implementation, adequate logging of system changes, and appropriate



                                                             Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
24       PUBLIC                                              Security Information for SAP S/4HANA for Financial Products Subledger

usage of the system are the basic technical requirements for compliance with data privacy legislation and
   other legislation.




Generic Fields

You need to make sure that no personal data enters the system in an uncontrolled or non-purpose related way,
for example, in free-text fields, through APIs, or customer extensions. Note that these are not subject to the
read access logging (RAL) example configuration.

    Note

   Take into account that the Application Log may contain personal data in an unstructured way, i.e. in the
   message fields. The protocol may contain the Bank Account Number (or Contract ID respectively) or the
   Business Partner ID, for example.

   The application log is accessible for example via the CVPM monitor or transaction SLG1. In addition, test
   runs of CVPM processes display protocols and detail logs instantly.




3.5.2 Glossary


 Term                                                                        Definition


 Artificial Intelligence (AI)                                                The simulation of human intelligence processes by machines
                                                                             and computer systems – typically by learning, coming to its
                                                                             own conclusions, appearing to understand complex content,
                                                                             engaging in natural dialogs with people, enhancing human
                                                                             cognitive performance (also known as cognitive computing)
                                                                             or replacing people on execution of nonroutine tasks. Appli-
                                                                             cations include autonomous vehicles, automatic speech rec-
                                                                             ognition and generation and detecting novel concepts and
                                                                             abstractions (useful for detecting potential new risks and
                                                                             aiding humans to quickly understand very large bodies of
                                                                             ever-changing information)

 Automated Decision Making                                                   The ability to make decisions by technological means with-
                                                                             out human involvement.

 Blocking                                                                    A method of restricting access to data for which the primary
                                                                             business purpose has ended.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                        PUBLIC         25

Term                         Definition


Business Purpose             The legal, contractual, or in other form justified reason for
                             the processing of personal data to complete an end-to-end
                             business process. The personal data used to complete the
                             process is predefined in a purpose, which is defined by the
                             data controller. The process must be defined before the per-
                             sonal data required to fulfill the purpose can be determined.

Consent                      The action of the data subject confirming that the usage
                             of his or her personal data shall be allowed for a given pur-
                             pose. A consent functionality allows the storage of a consent
                             record in relation to a specific purpose and shows if a data
                             subject has granted, withdrawn, or denied consent.

Data Subject                 Any information relating to an identified or identifiable natu-
                             ral person ("data subject"). An identifiable natural person is
                             one who can be identified, directly or indirectly, in particular
                             by reference to an identifier such as a name, an identifica-
                             tion number, location data, an online identifier, or to one or
                             more factors specific to the physical, physiological, genetic,
                             mental, economic, cultural, or social identity of that natural
                             person.

Deletion                     Deletion of personal data so that the data is no longer avail-
                             able.

End of Business              Defines the end of active business and the start of residence
                             time and retention period.

End of Purpose (EoP)         The point in time when the processing of a set of personal
                             data is no longer required for the primary business purpose,
                             for example, when a contract is fulfilled. After the EoP has
                             been reached, the data is blocked and can only be accessed
                             by users with special authorizations (for example, tax audi-
                             tors).

End of Purpose (EoP) check   A method of identifying the point in time for a data set when
                             the processing of personal data is no longer required for the
                             primary business purpose. After the EoP has been reached,
                             the data is blocked and can only be accessed by users with
                             special authorization, for example, tax auditors.

Personal data                Any information relating to an identified or identifiable natu-
                             ral person ("data subject"). An identifiable natural person is
                             one who can be identified, directly or indirectly, in particular
                             by reference to an identifier such as a name, an identifica-
                             tion number, location data, an online identifier, or to one or
                             more factors specific to the physical, physiological, genetic,
                             mental, economic, cultural, or social identity of that natural
                             person.




                               Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
26     PUBLIC                  Security Information for SAP S/4HANA for Financial Products Subledger

Term                                                                        Definition

 Processing of Personal Data                                                 Processing means any operation or set of operations which
                                                                             is performed on personal data or on sets of personal data,
                                                                             whether or not by automated means, such as collection, re-
                                                                             cording, organisation, structuring, storage, adaptation or al-
                                                                             teration, retrieval, consultation, use, disclosure by transmis-
                                                                             sion, dissemination or otherwise making available, alignment
                                                                             or combination, restriction, erasure or destruction.

 Purpose                                                                     The information that specifies the reason and the goal for
                                                                             the processing of a specific set of personal data. As a rule,
                                                                             the purpose references the relevant legal basis for the proc-
                                                                             essing of personal data.

 Residence period                                                            The period of time between the end of business and the
                                                                             end of purpose (EoP) for a data set during which the data
                                                                             remains in the database and can be used in case of sub-
                                                                             sequent processes related to the original purpose. At the
                                                                             end of the longest configured residence period, the data is
                                                                             blocked or deleted. The residence period is part of the over-
                                                                             all retention period.

 Retention period                                                            The period of time between the end of the last business
                                                                             activity involving a specific object (for example, a business
                                                                             partner) and the deletion of the corresponding data, subject
                                                                             to applicable laws. The retention period is a combination of
                                                                             the residence period and the blocking period.

 Sensitive personal data                                                     A category of personal data that usually includes the follow-
                                                                             ing type of information:

                                                                             •   Special categories of personal data, such as data reveal-
                                                                                 ing racial or ethnic origin, political opinions, religious or
                                                                                 philosophical beliefs, trade union membership, genetic
                                                                                 data, biometric data, data concerning health or sex life
                                                                                 or sexual orientation.
                                                                             •   Personal data subject to professional secrecy
                                                                             •   Personal data relating to criminal or administrative of-
                                                                                 fenses
                                                                             •   Personal data concerning insurances and bank or credit
                                                                                 card accounts




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                            PUBLIC          27

Term                                                     Definition


Technical and organizational measures (TOM)              Some basic requirements that support data protection and
                                                         privacy are often referred to as technical and organizational
                                                         measures (TOM). The following topics are related to data
                                                         protection and privacy and require appropriate TOMs, for
                                                         example:

                                                          •     Access control: Authentication features
                                                          •     Authorizations: Authorization concept
                                                          •     Read access logging
                                                          •     Transmission control / Communication security
                                                          •     Input control / Change logging
                                                          •     Availability control
                                                          •     Separation by purpose: Is subject to the organizational
                                                                model implemented and must be applied as part of the
                                                                authorization concept.




3.5.3 Consent

SAP S/4HANA for financial products subledger or SAP S/4HANA, financial posting gateway does not
provide functionality that allows data subjects to give and withdraw consent to collect and process their
personal data. SAP assumes that the user (for example, an SAP customer collecting data) has consent from
its data subject (a natural person such as a customer, contact, or account) to collect or transfer data to the
solution.

      Note

     SAP S/4HANA for financial products subledger supports you in the context of fulfilling regulatory
     requirements and multi-dimensional management analysis and reporting.




3.5.4 Read Access Logging

Read Access Logging is considered as an additional safeguard in the protection of personal data, because
it helps to identify potential illegitimate access to personal data. Read access to sensitive personal data is
partially based on legislation, and it is subject to logging functionality. Read access logging (RAL) is used to
monitor and log read access to sensitive personal data that was disclosed via user interface, which can be
extended to read access to other personal data. Data may be categorized as sensitive by law, by external
company policy, or by internal company policy. When these read accesses are logged, you should be able
check which user accessed personal data on which access channel and the date and time, depending on
the configuration. Read access logging enables you to answer questions about who accessed particular data
within a specified time frame. That logging also includes downloading attachments or files, logs for such events
shall contain information to identify the attachment. Additionally, as for Read Access Logging across system



                                                              Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
28       PUBLIC                                               Security Information for SAP S/4HANA for Financial Products Subledger

boundaries, the respective “access” shall be logged as soon as sensitive personal data crosses the boundary
from a trusted to an un-trusted area. Here are some examples of such questions:

 •    Who accessed the data of a given business entity, for example a bank account?
 •    Who accessed personal data, for example of a business partner?
 •    Which employee accessed personal information, for example religion?
 •    Which accounts or business partners were accessed by which users?

Furthermore, log records can be viewed and queried, but access to them is restricted by adequate
authorizations. The personal data for which read access shall be logged and the retention period of logs,
can be configured.

Read access logging is currently available in, but not limited to the following channels:

 •    Remote Function Calls (sRFC, aRFC, tRFC, qRFC, bgFRC)
 •    Dynpro
 •    Web Dynpro
 •    Web services
 •    Gateway (for OData)

The template below shows how these fields are logged and may be combined with additional fields in the
following business contexts.

 •    BW channel (for analytical queries of the Virtual Data Model)


 Configuration                                       Fields Logged           Business Context


 FPS_ASSG_CHG_DRVRS_SRV                              Contract ID             Assignment of contracts to change rea-
                                                                             sons in the Workplace for Financial Ac-
                                                                             countants and Actuaries

 FPSL_RDLVW_ALV                                      Contract ID             Result Data - Result Viewer


 BA_BT_DISPLAY                                       Contract ID             Display of business transactions

                                                     Business Partner ID

 BA_FT_DISPLAY                                       Contract ID             Display of financial transaction / finan-
                                                                             cial contract




Read Access Logging for Business Partner

Financial Products Subledger (software component S4FPSL) is an add-on that is installed on an SAP S/4HANA
instance. There are two different business objects available for the business partner in this type of installation:

 •    Recommended: SAP Business Partner, maintained in transaction BP
 •    Analytical Business Partner (aBP), maintained in transactions BPV1 (Create), BPV2 (Change), BPV3
      (Display)

      Recommendation

     We strongly recommend that you use SAP Business Partner.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                      PUBLIC    29

For more information about SAP Business Partner, see SAP Business Partner.

If you are still using the analytical business partner, read access logging is supported in the service channel for
the Financial Services Business Partner as of NetWeaver release SAP_ABA 7.40. The following LOG domains
are available in transaction SRALMANAGER:

Domain                                                      Description

FS_BP_INTERNAL_ID                                           Business Partner Number

FS_BP_UUID                                                  Business Partner GUID

FS_BP_IDENTIFICATION_ID                                     Business Partner Identification Number

FS_BP_IDENTIFICATION_TYPE_CODE                              Business Partner Identification Type


Sample configurations are available for the following service operations:

•     Retrieve Business Partner
•     Update Business Partner
•     Inform Business Partner




3.5.5 Information Retrieval

Data subjects have the right to receive information regarding their personal data that is being processed. The
information retrieval feature supports you in complying with the relevant legal requirements for data protection
by allowing you to search for and retrieve all personal data for a specified data subject. The search results
are displayed in a comprehensive and structured list containing all personal data of the data subject specified,
organized according to the purpose for which the data was collected and processed.

For information on reporting, the Information Retrieval Framework can be used. The guide mentioned under
More Information explains how you create a purpose, which enables the data retrieval process, and how you
display the consolidated data of the business partner.

      Note

     The entry point for the Information Retrieval report is the Business Partner ID of the central Business
     Partner.


You can retrieve the information by using the following ILM objects when you create a purpose:

•     BA1_F1_040 (Financial Products Subledger: Archiving of Contract Data)
•     BA1_F1_041 (Financial Products Subledger: Archiving of Securities)
•     BA1_F1_043 (Financial Products Subledger: Archiving of Securities Accounts)
•     BA1_F2_035 (Financial Products Subledger: Business Transaction)

Results data area (RDL) and result type do not have their own fixed ILM objects (the respective ILM objects are
generated and cannot be used here directly). Therefore, the RDL tables must be added to the IRF models.




                                                              Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
30       PUBLIC                                               Security Information for SAP S/4HANA for Financial Products Subledger

More Information

For information on how to configure and use the IRF models, see SAP Note 2725637                  , which contains the
guide IRF Data Model Configuration for Financial Products Subledger ILM Objects.

SAP Note 2725511              - IRF Tool: Data collection displays field value instead of text for some characteristics and
key figures

SAP Note 2725637               - IRF for ILM Objects in Financial Products Subledger

For information on the information retrieval framework, see Information Retrieval Framework (IRF)

For more information about data archiving and data deletion in Financial Products Subledger, see Data
Archiving and Data Destruction.




3.5.6 Deletion of Personal Data




Simplified Blocking and Deletion

The processing of personal data is subject to applicable laws related to the deletion of this data when the
specified, explicit, and legitimate purpose for processing this personal data has expired. If there is no longer
a legitimate purpose, that requires the retention and use of personal data, it must be deleted irrecoverably.
Blocking is necessary when the original retention period has expired but additional applicable extended and
overruling (mandated by law) retention periods are still in place. After the expiration of the longest retention
period, the data must be deleted.




Deletion of Personal Data

When considering compliance with data protection regulations, it is also necessary to consider compliance
with industry-specific legislation in different countries. A typical potential scenario in certain countries is
that personal data shall be deleted after the specified, explicit, and legitimate purpose for the processing
of personal data has ended, but only if no other retention periods are defined in legislation, for example,
retention periods for financial documents. Legal requirements in certain scenarios or countries also often
require blocking of data in cases where the specified, explicit, and legitimate purposes for the processing of
this data have ended, however, the data still has to be retained in the database due to other legally mandated
retention periods. Sometimes, transactional data are personal data with relation to a master data object, e.g.
a sales order with reference to a business partner. Therefore, the challenge for deletion and blocking is first to
handle transactional data and finally other data, such as business partner data.

This SAP product might process data (personal data) that is subject to the data protection laws applicable in
specific countries as described in SAP Note 1825544 .



Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                          PUBLIC     31

Deletion
To enable even complex scenarios, SAP simplifies existing deletion functionalities to cover data objects that
are personal data by default. For this purpose, SAP uses SAP Information Lifecycle Management (ILM) to
help you set up a compliant information lifecycle management process in an efficient and flexible manner.
The functions that support the simplified blocking and deletion of personal data are not delivered in one large
implementation, but in several waves. Scenarios or products that are not specified in SAP Note 1825608
(central Business Partner) and SAP Note 2007926          (ERP Customer and Vendor) are not yet subject to
simplified blocking and deletion. Nevertheless, it is also possible to destroy personal data for these scenarios or
products. In these cases, you have to use an existing archival or deletion functionality or implement individual
retention management of relevant business data throughout its entire lifecycle. The ILM component supports
the entire software lifecycle including storage, retention, blocking, and deletion of data.

This SAP product uses SAP ILM to support the deletion of personal data as described in the following sections:

End-of-Purpose Check
An end of purpose (EoP) check determines whether data is still relevant for business activities based on the
retention period defined for the data. The retention period is part of the overall lifecycle of personal data which
consists of the following phases:

•    Business activity: The relevant data is used in ongoing business, for example contract creation, delivery or
     payment.
•    Residence period: The relevant data remains in the database and can be used in case of subsequent
     processes related to the original purpose, for example reporting obligations.
•    Blocking period: The relevant data needs to be retained for legal reasons. During the blocking period,
     business users of SAP applications are prevented from displaying and using this data; it can only be
     processed in case of mandatory legal provisions.
•    Deletion: The data is deleted and no longer exists in the database.




For Business Partner, the following EoP report is available: BUPA_PREPARE_EOP.

To check whether a business partner is still used in contracts or portfolios, you need to make the following
settings:

In the Customizing activity Register Application Function Modules for EoP Check, you need to ensure that
there is an entry for function module /BA1/DP_BP_EOP_CHECK with the application name FPSL. The function
module checks for the validity period of a business partner in its contracts or portfolios.



                                                             Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
32     PUBLIC                                                Security Information for SAP S/4HANA for Financial Products Subledger

If a valid-to date has been defined, the system adds 365 days to this date to get the end of business date. The
business partner can only be blocked and deleted when this end of business date is reached. If the validity
period is not limited (valid-to date = 9999-12-31), the business partner is still used.


Blocking

Blocking of data can impact system behavior in the following ways:

 •   Display: The system does not display blocked data.
 •   Change: It is not possible to change a business object that contains blocked data.
 •   Create: It is not possible to create a business object that contains blocked data
 •   Copy/Follow-Up: It is not possible to copy a business object or perform follow-up activities for a business
     object that contains blocked data.
 •   Search: It is not possible to search for blocked data or to search for a business object using blocked data in
     the search criteria.

It is possible to display blocked data if a user has special authorization; however, it is still not possible to create,
change, copy, or perform follow-up activities on blocked data.

Data blocking is handled in the following ways:

 •   ILM-enabled archiving: Archiving blocks the processing of data completely as soon as the data is removed
     from the application tables.
     You can configure the system so that it supports read access from the application to the archive. We do not
     recommend this because it can slow down runtime performance. If you choose to use this feature, make
     sure that it is compliant with your data protection and privacy regulations.
 •   Masking: This is mainly a UI function (for example, SAP GUI or ALV) that does not prevent data from being
     used in mass data processing (for example, in CVPM processes) that then leads to information production
     (for example, the creation of subledger journal entries in the results data).




Configuration: Simplified Blocking and Deletion for Business Partner


You configure the settings for blocking and deleting business partner master data in Customizing for Cross-
Application Components under Data Protection.

 •   Make the settings for authorization management under                     Data Protection     Authorization Management .
 •   Make the settings for blocking data in Customizing for Cross-Application Components under                      Data
     Protection        Blocking and Unblocking                Business Partner .




More Information


For more information about data archiving and deletion, see SAP Help Portal at https://help.sap.com/
S4FPSL. Access the Application Help under Product Assistance and choose                         Infrastructure (FS-FPS-IF)
  Data Archiving and Deletion in Financial Products Subledger .



Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                               PUBLIC   33

For more information about blocking and deleting personal data, see SAP Help Portal at https://help.sap.com/
S4FPSL. Access the Application Help under Product Assistance and choose                Basic Settings          Blocking and
Deletion of Personal Data in Financial Products Subledger .




3.5.7 Change Log

Creation and change of personal data need to be documented. Therefore, for review purposes or as a result of
legal regulations, it may be necessary to track the changes made to this data. When these changes are logged,
you should be able to check which user made which change, the date and time, the previous value, and the
current value, depending on the configuration. Furthermore, log records can be viewed and queried, but access
to them is restricted by adequate authorizations. The personal data for which changes shall be logged and the
retention period of logs, can be configured..

Defining Fields to Be Logged
SAP S/4HANA for financial products subledger processes personal data of, for example, business partners
and financial contracts that are involved in change requests and activities. If any changes are made regarding
the business partner, such personal data, the system logs the following information on personal data per
change request and activity:

•    The user who changed data
•    The date and time of the change
•    The change type (update, insert, deletion, single field documentation)
•    The identifying keys and their values of the data records
•    The heading name for the attribute that was changed

Most business objects, like the analytical business partner or the financial contract, are master data with a
specific versioning scheme that does not change or overwrite data but that always creates new data records
in the respective database tables. Therefore, in contrast to several other SAP products and applications, SAP
S/4HANA for financial products subledger does not log the changes via Change Documents, but the system
holds a full version history of the business objects unless they are archived.

For more information, see SAP Note 2709579        - Change Logging: How-to-Guide for Financial Products
Subledger.

See Also
For more information on change documents, see the documentation at https://help.sap.com/nw. Choose the
relevant SAP NetWeaver version and open the following documentation:

•    Under Application Help, go to   SAP NetWeaver Library: Function-Oriented View                 Application Server ABAP
       Other Services   Services for Application Developers      Change Documents .
•    Open the SAP NetWeaver Security Guide and go to       Security Aspects for Lifecycle Management
       Auditing and Logging .

Personal data is subject to frequent changes. Therefore, for review purposes or as a result of legal regulations,
it may be necessary to track the changes made to this data. When these changes are logged, you should be
able to check which employee made which change, the date and time, the previous value, and the current
value, depending on the configuration. It is also possible to analyze errors in this way.



                                                            Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
34     PUBLIC                                               Security Information for SAP S/4HANA for Financial Products Subledger

3.6           Security for Additional Applications or Other
              Components

This section describes security aspects relating to additional applications used in SAP S/4HANA for financial
products subledger.




Integration with Financial Services Data Management (FSDM): Data
Federation

The integration with SAP Financial Services Data Management (FSDM) through data federation is based on
generated HANA SQL views.

These SQL views do not provide information about data that is blocked (in the context of business partner
blocking and DPP). Therefore, data federation must be used for read-only purposes only. It must not be used
for data extraction because it cannot notify a data consumer about the end of the lifecycle of a data object
in SAP S/4HANA for financial products subledger. Since the SQL views do not prevent blocked data from
being displayed if the data objects are related to a blocked central business partner, any business objects in
SAP S/4HANA for financial products subledger that need to be blocked must be blocked using ILM-enabled
archiving.

In addition, the SQL views do not explicitly show the purpose of data processing that is specified within SAP
S/4HANA for financial products subledger. The data consumer must ensure that the legitimate purpose of
data processing is being adhered to.




3.7           Other Required Documents for Security

This section provides an overview of other security-related documents.

SAP S/4HANA for financial products subledger is based on SAP S/4HANA. This means that the security
guides relevant for SAP S/4HANA also apply.


 Resource                                                                    Where to Find It

 Security Guide for SAP S/4 HANA                                             At https://help.sap.com/s4hana, under Product
                                                                             Documentation.

 Security Guide for SAP HANA                                                 At https://help.sap.com/hana, under Security.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                        PUBLIC   35

4         Installing SAP S/4HANA for Financial
          Products Subledger


This section provides information about how to prepare for installation and what to do before and after the
installation of SAP S/4HANA for financial products subledger.

Financial Products Subledger is based on SAP S/4HANA. For general installation information, see the
Installation Guide for SAP S/4HANA at https://help.sap.com/s4hana.




4.1       Pre-Installation Tasks

There are two options for installing the Financial Products Subledger back end:

1. If your SAP S/4HANA system already exists, you plan a maintenance transaction with the maintenance
   planner to install SAP S/4HANA for financial products subledger 2306 in addition.
   You can install the add-on product version either using Software Update Manager (SUM) or using SAP
   Add-On Installation Tool (transaction SAINT) and the STACK.XML file.
2. If you plan a new system, you can install SAP S/4HANA and SAP S/4HANA for financial products
   subledger 2306 together in one maintenance transaction in the maintenance planner.
   To install the complete system, you have to use Software Provisioning Manager (SWPM) to install SAP
   S/4HANA, and SUM to install the required support package stacks and add-on product versions.

For more information about software logistics tools, see https://support.sap.com/en/tools/software-logistics-
tools.html .

In both cases, you use the maintenance planner to plan your system landscape and generate a stack XML file
based on the required product versions and product instances. You select and download the installation files in
the maintenance planner.

Choose the add-on product version S/4HANA FIN PROD SUBLDGR 2306:

•    Product instance Financial Products Subledger or the main component S4FPSL 300
•    Product instance Financial Products SubledgerUI for the UI component UIFPSL 200

For more information about the maintenance planner, see https://help.sap.com/viewer/p/
MAINTENANCE_PLANNER.




                                                          Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
36     PUBLIC                                                             Installing SAP S/4HANA for Financial Products Subledger

4.2           Overall Installation Sequence

1. Installation

Execute the plan and perform the installation based on the stack XML file and your Maintenance Planner
transaction.

For more information about Maintenance Planner and Execute Plan, see the Execute Plan section of the
Maintenance Planner User Guide on SAP Help Portal at Maintenance Planner. You will find the Maintenance
Planner User Guide under Other.




2. Implementation

You can implement the add-on using Software Update Manager (SUM). For more information, see Software
Update Manager .

Alternatively, you can implement the add-on using SAP Add-On Installation Tool (SAINT) and the stack
XML. For more information, see SAP Add-On Installation Tool and Support Package Manager. You will find the
documentation under Application Help.




3. Completion

To complete the installation, see Release Information Note 3328628                           .




4.2.1 Architecture Overview

A Financial Products Subledger system consists of (at least) two logical clients:

 Logical Client                                                              Use

 One Tool BW client                                                          Provides services to the Financial Products Subledger cli-
                                                                             ents, such as a characteristics repository for primary objects
                                                                             in the source data.

                                                                                Note

                                                                               This is an auxiliary client that is required because the
                                                                               client concept is not known to BW. There can be only
                                                                               one BW client in one system. Once you have chosen a
                                                                               BW client, you can no longer change it.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Installing SAP S/4HANA for Financial Products Subledger                                                                       PUBLIC      37

Logical Client                                           Use

One or more Financial Products Subledger clients         This is the application client in which Financial Products
                                                         Subledger functions are used.

                                                         It uses the functionality offered by the Tool BW. As several
                                                         Financial Products Subledger clients can use one Tool BW
                                                         client, the data stored in the Tool BW must be separated
                                                         according to source client.

                                                         For this reason, when you set up the system, you need
                                                         to assign a source system ID (characteristic 0SOURSYS-
                                                         TEM) for use in BW to each Financial Products Subledger
                                                         client in Customizing for Financial Products Subledger

                                                         under     Basic Settings       Global Settings        Define System

                                                         Landscape for Financial Products Subledger              .


      Note

     We do not recommend using the same physical client for the Tool BW client and the Financial Products
     Subledger client.




4.2.2 Post-Installation Tasks

Complete the following steps before making any Customizing settings or installing Business Content:

•     Change the system settings
•     Set up the Tool BW client
•     Set up a Financial Products Subledger client




4.2.2.1            Namespace Settings

To ensure that the system runs correctly, set the following namespaces to modifiable using transaction
SCTS_RSWBO004:

Set the following namespaces for characteristics and key figures that are created in Customizing to modifiable:

•     /B20/
•     /B20C/
•     /BA1/
•     /BA1C/
•     /BIC/



                                                           Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
38       PUBLIC                                                            Installing SAP S/4HANA for Financial Products Subledger

Additionally, if you want to use Accounting for Enabled Emissions, set the following namespaces to modifiable
as well:

 •    /G20/
 •    /G20C/
 •    /GH1/
 •    /GH1C/

      Note

     You can set these namespaces to not modifiable in systems (such as the productive system) if you
     transport manually created or generated InfoObjects from the development system to the target system.


These namespaces are used for generated objects for the Tool BW. They need to be modifiable when
InfoObjects are created manually or generated in the characteristic or key figure monitor, and when you
activate the DLL content.

      Note

     For SAP S/4HANA for Financial Products Subledger, please use the monitors for characteristics and key
     figures in Customizing for Financial Products Subledger under                      Basic Settings     Settings for Meta Data
      Characteristics          Characteristic Monitor            and under     Key Figures    Key Figure Monitor .

     For Accounting for Enabled Emissions, please use the monitors for characteristics and key figures in
     Customizing for Accounting for Enabled Emissions under                         Basic Settings     Settings for Meta Data
      Characteristics          Monitor for Characteristics              and under   Key Figures      Monitor for Key Figures .


Additional Information About the Namespaces Used in SAP S/4HANA for Financial Products
Subledger
 •    /B20/
       •   Namespace of generated DDIC objects of InfoObjects in namespace /BA1/.
           This namespace needs to be modifiable when you generate InfoObjects for fixed characteristics in the
           characteristic monitor or when you generate InfoObjects for SAP key figures in the key figure monitor.
 •    /B20C/
       •   Namespace of generated DDIC objects of InfoObjects in namespace /BA1C/.
           This namespace needs to be modifiable when you generate InfoObjects in namespace /BA1C/ in the
           characteristic monitor or key figure monitor.
 •    /BA1/
       •   Namespace of InfoObjects generated for a fixed characteristic (/BA1/C..), SAP key figure (/BA1/K...).
            •    InfoObjects for fixed characteristics are generated on demand in the characteristic monitor using
                 the Create InfoObject or Update InfoObject function.
            •    InfoObjects for SAP key figures are generated on demand in the key figure monitor using the
                 Generate InfoObject function.
       •   Activation of BI Content for Data Loading Process
 •    /BA1C/
       •   Namespace of InfoObjects generated for a Business Content characteristic or key figure.
           This namespace needs to be modifiable when you generate InfoObjects in namespace /BA1C/ in the
           characteristic monitor or key figure monitor.



Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Installing SAP S/4HANA for Financial Products Subledger                                                                 PUBLIC      39

•    /BIC/
     •    Namespace of generated DDIC objects of InfoObjects without prefix.
          This namespace needs to be modifiable when you generate InfoObjects without prefix in the
          characteristic monitor or key figure monitor.
•    /1BA/ (not modifiable)
     •    Namespace for DDIC objects and reports generated by Financial Products Subledger

Additional Information About the Namespaces Used in Accounting for Enabled Emissions
•    /G20/
     •    Namespace of generated DDIC objects of InfoObjects in namespace /GH1/.
          This namespace needs to be modifiable when you generate InfoObjects for fixed characteristics in the
          monitor for characteristics or when you generate InfoObjects for SAP key figures in the monitor for key
          figures.
•    /G20C/
     •    Namespace of generated DDIC objects of InfoObjects in namespace /GH1C/.
          This namespace needs to be modifiable when you generate InfoObjects in namespace /GH1C/ in the
          monitor for characteristics or the monitor for key figures.
•    /GH1/
     •    Namespace of InfoObjects generated for a fixed characteristic (/GH1/C..), SAP key figure.
           •      InfoObjects for fixed characteristics are generated on demand in the monitor for characteristics
                  using the Create InfoObject or Update InfoObject function.
           •      InfoObjects for SAP key figures are generated on demand in the monitor for key figures using the
                  Generate InfoObject function.
     •    Activation of BI Content for Data Loading Process
•    /GH1C/
     •    Namespace of InfoObjects generated for a Business Content characteristic or key figure.
          This namespace needs to be modifiable when you generate InfoObjects in namespace /GH1C/ in the
          monitor for characteristics or the monitor for key figures.
•    /BIC/
     •    Namespace of generated DDIC objects of InfoObjects without prefix.
          This namespace needs to be modifiable when you generate InfoObjects without prefix in the monitor
          for characteristics or the monitor for key figures.
•    /1GH/ (not modifiable)
     •    Namespace for DDIC objects and reports generated by Accounting for Enabled Emissions.




4.2.2.2               System Parameters

Adjust the system parameters to the specific system environment and data volume.




                                                                Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
40       PUBLIC                                                                 Installing SAP S/4HANA for Financial Products Subledger
