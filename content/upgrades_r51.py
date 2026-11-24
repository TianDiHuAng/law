# -*- coding: utf-8 -*-
"""R51 升级为 L2 的条目内容。"""


def D(w, d):
    return {"with": w, "difference": d}


UPGRADES_R51 = {
    "data-data-governance": dict(
        definition_source="《中华人民共和国数据安全法》及数据治理相关标准（版本：2021年通过，核对日期：2026-11-24）。",
        elements=["治理组织", "数据质量", "数据安全", "权限控制", "生命周期管理"],
        conditions=["数据处理者建立治理制度", "明确责任人与职责", "覆盖采集、存储、使用、共享、销毁各环节"],
        effects=["提升数据质量与安全水平", "满足合规审计要求", "支撑数据要素价值实现"],
        exceptions=["法律、行政法规另有规定的", "规模较小的处理者可简化治理结构"],
        cases=[],
        controversies=[dict(issue="数据治理与合规管理的关系",
                            views=[dict(holder="包含说", basis="数据治理涵盖合规，是更上位的管理框架"),
                                   dict(holder="并行说（部分观点）", basis="合规是底线要求，治理是价值导向，二者并行")])],
        distinctions=[D("数据治理", "组织与制度层面的管理体系"), D("数据安全", "安全保护义务")],
        misconceptions=[dict(claim="数据治理只是IT部门的事", correction="涉及业务、法务与高层治理，是全组织事务"),
                        dict(claim="治理制度建立后无需更新", correction="应随业务与法规变化持续迭代")],
    ),
    "data-asset-recognition": dict(
        definition_source="财政部《企业数据资源相关会计处理暂行规定》及相关会计准则（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["确认条件", "资产类别", "计量方式", "披露要求"],
        conditions=["数据资源可辨认", "企业拥有或控制", "经济利益很可能流入", "成本能可靠计量"],
        effects=["符合条件的数据资源可确认为无形资产或存货", "影响资产负债表与利润表", "需按规定披露相关信息"],
        exceptions=["研究阶段支出一般费用化", "不符合确认条件的列为费用"],
        cases=[],
        controversies=[dict(issue="数据资源确认为资产的条件",
                            views=[dict(holder="严格确认说", basis="须满足可辨认、控制与经济利益流入等严格条件"),
                                   dict(holder="鼓励确认说（部分观点）", basis="应适度放宽以推动数据要素市场化")])],
        distinctions=[D("数据资产入表", "会计确认"), D("数据资产登记", "权属登记")],
        misconceptions=[dict(claim="有数据就可以入表", correction="须满足会计确认条件并通过成本归集"),
                        dict(claim="入表等于数据确权", correction="会计确认不产生法律上的权属效力")],
    ),
    "data-factor-market": dict(
        definition_source="数据要素市场化配置改革相关文件（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["数据产权", "流通交易", "收益分配", "安全治理"],
        conditions=["数据依法确权或登记", "通过合规交易场所或机制流通", "保障数据安全与个人权益"],
        effects=["数据可作为生产要素进入市场", "形成数据交易与服务体系", "违规交易承担法律责任"],
        exceptions=["涉及国家安全与个人信息的交易受严格限制", "法律、行政法规禁止交易的数据不得流通"],
        cases=[],
        controversies=[dict(issue="数据产权结构性分置的落地",
                            views=[dict(holder="三权分置说（政策取向）", basis="资源持有权、加工使用权与产品经营权分置"),
                                   dict(holder="统一产权说（部分学者）", basis="应建立统一的数据产权规则，避免权利碎片化")])],
        distinctions=[D("数据要素市场", "要素配置机制"), D("数据交易场所", "具体交易平台")],
        misconceptions=[dict(claim="数据可以像商品一样自由买卖", correction="须遵守个人信息保护与数据安全限制"),
                        dict(claim="数据确权已完成立法", correction="数据产权规则仍在政策推进与立法探索中")],
    ),
    "data-revenue-sharing": dict(
        definition_source="数据要素市场化配置改革文件及《个人信息保护法》（核对日期：2026-11-24；具体条文号待核实）。",
        elements=["贡献认定", "分配机制", "来源者权益", "集体分配"],
        conditions=["数据参与价值创造", "各方贡献可识别或可约定", "不损害数据来源者权益"],
        effects=["按贡献分配收益", "数据来源者可获得相应权益保障", "分配争议可依合同或法律解决"],
        exceptions=["公共数据收益分配依特别规定执行", "法律、行政法规另有规定的"],
        cases=[],
        controversies=[dict(issue="个人是否应参与数据收益分配",
                            views=[dict(holder="个人分享说", basis="个人是数据来源者，应分享数据利用收益"),
                                   dict(holder="公共利益说（部分观点）", basis="个人已通过服务获得对价，收益主要归处理者与经营者")])],
        distinctions=[D("收益分配", "价值分配机制"), D("数据确权", "权利归属认定")],
        misconceptions=[dict(claim="收益分配规则已经法定化", correction="具体规则仍在探索，多以合同与政策指引为主"),
                        dict(claim="个人无权就数据利用主张任何权益", correction="个人信息保护法赋予个人知情、决定等权利")],
    ),
}