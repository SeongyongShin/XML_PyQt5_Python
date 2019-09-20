def findXslt(str_name):
    print(str_name)
    if str_name == "[건보]자격득실확인서":
        return "xslt_nhis_ja"
    elif str_name == "[건보]납부확인서":
        return "xslt_nhis_nabbu"
    elif str_name == "[건보]완납확인서":
        return "xslt_nhis_wannab"
    # elif (str_name == "[건보]건강검진이력"):
    #     return ""
    elif str_name == "[건보]진료이력":
        return "xslt_nhis_jinryo"
    elif str_name == "[건보]자격확인서":
        return "xslt_nhis_jh"
    elif str_name == "[민원]주민등록초본":
        return "xslt_mw24_c"
    elif str_name == "[민원]주민등록등본":
        return "xslt_mw24_d"
    elif str_name == "[민원]지방세납세증명":
        return "xslt_mw24_jibangse"
    elif str_name == "[정부]주민등록초본":
        return "xslt_mw24_d"
    elif str_name == "[정부]주민등록등본":
        return "xslt_mw24_d"
    # elif (str_name == "[정부]출입국사실증명"):
    #     return ""
    # elif (str_name == "[정부]외국인등록 사실증명"):
    #     return ""
    # elif (str_name == "[정부]외국인국내거소 사실증명"):
    #     return ""
    elif str_name == "[정부]지방세납세증명":
        return "xslt_mw24_jibangse"
    elif str_name == "[국세청]소득금액증명(봉급생활자)":
        return "xslt_nts_s_J"
    # elif (str_name == "[국세청]소득금액증명(사업자)"):
    #     return ""
    elif str_name == "[국세청]소득금액증명(종합소득)":
        return "xslt_nts_s_b"
    elif str_name == "[국세청]사업자등록증명원":
        return "xslt_nts_saupja"
    # elif (str_name == "[국세청]부가가치세 과세표준증명"):
    #     return ""
    # elif (str_name == "[국세청]부가가치세 면세사업자 수입금액증명"):
    #     return ""
    # elif (str_name == "[국세청]납세증명서"):
    #     return ""
    # elif (str_name == "[국세청]연말정산 원천징수영수증"):
    #     return ""
    elif str_name == "[국세청]소득세액공제":
        return "xslt_nts_gongje"
    elif str_name == "[국세청]폐업사실증명":
        return "xslt_nts_pieup"
    elif str_name == "[국세청]사업장리스트":
        return "xslt_nts_saupjanglist"
    # elif (str_name == "[국세청]소득확인증명서"):
    #     return ""
    # elif (str_name == "[국세청]납세내역증명서"):
    #     return ""
    elif str_name == "[대법원]기본증명서":
        return "xslt_scf_gibon"
    elif str_name == "[대법원]가족관계증명서":
        return "xslt_scf_gajok"
    elif str_name == "[대법원]혼인관계증명서":
        return "xslt_scf_honin"
    elif str_name == "[대법원]제적초본":
        return "xslt_scj_c"
    elif str_name == "[대법원]제적등본":
        return "xslt_scj_d"
    elif str_name == "4대보험 가입내역":
        return "xslt_4insu"
    elif str_name == "자동차 보험 가입 이력":
        return "xslt_aipis_reqrefund"
    elif str_name == "자동사고이력조회":
        return "xslt_ch_carhistory"
    elif str_name == "[손해보험]내보험찾아줌":
        return "xslt_conti_insusearch"
    elif str_name == "자동차등록원부":
        return "xslt_ecar"
    elif str_name == "운전경력증명서":
        return "xslt_efine_licensecareer"
    elif str_name == "BIDV":
        return "xslt_bidv"
    elif str_name == "개인범죄경력확인서":
        return "xslt_crime_search"
    elif str_name == "[국민연금] 연금지급내역증명서":
        return "xslt_kmeg_jigeup"
    elif str_name == "[연금포털] 내연금찾기":
        return "xslt_findmypension"
    elif str_name == "테스트":
        return ""

    return ""


def itemList():
    return ['테스트', '[건보]자격득실확인서', '[건보]납부확인서', '[건보]완납확인서', '![건보]건강검진이력', '[건보]진료이력', '[건보]자격확인서'
        , '[민원]주민등록초본', '[민원]주민등록등본', '[민원]지방세납세증명'
        , '[정부]주민등록초본', '[정부]주민등록등본', '![정부]출입국사실증명', '![정부]외국인등록 사실증명', '![정부]외국인국내거소 사실증명', '![정부]지방세납세증명'
        , '[국세청]소득금액증명(봉급생활자)', '![국세청]소득금액증명(사업자)', '[국세청]소득금액증명(종합소득)', '[국세청]사업자등록증명원'
        , '![국세청]부가가치세 과세표준증명', '![국세청]부가가치세 면세사업자 수입금액증명', '![국세청]납세증명서', '![국세청]연말정산 원천징수영수증'
        , '[국세청]소득세액공제', '[국세청]폐업사실증명', '[국세청]사업장리스트', '![국세청]소득확인증명서', '![국세청]납세내역증명서'
        , '[대법원]기본증명서', '[대법원]가족관계증명서', '[대법원]혼인관계증명서', '[대법원]제적초본', '[대법원]제적등본'
        , '4대보험 가입내역', '자동차 보험 가입 이력', '자동사고이력조회', '[손해보험]내보험찾아줌', '자동차등록원부', '운전경력증명서', 'BIDV', '개인범죄경력확인서','[국민연금] 연금지급내역증명서'
        , '[연금포털] 내연금찾기'

            ];