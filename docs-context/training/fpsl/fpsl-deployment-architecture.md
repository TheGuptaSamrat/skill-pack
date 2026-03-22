Classification: official-source-derived
Source basis: FPSL_ADMINGUIDE_EN.pdf, pages 6-10
Trust usage: supported deployment patterns, system components, architecture framing
Do not use for: specific customer deployment decisions without assessment
Topics covered: system architecture, deployment options, embedded vs. hub, front-end/back-end, landscape planning

# FPSL System Architecture and Deployment Options
2         About SAP S/4HANA for Financial
          Products Subledger


SAP S/4HANA for financial products subledger (also referred to here as Financial Products Subledger) is a
comprehensive subledger for financial products for banks, insurance and reinsurance companies, fintechs,
and other corporations. Deployed as an add-on to SAP S/4HANA, it is based on a highly simplified core and
designed for large data volumes, making use of SAP HANA capabilities. With SAP Fiori user experience and a
streamlined data model it is designed to run simple.

Combining financial and management accounting, Financial Products Subledger allows you to produce
multiple, reconciled valuations for financial products.

Some features may require a separate license. For further information, please contact your SAP Account
Executive.

Accounting for Enabled Emissions (AFEE) is a part of SAP S/4HANA for financial products subledger. It
enables you to manage carbon accounting in the same way as you manage financial accounting. Financing data
and emissions data, measured in carbon dioxide equivalents (CO2e), are combined to create subledger journal
entries for your carbon balance sheet.

The following two use cases are possible:

•   You use Accounting for Enabled Emissions together with SAP S/4HANA for financial products
    subledger, and the financing data stems from there.
•   You use Accounting for Enabled Emissions independently of SAP S/4HANA for financial products
    subledger, and import the financing data to the system.




Implementation Considerations

If you want to install the software components of SAP S/4HANA for financial products subledger in the
context of the implementation project for a broader solution such as subledger accounting for insurance
contracts, it is essential that you familiarize yourself with the content of the corresponding solution description
before beginning the installation.

For more information, see the Product Page for SAP S/4HANA for financial products subledger.




Integration

The back-end instance SAP S/4HANA for financial products subledger contains the business logic and is an
add-on for SAP S/4HANA.

In addition, there is a front-end instance Financial Products Subledger UI, which contains Fiori applications as
an add-on for SAP Fiori Front-End Server. These Fiori applications are not relevant for SAP S/4HANA, financial
posting gateway.



                                                            Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
6      PUBLIC                                                                  About SAP S/4HANA for Financial Products Subledger

You can choose to implement an embedded deployment with the back-end and front-end on the same
server or to implement a hub deployment. When you are implementing the hub deployment option, you use
separate servers for the back-end and front-end components in your landscape. You find further information
for the landscape planning and installation of Fiori applications in the corresponding SAP Fiori Implementation
Information.




2.1           System Architecture for SAP S/4HANA for Financial
              Products Subledger

This section describes the technical system architecture and the software components involved.

SAP S/4HANA for financial products subledger (S4FPSL) is an add-on to the SAP S/4HANA core.




System Architecture

SAP Analytics Cloud (SAC), Business Warehouse (BW), and other SAP or third-party systems must be
deployed separately.

The overall system architecture can look like this:




You can opt for a minimal system landscape, a maximal system landscape, or a mixed approach depending on
your individual needs. In a minimal system landscape, as many components as possible are deployed together.
In a maximal system landscape, as many components as possible are deployed separately.




Back End and Front End

For SAP S/4HANA for financial products subledger, you can choose between a single-instance installation
(one software stack) and a dual-instance installation (two software stacks) as illustrated below.



Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
About SAP S/4HANA for Financial Products Subledger                                                 PUBLIC         7

In a single-instance deployment, you deploy the back end and front end together, whereas in a dual-instance
installation, you deploy them separately.

•   SAP S/4HANA 2022 or SAP S/4HANA 2023




Back End

Financial Products Subledger with its back-end applications is an add-on for SAP S/4HANA 2022 or SAP
S/4HANA 2023. You must install the following product instance:


Product Instance                                        Release


SAP S/4HANA server                                      SAP S/4HANA 2022 or SAP S/4HANA 2023


You can then install the following instance of Financial Products Subledger with its comprised software
components:

                            Required SAP S/4HANA                                               Comprised Software Com-
Product Instance            version                     Release                                ponent Versions

Financial Products Subledger SAP S/4HANA 2022 or SAP    SAP S/4HANA for financial              S4FPSL 300
                             S/4HANA 2023               products subledger 2306
                                                                                               S4FSFND 200



Front End

Financial Products Subledger with its front-end SAP Fiori applications is an add-on for SAP FIORI FES 2022
FOR S/4HANA or SAP FIORI FES 2023 FOR S/4HANA.


Deployment Scenario         Product Instance            Release                                Comment

Embedded                    Financial Products Subledger SAP S/4HANA for financial             The required front-end server
                                                         products subledger 2306               is part of the back-end soft-
                                                                                               ware stack.




                                                           Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
8     PUBLIC                                                                  About SAP S/4HANA for Financial Products Subledger

Deployment Scenario                    Product Instance                     Release                     Comment

 Hub                                    SAP Front-End Server 7.52            SAP FIORI FES 2022 FOR S/
                                                                             4HANA or SAP FIORI FES
                                        (Hub) or
                                                                             2023 FOR S/4HANA
                                        SAP Front-End Server 7.57 or

                                        SAP Frontend Server 7.58


You can then install the following product instance of Financial Products Subledger with its comprised
software component.

                                                                                               Comprised Software Component Ver-
 Product Instance                                    Release                                   sions

 Financial Products Subledger UI                     SAP S/4HANA for financial products        UIFPSL 200
                                                     subledger 2306




Hardware and Software Requirements

The minimum system requirements for Financial Products Subledger are described in SAP Note 3332935
for ABAP add-on S4FPSL 300, in SAP Note 3238110    for ABAP add-on S4FSFND 200, and in SAP Note
3069246     for UIFPSL 200.

You can find more information about sizing at https://www.sap.com/about/benchmark/sizing.expert-
sizing.html#expert-sizing .




2.2           Overview of Required SAP Notes

The following SAP Notes are essential for installing, upgrading, and operating SAP S/4HANA for financial
products subledger.

Make sure that you have the latest version of each SAP Note, which is available on the SAP Support Portal at
http://support.sap.com/notes .

    Note

   Before you start the installation, have a look at the Release Information Notes 3328628                     , 3069369      ,
   and 3331588 .



 SAP Note Number                                     Title                                     Description

 3328628                                             Release Information About S4FPSL300 Information about the add-on
                                                     Support Packages                    S4FPSL300




Administration Guide for SAP S/4HANA for Financial Products Subledger 2306
About SAP S/4HANA for Financial Products Subledger                                                                   PUBLIC        9

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
