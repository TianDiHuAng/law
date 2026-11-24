# -*- coding: utf-8 -*-
"""R54 升级为 L2 的法律文本导读条目。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R54 = {
    "law-cpc": dict(
        definition_source="《中华人民共和国刑事诉讼法》（版本：2018年10月26日修正，核对日期：2026-11-24）。",
        elements=["总则（任务与基本原则）", "立案、侦查与提起公诉", "审判（一审、二审、死刑复核、审判监督）", "执行", "特别程序"],
        conditions=["有犯罪事实需要追究刑事责任", "依法定管辖与程序推进", "保障诉讼参与人权利"],
        effects=["国家追诉犯罪并保障人权", "生效裁判进入执行", "违法程序可能导致证据排除或程序回转"],
        exceptions=["不立案、撤案、不起诉可终止程序", "特别程序（如缺席审判、速裁）另有规定"],
        cases=[],
        controversies=[dict(issue="以审判为中心与侦查中心",
                            views=[dict(holder="审判中心说（改革方向）", basis="庭审实质化，证据裁判在法庭形成"),
                                   dict(holder="侦查基础说（部分实务观点）", basis="侦查质量决定案件质量")])],
        distinctions=[D("刑事诉讼法", "追诉犯罪的程序法"), D("刑法", "规定犯罪与刑罚的实体法")],
        misconceptions=[dict(claim="立案就意味着有罪", correction="立案仅启动程序，是否有罪由法院判决"),
                        dict(claim="口供是定案的关键", correction="不得强迫自证其罪，应重证据、不轻信口供")],
    ),
    "law-civil-procedure": dict(
        definition_source="《中华人民共和国民事诉讼法》（版本：2023年9月1日修正，核对日期：2026-11-24）。",
        elements=["总则与管辖", "审判组织与回避", "证据", "保全与先予执行", "第一审普通程序与简易程序", "第二审程序", "特别程序", "执行程序"],
        conditions=["当事人适格", "属于法院主管与管辖", "依法起诉与应诉"],
        effects=["法院依法审理并作出裁判", "生效裁判具有既判力与执行力", "当事人享有上诉与申请再审权利"],
        exceptions=["仲裁协议排除法院管辖", "依法应当先行调解或适用特别程序的除外"],
        cases=[],
        controversies=[dict(issue="职权探知与当事人处分权的边界",
                            views=[dict(holder="当事人主义说", basis="民事诉讼以当事人处分与举证为主导"),
                                   dict(holder="职权干预说（部分观点）", basis="涉及公共利益或身份关系时法院应主动查明")])],
        distinctions=[D("民事诉讼法", "解决民事纠纷的程序法"), D("民法典", "民事实体权利法")],
        misconceptions=[dict(claim="起诉必须请律师", correction="当事人可自行起诉，律师代理非强制"),
                        dict(claim="判决生效后无法救济", correction="符合条件的可申请再审或检察监督")],
    ),
    "law-admin-litigation": dict(
        definition_source="《中华人民共和国行政诉讼法》（版本：2017年6月27日修正，核对日期：2026-11-24）。",
        elements=["受案范围", "管辖", "诉讼参加人", "证据", "起诉与受理", "审理与判决", "执行"],
        conditions=["被诉行为属于可诉行政行为", "原告与被诉行为有利害关系", "在法定期限内起诉"],
        effects=["法院审查行政行为合法性", "违法行政行为可被撤销或确认违法", "生效判决具有拘束力"],
        exceptions=["国家行为、内部行为等不属于受案范围", "法律规定复议前置的须先复议"],
        cases=[],
        controversies=[dict(issue="受案范围的扩张",
                            views=[dict(holder="逐步扩大说", basis="受案范围应随法治发展逐步扩大"),
                                   dict(holder="法定范围说（部分实务观点）", basis="应严格依法律规定确定受案范围")])],
        distinctions=[D("行政诉讼", "审查行政行为合法性"), D("行政复议", "行政机关内部层级监督")],
        misconceptions=[dict(claim="所有行政行为都可诉", correction="法律明确排除的行为不可诉"),
                        dict(claim="行政诉讼可以调解结案", correction="行政诉讼原则上不适用调解，行政赔偿与补偿除外")],
    ),
    "law-administrative-license": dict(
        definition_source="《中华人民共和国行政许可法》（版本：2019年4月23日修正，核对日期：2026-11-24）。",
        elements=["许可设定与规定", "许可的实施机关", "许可程序（申请、受理、审查、决定）", "听证", "期限", "收费", "监督检查"],
        conditions=["属于依法设定的行政许可事项", "申请人符合法定条件", "依法定程序提出申请"],
        effects=["准予许可后取得相应资格或权利", "行政机关负监督检查义务", "违法许可可被撤销"],
        exceptions=["依法可不设行政许可的事项通过其他方式管理", "紧急情况下可简化程序"],
        cases=[],
        controversies=[dict(issue="行政许可与备案、登记的关系",
                            views=[dict(holder="区分说", basis="许可是事前准入控制，备案登记多为事后信息报送"),
                                   dict(holder="功能替代说（部分观点）", basis="部分许可可转为备案以降低市场准入门槛")])],
        distinctions=[D("行政许可", "事前准入控制"), D("行政处罚", "对违法行为的制裁")],
        misconceptions=[dict(claim="许可一经作出不可撤销", correction="违法作出的许可可依法撤销"),
                        dict(claim="许可申请可以无限期拖延", correction="行政机关应在法定期限内作出决定")],
    ),
}