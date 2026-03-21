Classification: official-source-derived
Source basis: FPSL_ADMINGUIDE_EN.pdf, pages 10-22
Trust usage: user types, role concepts, authorization object structure, security framework
Do not use for: specific customer security policies or role assignments
Topics covered: security, user management, authorization objects, roles, access control, authentication

# Security, User Management, and Authorization
SAP Note Number   Title                                         Description

3069369           Release Information About UIFPSL200           Information about software component
                                                                version UIFPSL200

1668882           Note Assistant: Important Notes for           Corrections to the Note Assistant. Al-
                  SAP_BASIS                                     ways make sure you have the latest ver-
                  730,731,740,750,751,752,753,754,755,75        sion of this SAP Note installed in your
                  6                                             system before using transaction SNOTE
                                                                or SPAU.

3093855           Note Assistant: Important SAP Notes           Allows you to automatically implement
                  for the Revamped Note Assistant               note corrections in your ABAP systems

                  SAP S/4HANA for Financial Products            How to install Business Content for
3330659
                  Subledger 2306: Business Content In-
                                                                SAP S/4HANA for financial products
                  stallation
                                                                subledger.

                  Accounting for Enabled Emissions -            How to install Business Content for
3533825
                  Business Content Installation                 Accounting for Enabled Emissions.
                                                                This is only relevant if you use
                                                                Accounting for Enabled Emissions.

2722778           Configuration for Integrating Financial       You want to integrate Financial
                  Products Subledger with General               Products Subledger with General
                  Ledger                                        Ledger.

3332935           Release Strategy and Maintenance              Information on planning the installation,
                  Information for the ABAP Add-On               upgrades, and support packages of the
                  S4FPSL 300                                    ABAP add-on S4FPSL 300

3238110           Release Strategy and Maintenance              Information on planning the installation,
                  Information for the ABAP Add-On               upgrades, and support packages of the
                  S4FSFND 200                                   ABAP add-on S4FSFND 200.

3069246           Release Strategy and Maintenance In- Information on planning the installation,
                  formation for the ABAP Add-On UIFPSL upgrades, and support packages of the
                  200                                  ABAP add-on UIFPSL 200.

70228             Add-Ons: Conditions and Upgrade               General information for add-ons.
                  Planning

2722355           Partitioning of Database Tables               For large data volumes, the partition-
                                                                ing of database tables is mandatory
                                                                for Financial Products Subledger. This
                                                                supports runtime optimization and data
                                                                volume management.

2709579           Change Logging: How-To Guide for              Changes to personal data can be traced
                  Financial Products Subledger                  and reviewed.

2874355           How to Monitor and Operate S4FPSL             To avoid a decrease in runtime perform-
                                                                ance and to maintain high quality data
                                                                processing, you need to monitor the
                                                                system status on a daily basis.

2798428           Data Tiering in SAP S/4HANA for fi-     Guidance on how to set up a na-
                  nancial products subledger, banking ed- tive storage extension for Financial
                  ition / Smart AFI                       Products Subledger, banking edition.




                                         Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
10      PUBLIC                                              About SAP S/4HANA for Financial Products Subledger

SAP Note Number                                     Title                                Description

 2637010                                             Smart AFI / FPSL banking edition -   Guidance on how to set up a scale-out
                                                     Multi-Node Support                   setup for Financial Products Subledger,
                                                                                          banking edition.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
About SAP S/4HANA for Financial Products Subledger                                                                  PUBLIC      11

3           Security Information for SAP S/4HANA
            for Financial Products Subledger


This section deals with security topics relevant for SAP S/4HANA for financial products subledger.




3.1         User Management

This section provides an overview of how you manage and authenticate users in SAP S/4HANA for financial
products subledger.

Financial Products Subledger uses the user management and authentication mechanisms provided for SAP
S/4HANA. The security recommendations and guidelines for user administration and authentication described
in the SAP S/4HANA Security Guide also apply to Financial Products Subledger.




3.1.1 User Types

This section describes the types of users relevant for SAP S/4HANA for financial products subledger.

These user types do not exist in the system automatically. You can create and configure your own user types,
such as the following examples:


User Type                                               Description

Expert                                                  The expert is allowed to use the transactions in the SAP
                                                        Easy Access Menu for Financial Products Subledger. This
                                                        user type can display source data and results data and is
                                                        able to execute CVPM processes.

Customizer                                              The customizer is allowed to configure the Financial
                                                        Products Subledger system.

Administrator                                           The administrator is allowed to administer the Financial
                                                        Products Subledger system beyond the business scope of
                                                        the expert and the customizer. This user type manages the
                                                        integration of Financial Products Subledger into the system
                                                        landscape, for example.




                                                          Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
12       PUBLIC                                           Security Information for SAP S/4HANA for Financial Products Subledger

3.1.2 User Administration Tools

This section lists the tools available for user management and administration for SAP S/4HANA for financial
products subledger.


 Tool                                                                        Description


 User and role maintenance with SAP NetWeaver AS ABAP                        For more information, see the User Management sec-
                                                                             tion in the Security Guide for SAP S/4HANA at https://
 (Transactions SU01, PFCG)
                                                                             help.sap.com/viewer/p/SAP_S4HANA_ON-PREMISE.




3.1.3 Authentication and Single Sign-On

This section describes how authentication and single sign-on for users is implemented in SAP S/4HANA for
financial products subledger.

SAP S/4HANA for financial products subledger supports the Single Sign-On (SSO) mechanisms provided
by SAP NetWeaver. Therefore, the security recommendations and guidelines for user administration and
authentication as described in the SAP NetWeaver Security Guide also apply to SAP S/4HANA for financial
products subledger.

For more information, see SAP NetWeaver Security.




3.2           Role and Authorization Concept

This section describes the roles and authorizations available in SAP S/4HANA for financial products
subledger.

Financial Products Subledger uses the authorization concept provided by SAP NetWeaver AS ABAP.
Therefore, the recommendations and guidelines for authorizations described in the SAP NetWeaver AS
Security Guide ABAP also apply to SAP S/4HANA for financial products subledger.

The SAP NetWeaver authorization concept is based on assigning authorizations to users based on roles. For
role maintenance, use the profile generator (transaction PFCG) on the AS ABAP.

    Note

   For more information about how to create roles, see the role administration information at SAP NetWeaver
   Security.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                       PUBLIC    13

3.2.1 Authorization Objects

This section lists the most important security-relevant authorization objects that are used by SAP S/4HANA
for financial products subledger.


Authorization Object       Field                       Field Description                     Object Description


F_BABR_REG                 /BA1/BRSRC                  Source System                         FPSL: Access in Register
                                                                                             Process Step
                           /BA1/LGENT                  Legal Entity

                           ACTVT                       Activity

F_BABR_BAS                 /BA1/BRSRC                  Source System                         FPSL: Basic Authorizations in
                                                                                             Accounting
                           /BA1/LGENT                  Legal Entity

                           ACC_SYSTEM                  Accounting System                         Recommenda-
                                                                                                tion
                           ACTVT                       Activity
                                                                                                We strongly recom-
                                                                                                mend that you fill
                                                                                                the source data
                                                                                                field LEGAL_ENTITY
                                                                                                for contracts and se-
                                                                                                curities accounts (da-
                                                                                                tabase table /BA1/
                                                                                                F1_CON_FLAT). Other-
                                                                                                wise, the extensive au-
                                                                                                thorization check for
                                                                                                the legal entity in mas-
                                                                                                ter data and transaction
                                                                                                data using authorization
                                                                                                object F_BABR_BAS is
                                                                                                not supported (see also
                                                                                                Critical Combinations
                                                                                                [page 20]).


/GH1/LGENT                 /GH1/LGENT                  Legal Entity (AFEE)                   AFEE: Basic Authorization for
                                                                                             Legal Entity

F_BABR_CLC                 /BA1/BRCLC                  Calculator                            FPSL: Calculator

                           /BA1/BRSRC                  Source System

                           /BA1/LGENT                  Legal Entity

                           ACC_SYSTEM                  Accounting System

                           ACTVT                       Activity




                                                         Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
14    PUBLIC                                             Security Information for SAP S/4HANA for Financial Products Subledger

Authorization Object                   Field                                Field Description             Object Description

 F_BABR_UI                              /BA1/APP                             Application (in Fiori or      FPSL: Frontend (UI, Work
                                                                             ODATA Context)                Center, ODATA, CDS Views)
                                        /BA1/BUSSG
                                                                             Segment for Segmental Re-     F_BABR_UI is the most im-
                                        /BA1/KOKRS
                                                                             porting                       portant authorization object
                                        /BA1/LGENT                                                         for the CDS views in the Vir-
                                                                             Controlling Area
                                                                                                           tual Data Model.
                                        /BA1/ORGUT
                                                                             Legal Entity
                                        /BA1/PCTR
                                                                             Organizational Unit
                                        ACC_SYSTEM
                                                                             Profit Center
                                        ACTVT
                                                                             Accounting System

                                                                             Activity

 F_BABR_GLC                             /BA1/LGENT                           Legal Entity                  FPSL: General Ledger Con-
                                                                                                           nection
                                        ACTVT                                Activity

 F_BABR_ADJ                             /BA1/LGENT                           Legal Entity                  FPSL: Manual Adjustments
                                                                                                           and Workflow
                                        /BA1/PCATG                           Process Category

                                        ACC_SYSTEM                           Accounting System

                                        ACTVT                                Activity

 F_BAFC_PCD                             /BA1/FCPRC                           Process Step ID for Process   FPSL: Process Controller

                                                                             Controller
                                        ACTVT
                                                                             Activity

 F_BABR_SCB                             ACTVT                                Activity                      FPSL: Subledger Coding
                                                                                                           Block
                                        ACC_SYSTEM                           Accounting System

                                        /BA1/LGENT                           Legal Entity

 F_BABR_FPS                             /BA1/ACCSC                           Accounting Scenario           FPSL: Forecasting, Planning,
                                                                                                           and Simulation
                                        /BA1/FPSST                           Status of Scenario Results

                                        /BA1/NBSCN                           New Business Scenario

                                        ACTVT                                Activity

 F_FPS_TLS                              /BA1/TOOLS                           Tools                         Tool Methods, Utilities

                                        ACTVT                                Activity




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                         PUBLIC       15

Authorization Object   Field        Field Description                     Object Description

F_BAHW_RES             /BA1/F0CH1   Characteristic Value 1 (for           Results Data: Authorization
                                    Authorization Field)                  for Result Object
                       /BA1/F0CH2
                                    Characteristic Value 2 (for           Required for the results
                       /BA1/F0CH3
                                    Authorization Field)                  viewer and for the execution
                       /BA1/F0CH4                                         of CVPM process to enable
                                    Characteristic Value 3 (for
                                                                          read and write access to the
                       /BA1/F0CH5   Authorization Field)
                                                                          results data.
                       /BA1/F0CH6   Characteristic Value 4 (for
                                    Authorization Field)
                       /BA1/F0CH7
                                    Characteristic Value 5 (for
                       /BA1/HWRDA
                                    Authorization Field)
                       /BA1/HWRT
                                    Characteristic Value 6 (for
                       ACTVT        Authorization Field)

                                    Characteristic Value 7 (for
                                    Authorization Field)

                                    Results Data Area

                                    Result Type

                                    Activity

F_BAFW_PM              /BA1/F0CH1   Characteristic Value 1 (for           CVPM Authorization Object
                                    Authorization Field)
                       /BA1/F0CH2                                         You can use this authoriza-
                                    Characteristic Value 2 (for           tion object to separate tasks
                       /BA1/F0CH3
                                    Authorization Field)                  involved in the execution of
                       /BA1/F0CH4                                         processes.
                                    Characteristic Value 3 (for
                       /BA1/F0CH5   Authorization Field)

                       /BA1/F0CH6   Characteristic Value 4 (for
                                    Authorization Field)
                       /BA1/PAR
                                    Characteristic Value 5 (for
                       /BA1/PRO
                                    Authorization Field)
                       /BA1/SEQ
                                    Characteristic Value 6 (for
                       ACTVT        Authorization Field)

                                    Process Partition

                                    Analytical Process

                                    Step Sequence

                                    Activity




                                      Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
16    PUBLIC                          Security Information for SAP S/4HANA for Financial Products Subledger

Authorization Object                   Field                                Field Description               Object Description

 F_BAF3_GDS                             /BA1/F3SID                           ID of a Primary Data Source     Authorization for General Pri-
                                                                                                             mary Data Sources
                                        /BA1/F3STP                           Category of a Primary Data
                                                                             Source
                                        ACTVT
                                                                             Activity

 F_BAFF_ET                              /BA1/ETAPP                           Application Class for En-       Authorization for Enhance-
                                                                             hancement Tool Authoriza-       ment Tool
                                        /BA1/ETTEC
                                                                             tions
                                                                                                             Includes the critical activities
                                        ACTVT
                                                                             Technical Control Parame-       for changing DDIC objects
                                                                             ters - Control via Authoriza-   but without actual DDIC au-
                                                                             tion                            thorization.

                                                                             Activity

 F_BAF2_BTC                             /BA1/F2BTC                           Business Transaction Class      Authorization for Business
                                                                                                             Transaction Via BT Class
                                        ACTVT                                Activity

 F_BAF0_ADM                             ACTVT                                Activity                        Admin: RFC Destination and
                                                                                                             Characteristic Registration

 F_BAF1_AUG                             /BA1/F1AUG                           Authorization Group             Authorization for Objects via
                                                                                                             Authorization Group
                                        ACTVT                                Activity




Authorization Objects for Business Partner


SAP S/4HANA for financial products subledger (software component S4FPSL) is an add-on that is installed
on an SAP S/4HANA instance. There are two different business objects available for the business partner in
this type of installation:

 •    Recommended: SAP Business Partner, maintained in transaction BP
 •    Analytical Business Partner (aBP), maintained in transactions BPV1 (Create), BPV2 (Change), BPV3
      (Display)

      Recommendation

     We stongly recommend that you use SAP Business Partner.


For more information about the authorization objects for SAP Business Partner, see Authorization
Management.

If you are still using the analytical business partner, the table below shows the security-relevant authorization
objects that are used by the Business Partner for Financial Services component in Financial Products
Subledger.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                          PUBLIC        17

Authorization Object                                      Description

B_BUPA_ATT                                                Business Partner: Authorization Types

B_BUPA_FDG                                                Business Partner: Field Groups

B_BUPA_GRP                                                Business Partner: Authorization Groups

B_BUPA_RLT                                                Business Partner: BP Roles

B_BUPA_PGM                                                FS Business Partner Custom Grouping

B_BUPR_BZT                                                Business Partner Relationships: Relationship Categories

B_BUPR_FDG                                                Business Partner Relationships: Field Groups

B_BUPA_CRI                                                FS Business Partner: BP Role Cat./Differentiation Criterion

B_BUPA_CRS                                                Business Partner: Credit Standing Data

B_BUPA_RAT                                                Business Partner: Rating Procedures

B_BUPA_SLV                                                Selection Variant for Total Commitment

B_CCARD                                                   Payment Cards

B_CLEANSE                                                 Business Partner: Data Cleansing

B_BUP_PCPT                                                Business Partner: Purpose Complete


Additional Information:

•     Employees, VIPs, and other restricted groups of business partners need to be secured by separate groups.
      Restrictions are possible using field AUGRP in table BUT000 (authorization object B_BUPA_GRP) or field
      GROUP_FEATURE in table BP001 (authorization object B_BUPA_PGM).

You can use authorization object B_CCARD to grant different authorizations for creating, displaying, or
changing payment card data.

      Note

     This information is specific to Business Partner only. SAP S/4HANA for financial products subledger
     does not provide any card-specific security requirements. Moreover, information such as credit card
     numbers must not be stored in the Financial Products Subledger database.


In CRM, you can use authorization object B_CARD_SEC (Authorization Encryption Master) to control the
encryption or decryption of payment card data.

For more information, see SAP Customer Relationship Management. Under Application Help, choose                             Basic
Functions         Payment Card Processing   Security for Payment Card Data .

In addition, see the Security Guide under Security.

•     In the SAP GUI channel, you can use the authorization object B_BUPA_FDG for UI channel-specific, detailed
      checks at BDT field-group level.



                                                            Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
18       PUBLIC                                             Security Information for SAP S/4HANA for Financial Products Subledger

•    You can also check at a more detailed level in the service channel. To do so, you must define your own
      authorization objects. The corresponding checks must be implemented in the enhancement BAdIs of the
      Business Partner services.
 •    If you activate the SACF scenario FSBP_RATINGS (FS-BP: Scenario for Ratings and Credit Standing Data)
      in the Workbench for Switchable Authorization Check Scenarios (transaction SACF), you can also use
      the FS-BP authorization objects B_BUPA_RAT (Business Partner: Ratings) and B_BUPA_CRS (Business
      Partner: Credit Standing Data).
 •    You can use authorization object S_TABU_NAM to control authorizations for settings in the Customizing
      activity Set Rating Procedures and Ratings (maintenance view V_TP021).


Standard Authorization Groups in Tables

Direct table access for FS-BP tables (using transaction SE16, for example) is only possible using the following
authorization groups of authorization object S_TABU_DIS:

 Authorization Group                                                         Description

 BPOA                                                                        Business Partner Application Data

 BPOS                                                                        Business Partner Control Tables

 BPOC                                                                        Business Partner Customizing Tables

 BPAA                                                                        Analytical Business Partner Application Data

 BPAS                                                                        Analytical Business Partner Control Tables

 BPAC                                                                        Analytical Business Partner Customizing Tables



Critical Combinations

The SAP_CA_BP_DEVELOPER_AG role contains * values for authorizations. These * authorizations are critical
because they allow unrestricted access to data or activities.


Authorization for Data Access Interface

When generating views for the Data Access Interface, enable authorization checks in Customizing for Financial
Products Subledger under                  Infrastructure         Data Access Interface          Enable Authorization Checks in DAI .




3.2.2 Standard Roles

This section describes the standard roles used by SAP S/4HANA for financial products subledger.

      Note

     You can use these roles as template roles.




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                         PUBLIC   19

Role                                                       Description

SAP_FPS_CUSTOMIZER                                         This role contains authorizations for making Customiz-
                                                           ing settings for Subledger Accounting (/BA1/Subledger Ac-
                                                           counting).

SAP_FPS_EXP_FINANCIAL_ACCTNT                               This role contains authorizations for the SAP Easy Access
                                                           Menu for Financial Products Subledger.

SAP_FPS_EXP_FINANCIAL_PLANNER                              This role contains authorizations for the SAP Easy Access

                                                           Menu for      Financial Products Subledger            Forecasting,

                                                           Planning, and Simulation        .

SAP_FPS_EXP_VDM_REPORTING                                  This role contains authorizations for using CDS views of the
                                                           Virtual Data Model for Financial Products Subledger.

SAP_GGA_CUSTOMIZER                                         This role contains authorizations for making Customizing
                                                           settings for Accounting for Enabled Emissions (/GH1/).

SAP_GGA_EXPERT_ACCOUNTANT                                  This role contains authorizations for the SAP Easy Access
                                                           Menu for Accounting for Enabled Emissions.


An administrator or a technical user can have all of the roles listed, together with specific profiles for
Customizing transports or BW as described in Setting Up a Financial Products Subledger Client [page 51].




3.2.3 Critical Combinations

This section describes combinations of roles and authorizations in SAP S/4HANA for financial products
subledger.

SAP S/4HANA for financial products subledger (FPSL) runs on SAP S/4HANA. Be careful when you combine
FPSL roles with non-FPSL roles. This might be necessary if you want to configure access to the General Ledger
in SAP S/4HANA, for example. Define the authorization object S_RFC restrictively and do not provide it with
wildcard (*) authorizations.

The table below contains some of the most important authorization objects in Financial Products Subledger.

      Note

     When you design roles for Financial Products Subledger business experts, a good starting point from
     a theoretical perspective is to initially consider the authorization objects F_BAFW_PM and F_BABR_BAS.
     Authorization object F_BAFW_PM defines more or less the range of CVPM processes (technically, these
     are ABAP reports) that a business expert is allowed to execute. This goes along with a corresponding
     definition of authorization object S_TCODE since the transaction codes point to specific ABAP reports
     (CVPM processes). Furthermore, authorization object F_BABR_BAS controls access to data, mainly and
     most importantly driven by the field Legal Entity (which corresponds to the company code). With this
     two-dimensional setup of authorizations, the main defense lines are already defined. This also applies to
     Accounting for Enabled Emissions with authorization object /GH1/LGENT, but not F_BABR_BAS.




                                                             Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
20       PUBLIC                                              Security Information for SAP S/4HANA for Financial Products Subledger

Authorization Object                                                        Use

 F_BAFW_PM                                                                   Processing data in the context of CVPM processes. Wildcard
                                                                             authorizations (starting with *) in the Analytical Process
                                                                             field /BA1/PRO are critical.

 F_BAHW_RES                                                                  Accessing results data

 F_BAF1_AUG or                                                               Accessing source data

 F_BAF2_BTC

 F_BABR*                                                                     Specific to the accounting logic.

                                                                             F_BABR_BAS is used to check the legal entity (/BA1/LGENT
                                                                             - Legal Entity) in source data, results data, and CVPM proc-
                                                                             esses.

                                                                             The Source Data field LEGAL_ENTITY must be filled for
                                                                             contracts and securities accounts (database table /BA1/
                                                                             FL_CON_FLAT). Otherwise authorization checks on the legal
                                                                             entity cannot be supported properly.

                                                                                Note

                                                                               F_BABR_BAS is the most important authorization object
                                                                               for checking the legal entity. To a large extent, this check
                                                                               is based on the field LEGAL_ENTITY in the financial con-
                                                                               tract in the source data. Therefore, we strongly recom-
                                                                               mend that when you load financial contracts, the data-
                                                                               base field LEGAL_ENTITY is filled. (Do not enter a legal
                                                                               entity by using entries from other fields that are map-
                                                                               ped to the characteristic Legal Entity /BA1/C55LGENT
                                                                               in the subledger coding block). This also applies to
                                                                               the definition of securities accounts and portfolios in
                                                                               the source data. To be clear: An entry in the the field
                                                                               LEGAL_ENTITY is mandatory; not only for supporting
                                                                               the proper execution of accounting processes but also
                                                                               for authorization checks in value helps, database access
                                                                               and process execution.


                                                                             In addition, F_BABR_UI is the most important authorization
                                                                             object for CDS views of the Virtual Data Model.

 /GH1/LGENT                                                                  Used to check the legal entity (/GH1/LGENT) in the results
                                                                             data and CVPM processes for Accounting for Enabled
                                                                             Emissions.

                                                                             Results are displayed or processes are executed only for
                                                                             legal entities for which an authorization exists. For this
                                                                             purpose, the CDS Views /GH1/CVC_LGENT_EXEC, /GH1/
                                                                             CVC_LGENT_DIS, and /GH1/CVC_LGENTF4 check this au-
                                                                             thorization object.

 F_BAFC_PCD                                                                  Process Controller




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
Security Information for SAP S/4HANA for Financial Products Subledger                                                           PUBLIC        21

Authorization Object                                 Use

F_BAFF_ET                                            Enhancement Tool for DDIC extensions in source data, re-
                                                     sults data, and accounting.

                                                     Only relevant for system administrators and power users:
                                                     Edit or change activities are generally required.

F_FPS_TLS                                            Used in several technical tool reports, such as where-used
                                                     lists, code generation for derivation and mapping routines,
                                                     or ASU-delivery functions




Related Information

System Architecture for SAP S/4HANA for Financial Products Subledger [page 7]




3.3      Network and Communication Security

This section provides an overview of the network topology and communication protocols used by SAP S/
4HANA for financial products subledger.

The network topology for Financial Products Subledger is based on the topology used by SAP NetWeaver,
SAP HANA, and SAP S/4HANA. The security guidelines and recommendations described in the security guides
for these components also apply to the Financial Products Subledger.




Related Information

System Architecture for SAP S/4HANA for Financial Products Subledger [page 7]
https://help.sap.com/viewer/nwguidefinder
https://help.sap.com/viewer/p/SAP_HANA_PLATFORM
https://help.sap.com/viewer/p/SAP_S4HANA_ON-PREMISE




                                                       Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
22    PUBLIC                                           Security Information for SAP S/4HANA for Financial Products Subledger
