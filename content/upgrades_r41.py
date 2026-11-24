# -*- coding: utf-8 -*-
"""R41 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R41 = {
    "crim-prep": dict(
        definition_source="《中华人民共和国刑法》第二十二条（版本：1997年修订，历次修正案至（十二），核对日期：2026-11-24）。",
        elements=["为实施犯罪", "准备工具", "制造条件", "尚未着手"],
        conditions=["主观上具有犯罪故意", "客观上实施准备工具或制造条件的行为", "尚未着手实行犯罪"],
        effects=["可以比照既遂犯从轻、减轻处罚或者免除处罚", "预备行为本身可能另构成其他犯罪", "预备与犯意表示的区别影响可罚性"],
        exceptions=["情节显著轻微危害不大的可不认为是犯罪", "单纯犯意表示不受处罚"],
        cases=[],
        controversies=[dict(issue="预备行为的可罚性根据",
                            views=[dict(holder="抽象危险说", basis="预备行为对法益形成抽象危险，故应予处罚"),
                                   dict(holder="形式预备犯说（部分学者）", basis="刑法原则上不处罚预备，只在分则特别规定时例外")])],
        distinctions=[D("犯罪未遂", "已经着手实行"), D("犯意表示", "仅以口头或书面表达犯罪意图")],
        misconceptions=[dict(claim="只要买了作案工具就是犯罪预备", correction="须具有实施特定犯罪的故意且行为指向该犯罪"),
                        dict(claim="预备一定免除处罚", correction="预备犯可以从轻、减轻或免除处罚，由法官裁量")],
    ),
    "crim-discontinuation": dict(
        definition_source="《中华人民共和国刑法》第二十四条（版本：1997年修订，历次修正案至（十二），核对日期：2026-11-24）。",
        elements=["自动放弃犯罪", "自动有效防止犯罪结果发生", "自动性", "彻底性", "有效性"],
        conditions=["在犯罪过程中放弃或防止结果", "出于行为人意志以内原因", "中止行为与结果未发生之间有因果关系"],
        effects=["没有造成损害的应当免除处罚", "造成损害的应当减轻处罚", "中止犯不适用未遂的从宽规则"],
        exceptions=["因意志以外原因未能防止结果的不成立中止", "结果已发生且中止行为无因果贡献的不成立中止"],
        cases=[],
        controversies=[dict(issue="中止“自动性”的判断标准",
                            views=[dict(holder="主观说", basis="只要行为人自认为可以继续实施而放弃即具自动性"),
                                   dict(holder="客观说（部分学者）", basis="应结合一般人视角判断是否存在继续实施的可能性")])],
        distinctions=[D("犯罪未遂", "因意志以外原因未得逞"), D("犯罪既遂", "构成要件全部实现")],
        misconceptions=[dict(claim="中止一定免除处罚", correction="造成损害的应当减轻处罚，未造成损害的才免除"),
                        dict(claim="放弃后结果发生仍算中止", correction="须有效防止结果发生才成立中止")],
    ),
    "crim-joinder": dict(
        definition_source="《中华人民共和国刑法》第六十九条至第七十一条（版本：1997年修订，历次修正案至（十二），核对日期：2026-11-24）。",
        elements=["数罪", "分别定罪量刑", "并罚规则", "执行刑"],
        conditions=["一人犯数罪", "各罪均经审判认定", "在法定期限内发现"],
        effects=["限制加重原则为主，吸收与并科为辅", "判决宣告后发现漏罪适用先并后减", "又犯新罪适用先减后并"],
        exceptions=["判处死刑或无期徒刑的采取吸收原则", "附加刑仍须执行"],
        cases=[],
        controversies=[dict(issue="同种数罪是否并罚",
                            views=[dict(holder="一罪从重说（实务通说）", basis="同种数罪原则上按一罪从重处罚，不实行并罚"),
                                   dict(holder="并罚说（部分学者）", basis="同种数罪亦应并罚，以体现罪责刑相适应")])],
        distinctions=[D("数罪并罚", "对一人所犯数罪合并决定执行刑"), D("一罪从重", "同种数罪按一罪加重处罚")],
        misconceptions=[dict(claim="数罪并罚就是刑期相加", correction="采限制加重原则，在总和刑期以下、最高刑期以上决定"),
                        dict(claim="缓刑期间又犯新罪不并罚", correction="应撤销缓刑，对新罪与旧罪依法并罚")],
    ),
    "proc-criminal-flow": dict(
        definition_source="《中华人民共和国刑事诉讼法》关于立案、侦查、起诉、审判、执行的规定（版本：2018年修正，核对日期：2026-11-24；具体条文号待核实）。",
        elements=["立案", "侦查", "审查起诉", "审判", "执行"],
        conditions=["有犯罪事实需要追究刑事责任", "属于相应机关管辖", "依法定程序推进"],
        effects=["案件进入下一阶段", "各阶段均有救济与监督机制", "生效裁判进入执行"],
        exceptions=["不立案、撤案、不起诉可终止流程", "特别程序另有规定"],
        cases=[],
        controversies=[dict(issue="以审判为中心与侦查中心",
                            views=[dict(holder="审判中心说（改革方向）", basis="庭审实质化，证据裁判在法庭形成"),
                                   dict(holder="侦查基础说（部分实务观点）", basis="侦查质量决定案件质量，实务中侦查仍是重心")])],
        distinctions=[D("刑事诉讼流程", "国家追诉犯罪的程序链条"), D("民事诉讼流程", "解决平等主体间纠纷")],
        misconceptions=[dict(claim="立案就等于有罪", correction="立案只是启动程序，是否构成犯罪由法院判决"),
                        dict(claim="不起诉等于无罪判决", correction="不起诉是程序处理，与法院无罪判决性质不同")],
    ),
}