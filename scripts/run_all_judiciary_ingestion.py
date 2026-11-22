# -*- coding: utf-8 -*-
"""
Execution script to rebuild all 181 Judiciary Tests from the 9 clean master JSON files.
"""

import json
import os
import glob
import re
from ingest_all_judiciary_clean import format_question, update_test_file, save_cache, FILES

def load_json(path):
    print(f"Loading {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

print("Loading 9 downloaded clean master JSONs...")
cpc_data = load_json(FILES['cpc'])
crpc_data = load_json(FILES['crpc'])
evidence_data = load_json(FILES['evidence'])
ipc_data = load_json(FILES['ipc'])
const_data = load_json(FILES['constitution'])
minor_acts_data = load_json(FILES['minor_acts'])
tort_lim_data = load_json(FILES['tort_lim_sra_trust'])
tpa_contract_data = load_json(FILES['tpa_contract'])
juris_data = load_json(FILES['juris_int_org'])

stats = {}

# 1. CPC (20 tests)
print("\n--- Ingesting CPC (20 tests) ---")
cpc_ch = cpc_data['chapters']
cpc_sub = "Code of Civil Procedure, 1908"
cpc_sub_hi = "सिविल प्रक्रिया संहिता, 1908"

cpc_mapping = [
    ("tests/judiciary_pyq/cpc/cpc_pyq_t01_preliminary.json", cpc_ch[0]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t02_jurisdiction_and_res_judicata.json", cpc_ch[1]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t03_place_of_suing_and_institution_of_suits.json", cpc_ch[2]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t04_summons_and_discovery.json", cpc_ch[3]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t05_judgment_decree_and_costs.json", cpc_ch[4]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t06_execution.json", cpc_ch[5]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t07_incidental_proceedings.json", cpc_ch[6]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t08_suits_in_particular_cases.json", cpc_ch[7]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t09_special_proceedings_adr.json", cpc_ch[8]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t10_supplemental_proceedings.json", cpc_ch[9]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t11_appeals.json", cpc_ch[10]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t12_reference_review_and_revision.json", cpc_ch[11]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t13_high_court_rules_and_special_provisions.json", cpc_ch[12]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t14_miscellaneous_provisions.json", cpc_ch[13]['questions']),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t15_orders_01_to_10_parties_pleadings_and_issues.json", cpc_ch[14]['questions'][0:197]),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t16_orders_11_to_20_discovery_admissions_and_trial.json", cpc_ch[14]['questions'][197:255]),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t17_order_21_execution_of_decrees_and_orders.json", cpc_ch[14]['questions'][255:286]),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t18_orders_22_to_32_incidental_and_special_suits.json", cpc_ch[14]['questions'][286:356]),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t19_orders_33_to_51_indigent_injunctions_and_appeals.json", cpc_ch[14]['questions'][356:450]),
    ("tests/judiciary_pyq/cpc/cpc_pyq_t20_miscellaneous_and_practice_questions.json", cpc_ch[15]['questions'])
]

cpc_tot = 0
for path, qs in cpc_mapping:
    cnt = update_test_file(path, qs, cpc_sub, cpc_sub_hi)
    cpc_tot += cnt
stats['cpc'] = cpc_tot
print(f"CPC rebuilt: 20 tests, {cpc_tot} questions.")

# 2. CRPC (39 tests)
print("\n--- Ingesting CrPC (39 tests) ---")
crpc_ch = crpc_data['chapters']
crpc_sub = "Code of Criminal Procedure, 1973"
crpc_sub_hi = "दंड प्रक्रिया संहिता, 1973"

crpc_files = sorted(glob.glob(r'tests/judiciary_pyq/crpc/*.json'))
crpc_tot = 0
for idx, fpath in enumerate(crpc_files):
    qs = crpc_ch[idx]['questions']
    cnt = update_test_file(fpath, qs, crpc_sub, crpc_sub_hi)
    crpc_tot += cnt
stats['crpc'] = crpc_tot
print(f"CrPC rebuilt: {len(crpc_files)} tests, {crpc_tot} questions.")

# 3. Evidence (17 tests)
print("\n--- Ingesting Evidence (17 tests) ---")
ev_ch = evidence_data['chapters']
ev_sub = "Indian Evidence Act, 1872"
ev_sub_hi = "भारतीय साक्ष्य अधिनियम, 1872"

ev_mapping = [
    ("tests/judiciary_pyq/evidence/evidence_pyq_t01_preliminary.json", ev_ch[0]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t02_relevancy_and_res_gestae.json", ev_ch[1]['questions'][0:122]),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t03_admissions_and_confessions.json", ev_ch[1]['questions'][122:248]),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t04_dying_declaration_and_statements.json", ev_ch[1]['questions'][248:326]),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t05_statements_under_special_circumstances.json", ev_ch[1]['questions'][326:368]),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t06_expert_opinion_and_character.json", ev_ch[1]['questions'][368:445]),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t07_facts_need_not_be_proved.json", ev_ch[2]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t08_oral_and_documentary_evidence.json", ev_ch[3]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t09_public_documents.json", ev_ch[4]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t10_presumptions_as_to_documents.json", ev_ch[5]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t11_exclusion_of_oral_by_documentary_evidence.json", ev_ch[6]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t12_burden_of_proof.json", ev_ch[7]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t13_estoppel.json", ev_ch[8]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t14_witnesses_competency_privilege.json", ev_ch[9]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t15_examination_of_witnesses.json", ev_ch[10]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t16_improper_admission_and_rejection.json", ev_ch[11]['questions']),
    ("tests/judiciary_pyq/evidence/evidence_pyq_t17_practice_and_revision_questions.json", ev_ch[12]['questions'])
]

ev_tot = 0
for path, qs in ev_mapping:
    cnt = update_test_file(path, qs, ev_sub, ev_sub_hi)
    ev_tot += cnt
stats['evidence'] = ev_tot
print(f"Evidence rebuilt: 17 tests, {ev_tot} questions.")

# 4. IPC (26 tests)
print("\n--- Ingesting IPC (26 tests) ---")
ipc_ch = ipc_data['chapters']
ipc_sub = "Indian Penal Code, 1860"
ipc_sub_hi = "भारतीय दंड संहिता, 1860"

ipc_mapping = [
    ("tests/judiciary_pyq/ipc/ipc_pyq_t01_general_introduction.json", ipc_ch[0]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t02_preliminary_and_jurisdiction.json", ipc_ch[1]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t03_general_explanations.json", ipc_ch[2]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t04_punishments.json", ipc_ch[3]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t05_general_exceptions_excusable_acts.json", ipc_ch[4]['questions'][0:148]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t06_right_of_private_defence.json", ipc_ch[4]['questions'][148:218]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t07_abetment.json", ipc_ch[5]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t08_criminal_conspiracy.json", ipc_ch[6]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t09_offences_against_state_and_armed_forces.json", ipc_ch[7]['questions'] + ipc_ch[8]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t10_offences_against_public_tranquillity.json", ipc_ch[9]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t11_offences_relating_to_public_servants_and_elections.json", ipc_ch[10]['questions'] + ipc_ch[11]['questions'] + ipc_ch[12]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t12_false_evidence_and_public_justice.json", ipc_ch[13]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t13_coin_stamps_public_health_and_religion.json", ipc_ch[14]['questions'] + ipc_ch[15]['questions'] + ipc_ch[16]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t14_offences_affecting_life_homicide_murder.json", ipc_ch[17]['questions'][0:146]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t15_miscarriage_hurt_and_grievous_hurt.json", ipc_ch[17]['questions'][146:205]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t16_wrongful_restraint_and_confinement.json", ipc_ch[17]['questions'][205:231]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t17_criminal_force_and_assault.json", ipc_ch[17]['questions'][231:267]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t18_kidnapping_abduction_slavery.json", ipc_ch[17]['questions'][267:319]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t19_sexual_offences.json", ipc_ch[17]['questions'][319:387]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t20_theft_extortion_robbery_dacoity.json", ipc_ch[18]['questions'][0:117]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t21_criminal_misappropriation_and_breach_of_trust.json", ipc_ch[18]['questions'][117:168]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t22_cheating_mischief_criminal_trespass.json", ipc_ch[18]['questions'][168:221]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t23_forgery_documents_property_marks.json", ipc_ch[19]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t24_marriage_cruelty_defamation.json", ipc_ch[20]['questions']),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t25_criminal_intimidation_insult_attempt.json", ipc_ch[21]['questions'][0:43]),
    ("tests/judiciary_pyq/ipc/ipc_pyq_t26_important_cases_and_revision_questions.json", ipc_ch[21]['questions'][43:122])
]

ipc_tot = 0
for path, qs in ipc_mapping:
    cnt = update_test_file(path, qs, ipc_sub, ipc_sub_hi)
    ipc_tot += cnt
stats['ipc'] = ipc_tot
print(f"IPC rebuilt: 26 tests, {ipc_tot} questions.")

# 5. Constitution (24 tests)
print("\n--- Ingesting Constitution (24 tests) ---")
cst_ch = const_data['chapters']
cst_sub = "Indian Constitution"
cst_sub_hi = "भारतीय संविधान"

cst_mapping = [
    ("tests/judiciary_pyq/constitution/const_pyq_t01_historical_background.json", cst_ch[0]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t02_preamble.json", cst_ch[1]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t03_union_territories_and_citizenship.json", cst_ch[2]['questions'] + cst_ch[3]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t04_fundamental_rights_state_and_laws.json", cst_ch[4]['questions'][0:63]),
    ("tests/judiciary_pyq/constitution/const_pyq_t05_right_to_equality.json", cst_ch[4]['questions'][63:154]),
    ("tests/judiciary_pyq/constitution/const_pyq_t06_right_to_freedom_and_life.json", cst_ch[4]['questions'][154:284]),
    ("tests/judiciary_pyq/constitution/const_pyq_t07_exploitation_religion_cultural_rights.json", cst_ch[4]['questions'][284:324]),
    ("tests/judiciary_pyq/constitution/const_pyq_t08_constitutional_remedies.json", cst_ch[4]['questions'][324:387]),
    ("tests/judiciary_pyq/constitution/const_pyq_t09_directive_principles_of_state_policy.json", cst_ch[5]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t10_fundamental_duties.json", cst_ch[6]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t11_president_and_vice_president.json", cst_ch[7]['questions'][0:103]),
    ("tests/judiciary_pyq/constitution/const_pyq_t12_parliament.json", cst_ch[7]['questions'][103:179]),
    ("tests/judiciary_pyq/constitution/const_pyq_t13_union_judiciary_supreme_court_cag.json", cst_ch[7]['questions'][179:286]),
    ("tests/judiciary_pyq/constitution/const_pyq_t14_state_executive_and_legislature.json", cst_ch[8]['questions'][0:43]),
    ("tests/judiciary_pyq/constitution/const_pyq_t15_high_courts_and_subordinate_courts.json", cst_ch[8]['questions'][43:99]),
    ("tests/judiciary_pyq/constitution/const_pyq_t16_panchayats_municipalities_and_uts.json", cst_ch[9]['questions'] + cst_ch[10]['questions'] + cst_ch[11]['questions'] + cst_ch[12]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t17_relations_between_union_and_states.json", cst_ch[13]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t18_finance_property_contracts_trade.json", cst_ch[14]['questions'] + cst_ch[15]['questions'] + cst_ch[16]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t19_services_tribunals_and_elections.json", cst_ch[17]['questions'] + cst_ch[18]['questions'] + cst_ch[19]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t20_emergency_and_special_provisions.json", cst_ch[20]['questions'] + cst_ch[21]['questions'] + cst_ch[22]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t21_amendment_and_miscellaneous.json", cst_ch[23]['questions'] + cst_ch[24]['questions'] + cst_ch[25]['questions'] + cst_ch[26]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t22_schedules_of_constitution.json", cst_ch[27]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t23_landmark_and_recent_cases.json", cst_ch[28]['questions']),
    ("tests/judiciary_pyq/constitution/const_pyq_t24_miscellaneous_and_revision_questions.json", cst_ch[29]['questions'])
]

cst_tot = 0
for path, qs in cst_mapping:
    cnt = update_test_file(path, qs, cst_sub, cst_sub_hi)
    cst_tot += cnt
stats['constitution'] = cst_tot
print(f"Constitution rebuilt: 24 tests, {cst_tot} questions.")

# 6. UP Minor Acts (9 tests)
print("\n--- Ingesting UP Minor Acts (9 tests) ---")
ma_ch = minor_acts_data['chapters']
ma_sub = "UP Judiciary Minor Acts"
ma_sub_hi = "यूपी न्यायिक सेवा लघु अधिनियम"

ma_files = sorted(glob.glob(r'tests/judiciary_pyq/minor_acts/*.json'))
ma_tot = 0
for idx, fpath in enumerate(ma_files):
    qs = ma_ch[idx]['questions']
    cnt = update_test_file(fpath, qs, ma_sub, ma_sub_hi)
    ma_tot += cnt
stats['minor_acts'] = ma_tot
print(f"UP Minor Acts rebuilt: 9 tests, {ma_tot} questions.")

# 7. Tort (7 tests)
print("\n--- Ingesting Tort (7 tests) ---")
tl_ch = tort_lim_data['chapters']
tort_sub = "Law of Tort"
tort_sub_hi = "अपकृत्य विधि"

tort_mapping = [
    ("tests/judiciary_pyq/tort/tort_pyq_t01_definition_and_nature.json", tl_ch[0]['questions'] + tl_ch[1]['questions']),
    ("tests/judiciary_pyq/tort/tort_pyq_t02_vicarious_state_liability_and_joint.json", tl_ch[2]['questions'] + tl_ch[3]['questions'] + tl_ch[4]['questions']),
    ("tests/judiciary_pyq/tort/tort_pyq_t03_general_defences.json", tl_ch[5]['questions']),
    ("tests/judiciary_pyq/tort/tort_pyq_t04_negligence_nuisance_and_trespass.json", tl_ch[6]['questions'] + tl_ch[7]['questions'] + tl_ch[8]['questions']),
    ("tests/judiciary_pyq/tort/tort_pyq_t05_defamation.json", tl_ch[9]['questions']),
    ("tests/judiciary_pyq/tort/tort_pyq_t06_strict_liability_malicious_prosecution_remedies.json", tl_ch[10]['questions'] + tl_ch[11]['questions'] + tl_ch[12]['questions']),
    ("tests/judiciary_pyq/tort/tort_pyq_t07_miscellaneous_and_landmark_cases.json", tl_ch[13]['questions'])
]

tort_tot = 0
for path, qs in tort_mapping:
    cnt = update_test_file(path, qs, tort_sub, tort_sub_hi)
    tort_tot += cnt
stats['tort'] = tort_tot
print(f"Tort rebuilt: 7 tests, {tort_tot} questions.")

# 8. Limitation (2 tests)
print("\n--- Ingesting Limitation (2 tests) ---")
lim_sub = "Limitation Act, 1963"
lim_sub_hi = "परिसीमा अधिनियम, 1963"
lim_ch = tl_ch[14]['questions']

lim_mapping = [
    ("tests/judiciary_pyq/limitation/limitation_pyq_t01_limitation_of_suits_and_appeals.json", lim_ch[0:74]),
    ("tests/judiciary_pyq/limitation/limitation_pyq_t02_computation_acknowledgment_and_schedule.json", lim_ch[74:156])
]

lim_tot = 0
for path, qs in lim_mapping:
    cnt = update_test_file(path, qs, lim_sub, lim_sub_hi)
    lim_tot += cnt
stats['limitation'] = lim_tot
print(f"Limitation rebuilt: 2 tests, {lim_tot} questions.")

# 9. SRA (2 tests)
print("\n--- Ingesting SRA (2 tests) ---")
sra_sub = "Specific Relief Act, 1963"
sra_sub_hi = "विनिर्दिष्ट अनुतोष अधिनियम, 1963"
sra_ch = tl_ch[15]['questions']

sra_mapping = [
    ("tests/judiciary_pyq/sra/sra_pyq_t01_possession_and_specific_performance.json", sra_ch[0:76]),
    ("tests/judiciary_pyq/sra/sra_pyq_t02_rectification_declaratory_injunctions.json", sra_ch[76:146])
]

sra_tot = 0
for path, qs in sra_mapping:
    cnt = update_test_file(path, qs, sra_sub, sra_sub_hi)
    sra_tot += cnt
stats['sra'] = sra_tot
print(f"SRA rebuilt: 2 tests, {sra_tot} questions.")

# 10. Trust & Equity (1 test)
print("\n--- Ingesting Trust & Equity (1 test) ---")
te_sub = "Law of Trust & Equity"
te_sub_hi = "न्यास एवं साम्य विधि"
te_qs = tl_ch[16]['questions'] + tl_ch[17]['questions']

cnt = update_test_file("tests/judiciary_pyq/trust_equity/trust_equity_pyq_t01_equity_and_trusts.json", te_qs, te_sub, te_sub_hi)
stats['trust_equity'] = cnt
print(f"Trust & Equity rebuilt: 1 test, {cnt} questions.")

# 11. TPA (8 tests)
print("\n--- Ingesting TPA (8 tests) ---")
tpa_ch = tpa_contract_data['chapters']
tpa_sub = "Transfer of Property Act, 1882"
tpa_sub_hi = "सम्पत्ति अन्तरण अधिनियम, 1882"

tpa_mapping = [
    ("tests/judiciary_pyq/tpa/tpa_pyq_t01_preliminary.json", tpa_ch[0]['questions']),
    ("tests/judiciary_pyq/tpa/tpa_pyq_t02_transfer_unborn_and_perpetuity.json", tpa_ch[1]['questions'][0:91]),
    ("tests/judiciary_pyq/tpa/tpa_pyq_t03_vested_contingent_and_election.json", tpa_ch[1]['questions'][91:158]),
    ("tests/judiciary_pyq/tpa/tpa_pyq_t04_ostensible_owner_lis_pendens_part_performance.json", tpa_ch[1]['questions'][158:234]),
    ("tests/judiciary_pyq/tpa/tpa_pyq_t05_sale_of_immovable_property.json", tpa_ch[2]['questions']),
    ("tests/judiciary_pyq/tpa/tpa_pyq_t06_mortgages_and_charges.json", tpa_ch[3]['questions']),
    ("tests/judiciary_pyq/tpa/tpa_pyq_t07_leases_of_immovable_property.json", tpa_ch[4]['questions']),
    ("tests/judiciary_pyq/tpa/tpa_pyq_t08_exchanges_gifts_and_actionable_claims.json", tpa_ch[5]['questions'] + tpa_ch[6]['questions'] + tpa_ch[7]['questions'] + tpa_ch[8]['questions'])
]

tpa_tot = 0
for path, qs in tpa_mapping:
    cnt = update_test_file(path, qs, tpa_sub, tpa_sub_hi)
    tpa_tot += cnt
stats['tpa'] = tpa_tot
print(f"TPA rebuilt: 8 tests, {tpa_tot} questions.")

# 12. Contract (11 tests)
print("\n--- Ingesting Contract Act (11 tests) ---")
con_ch = tpa_contract_data['chapters']
con_sub = "Indian Contract Act, 1872"
con_sub_hi = "भारतीय संविदा अधिनियम, 1872"

con_part2 = con_ch[11]['questions'] + con_ch[12]['questions']
con_mapping = [
    ("tests/judiciary_pyq/contract/contract_pyq_t01_preliminary_and_definitions.json", con_ch[9]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t02_communication_acceptance_revocation.json", con_ch[10]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t03_capacity_and_free_consent.json", con_part2[0:141]),
    ("tests/judiciary_pyq/contract/contract_pyq_t04_void_agreements_and_contingent.json", con_part2[141:285]),
    ("tests/judiciary_pyq/contract/contract_pyq_t05_performance_and_discharge.json", con_ch[13]['questions'] + con_ch[14]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t06_quasi_contracts.json", con_ch[15]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t07_breach_and_damages.json", con_ch[16]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t08_indemnity_and_guarantee.json", con_ch[17]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t09_bailment_and_pledge.json", con_ch[18]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t10_agency.json", con_ch[19]['questions']),
    ("tests/judiciary_pyq/contract/contract_pyq_t11_miscellaneous_and_revision.json", con_ch[20]['questions'])
]

con_tot = 0
for path, qs in con_mapping:
    cnt = update_test_file(path, qs, con_sub, con_sub_hi)
    con_tot += cnt
stats['contract'] = con_tot
print(f"Contract rebuilt: 11 tests, {con_tot} questions.")

# 13. Jurisprudence (8 tests)
print("\n--- Ingesting Jurisprudence (8 tests) ---")
j_ch = juris_data['chapters']
j_sub = "Jurisprudence"
j_sub_hi = "विधिशास्त्र"

j_mapping = [
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t01_definition_and_scope.json", j_ch[0]['questions']),
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t02_natural_law_and_analytical_school.json", j_ch[1]['questions'] + j_ch[2]['questions']),
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t03_historical_sociological_realist_schools.json", j_ch[3]['questions'] + j_ch[4]['questions'] + j_ch[5]['questions'] + j_ch[6]['questions']),
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t04_sources_of_law_custom_precedent_legislation.json", j_ch[7]['questions']),
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t05_jural_concepts_rights_and_duties.json", j_ch[8]['questions']),
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t06_possession_and_ownership.json", j_ch[9]['questions'] + j_ch[10]['questions']),
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t07_person_property_and_liability.json", j_ch[11]['questions'] + j_ch[12]['questions'] + j_ch[13]['questions']),
    ("tests/judiciary_pyq/jurisprudence/juris_pyq_t08_miscellaneous_and_practice_questions.json", j_ch[14]['questions'])
]

j_tot = 0
for path, qs in j_mapping:
    cnt = update_test_file(path, qs, j_sub, j_sub_hi)
    j_tot += cnt
stats['jurisprudence'] = j_tot
print(f"Jurisprudence rebuilt: 8 tests, {j_tot} questions.")

# 14. International Organization (7 tests)
print("\n--- Ingesting International Organization (7 tests) ---")
io_sub = "International Organization"
io_sub_hi = "अन्तर्राष्ट्रीय संगठन"

io_mapping = [
    ("tests/judiciary_pyq/international_org/int_org_pyq_t01_un_charter_and_principles.json", j_ch[15]['questions']),
    ("tests/judiciary_pyq/international_org/int_org_pyq_t02_general_assembly.json", j_ch[16]['questions']),
    ("tests/judiciary_pyq/international_org/int_org_pyq_t03_security_council.json", j_ch[17]['questions']),
    ("tests/judiciary_pyq/international_org/int_org_pyq_t04_ecosoc_trusteeship_secretariat.json", j_ch[18]['questions'] + j_ch[19]['questions']),
    ("tests/judiciary_pyq/international_org/int_org_pyq_t05_international_court_of_justice.json", j_ch[20]['questions']),
    ("tests/judiciary_pyq/international_org/int_org_pyq_t06_secretariat_and_specialized_agencies.json", j_ch[21]['questions'] + j_ch[22]['questions']),
    ("tests/judiciary_pyq/international_org/int_org_pyq_t07_current_international_affairs.json", j_ch[23]['questions'])
]

io_tot = 0
for path, qs in io_mapping:
    cnt = update_test_file(path, qs, io_sub, io_sub_hi)
    io_tot += cnt
stats['international_org'] = io_tot
print(f"International Org rebuilt: 7 tests, {io_tot} questions.")

save_cache()

grand_total = sum(stats.values())
print("\n==========================================")
print(f"INGESTION COMPLETE!")
print(f"Total Tests Rebuilt: 181")
print(f"Total Questions Ingested: {grand_total}")
for k, v in stats.items():
    print(f"  {k:20s}: {v} Qs")
print("==========================================")
