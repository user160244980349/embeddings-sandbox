from pprint import pprint

_ID = -1


def first_party_scenario(onto, r, pi, fp, u):
    evidence = None
    data_collection = None
    data_use = None
    purpose = None
    mechanism = None
    identifiability = None
    mode = None
    data = None

    if r["attributes"]["Choice Scope"]["value"] == "Collection" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        data_collection = onto.DataCollectionActivity()

    if r["attributes"]["Choice Scope"]["value"] == "Use" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        data_use = onto.DataUseActivity()

    # Purpose
    if r["attributes"]["Purpose"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Purpose"].keys():
        purpose_e = onto.Evidence()
        purpose_e.evidenceContent = r["attributes"]["Purpose"][
            "selectedText"]

        purpose = onto.DataActivityPurpose()
        purpose.hasEvidence.append(purpose_e)

    # Mechanism
    if r["attributes"]["Action First-Party"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Action First-Party"].keys():
        mechanism_e = onto.Evidence()
        mechanism_e.evidenceContent = r["attributes"]["Action First-Party"][
            "selectedText"]

        mechanism = onto.DataCollectionMechanism()
        mechanism.hasEvidence.append(mechanism_e)

    # Mode
    if r["attributes"]["Collection Mode"]["value"] != "Unspecified" \
            and "selectedText" in r["attributes"]["Collection Mode"].keys() \
            and mechanism:
        mode_e = onto.Evidence()
        mode_e.evidenceContent = r["attributes"]["Collection Mode"]["selectedText"]

        mode = onto.DataCollectionMode()
        mode.hasEvidence.append(mode_e)

        mechanism.hasMode.append(mode)

    # Identifiability
    if r["attributes"]["Identifiability"]["value"] != "Unspecified" \
            and r["attributes"]["Identifiability"]["value"] != "not-selected" \
            and "selectedText" in r["attributes"]["Identifiability"].keys():
        identifiability_e = onto.Evidence()
        identifiability_e.evidenceContent = r["attributes"]["Identifiability"][
            "selectedText"]

        identifiability = onto.PseudoAnonymization()
        identifiability.hasEvidence.append(identifiability_e)

    # Data
    if r["attributes"]["Personal Information Type"]["value"] != "Unspecified" \
            and "selectedText" in r["attributes"]["Personal Information Type"].keys() \
            and (data_use or data_collection):

        if r["attributes"]["Personal Information Type"]["value"] == "Health":
            data = onto.HealthData()

        if r["attributes"]["Personal Information Type"]["value"] == "Unspecified":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Cookies and tracking elements":
            data = onto.TrackingData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Personal identifier":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "IP address and device IDs":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Financial":
            data = onto.FinancialData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "User online activities":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"]["value"] == "User profile":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Contact":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Other":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Computer information":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Survey data":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Generic personal information":
            data = onto.GenericData()

        if r["attributes"]["Personal Information Type"]["value"] == "Demographic":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Social media data":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Location":
            data = onto.TrackingData()

        if data:
            data_e = onto.Evidence()
            data_e.evidenceContent = r["attributes"]["Personal Information Type"][
                "selectedText"]

            data.hasEvidence.append(data_e)

            pi.considersData.append(data)
            u.ownsData.append(data)

    if data_use or data_collection:
        evidence = onto.Evidence()
        evidence.evidenceContent = r["segment_text"]

    if data_use:
        pi.considersActivity.append(data_use)
        fp.initiatesActivity.append(data_use)
        if purpose:
            data_use.hasDataActivityPurpose.append(purpose)
        if mechanism:
            data_use.hasDataCollectionMechanism.append(mechanism)
        if identifiability:
            data_use.hasDataCollectionMechanism.append(identifiability)
        if data:
            data_use.isAppliedToData.append(data)
        data_use.hasEvidence.append(evidence)

    if data_collection:
        pi.considersActivity.append(data_collection)
        fp.initiatesActivity.append(data_collection)
        if purpose:
            data_collection.hasDataActivityPurpose.append(purpose)
        if mechanism:
            data_collection.hasDataCollectionMechanism.append(mechanism)
        if identifiability:
            data_collection.hasDataCollectionMechanism.append(identifiability)
        if data:
            data_collection.isAppliedToData.append(data)
        data_collection.hasEvidence.append(evidence)
        data_collection.collectsDataFromAgent.append(u)


def third_party_scenario(onto, r, pi, fp, tp, u):
    evidence = None
    data_collection = None
    data_sharing = None
    purpose = None
    mechanism = None
    identifiability = None
    mode = None
    data = None

    if r["attributes"]["Choice Scope"]["value"] == "Collection" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        data_collection = onto.DataCollectionActivity()

    if r["attributes"]["Choice Scope"]["value"] == "Sharing" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        data_sharing = onto.DataSharingActivity()

    # Purpose
    if r["attributes"]["Purpose"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Purpose"].keys():
        purpose_e = onto.Evidence()
        purpose_e.evidenceContent = r["attributes"]["Purpose"][
            "selectedText"]

        purpose = onto.DataActivityPurpose()
        purpose.hasEvidence.append(purpose_e)

    # Mechanism
    if r["attributes"]["Action Third Party"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Action Third Party"].keys():
        mechanism_e = onto.Evidence()
        mechanism_e.evidenceContent = r["attributes"]["Action Third Party"][
            "selectedText"]

        mechanism = onto.DataCollectionMechanism()
        mechanism.hasEvidence.append(mechanism_e)

    # Mode
    if r["attributes"]["Choice Scope"]["value"] != "Unspecified" \
            and "selectedText" in r["attributes"]["Choice Scope"].keys() \
            and mechanism:
        mode_e = onto.Evidence()
        mode_e.evidenceContent = r["attributes"]["Choice Scope"]["selectedText"]

        mode = onto.DataCollectionMode()
        mode.hasEvidence.append(mode_e)

        mechanism.hasMode.append(mode)

    # Identifiability
    if r["attributes"]["Identifiability"]["value"] != "Unspecified" \
            and r["attributes"]["Identifiability"]["value"] != "not-selected" \
            and "selectedText" in r["attributes"]["Identifiability"].keys():
        identifiability_e = onto.Evidence()
        identifiability_e.evidenceContent = r["attributes"]["Identifiability"][
            "selectedText"]

        identifiability = onto.PseudoAnonymization()
        identifiability.hasEvidence.append(identifiability_e)

    # Data
    if r["attributes"]["Personal Information Type"]["value"] != "Unspecified" \
            and "selectedText" in r["attributes"]["Personal Information Type"].keys() \
            and (data_sharing or data_collection):

        if r["attributes"]["Personal Information Type"]["value"] == "Health":
            data = onto.HealthData()

        if r["attributes"]["Personal Information Type"]["value"] == "Unspecified":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Cookies and tracking elements":
            data = onto.TrackingData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Personal identifier":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "IP address and device IDs":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Financial":
            data = onto.FinancialData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "User online activities":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"]["value"] == "User profile":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Contact":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Other":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Computer information":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Survey data":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Generic personal information":
            data = onto.GenericData()

        if r["attributes"]["Personal Information Type"]["value"] == "Demographic":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Social media data":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Location":
            data = onto.TrackingData()

        if data:
            data_e = onto.Evidence()
            data_e.evidenceContent = r["attributes"]["Personal Information Type"][
                "selectedText"]

            data.hasEvidence.append(data_e)

            pi.considersData.append(data)
            u.ownsData.append(data)

    if data_sharing or data_collection:
        evidence = onto.Evidence()
        evidence.evidenceContent = r["segment_text"]

    if data_sharing:
        pi.considersActivity.append(data_sharing)
        fp.initiatesActivity.append(data_sharing)
        if purpose:
            data_sharing.hasDataActivityPurpose.append(purpose)
        if mechanism:
            data_sharing.hasDataCollectionMechanism.append(mechanism)
        if identifiability:
            data_sharing.hasDataCollectionMechanism.append(identifiability)
        if data:
            data_sharing.isAppliedToData.append(data)
        data_sharing.hasEvidence.append(evidence)
        data_sharing.sharesDataWithAgent.append(tp)

    if data_collection:
        pi.considersActivity.append(data_collection)
        fp.initiatesActivity.append(data_collection)
        if purpose:
            data_collection.hasDataActivityPurpose.append(purpose)
        if mechanism:
            data_collection.hasDataCollectionMechanism.append(mechanism)
        if identifiability:
            data_collection.hasDataCollectionMechanism.append(identifiability)
        if data:
            data_collection.isAppliedToData.append(data)
        data_collection.hasEvidence.append(evidence)
        data_collection.collectsDataFromAgent.append(tp)


def user_choice_and_control(onto, r, pi, u):
    purpose = None
    mechanism = None
    data = None

    choice_and_control = onto.UserPrivacyControl()

    # Purpose
    if r["attributes"]["Purpose"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Purpose"].keys():
        purpose_e = onto.Evidence()
        purpose_e.evidenceContent = r["attributes"]["Purpose"][
            "selectedText"]

        purpose = onto.Purpose()
        purpose.hasEvidence.append(purpose_e)

    # Mechanism
    if r["attributes"]["Choice Type"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Choice Type"].keys():
        mechanism_e = onto.Evidence()
        mechanism_e.evidenceContent = r["attributes"]["Choice Type"][
            "selectedText"]

        mechanism = onto.DataControlMechanism()
        mechanism.hasEvidence.append(mechanism_e)

    # Data
    if r["attributes"]["Personal Information Type"]["value"] != "Unspecified" \
            and "selectedText" in r["attributes"]["Personal Information Type"].keys():

        if r["attributes"]["Personal Information Type"]["value"] == "Health":
            data = onto.HealthData()

        if r["attributes"]["Personal Information Type"]["value"] == "Unspecified":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Cookies and tracking elements":
            data = onto.TrackingData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Personal identifier":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "IP address and device IDs":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Financial":
            data = onto.FinancialData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "User online activities":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"]["value"] == "User profile":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Contact":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Other":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Computer information":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Survey data":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Generic personal information":
            data = onto.GenericData()

        if r["attributes"]["Personal Information Type"]["value"] == "Demographic":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Social media data":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Location":
            data = onto.TrackingData()

        if data:
            data_e = onto.Evidence()
            data_e.evidenceContent = r["attributes"]["Personal Information Type"][
                "selectedText"]

            data.hasEvidence.append(data_e)

            pi.considersData.append(data)
            u.ownsData.append(data)

    evidence = onto.Evidence()
    evidence.evidenceContent = r["segment_text"]

    pi.considersActivity.append(choice_and_control)
    u.initiatesActivity.append(choice_and_control)
    if purpose:
        choice_and_control.has.append(purpose)
    if mechanism:
        choice_and_control.hasPrivacyControlMechanism.append(mechanism)
    if data:
        choice_and_control.isAppliedToData.append(data)
    choice_and_control.hasEvidence.append(evidence)


def data_retention(onto, r, pi, fp, u):
    purpose = None
    period = None
    data = None

    retention = onto.DataRetentionActivity()

    # Purpose
    if r["attributes"]["Retention Purpose"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        purpose_e = onto.Evidence()
        purpose_e.evidenceContent = r["attributes"]["Retention Purpose"][
            "selectedText"]

        purpose = onto.DataActivityPurpose()
        purpose.hasEvidence.append(purpose_e)

    # Retention Period
    if r["attributes"]["Retention Period"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Retention Period"].keys():
        period_e = onto.Evidence()
        period_e.evidenceContent = r["attributes"]["Retention Period"][
            "selectedText"]

        period = onto.DataRetentionTime()
        period.hasEvidence.append(period_e)

    # Data
    if r["attributes"]["Personal Information Type"]["value"] != "Unspecified" \
            and "selectedText" in r["attributes"]["Personal Information Type"].keys():

        if r["attributes"]["Personal Information Type"]["value"] == "Health":
            data = onto.HealthData()

        if r["attributes"]["Personal Information Type"]["value"] == "Unspecified":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Cookies and tracking elements":
            data = onto.TrackingData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Personal identifier":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "IP address and device IDs":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Financial":
            data = onto.FinancialData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "User online activities":
            data = onto.AccountData()

        if r["attributes"]["Personal Information Type"]["value"] == "User profile":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Contact":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Other":
            data = onto.Data()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Computer information":
            data = onto.DeviceData()

        if r["attributes"]["Personal Information Type"]["value"] == "Survey data":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"][
            "value"] == "Generic personal information":
            data = onto.GenericData()

        if r["attributes"]["Personal Information Type"]["value"] == "Demographic":
            data = onto.SensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Social media data":
            data = onto.NonSensitiveData()

        if r["attributes"]["Personal Information Type"]["value"] == "Location":
            data = onto.TrackingData()

        if data:
            data_e = onto.Evidence()
            data_e.evidenceContent = r["attributes"]["Personal Information Type"][
                "selectedText"]

            data.hasEvidence.append(data_e)

            pi.considersData.append(data)
            u.ownsData.append(data)

    evidence = onto.Evidence()
    evidence.evidenceContent = r["segment_text"]

    pi.considersActivity.append(retention)
    fp.initiatesActivity.append(retention)
    if purpose:
        retention.hasDataActivityPurpose.append(purpose)
    if period:
        retention.hasDataRetentionTime.append(period)
    if data:
        retention.isAppliedToData.append(data)
    retention.hasEvidence.append(evidence)


def user_access(onto, r, pi, u):
    data = None

    evidence = onto.Evidence()
    evidence.evidenceContent = r["segment_text"]

    access = onto.UserAccessActivity()
    access.hasEvidence.append(evidence)
    pi.considersActivity.append(access)
    u.initiatesActivity.append(access)

    # Mechanism
    if r["attributes"]["Access Type"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Access Type"].keys():
        mechanism_e = onto.Evidence()
        mechanism_e.evidenceContent = r["attributes"]["Access Type"][
            "selectedText"]

        mechanism = onto.DataControlMechanism()
        mechanism.hasEvidence.append(mechanism_e)

    # Data
    if r["attributes"]["Access Scope"]["value"] != "Unspecified" \
            and "selectedText" in r["attributes"]["Access Scope"].keys():

        if r["attributes"]["Access Scope"]["value"] == "User account data":
            data = onto.AccountData()

        if r["attributes"]["Access Scope"]["value"] == "Other data about user":
            data = onto.NonSensitiveData()

        if r["attributes"]["Access Scope"]["value"] == "Profile data":
            data = onto.SensitiveData()

        if r["attributes"]["Access Scope"]["value"] == "Transactional data":
            data = onto.FinancialData()

    if data:
        data.hasEvidence.append(evidence)
        pi.considersData.append(data)
        access.isAppliedTo.append(data)


def do_not_track(onto, r, pi, u):
    opt = onto.UserOptControl()
    pi.considersActivity.append(opt)
    u.initiatesActivity.append(opt)

    evidence = onto.Evidence()
    evidence.evidenceContent = r["segment_text"]
    opt.hasEvidence.append(evidence)


def international_and_specific_audience(onto, r, u):
    category = onto.UserSpecialCategory()
    u.hasSpecialCategory.append(category)

    evidence = onto.Evidence()
    evidence.evidenceContent = r["segment_text"]
    category.hasEvidence.append(evidence)


def data_security(onto, r, pi, fp):
    mechanism = None

    # Mechanism
    if r["attributes"]["Security Measure"]["value"] != "Unspecified":
        if r["attributes"]["Security Measure"]["value"] == "Data access limitation":
            mechanism = onto.TechnicalMeasure()

        if r["attributes"]["Security Measure"]["value"] == "Generic":
            mechanism = onto.TechnicalMeasure()

        if r["attributes"]["Security Measure"]["value"] == "Secure user authentication":
            mechanism = onto.TechnicalMeasure()

        if r["attributes"]["Security Measure"]["value"] == "Secure data storage":
            mechanism = onto.Encryption()

        if r["attributes"]["Security Measure"]["value"] == "Other":
            mechanism = onto.SecurityMechanism()

        if r["attributes"]["Security Measure"]["value"] == "Privacy review/audit":
            mechanism = onto.OrganizationalMeasure()

        if r["attributes"]["Security Measure"]["value"] == "Privacy/Security program":
            mechanism = onto.TechnicalMeasure()

        if r["attributes"]["Security Measure"]["value"] == "Secure data transfer":
            mechanism = onto.Encryption()

        if r["attributes"]["Security Measure"]["value"] == "Privacy training":
            mechanism = onto.OrganizationalMeasure()

        mechanism_e = onto.Evidence()
        mechanism_e.evidenceContent = r["segment_text"]
        mechanism.hasEvidence.append(mechanism_e)

    if mechanism:
        activity = onto.Activity()
        pi.considersActivity.append(activity)
        activity.hasMechanism.append(mechanism)
        fp.initiatesActivity.append(activity)


def policy_change(onto, r, pi, fp):
    mechanism = None
    cause = None
    change = onto.PolicyChangeActivity()

    pi.considersActivity.append(change)
    fp.initiatesActivity.append(change)

    change_e = onto.Evidence()
    change_e.evidenceContent = r["segment_text"]
    change.hasEvidence.append(change_e)

    # Mechanism
    if r["attributes"]["Notification Type"]["value"] == "Personal notice":
        mechanism = onto.NotificationMechanism()

    if r["attributes"]["Notification Type"]["value"] == "General notice on website":
        mechanism = onto.OnWebsitePage()

    if r["attributes"]["Notification Type"]["value"] == "General notice in privacy policy":
        mechanism = onto.InPrivacyPolicy()

    if r["attributes"]["Notification Type"]["value"] == "Other":
        mechanism = onto.NotificationMechanism()

    if mechanism:
        mechanism.hasEvidence.append(change_e)
        change.hasMechanism.append(mechanism)

    if cause:
        if r["attributes"]["User Choice"]["value"] != "Unspecified" \
                and "selectedText" in r["attributes"]["User Choice"].keys():

            # Cause
            if r["attributes"]["Change Type"]["value"] == "Privacy relevant change":
                cause = onto.PrivacyRelatedCause()

            if r["attributes"]["Change Type"]["value"] == "Non-privacy relevant change":
                cause = onto.NonPrivacyRelatedCause()

            if r["attributes"]["Change Type"][
                "value"] == "In case of merger or acquisition":
                cause = onto.MergeAcquisitionCause()

            if r["attributes"]["Change Type"]["value"] == "Other":
                cause = onto.OtherPolicyChangeCause()

            cause_e = onto.Evidence()
            cause_e.evidenceContent = r["attributes"]["User Choice"]["selectedText"]
            cause.hasEvidence.append(cause_e)
            change.hasPolicyChangeCause.append(cause)


def process_opp(onto, policy):
    """
    Constructing ontology
        onto = construct_ontology()

    Making individuals
        i1 = onto.PrivacyPolicy()
        i2 = onto.Data()
        i3 = onto.DataProtectionOfficer()

    DataProperty assertion]
        i4 = onto.Evidence()
        i4.evidenceContent = "text"

    ObjectProperty assertion
        i2.hasEvidence = [i4]
        i1.considersData.append(i2)

    Finishing work
        finish(onto)

    mappings = {
        "First Party Collection/Use": "DataCollectionActivity",
        "Third Party Sharing/Collection": "DataSharingActivity",
        "User Choice/Control": "ConsentActivity",
        "User Access, Edit and Deletion": "UserAccessActivity",
        "Data Retention": "DataRetentionActivity",
        "Data Security": "SecurityMechanism",
        "Policy Change": "PolicyChangeActivity",
        "Do Not Track": "UserOptActivity",
        "International and Specific Audiences": "UserSpecialCategory",
    }

    Data Security is needed to be connected with all activities

    Notions:
        Write migration scheme for each category of OPP-115
        Data Security goes in the end and is connected to all activities
        Three of actors are mandatory and unique FP, TP, and User
    """
    global _ID
    _ID += 1

    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyId = int(policy["id"])
    policy_instance.policyWebsite = policy["name"]
    policy_instance.considersAgent.extend([user, first_party, third_party])

    for a in policy["annotations"]:
        if a["category"] == "Other":
            continue

        if a["category"] == "First Party Collection/Use":
            first_party_scenario(onto, a, policy_instance, first_party, user)

        if a["category"] == "Third Party Sharing/Collection":
            third_party_scenario(onto, a, policy_instance, first_party, third_party,
                                 user)

        if a["category"] == "User Choice/Control":
            user_choice_and_control(onto, a, policy_instance, user)

        if a["category"] == "Data Retention":
            data_retention(onto, a, policy_instance, first_party, user)

        if a["category"] == "User Access, Edit and Deletion":
            user_access(onto, a, policy_instance, user)

        if a["category"] == "Do Not Track":
            do_not_track(onto, a, policy_instance, user)

        if a["category"] == "International and Specific Audiences":
            international_and_specific_audience(onto, a, user)

        if a["category"] == "Data Security":
            data_security(onto, a, policy_instance, first_party)

        if a["category"] == "Policy Change":
            policy_change(onto, a, policy_instance, first_party)

    return onto
