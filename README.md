<h1 align="center">
  <a href="https://www.holyname.org/foundation/haitihealthpromise.aspx"><img src="https://crudem.org/wp-content/uploads/2023/07/2021HN-Logo_RGB_Horizontal_HHP-scaled-e1690430519668.jpg" alt="Ozone HSC" width="30%"/></a>
</h1>

<p align="center">
    <b>Ozone HSC</b> is a child distribution of <a href="https://www.ozone-his.com/case-studies/case-study-ht-1">Ozone Haiti</a> configured to address the needs of the Hôpital de Sacré-Coeur in Milot, Haiti.
    <br/>
</p>

---

<br/>

<p align="center">
    <a href="https://docs.ozone-his.com/"><img src="https://raw.githubusercontent.com/ozone-his/.github/refs/heads/main/profile/ozone-logo.png" alt="Ozone" width="20%"/></a>
</p>

<h3 align="center">The Instant HIS</h3>

<p align="center">
    <br/>Engage with the Ozone community and access useful resources below:
</p>

<h3 align="center">
    <a href="https://github.com/ozone-his/">Code</a>&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://docs.ozone-his.com/">Docs</a>&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://talk.openmrs.org/c/software/ozone-his/70">Forum</a>&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://openmrs.slack.com/archives/C02PYQD5D0A">Chat Room</a>
</h3>

## Release Notes

<details>
  <summary><b>Version 2.1.0</b></summary>
   <ul>
    <li>Depends on:
     <ul>
      <li><a href="https://docs.ozone-his.com/users/#ozone-his-apps">Ozone 1.0.0-alpha.13</a></li>
      <li><a href="https://github.com/mekomsolutions/ozone-haiti?tab=readme-ov-file#release-notes">Ozone Haiti 1.1.0</a></li>
     </ul>
    </li>
   </ul>

   <b>Specific notes</b>

   <ul>
    <li>Added active medication and conditions in IPD summary page.</li>
    <li>Set Indication to optional for drug orders.</li>
    <li>Added missing login and visit locations.</li>
    <li>Made units of measurement to display in clinical forms for numeric fields in Vitals and Biometrics.</li>
    <li>Updated uuid for Administration location.</li>
    <li>Added 'Account Management' external link to app menu.</li>
    <li>Removed config to show medications and conditions in IPD summary.</li>
    <li>Added OpenMRS billing module dependency.</li>
    <li>Added reports for pregnant women receiving iron folate, prenatal multi-vitamins, total children seen, and patients with diagnosis.</li>
    <li>Added mandatory identifier from Patient registration form.</li>
    <li>Updated Ozone version to 1.0.0-alpha.13.</li>
    <li>Updated ozone-pro version to point to 1.0.0-alpha.14.</li>
    <li>Removed ampathformstranslation folder and exclude Consultation.json file from Haiti.</li>
    <li>Removed SSO support.</li>
    <li>Cleaned up imaging orders concepts list.</li>
    <li>Added missing Odoo Addons.</li>
    <li>Made NGINX proxy build context configurable via environment variable.</li>
    <li>Removed ozone_settings Odoo addon & add Odoo initializer default settings.</li>
    <li>Updated Odoo configs to match HSC Prod.</li>
    <li>Updated Nurse, Doctor & Registrar roles.</li>
    <li>Remove unnecessary .gitkeep in frontend_config directory.</li>
    </ul>
</details>

<details>
  <summary><b>Version 2.0.0</b></summary>
   <ul>
    <li>Depends on:
     <ul>
      <li><a href="https://docs.ozone-his.com/users/#ozone-his-apps">Ozone 1.0.0-alpha.13</a></li>
      <li><a href="https://github.com/mekomsolutions/ozone-haiti?tab=readme-ov-file#release-notes">Ozone Haiti 1.0.0</a></li>
     </ul>
    </li>
   </ul>

   <b>Specific notes</b>

   <ul>
    <li>Set license to MPL 2.0.</li>
    <li>Added GitHub Action continuous integration pipeline.</li>
    <li>Set up concepts and Registration page.</li>
    <li>Configured clinical forms.</li>
    <li>Added mode of arrival form.</li>
    <li>Added emergency follow up form.</li>
    <li>Added '.ocd3.yml' file.</li>
    <li>Fixed email person attribute type uuid.</li>
    <li>Fixed capture patient photo feature.</li>
    <li>Configured Vitals and Anthropometry form to match original HSC form.</li>
    <li>Added 'dateAndTimeOfDeath' to death fields.</li>
    <li>Configured registration form with HSC form sections.</li>
    <li>Added visit attributes 'Mode of arrival' and 'Level of emergency severity assessment'.</li>
    <li>Added translation for visit attributes and update frontend config to show visit attribute fields.</li>
    <li>Ensured successful loading of configurations.</li>
    <li>Fixed logo in patient chart.</li>
    <li>Adjusted GitHub workflow to pass validation.</li>
    <li>Removed duplicate files inherited from Haiti Distro.</li>
    <li>Set Numéro Dossier as primary identifier for the patient identifier sticker.</li>
    <li>Fixed weight and height UUIDs.</li>
    <li>Added missing OpenMRS concept configs.</li>
    <li>Replaced existing drug concepts with the HSC drugs.</li>
    <li>Updated 'ozone/' to 'configs/' for serving frontend configurations.</li>
    <li>Added Odoo initializer configurations.</li>
    <li>Configured attachments-overview-widget as part of patient summary.</li>
    <li>Removed mode of arrival tag from patient banner.</li>
    <li>Disabled manual entry for 'Numero Dossier'.</li>
    <li>Configured lab order basket and results viewer widgets.</li>
    <li>Added HSC specific encounter types and privileges.</li>
    <li>Added 'allergies-details-widget' to patient summary dashboard.</li>
    <li>Moved 'Triage' from visit attributes to Vitals and Biometrics.</li>
    <li>Fixed contact and address information in patient banner.</li>
    <li>Added 'Email' to person attribute types config and fixed address translation.</li>
    <li>Fixed consultation prénatale edit privilege.</li>
    <li>Fixed missing concept 'Family History Set'.</li>
    <li>Updated material to medical supply order type.</li>
    <li>Added missing concept vacine lot number.</li>
    <li>Disabled lab reference number.</li>
    <li>Added contact person's phone number to patient banner.</li>
    <li>Adjusted count of active visits to be shown in a single page to 50.</li>
    <li>Configured locations in IPD and OPD.</li>
    <li>Added active visit obs config.</li>
    <li>Added page size and print scale config for patient identifier sticker.</li>
    <li>Moved Triage question and made optional.</li>
    <li>Added 'vitalSignsConceptSetUuid' config.</li>
    <li>Updated 'Pain Scale' to display the range as part of the label.</li>
    <li>Added config for advanced patient search app.</li>
    <li>Updated orderables for imaging and procedure order types.</li>
    <li>Added imaging and procedures order types.</li>
    <li>Added clinical form translations.</li>
    <li>Updated configuration for print identifier sticker functionality.</li>
    <li>Fixed banner app's configuration.</li>
    <li>Replaced lab order type with test order type in the order basket.</li>
    <li>Added style obs-by-encounter-widget.</li>
    <li>Moved medical supply order type to Ozone Haiti.</li>
    <li>Added labels with units for weight, height, temperature, abnominal diameter, head circumference and mid-upper arm circumference.</li>
    <li>Removed laboratory app.</li>
    <li>Added translation overrides for app navigation menu items.</li>
    <li>Added 'stock_extension' add-on and 'docker-compose-override.yml' file.</li>
    <li>Updated the config for different orders to hide reference field.</li>
    <li>Adjusted frontend config translations.</li>
    <li>Fixed typo in the Ozone frontend config JSON file.</li>
    <li>Removed form concept labels and adjust some multi-selects.</li>
    <li>Added Ozone Pro features to ozone-hsc distro.</li>
    <li>Removed order types in favor of Haiti level.</li>
    <li>Removed 'vitals-overview-widget'.</li>
    <li>Update the drug order type UUID.</li>
    <li>Added more person attributes on patient banner.</li>
    <li>Removed unnecessary triage visit attribute.</li>
    <li>Added location tag 'Transfer loaction.</li>
    <li>Moved the 'life style' table into the patient chart summary dashboard.</li>
    <li>Added ability of transferring patients between locations.</li>
    <li>Added order basket action menu.</li>
    <li>Created form for HSC Emergency Department.</li>
    <li>Added monitoring config.</li>
    <li>Renamed OpenMRS frontend config.</li>
    <li>Enabled SSO integration.</li>
    <li>Fixed 'Drug Order' type UUID.</li>
    <li>Fixed OpenMRS ERP properties env substitution</li>
    <li>README as per Ozone's rebranding.</li>
    <li>Centered README w/ references to Haiti Health Promise.</li>
    <li>Fixed Odoo broken dataflows + override EIP_FHIR_RESOURCES.</li>
    <li>Copied EIP Keycloack OpenMRS database creation script.</li>
    <li>Copied full data directory from Ozone instead of only MySQL.</li>
    <li>Added medical supply product UOMs.</li>
    <li>Assign encounter privileges to 'Registration Clerk' and 'Nurse limited' roles.</li>
    <li>Renamed Kit -> Kit and Bag -> Sachet.</li>
    <li>Consolidated Liquibase changesets into single liquibase.xml file.</li>
    <li>Updated drug order UUID.</li>
    <li>Voided email field from OpenMRS module appointments in favor of known hardcoded UUID.</li>
    <li>Fixed ODOO_USER and ODOO_PASSWORD values.</li>
    <li>Fixed missing dependency tracker configuration.</li>
    <li>Removed metadatatermmappings will be inherited from Haiti distro.</li>
    <li>Fixed the numeric fields in clinical forms.</li>
    <li>Removed password changer from user panel slot in primary navigation app.</li>
    <li>Used Tablet(s) instead of Tablet as dosage unit for drugs.</li>
  </ul>
</details>
