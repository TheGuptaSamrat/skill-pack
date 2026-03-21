## IMG_20260321_174826930.jpg

...
X CVPM_Framework
SAP CVPM Framework

---

## IMG_20260321_174832827.jpg

SAP Calculation and Valuation Process Manager (CVPM) is a
core framework within Financial Products Subledger (FPSL
used to manage, execute, and monitor complex, step-based
financial calculations
UBS
12-Jan-2026
Internal

---

## IMG_20260321_174840066.jpg

Key Aspects of SAP CVPM:
Functionality: CVPM orchestrates analytical processes, including data extraction,
valuation, and regulatory reporting, using pre-defined step sequences.
Process Monitor: The CVPM Process Monitor (/BA1/CVPM_MONITOR) allows to
view, analyze, and manage the lifecycle of these background jobs.
Integration: It acts as an engine within the FPSL infrastructure, interfacing with
the Source Data Layer (SDL) and RDL.
Key Capabilities: It is crucial for running calculations in FPSL and supports parallel
processing to handle large volumes of data.
LIR

---

## IMG_20260321_174844252.jpg

Implementation Steps of AMDP using CVPM:
1. Create SERVER class - Z_CL_CM_BS_SOLUTION_WL
2. Create CVPM class - Z_CL_CM_BS_SOLUTION
3. Create SERVER for Primary Datasources (PDS)
4. Create Primary Datasource (PDS) - Z_CL_CM_BS_SOLUTION_WL
5. Create Analytical Process - Z_CM_BS_SOLUTION
6. Create Sequences for Analytical Process - Z_CM_BS_SOLUTION
7. Execute CVPM job - Z_CM_BS_SOLUTION from se38 or Airflow and monitor

---

## IMG_20260321_174917193.jpg

1. Create SERVER class - Z_CL_CM_BS_SOLUTION_WL :
Class Builder: Display Class Z_ CL_CM_BS_SOLUTION_WL
loal Definitions/implementations Local Test Classes
Снн/Interface
Properties
Interfaces
2_CL SOLUTION SL
Friends
Implemented / Active
Att/Butey
Methods
Events Types
& Source Cod
Properties
Interface
/BAL/1T_73_908_SOURCE
/BAL/17_73_908_800BCK_EXTA
/BA1/1T_73_909_CUBT
Alutract Final
Model..
0
Descrption
SDL-D5) Dete Insertese Bot Dese Soure
Exteneion to Interfere 00E BORR
SDL D8: Cuetonising Shooters
0
Class/Interface
Properties
Interfaces
Trende
Attributes
Implemented / Active
Methods
Events / Types
Properties
Attrbute
/BA1/15_73_ODS_CUST-CON_DA_SEL CHAR NO
BAL/TT_F3_GDA_CUST-CON_DS_SEL CHAR OPT
BAL/TF_F3_GDA_CUST-CON_DS_SEL_ CHAR, REQ
/BA1/17_T3_GDR_CUST-CON_DM_SEL,CRAR SWVALUE
/BAL/TF_T3_GD9_COST-CON_DS_SEL CHAR OPT_SIG
/BAL/TT_73_GDA_COST-CONDY_SEL UNTT_ NO
/BAL/17_73_6D1_COST-CON_DO_SEA UNIT_ SIEVALUT
/BAL/1T_T7_GD9_CUST-COM_D8_KTND_ST
BAL/1T_T3_0D9_CUST-CON_DS_KIND_FL
/BAL/IT_73_609_CUST-COM_DS_7778, 6D8
A CURSOR
R PACKAGE 812X
A STROCTURE
Level
Constant
Constant
Constant
Constant
Constant
Constant
Constant
Constant
Publi
Publi
Pubic
Pubk:
Pubk
Pubk:
Pubi
Pubk
Constant
Constant
Instance Ambute
Pubk
Instance Attrute Pubk
Instance Attrtute Pubk
Ro. Typng
L Варе
L Type
С туре
O Type
Туре
Type
• Туре
Type
12-Jan-2026
Interna
ланові 18
/s/79_308_06_580_C838
883/73_098_86_581_CHA8
3AL/73_88_80_583_CHAD
BAL./F3_898_09_S8L_CRAS
/BAL/73_808_06_98382T7_3817
BaL/79_000_00_9001017 3037
/BAL/F3_008_06_K080
/BAL/E3_0TE_09_KT80
BAL/TO_OTE OSTERE
3AL/F3_0T2_FACI00A S122
3AL/T3_DTE_DS_STRDC
Descrption
* ID of Selection Characterstic
* 1D of Selection Characterstic
* ID of Selection Characteristic
JAD of Selection Characteristic
ID of Selection Characteristic
'4'
MAnit Indicator of a Key Figure for Sele..!
JAne Indicator of a Key Figure for Sele... 3
/Type of Data Source
Type of Data Source
12
Data Source Category
Initial Value

---

## IMG_20260321_174928497.jpg

Create SERVER class - Z_CL_CM_BS_SOLUTION_WL :
Class Builder Class Z_CL_CM_BS_SOLUTION_WL Display
Pattern
Pretty Printer
actve
Signature
Class Builder: Display Class Z_ CL_CM_ BS_SOLUTION_ WL
098806/862
2 COL BS SOLUTION NI
Local Defintions/Implementations
Local Test casses
# Source Code-Based
Class documentation
Properbes Interfaces
• Parameters 48 Exceptions E Sourcecode aR
/BAL/1T_T3_GDS_CUST-READ_CHAP_IEXT
/BAL/17_T)_GDS_CUST-READ_ATTR_VALUT_TEXT
/BA1/1F T3 GDS CUST-CHECK CUS:
BA4/1-0-005_SOURCE_EXT2-DELETE_PACK_MLT
/BAJ/IT_T3_GDS
OURCE_EXTS-CHECK_FOR_PARALLEL MODE
DAL: 11 13 005
SOURCE-GET_DATA_SNE
/BAL/IF_F3_GDS_SOURCE-PACK_DRTA_MLT
BAL/IT_73_G0S_SOURCE-GET_BACK, ALT
/BAL/IT_T3_0D5_S0URCE-GET_N0_MLT
/BAL/17_T3_GDS_SOURCZ-GET_DELTA_DATA_MLT
/BAL/1T_T3_GDS_SOURCE-BACK_DELTA_DATA MLT
BAL/1T_T9_GDS_SOURCZ-GET_NO_DELTA_MLT
Text eement
INTe
ovides all Characteristics and Key Figures of a Server
Provides all Attrbutes of a Server and Their Values
wete source customang neck
Provaes rostole vales or an Aurbute Hier
As the Server Which Reade Mode Is to Be Used
vides One or More Single Records of a Serve
Prepares Reading a Workist by Package
es a Package from Workists Prepared by GET_PACK
the No.of Packages for Paralei Reading of Packages
rowdies a Delta Workist
tape pr tackage keading of Deta Workist
Provdes the No. of Packages for a Paral.Detta Package Read
Method
/BA1/IF_F3_GDS_SOURCE-PACK DATA MLI
22
23
24
1v_client = sy-mandt.
OPEN CURSOR @g_cursor
SELECT
FOR
/BA1/C55POSTD,
28
/BA1/ C55CONTID
FROM /BA1/HFSPD
30
WHERE
/BA1/C55POSTD - @1v_busdate.
31
32
HIE sy-subrc > 0.
CLEAR a cursor.
Class Builder Class Z_ CL_CM_BS_SOLUTION_WL Display
Pattern
Pretty Printer
Signature
REPublic Section
Method
13
14
15
/BA1/IF_E3_GDS_SOURCE-GET_PACK_MLT
active
CREATE DATA e_ref_ds_data_tab TYPE STANDARD TABLE OF
(_structure).
ASSIGN e_ref_da_data_tab->* TO <1_cab_ export).
REFRESH
<1_tab_ export>.
19
FETCH NEXT CURSOR ®9_CUISOL INTO CORRESPONDING FIBIDS OF TABLE (<1_tab_export>
PACKAGE SIZE @_package_size.
22
IF sy-subre > 0.
CLOSE CURSOR @_cursOr.
e_tla_end of data - "*'.
ENDIF.
27
endmethod.
Protected
12-lan-2026
UBS

---

## IMG_20260321_174936517.jpg

2. Create a CVPM class - Z_CL_CM_BS_SOLUTION :
Class Builder: Display Class Z_ CL_CM_ BS_SOLUTION
E Local Definitions/Implementations
Class/Interface
Properties
Interfaces
2_CL_CM_BSSOLUIION
Friends
Attributes
Implemented / Active
Methods
Events
Types
Aliases
Properties
Hilter
Interface
/BAL/IF_AL_EW_ENRICH_PARAM
/BA1/IF_AL_EW_ENRICH_DATA
IF_AMDP_MARKER_ HDB
Abstract
Final
Model...
Description
Parameter Enrichment Step
Data Enrichment Step
Marker Interface for DB Procedure:
Class/Interface
Properties
Interfaces
2_CI_CM_BS_SOLUTION
Friends
Attributes
Implemented / Active
Methods
Events
Types
Aliases
Properties
ДТ
Type
/BAL/IF_AL_EN _ENRICH_DATA-I_STR_PARAM
/BAL/IF_AL_EW_ENRICH_PARAM I_STR_PARAM
TY_SIR_HESPD_PDS
I_SIR_HESPD_PDS
Visibility
Public
Public
Public
Public
Filter
Typing
Туре
Туре
Associated Type
/BAL/IF_AL_EW_RUN=>I_STR_PARAM
/BAL/IF_AL_EW_RUN=>T_STR_PARAM
Type
Туре
Class Builder: Display Class Z_CL_CM_BS_SOLUTION
Local Definitions/Implementations
# Local Test Classes
Class/Interface
Properties
Interfaces
2_CL_CM BS_SOLUTION
Friends
Attributes
Implemented / Active
Methods
Events
Types
Parameters
Exceptions
Method
/BA1/IF_AL_EW_ENRICH_DATA-S_CREATE
/BA1/IF_AL_EW_ENRICH_DATA-EXECUTE
/BA1/IF_AL_EW_ENRICH_PARAM-S_CREATE
/BA1/IF_AL_EW_ENRICH_PARAM-EXECUTE
INSERT_BAL_SNAPSHOT_DATA
Sourcecode
205
Level
Visibility
Static Method
Public
Instance Method Public
Static Method
Public
Instance Method Public
Static Method Public
Filter
M... Description
Generates Instance for Data Enrichment Step
Runs Data Enrichment Step
Generates Instance for Parameter Enrichment Step
Runs Parameter Enrichment Step
Description
Run Parameters
12-Jan-2026
Internal

---

## IMG_20260321_174944937.jpg

2. Create a CVPM class - Z_CL_CM_BS_SOLUTION :
Class Builder Class Z_ CL_CM_BS_SOLUTION Display
Pattem
Pretty Printer Signature Publ Section Protected Section Private Section
Text Elements
ective
Method
37
3%
43
/BA1/T8_AL_TV_ENRICH_DATA-EXECUTE
1v_cllent - sy-mandt.
_counter counter
CLEAR 10_ Atapa_poe.
step_data
ASSION 1_step_detes dete
70
ASSIGN
COMPONENT
ASSIGN
COMPONENT
(lv_cont_ad>
15
ASSIGNED,
1v_counter - 1v_coanter * 1.
18_htapd_pas-contractad • 4*_cost_AD,
1a_htapd_pda-Counter - 1v_countes
ENDLE.
APPEND 1a_Atapd_pda To 2t_Atapa_ods.
CLEAR 1a_htapd_pds.
ENDLOOR.
CALL NETHOD 2_C_ CM_85_SOLUTIO- INSERT_BAL_SAPSHOT_DATAL
EXPORTING
*y_entity - 1r entity
1*_Desdate - 2v_busdate
Ay_trondatetime - 1y _tromtime
*e_client = 1y_cliest
package_keyliss + It stapa_pds.
- EXPORTING
41454) TO FIELD-SYMBOL (Clv_poating_date)) .
dasa T0
FIELD-SYMBOL (cly_cont_1d) .
12-Jan-2026
Internal

---

## IMG_20260321_174954036.jpg

reate a CVPM class - Z_CL_CM_BS_SOLUTION :
Class Builder Class Z_CL_CM_BS_SOLUTION Display
Pattern
Pretty Printer
active
Signature
REPublic Section
Method
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
1 GR
INSERT_BAL_SNAPSHOT_DATA
"/BA1/C55SLACC",
"/BA1/IGL_ACCOUNT",
"/ BA1/C55BUKRS",
"/BA1/C55CHGRSN" ,
SUM ("/BA1/K5SAMOBJ") ,
"/BA1/OBJ_CURR",
SUM ("/BA1/K5SAMBAL") ,
"/BA1/BIL_CURR",
SUM ("/BA1/K5SAMGRP") ,
"/BAI/GRP_CURR" ,
1 AS NEW_RECORDS_IN_HESPD
FROM "/BA1/HESPD" H INNER JOIN #package_ keylist F
ON "/BA1/C55CONTID" = contractid
WHERE CLIENT - :iv_client
AND "/BA1/C65POSTD" <= : iv busdate
AND TRIM| LEFT | RTRIM| "/BA1/C55POSTD" ), 4 )) - RRIM IBFT ( RIRIM :İV
busdate 1, 4;
/* AND
B"/BA1/C65LGENT" - iiv_entity AND
L "/BA1/C55CONSRC" - ; iv_sresystem */
/ *AND
"/BA1/CROTSIMP"›= ¡iv fromdatetime AND
L "/BA1/CROTSTMP" < ¡iv_todatetime*/
GROUP BY
Connter

---

## IMG_20260321_175002770.jpg

3. Create SERVER for Primary Datasources:
T-Code SE54 to create Server - /BA1/VC_TF3_GDSSV in Cluster and click Test
Change View "Server for General Primary Data Sources": Details
6g New Entries
Generate Table Maintenance Dialog: Initial Table/View Screen
ole view Varant
Dialog Structure
• B Server for General Prima
• • Attributes of the Ser
• M Delta Read Modes for
Edit Table/View
• ABAP Dictionary
•Generated Objects
•Authorization Groups
•Assgn Authorz. Group
Events
VIEW 2OR
Maxmum No. of Hits
SALVE TES GOSSH
Server
ZCBS
Server for General Primary Data Sources
Balance Snapshot
Server
Component
Server Class
DataReadGrp
• Single Rec.Sel.
• Buffering
DS Buffering
/ Sel.by Worklist
•Sort
/ Read by Package
Read in Parall.
• Delta Approach
• Correction Srvr
•Primary Obj. St
• Aggregation
• Only Parallel
• BAdI Count Pack
0001
12-Jan-2026
Internal
UJU

---

## IMG_20260321_175011372.jpg

3. Create SERVER for Primary Datasources:
Change View "Server for General Primary Data Sources": Overview
Change View "Server for General Primary Data Sources": Overview
New Entries
LD
Eo
Dialog Structure
Server for General Prima
• Attributes of the Ser
• Delta Read Modes for
Server for General Primary Data Sources
Server
Data Source Server
DI_CNT_END
Data Lifecycle Management - Limit Validity
FILE
File
Worklist for Model Assignment
GHG
GL_CONN
RDL_TAB_WL
RDI_VIEW
REGISTER
RIA_PC
SAFI_ADJ_R
SAFI_EPS
SAFI_IAD
SAFI_RNG
SDLCONFLAT
TABLE
ZBS
ZCBS
Greenhouse Gas Accounting
General Ledger Connection
Results Data Layer-Based Worklist
Results Data Layer
Register Process
Process Controller Objects
Select Manual Journal Entries Not Reset
Forecasting, Planning, and Simulation
Credit Risk Attribute Determinat. (Input)
Range Processing for RDL
Contract Server for Primary Objects (MDF
Table
BalanceSnapshot
Balance Snapshot
Component Server Class
11
/BA1/CL_AL_
/BA1/CL_E3_
RP
GH
55
RO
RO
55
/BA1/CL_AL_
/GH1/CL_GHG
/BA1/CL_AL_
/BA1/CL_AL_
/BAI/CL_AL_
/BA1/CL_AL_
/BAI/CL_AL_
55
55
55
55
11
/BA1/CL_AL_
/BAL/CL_AL_
/BA1/CL_AL_
/BAL/CL_AL_
/BA1/CL_AL_
/BA1/CL_F3_
55
77
2CLCMBS-
2_CL_CM_BS_
12-Jan-2026
Internal
UBS

---

## IMG_20260321_175020980.jpg

4. Create Primary Datasource (PDS) -Z_CL_CM_BS_SOLUTION_WL :
SPRO
Display IMG
Existing BC Sets °BC Sets for Activity 6 Activated BC Secs for Activicy Apply Fiter Change Log Compare Where Else Ut
Structure
- 6a
:
SAP Customizing Implementation Guide
Commercial Project Management
Profitablty and Performance Management
UBS.SAP - Portal Configuration
Activate Business Functions
Conversion of Accounting to SAP S/4HANA
ABAP Platform
Enterprise Structure
Cross-Application Components
Moble Application Integration Framework Configuration
SAP Portfolo and Project Management
Financial Accounting
Fancal Supply Chan Management
Multi-Bank Connectivity Connector
Strategic Enterpse Management/Business Analytics
Financial Products Subledger
Basic Settings
Data Model
Subledger Accounting
Forecasting, Planning, and Simulation
Notes to Financal Statements
Preparatory Processng
Infrastructure
Data Loading Process
Data Sources for Workists
• 6o Edt Appication Areas for Data Sources
• Ra Edk Data Sources
Calculation and Valuation Process Manager (CVPM)
BEdt Genenic BW Data Extraction Using CVPM
Data Access Interface
Interfaces to Account Management
Settings for Web Services (SOAP)

---

## IMG_20260321_175028933.jpg

4. Create Primary Datasource (PDS) - Z_CL_CM_BS_SOLUTION_WL:
Display Primary Data Sources
Data Sources - Technical View
Workist
L Data Sources for Worklists
Custom Data Sources
Technical Detals
Data Source for Balance Snapshot
/FC1/BT_STAGING
/FC1/MP_STAGING
Z_a_CM_BS_SOLUTION_WL
Header Data
Data Sice Type
Data Sice Cat.
Data Source
General Data
Description
Server
Status
Data Reading Group
DRG ID (Server)
Owner
Data Structure
Enh. Data Structure
SGS Structure
Created On
Created By
Areas
Selection of Worklist *
Data Source
2_CL_CM_BS_SOLUTION WL
Attribute
Chars.
Key Figs
Data Source for Balance Snapahot
Data Source for Balance Snapshot
Balance Snapshot
Active
0001
0001
/18A/F3_STR_GDS_ 80C98639434388
/1BA/T3_STR_GDX_80C9868943A388
05.02.2026
43877575
Changed On
Changed by
11.02.2026
43877575

---

## IMG_20260321_175040416.jpg

4. Create Primary Datasource (PDS):
The parameter defined in the Worklist class will get auto populate in below section and required
parameters to be selected.
Display Primary Date Sources
6g
Data Sources - Technical View
* Workäst
Data Sources for Workists
Custom Data Sources
Technical Detals
Header Data
Data Sice Type
Data Sice Cat.
Data Source
General Data
Areas
Selection of Workst -
Data Source
2_CLCLBS_SOLUTION WI
Attrbute
Chars.
/ Data Source for Balance Snapshot
% Data Source for Balance Snapshot
/FCL/MP_STAGING
ZO_OM_BS_SOLUTION_WL
Key Figs
Characteristic
/BA1/C55CONTID
/BA1/CSSPOSTD
Gran.
Div.C.
Selection Char.
Optional
Optional
Long Description
• Contract/Portfolo
• Posting Date
losong Date
12-Jan-2026
Internal

---

## IMG_20260321_175049368.jpg

5. Create Analytical Process - Z
_CM_BS_SOLUTION:
Display IMG
Existing BC Sets &°BC Sets for Activity
& Activated BC Sets for Activity
Apply Filter
Change View "Analytical Processes": Details
Structure
Financial Products Subledger
Basic Settings
Data Model
Subledger Accounting
Forecasting, Planning, and Simulation
Notes to Financial Statements
Preparatory Processing
Infrastructure
Data Loading Process
Data Sources for Workists
• To Assign Fields from Tables and Structures to Characteristics
• a # Edit Application Areas for Data Sources
• La F Edit Data Sources
• I6o # Assign Authorization Characteristic Profiles to Data Sources
Calculation and Valuation Process Manager (CVPM)
General Settings for Custom Processes
• IEa Application Log: Edit Subobject for CVPM
• 6a Edit Analytical Processes
• I6o E Define Process-Specific Pushbuttons
• Is Edit Custom Step Sequences for Analytical Processes
• 160 ₴
Edit Fixed Step Sequences for Analytical Processes
Define Package Size Per Legal Entity, Accounting System, and Source System
Dialog Structure
- Be Analytical Processes
• Process Parameter
• M Data Reading Groups
• Ea Technical Settings
• ERC Status Manageme
Analyt. Process
Z_CM_BS_SOLUTION
Analytical Processes
Report title
CVPM for Balance Snapshot Solution
Step Controller
Process Category
•System Process
Leading Process
Run Group Gen.
• Latest Time Stamps
Dynamic Selections
ODS on Sel. Scr
Subobject
Auth. Category
/BAL/CL_AL_EN_STEP_CONTROL_SQ
Standalone Process
Always
No Dynamic Selections
WI
12-Jan-2026
Internal
UBS

---

## IMG_20260321_175123150.jpg

5. Create Analytical Process - Z_CM_BS_SOLUTION:
Display IMG
Existing BC Sets 66 BC Sets for Activity
6o' Activated BC Sets for Activity
Structure
Financial Products Subledger
Basic Settings
Data Model
Subledger Accounting
Forecasting, Planning, and Simulation
Notes to Financial Statements
Preparatory Processing
Infrastructure
Data Loading Process
Data Sources for Worklists
• 160
Assign Fields from Tables and Structures to Characteristics
Edit Application Areas for Data Sources
Edit Data Sources
Assign Authorization Characteristic Profiles to Data Sources
Calculation and Valuation Process Manager (CVPM)
General Settings for Custom Processes
• Го
• 160
Application Log: Edit Subobject for CVPM
Edit Analytical Processes
Define Process-Specific Pushbuttons
Edit Custom Step Sequences for Analytical Processes
• 160
Edit Fixed Step Sequences for Analytical Processes
• To
Define Package Size Per Legal Entity, Accounting System, and Source System
...
... .
Apply Filter Gây
Change View "Analytical Processes": Details
New Entries
Dialog Structure
* DAnalytical Processes
• • Process Parameter
• Data Reading Groups
• • Technical Settings
• RC Status Manageme
Analyt. Process
2_CM_BS_SOLUTION
Analytical Processes
Report title
CVPM for Balance Snapshot Solution
Step Controller
Process Category
• System Process
Leading Process
Run Group Gen.
• Latest Time Stamps
Dynamic Selections
ODS on Sel. Scrn
Subobject
Auth. Category
/ BA1/CL_AL_EN _STEP_CONTROL_SO
Standalone Process
Always
No Dynamic Selections
WL
2-Jan-2026
Internal
UBS

---

## IMG_20260321_175128565.jpg

5. Create Analytical Process - Z_CM_BS_SOLUTION:
Change View "Process Parameter": Overview
New Entries
Eo
E 6a
Dialog Structure
• Analytical Processes
• D Process Parameter
• Data Reading Groups
• Technical Settings
• RC Status Manageme
Analyt. Process
Report title
2_CM_BS_SOLUTION
CVPM for Balance Snapshot Solution
Process Parameter
Process Parameter
/BA1/C11SRCSY
/BA1/C55LGENT
/BA1/C55POSTD
/BA1/CROTSTMP
No.
2
Parameter Type
Single Value
Single Value
Single Value
Value Range
On Sel. Screen
Hidd
Change View "Data Reading Groups": Overview
6gy New Entries
Dialog Structure
Analytical Processes
• Process Parameter
• E Data Reading Groups
• Technical Settings
• RC Status Manageme
Analyt. Process
Report title
2_CM_BS_SOLUTION
CVPM for Balance Snapshot Solution
Data Reading Groups
DRG
Description
0001
Source Data
On Sel. Screen
Interval
Calculatn
12-Jan-2026
Internal
S Ul

---

## IMG_20260321_175134815.jpg

6. Create Sequences for Analytical Process - Z_CM_BS_SOLUTION:
Display IMG
Existing BC Sets 66^BC Sets for Activity
So Activated BC Sets for Activity Apply Filter Change Log Compa
Structure
Change View "Step Sequences": Details
New Entries ID Es
La 33 Fo
Financial Products Subledger
Basic Settings
Data Model
Subledger Accounting
Forecasting, Planning, and Simulation
Notes to Financial Statements
Preparatory Processing
Infrastructure
Data Loading Process
Data Sources for Workists
• 6a Assign Fields from Tables and Structures to Characteristics
• I6o @ Edit Application Areas for Data Sources
• [6a # Edit Data Sources
Assign Authorization Characteristic Profiles to Data Sources
Calculation and Valuation Process Manager (CVPM)
General Settings for Custom Processes
• TEa Application Log: Edit Subobject for CVPM
• To Edit Analytical Processes
• a Define Process-Specific Pushbuttons
Edit Custom Step Sequences for Analytical Processes
6a Edit Fixed Step Sequences for Analytical Processes
Define Package Size Per Legal Entity, Accounting System, and Source System
Edit Generic BW Data Extraction Using CVPM
Data Access interface
Interfaces to Account Management
Settings for Web Services (SOAP)
Dialog Structure
- Step Sequences
-M Steps
• D Repackaging Field:
• Job Distribution
• M Message Context
Analyt. Process
Report title
Step Sequence
Step Sequences
Description
Results Data Layer
Rsts Data Area
Result Grp Type
Result View
Application Log
• Cumulate Log
• Protect Mess.
• No Application Log
Other Settings
Error Threshold
Auth. Char.Prof.
RC Determination
• Process Partition
2_CA_BS_SOLUTION
CVPM for Balance Snapshot Solution
10
salance Snapst
12-Jan-2026
Internal
UBS

---

## IMG_20260321_175139433.jpg

6. Create Sequences for Analytical Process - Z_CM_BS_SOLUTION:
Change View "Steps": Overview
New Entries
EE
Dialog Structure
*
Step Sequences
• Steps
Repackaging Field:
Job Distribution
Message Context
Analyt. Process
Step Sequence
Description
Report title
63
_SOLUTION
10
Balance Snapshot
CVP for Balance Snapshot Solution
Steps
No.
15
20
30
Description
Enrich Parameters
Workdst
Ennich Data
Step Type
Enrich Parametera
Worklist Creation
Data Enrichment

---

## IMG_20260321_175148954.jpg

6. Create Sequences for Analytical Process - Z_CM_BS_SOLUTION:
Change View "Steps": Details
6ộg New Entries
Ee m
18
Dialog Structure
Step Sequences
- F
* Steps
Repackaging Field:
Job Distribution
• Message Context
Analyt. Process
Step Sequence
Description
Keport title
Step Number
Steps
Description
Step Type
Step Execution
2_CM_BS_SOLUTION
10
Balance Snapshot
CVPM for Balance Snapshot Solution
15
Enrich Parameters
Enrich Parameters
2_CL_OM_BS_SOLUTION
Worklist Creation
Change View "Steps": Details
60 New Entries ID Eo
Foa
Dialog Structure
• Step Sequences
* Steps
• Repackaging Field:
•I Job Distribution
• Message Context
Analyt. Process
Step Sequence
Description
Report title
Step Number
Steps
Description
Step Type
Step Execution
Worklist Creation
Data Srce Cat.
Data Source
Key Date Param.
Parameter Delta
Package Size
Analyzer
Status
12-Jan-2026
Internal
2_CM_BS_SOLUTION
10
Balance Snapshot
CVPM for Balance Snapshot Solution
20
Worklist
Worklist Creation
Data Source
CISSOLUTION HI
BAL/CSSPOSID
20.000
•Alow Overwnting of Package Size
Active
UBS

---

## IMG_20260321_175153966.jpg

6. Create Sequences for Analytical Process - Z_CM_BS_SOLUTION:
Change View "Steps": Details
6g New Entries
Eo
Dialog Structure
Step Sequences
• Steps
Repackaging Field:
Job Distribution
• Message Context
Analyt. Process
Step Sequence
Description
Report title
Step Number
Steps
Description
Step Type
Step Execution
2_CM_BS_SOLUTION
10
Balance Snapshot
CVPM for Balance Snapshot Solution
30
Enrich Data
Data Enrichment
2_CL_CM_BS_SOLUTION
12-lan

---

## IMG_20260321_175158982.jpg

7. Run CVPM job - Z_CM_BS_SOLUTION from se38 and monitor in below screen:
SAP Easy Access
Favontes
* ZASSIST - App: Raise Support Incident
SAP Menu
Connector for Multi-Bank Connectivity
3 Profitablity and Performance Management
3 Office
R Cross-Application Components
L Logistics
• El Accounting
Be Anandal Products Subledger
- Data Model
Subledger Accounting
Forecasting, Planning, and Simulation
General Ledger Connection
Notes to Financial Statements
Preparatory Processing
infrastructure
Data Loading Process
- Ee Calculation and Valuation Process Manager (CVPM)
• /BAL/PW_PROCMON - Start CVPM Process Monitor
Generic BW Data Extraction
1o0k
Accounting for Enabled Emissions
Human Resources
information Systems
Service
→ Tools
L WebCient Ul Framework
12-Jan-2026
Internal

---

## IMG_20260321_175203668.jpg

7. Run CVPM job- Z_CM_BS_SOLUTION from se38 and monitor in below screen:
Run Display (Database)
DUpdate
•
10
Kuns Found
Msg. Stat.
Error Msgs Analytical Process
Step Seq.
ZOM BS SOLUTION 10
Z OM BS SOLUTION 10
Z OM BS SOLUTION 10
ZOM BS SOLUTION 10
ZOM BS SOLUTION 10
Z OM BS SOLUTION 10
ZOM BS SOLUTION 10
Z OM BS SOLUTION 10
ZOM BS SOLUTION 10
Z OM BS SOLUTION 10
12 System Layout
Start of Run
End of Run
Runtime Test Run Job Name Job No. Program Name
2026/02/12 10:05:22 2026/02/12 10:08:14
Prog. Date
171524
2026/02/12 10:00:12 2026/02/12 10:00:51
APPL_CVPM 053622 12.02.2026
38394
APPL_CVPM 053035 12.02.2026
2026/02/12 09:57:08 2026/02/12 09:57:28
20469
2026/02/12 09:40:26 2026/02/12 09:42:57
APPL_CVPM 052728 12.02.2026
151184
2026/02/12 09:24:50 2026/02/12 09:24:51
APPL_CVPM 051108 12.02.2026
460
2026/02/12 09:21:54 2026/02/12 09:21:55
576
APPL_CVPM 045451 12.02.2026
2026/02/12 09:13:17 2026/02/12 09:13:18
APPL_CVPM 045154 12.02.2026
847
2026/02/12 09:04:18 2026/02/12 09:05:07
APPL_ CVPM 044317 12.02.2026
49300
2026/02/12 09:03:28 2026/02/12 09:03:30
1389
APPL_CVPM 043450 12.02.2026
APPL_ CVPM 043329 12.02.2026
2026/02/12 08:49:55 2026/02/12 08:50:19
24571
APPL_CVPM 042018 12.02.2026
12-Jan-2026
Internal

---

## IMG_20260321_175209996.jpg

7. Run CVPM job - Z_CM_BS_SOLUTION from se38 and monitor in below screen:
Display logs
& Technical Information
Date/Time/User
12.02.2026 05:35:22 43877575
Probiem Cass Other
Nu...
6
6
External ID
Object text
Subobject Text
7C1E52345DFB... Calculation and... Worklist for Pre... SE38
Transac...
Program
Mode
Log Number
Z_CM_BS_.. Dialog pro... 00000000000004124099
HE .
Ty
Message Text
Started run of ID 7C1E52345DFB1FD181F982C22B059A7E (start time 202602120435228965000')
Process 2_CM_85_SOLUTION has been started with step sequence 10
Process is run using UTC timestamp Source Data 202602120434158140720
161 packages were prepared for parallel processing using method 0205
161 packages containing 3204009 data records were processed
Run ended (end time 202602120438144208810)
Long
Det.
12-lan-2026

---

## IMG_20260321_175213034.jpg

7. Run CVPM job - Z_CM_BS_SOLUTION from se38 and monitor in below screen:
Display logs
o Technical Information
Date/Time/User
L 12.02.2026 05:35:22 43877575
• Problem Class Other
Nu...
6
6
External ID
Object text
Subobject Text Transac...
7C1E52345DFB... Calculation and... Worklist for Pre... SE38
Program
Mode
Log Number
Z_CM_BS_... Dialog pro...
00000000000004124099
STUP
0
Ty...
0
Message Text
6
Started run of ID 7C1E52345DFB1FD181F982C22B059A7E (start time 202602120435228965000')
Process Z_CM_BS_SOLUTION has been started with step sequence 10
Process is run using UTC timestamp Source Data' 202602120434158140720
161 packages were prepared for parallel processing using method 0205
161 packages containing 3204009 data records were processed
Run ended (end time 202602120438144208810)
Long Det.
2-lan-2026
Internal

---

