#!/usr/bin/env python3
"""Flashcard - Terminal English Vocabulary Trainer
   Word list: IT Due Diligence & IT Integration (CET-6+)"""

import json
import random
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "flashcard_data.json")

DEFAULT_WORDS = [
    {"en": "due diligence", "zh": "尽职调查", "example": "IT due diligence assesses the target's technology assets, liabilities, and risks before deal closure."},
    {"en": "acquisition", "zh": "收购；并购", "example": "The acquisition requires a thorough evaluation of all IT systems and contracts."},
    {"en": "divestiture", "zh": "资产剥离；分立", "example": "The divestiture involves separating the IT infrastructure of the sold business unit."},
    {"en": "carve-out", "zh": "业务剥离；分拆", "example": "A carve-out creates a standalone IT environment for the divested entity."},
    {"en": "indemnification", "zh": "赔偿；补偿", "example": "Indemnification clauses protect the buyer from pre-existing IT liabilities."},
    {"en": "escrow", "zh": "第三方托管", "example": "Source code escrow ensures access to critical software post-acquisition."},
    {"en": "warranty", "zh": "保证；担保", "example": "Warranty periods allow the buyer to discover IT system defects post-close."},
    {"en": "representation", "zh": "陈述；保证", "example": "The seller's representations cover IT asset ownership and license compliance."},
    {"en": "covenant", "zh": "契约；承诺", "example": "Transition service agreements contain restrictive covenants on IT operations."},
    {"en": "materiality", "zh": "重要性；实质性", "example": "Materiality thresholds determine which IT issues require formal disclosure."},
    {"en": "contingency", "zh": "或有事项；应急", "example": "Contingent IT liabilities can significantly impact purchase price adjustments."},
    {"en": "discrepancy", "zh": "差异；不符", "example": "A discrepancy in software license counts may indicate compliance risk."},
    {"en": "amortization", "zh": "摊销；分期偿还", "example": "Capitalized software costs require amortization over their useful life."},
    {"en": "capitalization", "zh": "资本化", "example": "Software development costs eligible for capitalization follow ASC 350-40 guidelines."},
    {"en": "depreciation", "zh": "折旧；贬值", "example": "IT hardware depreciation schedules affect the asset valuation model."},
    {"en": "appraisal", "zh": "评估；估价", "example": "Technology appraisal uses the income approach to determine fair value."},
    {"en": "valuation", "zh": "估值；定价", "example": "IT asset valuation is a critical component of purchase price allocation."},
    {"en": "earn-out", "zh": "盈利能力支付", "example": "Earn-out structures tie additional consideration to IT integration milestones."},
    {"en": "accrual", "zh": "应计；累积", "example": "IT project accruals affect the net working capital adjustment calculation."},
    {"en": "impairment", "zh": "减值", "example": "Goodwill impairment may result from overpaying for IT capabilities."},
    {"en": "liability", "zh": "负债；法律责任", "example": "Contingent IT liabilities must be disclosed in the schedule of exceptions."},
    {"en": "indemnity", "zh": "赔偿条款", "example": "Data breach indemnity clauses are heavily negotiated in IT service contracts."},
    {"en": "stipulation", "zh": "规定；约定", "example": "Transition agreements include stipulations on minimum service levels."},
    {"en": "exposure", "zh": "风险敞口", "example": "IT risk exposure spans cybersecurity, compliance, operational, and strategic dimensions."},
    {"en": "remediation", "zh": "补救；整改", "example": "Security remediation plans are a standard deliverable in the purchase agreement."},
    {"en": "discovery", "zh": "发现；探测", "example": "Automated discovery tools inventory all connected assets across the network."},
    {"en": "assessment", "zh": "评估；评定", "example": "A technical debt assessment quantifies the cost of deferred maintenance."},
    {"en": "benchmarking", "zh": "基准测试", "example": "IT spending benchmarks compare the target's costs against industry peer groups."},
    {"en": "baseline", "zh": "基线；基准", "example": "An IT cost baseline must be established before measuring synergy achievements."},
    {"en": "maturity", "zh": "成熟度", "example": "CMMI maturity levels indicate the reliability of the target's IT processes."},
    {"en": "capability", "zh": "能力；功能", "example": "IT capability maturity is assessed across people, process, and technology dimensions."},
    {"en": "dependency", "zh": "依赖关系", "example": "Application dependency mapping reveals hidden integration points."},
    {"en": "topology", "zh": "拓扑；布局", "example": "Network topology diagrams are essential infrastructure deliverables."},
    {"en": "hairball", "zh": "复杂集成网络", "example": "The application hairball makes system separation extremely difficult."},
    {"en": "legacy system", "zh": "遗留系统", "example": "Legacy system decommissioning is a major cost synergy driver post-merger."},
    {"en": "spaghetti architecture", "zh": "意大利面式架构", "example": "Spaghetti architecture results from years of ungoverned ad-hoc integrations."},
    {"en": "configuration drift", "zh": "配置漂移", "example": "Configuration drift between environments causes deployment failures."},
    {"en": "technical debt", "zh": "技术债务", "example": "Technical debt assessment is a critical due diligence deliverable."},
    {"en": "decommissioning", "zh": "退役；停用", "example": "System decommissioning includes secure data sanitization and asset disposal."},
    {"en": "deprecation", "zh": "弃用", "example": "API deprecation timelines must be communicated to all consumers."},
    {"en": "refactoring", "zh": "重构", "example": "Legacy code refactoring reduces technical debt before full integration."},
    {"en": "parallel run", "zh": "并行运行", "example": "A parallel run validates system behavior before the final cutover."},
    {"en": "rollback", "zh": "回滚；撤销", "example": "A tested rollback plan is mandatory before any production migration."},
    {"en": "rollforward", "zh": "前滚恢复", "example": "Transaction log rollforward recovers data to the exact point of failure."},
    {"en": "fallback", "zh": "回退；备用", "example": "The fallback procedure restores the previous state within four hours."},
    {"en": "integration", "zh": "整合；集成", "example": "Post-merger IT integration is the most complex and resource-intensive workstream."},
    {"en": "consolidation", "zh": "整合；合并", "example": "Data center consolidation reduces operational costs and carbon footprint."},
    {"en": "synergy", "zh": "协同效应", "example": "IT synergy targets are systematically tracked through a benefits realization framework."},
    {"en": "harmonization", "zh": "协调；统一", "example": "Policy harmonization across merging entities is a quick-win opportunity."},
    {"en": "rationalization", "zh": "合理化；优化", "example": "Application portfolio rationalization eliminates redundancy and reduces maintenance costs."},
    {"en": "standardization", "zh": "标准化", "example": "Standardization of the technology stack accelerates integration and reduces complexity."},
    {"en": "alignment", "zh": "对齐；协同", "example": "IT alignment with business strategy is validated during the due diligence phase."},
    {"en": "convergence", "zh": "融合；趋同", "example": "The convergence of IT and OT systems creates new cybersecurity risks."},
    {"en": "interoperability", "zh": "互操作性", "example": "Interoperability between different ERP platforms is a core integration challenge."},
    {"en": "portability", "zh": "可移植性", "example": "Cloud workload portability enables flexible multi-cloud deployment strategies."},
    {"en": "scalability", "zh": "可扩展性", "example": "Scalability testing determines whether the infrastructure can handle projected growth."},
    {"en": "elasticity", "zh": "弹性伸缩", "example": "Auto-scaling policies ensure elasticity during peak demand periods."},
    {"en": "redundancy", "zh": "冗余；备份", "example": "Geographic redundancy ensures continuous operation during regional outages."},
    {"en": "resilience", "zh": "韧性；恢复力", "example": "System resilience is quantitatively measured by RTO and RPO metrics."},
    {"en": "modularity", "zh": "模块化", "example": "Modular architecture simplifies the separation of divested business units."},
    {"en": "assimilation", "zh": "同化；吸收", "example": "Cultural assimilation between IT teams is often harder than technical integration."},
    {"en": "operating model", "zh": "运营模式", "example": "The target operating model defines the future-state IT organization structure."},
    {"en": "organizational design", "zh": "组织设计", "example": "Organizational design determines reporting lines, spans of control, and decision rights."},
    {"en": "center of excellence", "zh": "卓越中心", "example": "A Cloud Center of Excellence establishes best practices and governance frameworks."},
    {"en": "shared services", "zh": "共享服务", "example": "IT shared services consolidation eliminates duplicate functions across business units."},
    {"en": "mandate", "zh": "授权；任务", "example": "The integration team received a mandate to complete all workstreams within twelve months."},
    {"en": "governance", "zh": "治理；管理", "example": "A joint integration governance board oversees decision-making and issue escalation."},
    {"en": "oversight", "zh": "监督；监管", "example": "Program oversight ensures integration milestones are achieved on schedule."},
    {"en": "stakeholder", "zh": "利益相关者", "example": "Stakeholder buy-in at the executive level is critical for integration success."},
    {"en": "workstream", "zh": "工作流；工作包", "example": "The integration program comprises twelve parallel workstreams with dedicated leads."},
    {"en": "deliverable", "zh": "可交付成果", "example": "The Day-1 deliverable checklist includes 47 critical items requiring sign-off."},
    {"en": "milestone", "zh": "里程碑", "example": "Integration milestones are tracked through a centralized PMO dashboard."},
    {"en": "gate", "zh": "关卡；审批节点", "example": "Phase gates require formal sign-off before proceeding to the next integration stage."},
    {"en": "escalation", "zh": "升级；上报", "example": "Severity-1 integration issues require immediate escalation to the steering committee."},
    {"en": "triage", "zh": "分类；分诊", "example": "Integration issues are triaged based on business impact and urgency."},
    {"en": "cutover", "zh": "切换；转换", "example": "The cutover window is limited to 48 hours over the weekend period."},
    {"en": "day-one readiness", "zh": "首日就绪", "example": "Day-one readiness validates that all critical systems are operational at close."},
    {"en": "runbook", "zh": "操作手册", "example": "The integration runbook documents step-by-step procedures for every workstream."},
    {"en": "playbook", "zh": "行动手册", "example": "The integration playbook standardizes repeatable processes across all acquisitions."},
    {"en": "RACI", "zh": "责任分配矩阵", "example": "The RACI matrix clarifies decision rights and accountability for each integration activity."},
    {"en": "service-level agreement", "zh": "服务水平协议", "example": "SLA consolidation harmonizes service commitments across merged entities."},
    {"en": "dictator", "zh": "整合决策者", "example": "The integration dictator resolves functional disputes and enforces standardization."},
    {"en": "war room", "zh": "作战室", "example": "The integration war room convenes daily during the critical first 100 days."},
    {"en": "reconciliation", "zh": "对账；调节", "example": "Financial reconciliation between legacy and target ERP systems is mandatory."},
    {"en": "value realization", "zh": "价值实现", "example": "Value realization milestones are linked to executive compensation structures."},
    {"en": "architecture", "zh": "架构；体系结构", "example": "Enterprise architecture establishes principles, standards, and roadmaps for IT."},
    {"en": "infrastructure", "zh": "基础设施", "example": "Infrastructure due diligence covers network, storage, compute, and facilities."},
    {"en": "ecosystem", "zh": "生态系统", "example": "The legacy IT ecosystem consists of over 200 interconnected applications."},
    {"en": "middleware", "zh": "中间件", "example": "Middleware abstraction layers simplify integration between disparate systems."},
    {"en": "monolith", "zh": "单体架构", "example": "Monolith-to-microservices migration is typically a multi-year transformation."},
    {"en": "microservices", "zh": "微服务", "example": "Microservices architecture enables independent deployability and technology diversity."},
    {"en": "containerization", "zh": "容器化", "example": "Containerization improves workload portability across on-premise and cloud environments."},
    {"en": "virtualization", "zh": "虚拟化", "example": "Server virtualization consolidation significantly improves hardware utilization."},
    {"en": "federation", "zh": "联邦；联合", "example": "Identity federation enables single sign-on across all merged entities."},
    {"en": "mesh", "zh": "网状；网格", "example": "Service mesh provides observability, traffic management, and security for microservices."},
    {"en": "catalogue", "zh": "服务目录", "example": "The IT service catalogue documents all technology offerings and their owners."},
    {"en": "repository", "zh": "存储库；仓库", "example": "Source code repository migration is often underestimated in integration planning."},
    {"en": "lifecycle", "zh": "生命周期", "example": "Application lifecycle management policies define stages from inception to retirement."},
    {"en": "as-is", "zh": "现状分析", "example": "The as-is assessment documents the current-state architecture and processes."},
    {"en": "to-be", "zh": "目标状态", "example": "The to-be architecture defines the target integration end-state."},
    {"en": "greenfield", "zh": "全新建设", "example": "A greenfield implementation avoids legacy constraints but requires more investment."},
    {"en": "brownfield", "zh": "改造建设", "example": "Brownfield integration must coexist with existing systems during the transition."},
    {"en": "disparate", "zh": "不同的；异质的", "example": "Disparate legacy systems must be integrated into a unified technology platform."},
    {"en": "heterogeneous", "zh": "异构的", "example": "Heterogeneous environments significantly increase integration complexity."},
    {"en": "homogeneous", "zh": "同构的", "example": "A homogeneous technology stack simplifies maintenance and reduces operational costs."},
    {"en": "hybrid cloud", "zh": "混合云", "example": "Hybrid cloud strategies balance on-premise control with public cloud agility."},
    {"en": "multi-cloud", "zh": "多云", "example": "Multi-cloud deployments avoid vendor lock-in but add management complexity."},
    {"en": "tenancy", "zh": "租用；租户", "example": "Multi-tenancy architecture enables cost sharing across multiple business units."},
    {"en": "provisioning", "zh": "配置；部署", "example": "Infrastructure provisioning is fully automated through infrastructure-as-code pipelines."},
    {"en": "orchestration", "zh": "编排；协调", "example": "Cloud orchestration tools manage complex multi-tier application deployments."},
    {"en": "abstraction", "zh": "抽象化", "example": "Cloud abstraction layers decouple applications from underlying hardware specifics."},
    {"en": "instance", "zh": "实例", "example": "Reserved cloud instances reduce compute costs by up to sixty percent."},
    {"en": "consumption", "zh": "消费；用量", "example": "Cloud consumption-based pricing shifts IT costs from CAPEX to OPEX models."},
    {"en": "on-premise", "zh": "本地部署", "example": "On-premise to cloud migration is a core integration workstream."},
    {"en": "edge computing", "zh": "边缘计算", "example": "Edge computing reduces latency for real-time IoT and analytics workloads."},
    {"en": "serverless", "zh": "无服务器", "example": "Serverless architectures abstract infrastructure management entirely from developers."},
    {"en": "region", "zh": "区域；地区", "example": "Data residency requirements dictate which cloud regions are permissible."},
    {"en": "availability zone", "zh": "可用区", "example": "Availability zones provide fault isolation within a cloud provider region."},
    {"en": "disaster recovery", "zh": "灾难恢复", "example": "Disaster recovery planning must account for cross-region data replication."},
    {"en": "capacity planning", "zh": "容量规划", "example": "Capacity planning ensures infrastructure resources meet projected future demand."},
    {"en": "chargeback", "zh": "成本分摊", "example": "Cloud chargeback models allocate costs back to consuming business units."},
    {"en": "sizing", "zh": "规格确定", "example": "Proper workload sizing optimizes cost without sacrificing performance."},
    {"en": "co-location", "zh": "托管；共置", "example": "Co-location facilities provide physical security, power, and network connectivity."},
    {"en": "bare-metal", "zh": "裸机；物理机", "example": "Bare-metal performance is required for latency-sensitive financial trading workloads."},
    {"en": "cluster", "zh": "集群", "example": "The cluster configuration ensures high availability for mission-critical applications."},
    {"en": "encryption", "zh": "加密", "example": "End-to-end encryption protects sensitive data in transit and at rest."},
    {"en": "authentication", "zh": "身份验证", "example": "Multi-factor authentication is a mandatory security control for all systems."},
    {"en": "authorization", "zh": "授权；权限", "example": "Role-based authorization restricts system access based on job function."},
    {"en": "entitlement", "zh": "权限；权利", "example": "Entitlement reviews ensure user access aligns with current job responsibilities."},
    {"en": "attestation", "zh": "认证；证明", "example": "SOC2 attestation is a standard due diligence requirement for SaaS vendors."},
    {"en": "penetration", "zh": "渗透测试", "example": "Penetration testing identifies exploitable vulnerabilities in network perimeters."},
    {"en": "vulnerability", "zh": "漏洞；脆弱性", "example": "Vulnerability remediation is prioritized based on CVSS severity scores."},
    {"en": "breach", "zh": "违规；泄露", "example": "Historical data breaches must be fully disclosed during the due diligence process."},
    {"en": "forensic", "zh": "法医的；取证", "example": "Digital forensic analysis is required for thorough security incident investigation."},
    {"en": "audit trail", "zh": "审计轨迹", "example": "An immutable audit trail satisfies regulatory record-keeping and compliance requirements."},
    {"en": "privilege", "zh": "权限；特权", "example": "Least-privilege principles limit lateral movement in the event of compromise."},
    {"en": "hardening", "zh": "加固；强化", "example": "System hardening baselines must be applied across all acquired infrastructure."},
    {"en": "patching", "zh": "补丁管理", "example": "Patch management maturity is a strong indicator of operational discipline."},
    {"en": "zero trust", "zh": "零信任", "example": "Zero trust architecture assumes breach and verifies every access request."},
    {"en": "defense-in-depth", "zh": "纵深防御", "example": "Defense-in-depth layers preventive, detective, and corrective security controls."},
    {"en": "ransomware", "zh": "勒索软件", "example": "Ransomware resilience testing is a key due diligence consideration."},
    {"en": "phishing", "zh": "钓鱼攻击", "example": "Phishing simulation results indicate the organization's security awareness level."},
    {"en": "reconnaissance", "zh": "侦察", "example": "Network reconnaissance is often the first phase of an advanced attack."},
    {"en": "privilege escalation", "zh": "权限提升", "example": "Privilege escalation vulnerabilities must be patched on an emergency basis."},
    {"en": "compensating control", "zh": "补偿性控制", "example": "Compensating controls mitigate risk when primary controls cannot be implemented."},
    {"en": "governance", "zh": "数据治理", "example": "Data governance defines ownership, quality standards, and lineage requirements."},
    {"en": "stewardship", "zh": "管理职责", "example": "Data stewardship assigns clear accountability for data quality and integrity."},
    {"en": "lineage", "zh": "血缘；溯源", "example": "Data lineage tracking supports regulatory compliance and impact analysis."},
    {"en": "provenance", "zh": "来源；出处", "example": "Provenance metadata records the complete history of data origin and transformation."},
    {"en": "fidelity", "zh": "保真度；精确性", "example": "Data fidelity during migration must be validated through reconciliation procedures."},
    {"en": "integrity", "zh": "完整性；一致性", "example": "Referential integrity constraints prevent orphaned records in relational databases."},
    {"en": "deduplication", "zh": "去重", "example": "Data deduplication reduces storage footprint and accelerates migration timelines."},
    {"en": "normalization", "zh": "归一化；规范化", "example": "Data normalization resolves format inconsistencies across source systems."},
    {"en": "canonical", "zh": "规范的；标准", "example": "A canonical data model simplifies system integration through standardized formats."},
    {"en": "schema", "zh": "模式；架构", "example": "Schema mapping between source and target systems is the most time-consuming activity."},
    {"en": "extraction", "zh": "提取", "example": "ETL extraction processes must handle hundreds of disparate source systems."},
    {"en": "transformation", "zh": "转换", "example": "Data transformation rules must be documented and validated through testing."},
    {"en": "warehouse", "zh": "数据仓库", "example": "Enterprise data warehouse consolidation is a significant synergy initiative."},
    {"en": "data lake", "zh": "数据湖", "example": "A data lake architecture accommodates both structured and unstructured data."},
    {"en": "synchronization", "zh": "同步", "example": "Real-time synchronization is required between merged CRM platforms."},
    {"en": "replication", "zh": "复制", "example": "Database replication ensures data availability and consistency during cutover."},
    {"en": "archival", "zh": "归档", "example": "Data archival policies balance regulatory retention with storage costs."},
    {"en": "purge", "zh": "清除；销毁", "example": "Secure data purge processes are required before system decommissioning."},
    {"en": "privacy", "zh": "隐私", "example": "Privacy impact assessments are mandatory when processing personal data."},
    {"en": "data residency", "zh": "数据驻留", "example": "Data residency regulations require customer data to remain within national borders."},
    {"en": "compliance", "zh": "合规；遵循", "example": "Regulatory compliance spans GDPR, SOX, HIPAA, PCI-DSS, and local data protection laws."},
    {"en": "regulatory", "zh": "监管的", "example": "Regulatory filings must disclose all material IT risks and non-compliance items."},
    {"en": "statutory", "zh": "法定的", "example": "Statutory data retention periods vary significantly by jurisdiction."},
    {"en": "fiduciary", "zh": "信义；受托", "example": "Directors have fiduciary duties to oversee cybersecurity risks and IT governance."},
    {"en": "disclosure", "zh": "披露；公开", "example": "Material cybersecurity incidents require timely disclosure under SEC regulations."},
    {"en": "promulgation", "zh": "颁布；发布", "example": "Policy promulgation ensures all employees are aware of new compliance standards."},
    {"en": "arbitration", "zh": "仲裁", "example": "IT service disputes are typically subject to binding arbitration clauses."},
    {"en": "litigation", "zh": "诉讼", "example": "IP litigation risks must be assessed during the due diligence process."},
    {"en": "jurisdiction", "zh": "管辖范围", "example": "Data jurisdiction determines which legal and regulatory frameworks apply."},
    {"en": "sovereignty", "zh": "主权；自主", "example": "Data sovereignty laws restrict cross-border data transfers and processing."},
    {"en": "provision", "zh": "条款；准备金", "example": "Software maintenance contract provisions must be reviewed for renewal terms."},
    {"en": "contingent consideration", "zh": "或有对价", "example": "Earn-out structures link contingent consideration to IT integration milestones."},
    {"en": "adjudication", "zh": "裁决；判定", "example": "Dispute adjudication processes define formal resolution for service disagreements."},
    {"en": "sanction", "zh": "制裁；处罚", "example": "Export control sanctions may restrict technology transfer between entities."},
    {"en": "inherent risk", "zh": "固有风险", "example": "Inherent risk is assessed before considering the effect of internal controls."},
    {"en": "residual risk", "zh": "残余风险", "example": "Residual risk is accepted only when within the defined organizational appetite."},
    {"en": "control objective", "zh": "控制目标", "example": "COBIT control objectives align IT processes with business requirements."},
    {"en": "segregation of duties", "zh": "职责分离", "example": "Segregation of duties prevents conflicts of interest in financial systems."},
    {"en": "key control indicator", "zh": "关键控制指标", "example": "KCI monitoring provides early warning of control effectiveness degradation."},
    {"en": "capability maturity", "zh": "能力成熟度", "example": "Capability maturity assessments evaluate process reliability and repeatability."},
    {"en": "incident management", "zh": "事件管理", "example": "Incident management processes restore normal service operation as quickly as possible."},
    {"en": "problem management", "zh": "问题管理", "example": "Root cause analysis is the core activity of effective problem management."},
    {"en": "change management", "zh": "变更管理", "example": "Change advisory board approval is required for all production changes."},
    {"en": "release management", "zh": "发布管理", "example": "Release management coordinates the deployment of changes into production environments."},
    {"en": "configuration management", "zh": "配置管理", "example": "The configuration management database consolidates asset and dependency information."},
    {"en": "asset management", "zh": "资产管理", "example": "IT asset management tracks hardware and software throughout their full lifecycle."},
    {"en": "capacity management", "zh": "容量管理", "example": "Capacity management ensures IT resources meet current and future business demand."},
    {"en": "availability management", "zh": "可用性管理", "example": "Availability management targets ninety-nine point nine nine percent uptime for critical systems."},
    {"en": "continuity management", "zh": "连续性管理", "example": "IT service continuity management includes disaster recovery and crisis response plans."},
    {"en": "service catalog", "zh": "服务目录", "example": "The service catalog must be harmonized across the merged organization."},
    {"en": "service desk", "zh": "服务台", "example": "Service desk consolidation improves efficiency through unified ticketing and self-service."},
    {"en": "fulfillment", "zh": "履行；交付", "example": "Service request fulfillment automation reduces manual effort and improves response times."},
    {"en": "SLA breach", "zh": "服务违约", "example": "SLA breach penalties are calculated based on cumulative downtime duration."},
    {"en": "KPI", "zh": "关键绩效指标", "example": "IT KPIs track integration progress against the approved business case."},
    {"en": "dashboard", "zh": "仪表盘", "example": "The integration dashboard provides real-time visibility into all workstreams."},
    {"en": "error budget", "zh": "错误预算", "example": "Error budget policies balance service reliability against feature deployment velocity."},
    {"en": "post-mortem", "zh": "事后剖析", "example": "Post-mortem reports drive continuous improvement across IT operations."},
    {"en": "service-level objective", "zh": "服务等级目标", "example": "SLOs define measurable reliability targets for each critical service."},
    {"en": "warning notice", "zh": "预警通知", "example": "Service warning notices are issued before planned maintenance windows."},
    {"en": "continuous integration", "zh": "持续集成", "example": "Continuous integration automatically builds and tests code changes."},
    {"en": "continuous delivery", "zh": "持续交付", "example": "Continuous delivery automates the entire software release process to production."},
    {"en": "pipeline", "zh": "流水线", "example": "CI/CD pipeline consolidation accelerates software delivery across the merged entity."},
    {"en": "artifact", "zh": "构建产物", "example": "Artifact repository migration is one of the most underestimated integration tasks."},
    {"en": "blue-green", "zh": "蓝绿部署", "example": "Blue-green deployment minimizes downtime during software releases."},
    {"en": "canary", "zh": "金丝雀发布", "example": "Canary releases limit the blast radius of defective deployments."},
    {"en": "immutable", "zh": "不可变的", "example": "Immutable infrastructure eliminates configuration drift between environments."},
    {"en": "idempotent", "zh": "幂等的", "example": "Idempotent deployment scripts ensure consistent results regardless of execution count."},
    {"en": "instrumentation", "zh": "探针；监控", "example": "Application instrumentation provides granular performance and error tracking data."},
    {"en": "tracing", "zh": "链路追踪", "example": "Distributed tracing identifies performance bottlenecks across microservice boundaries."},
    {"en": "profiling", "zh": "性能分析", "example": "CPU profiling reveals performance hotspots in the application codebase."},
    {"en": "tail latency", "zh": "尾部延迟", "example": "Tail latency optimization is critical for real-time financial trading systems."},
    {"en": "chaos engineering", "zh": "混沌工程", "example": "Chaos engineering proactively validates system resilience under failure conditions."},
    {"en": "site reliability", "zh": "站点可靠性", "example": "Site reliability engineering applies software engineering to operations problems."},
    {"en": "deployment", "zh": "部署", "example": "Automated deployment pipelines reduce human error and accelerate releases."},
    {"en": "rollforward", "zh": "前滚修复", "example": "Rollforward deployment applies a fix rather than reverting to a previous version."},
    {"en": "strangler pattern", "zh": "绞杀者模式", "example": "The strangler pattern incrementally replaces legacy system functionality."},
    {"en": "big bang", "zh": "大爆炸式上线", "example": "Big bang deployments carry significant execution risk compared to phased rollouts."},
    {"en": "phased rollout", "zh": "分阶段部署", "example": "A phased rollout reduces risk by limiting the scope of each deployment wave."},
    {"en": "proof of concept", "zh": "概念验证", "example": "A proof of concept validates technical feasibility before full investment."},
    {"en": "business case", "zh": "商业论证", "example": "The IT integration business case must demonstrate measurable ROI within three years."},
    {"en": "synergy capture", "zh": "协同效应实现", "example": "Synergy capture tracking ensures integration delivers projected financial benefits."},
    {"en": "target operating model", "zh": "目标运营模式", "example": "The target operating model defines the future-state IT organization and processes."},
    {"en": "span of control", "zh": "管理幅度", "example": "A lean IT organization typically maintains a span of control of seven to ten."},
    {"en": "statement of work", "zh": "工作说明书", "example": "SOW scope creep is a common source of integration budget overruns."},
    {"en": "work package", "zh": "工作包", "example": "Each work package has defined deliverables, budget allocation, and owner accountability."},
    {"en": "critical path", "zh": "关键路径", "example": "The critical path determines the minimum integration timeline to completion."},
    {"en": "dependency mapping", "zh": "依赖关系映射", "example": "Dependency mapping reveals hidden relationships between applications and infrastructure."},
    {"en": "risk register", "zh": "风险登记册", "example": "The integration risk register tracks identified risks and mitigation measures."},
    {"en": "issue log", "zh": "问题日志", "example": "The issue log tracks all open integration problems with assigned owners."},
    {"en": "change control", "zh": "变更控制", "example": "Change control boards approve or reject integration scope changes."},
    {"en": "lessons learned", "zh": "经验教训", "example": "Lessons learned sessions capture knowledge for future acquisition integrations."},
    {"en": "benefits realization", "zh": "收益实现", "example": "Benefits realization tracks whether planned integration outcomes are achieved."},
    {"en": "earned value", "zh": "挣值管理", "example": "Earned value management measures integration progress against planned budgets."},
    {"en": "go-live", "zh": "上线投产", "example": "The go-live decision requires sign-off from all workstream leads."},
    {"en": "hypercare", "zh": "上线后护航", "example": "Hypercare provides intensive support during the first weeks after go-live."},
    {"en": "transition", "zh": "过渡；转型", "example": "The transition service agreement defines support duration and scope post-close."},
    {"en": "transformation", "zh": "转型；变革", "example": "Digital transformation initiatives often accelerate following a merger."},
    {"en": "outsourcing", "zh": "外包", "example": "IT outsourcing contracts require due diligence on vendor financial stability."},
    {"en": "insourcing", "zh": "内部化；内包", "example": "Insourcing previously outsourced IT functions may improve control and alignment."},
    {"en": "procurement", "zh": "采购", "example": "IT procurement consolidation leverages combined vendor volume for discounts."},
    {"en": "sourcing", "zh": "寻源；采购策略", "example": "Strategic sourcing evaluates alternative vendors for major technology categories."},
    {"en": "negotiation", "zh": "谈判；协商", "example": "Vendor contract renegotiation typically achieves fifteen to twenty percent savings."},
    {"en": "leverage", "zh": "杠杆；优势", "example": "Combined purchasing leverage improves pricing terms with enterprise software vendors."},
    {"en": "discount", "zh": "折扣；折让", "example": "Enterprise license agreement discounts depend on committed purchase volumes."},
    {"en": "true-up", "zh": "调整；补足", "example": "Annual license true-up reconciles deployed versus purchased software quantities."},
    {"en": "subcontractor", "zh": "分包商", "example": "Subcontractor risk flows through the prime vendor relationship."},
    {"en": "prime vendor", "zh": "主供应商", "example": "Prime vendor consolidation simplifies procurement and reduces administrative overhead."},
    {"en": "retainer", "zh": "顾问聘用金", "example": "IT advisory retainers provide access to specialized expertise on demand."},
    {"en": "vendor lock-in", "zh": "供应商锁定", "example": "Vendor lock-in risk must be assessed for all critical technology platforms."},
    {"en": "total cost of ownership", "zh": "总拥有成本", "example": "TCO analysis compares on-premise versus cloud deployment costs comprehensively."},
    {"en": "capital expenditure", "zh": "资本支出", "example": "IT CAPEX budgets cover hardware, software licenses, and infrastructure build-out."},
    {"en": "operational expenditure", "zh": "运营支出", "example": "Cloud migrations shift IT spending from CAPEX to OPEX accounting models."},
    {"en": "run-rate", "zh": "年化运行率", "example": "IT run-rate cost analysis establishes the synergy realization baseline."},
    {"en": "overhead", "zh": "间接费用", "example": "IT overhead allocation methodologies impact reported business unit profitability."},
    {"en": "recovery time objective", "zh": "恢复时间目标", "example": "RTO defines the maximum acceptable downtime for each critical system."},
    {"en": "recovery point objective", "zh": "恢复点目标", "example": "RPO defines the maximum acceptable data loss measured in time."},
    {"en": "failover", "zh": "故障切换", "example": "Automated failover ensures continuous operation during primary system failure."},
    {"en": "failback", "zh": "切回", "example": "Failback procedures restore operations to the primary site after recovery."},
    {"en": "active-active", "zh": "双活", "example": "Active-active architecture enables both sites to handle production traffic simultaneously."},
    {"en": "active-passive", "zh": "主备", "example": "Active-passive configuration maintains a standby copy for failover scenarios."},
    {"en": "hot standby", "zh": "热备", "example": "Hot standby systems are fully synchronized and ready for immediate failover."},
    {"en": "cold standby", "zh": "冷备", "example": "Cold standby systems require manual activation and data restoration processes."},
    {"en": "disaster tolerance", "zh": "灾难容错", "example": "Disaster tolerance defines the organization's ability to withstand catastrophic events."},
    {"en": "business impact analysis", "zh": "业务影响分析", "example": "BIA identifies critical business processes and their IT dependencies."},
    {"en": "exercise", "zh": "演练", "example": "Tabletop exercises validate disaster recovery procedures without production impact."},
    {"en": "maximum tolerable downtime", "zh": "最大可容忍停机时间", "example": "MTD defines the total duration a process can be unavailable before severe impact."},
    {"en": "resilience testing", "zh": "韧性测试", "example": "Resilience testing validates system behavior under extreme load conditions."},
    {"en": "fault tolerance", "zh": "容错", "example": "Fault-tolerant systems continue operating despite individual component failures."},
    {"en": "degraded mode", "zh": "降级模式", "example": "Critical systems must support degraded mode operation during partial outages."},
    {"en": "latency", "zh": "延迟", "example": "Network latency between merged offices affects real-time application performance."},
    {"en": "throughput", "zh": "吞吐量", "example": "Throughput capacity must be assessed for data replication and video conferencing."},
    {"en": "subnet", "zh": "子网", "example": "IP subnet conflicts between merging entities require comprehensive re-addressing."},
    {"en": "gateway", "zh": "网关", "example": "API gateway consolidation simplifies the combined integration architecture."},
    {"en": "firewall", "zh": "防火墙", "example": "Firewall rule consolidation reduces the overall attack surface."},
    {"en": "load balancer", "zh": "负载均衡器", "example": "Load balancer configuration ensures even traffic distribution across servers."},
    {"en": "peering", "zh": "对等连接", "example": "Direct peering between cloud VPCs reduces data transfer costs significantly."},
    {"en": "tunneling", "zh": "隧道技术", "example": "VPN tunneling provides encrypted connectivity during transitional network phases."},
    {"en": "backbone", "zh": "骨干网", "example": "The network backbone must support double the combined traffic post-merger."},
    {"en": "segmentation", "zh": "分段；隔离", "example": "Network segmentation limits blast radius in security incidents."},
    {"en": "demilitarized zone", "zh": "隔离区", "example": "DMZ architecture exposes public services while protecting internal networks."},
    {"en": "anycast", "zh": "任播", "example": "Anycast routing improves DNS resolution performance across global locations."},
    {"en": "jitter", "zh": "抖动", "example": "Jitter buffers compensate for variable packet arrival times in VoIP systems."},
    {"en": "bandwidth", "zh": "带宽", "example": "Bandwidth provisioning must account for data replication and backup traffic."},
    {"en": "contention", "zh": "争用；竞争", "example": "Network contention degrades application performance during peak usage periods."},
    {"en": "boil-the-ocean", "zh": "试图一次性解决所有问题", "example": "Avoid trying to boil the ocean — prioritize the critical twenty percent."},
    {"en": "low-hanging fruit", "zh": "容易实现的目标", "example": "License consolidation is low-hanging fruit for cost synergy realization."},
    {"en": "lift-and-shift", "zh": "直接迁移", "example": "Lift-and-shift migration minimizes application changes but defers optimization."},
    {"en": "rip-and-replace", "zh": "完全替换", "example": "Rip-and-replace strategies carry higher short-term risk than phased migration."},
    {"en": "bespoke", "zh": "定制的；专属的", "example": "Bespoke applications require specialized knowledge for ongoing maintenance."},
    {"en": "off-the-shelf", "zh": "现成的；成品", "example": "Off-the-shelf software is preferred over custom development when possible."},
    {"en": "minimum viable product", "zh": "最小可行产品", "example": "The MVP approach delivers business value early through iterative delivery."},
    {"en": "feed", "zh": "对外数据传输", "example": "Application feeds between the seller's and buyer's systems require careful mapping."},
    {"en": "tuck-in", "zh": "完全并入", "example": "A tuck-in acquisition fully absorbs the target into the acquirer's operations."},
    {"en": "bolt-on", "zh": "附加并购", "example": "A bolt-on acquisition adds complementary capabilities to existing business units."},
    {"en": "proof of value", "zh": "价值验证", "example": "A proof of value demonstrates business benefits before full-scale investment."},
    {"en": "observability", "zh": "可观测性", "example": "Observability platforms consolidate logs, metrics, and traces for unified monitoring."},
    {"en": "telemetry", "zh": "遥测", "example": "Infrastructure telemetry feeds the central monitoring and alerting system."},
    {"en": "idempotency", "zh": "幂等性", "example": "Idempotency is a fundamental principle of reliable infrastructure automation."},
    {"en": "canonical model", "zh": "标准模型", "example": "A canonical data model simplifies integration through standardized message formats."}
]

class FlashcardApp:
    def __init__(self):
        self.words = []
        self.known = set()
        self.unknown = set()
        self.history = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            self.words = data.get("words", [])
            self.known = set(data.get("known", []))
            self.unknown = set(data.get("unknown", []))
            self.history = data.get("history", [])
        else:
            self.words = DEFAULT_WORDS.copy()
            self.save_data()

    def save_data(self):
        data = {
            "words": self.words,
            "known": list(self.known),
            "unknown": list(self.unknown),
            "history": self.history,
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def clear_screen(self):
        os.system("clear" if os.name == "posix" else "cls")

    def show_header(self, title="📚 FLASHCARD TRAINER"):
        print("=" * 50)
        print(f"  {title}")
        print("=" * 50)
        print()

    def show_stats(self):
        total = len(self.words)
        known = len(self.known)
        unknown = len(self.unknown)
        pct = round(known / total * 100, 1) if total else 0
        print(f"  📊 Total: {total}  |  ✅ Known: {known}  |  ❌ Unknown: {unknown}  |  🎯 {pct}% mastered")
        print()

    def main_menu(self):
        while True:
            self.clear_screen()
            self.show_header()
            self.show_stats()
            print("  1️⃣  Start Review (all words)")
            print("  2️⃣  Review Unknown Words")
            print("  3️⃣  Review Known Words")
            print("  4️⃣  Add New Word")
            print("  5️⃣  Manage Words")
            print("  6️⃣  View History")
            print("  7️⃣  Reset Progress")
            print("  q  Quit")
            print()
            choice = input("  ▶  Choose: ").strip().lower()

            if choice == "1":
                self.start_review(self.words)
            elif choice == "2":
                unknown_words = [w for i, w in enumerate(self.words) if i in self.unknown]
                if not unknown_words:
                    input("  🎉 No unknown words! Press Enter...")
                else:
                    self.start_review(unknown_words, mode="unknown")
            elif choice == "3":
                known_words = [w for i, w in enumerate(self.words) if i in self.known]
                if not known_words:
                    input("  📭 No known words yet. Press Enter...")
                else:
                    self.start_review(known_words, mode="known")
            elif choice == "4":
                self.add_word()
            elif choice == "5":
                self.manage_words()
            elif choice == "6":
                self.show_history()
            elif choice == "7":
                self.reset_progress()
            elif choice == "q":
                self.save_data()
                print("\n  👋 See you next time!\n")
                break

    def start_review(self, word_list, mode="all"):
        if not word_list:
            return

        random.shuffle(word_list)
        idx = 0
        session_results = {"known": 0, "unknown": 0}

        while idx < len(word_list):
            self.clear_screen()
            self.show_header(f"📖 Reviewing — {mode.upper()}")
            print(f"  Card {idx + 1} of {len(word_list)}")
            print()

            word = word_list[idx]
            print(f"  📝  {word['en']}")
            print()

            if word.get("example"):
                print(f"  💬  {word['example']}")
                print()

            print("  [Enter] Show answer | [s] Skip | [q] Quit review")
            cmd = input("  ▶  ").strip().lower()

            if cmd == "q":
                break
            if cmd == "s":
                idx += 1
                continue

            # Show answer
            self.clear_screen()
            self.show_header("💡 ANSWER")
            print(f"  📝  {word['en']}")
            print(f"  🌏  {word['zh']}")
            print()
            if word.get("example"):
                print(f"  💬  {word['example']}")
            print()

            print("  [k] Known ✅   [u] Unknown ❌   [q] Quit")
            cmd = input("  ▶  ").strip().lower()

            word_idx = self.words.index(word)

            if cmd == "k":
                self.known.add(word_idx)
                self.unknown.discard(word_idx)
                session_results["known"] += 1
                self.history.append({"time": datetime.now().isoformat(), "word": word["en"], "result": "known"})
                idx += 1
            elif cmd == "u":
                self.unknown.add(word_idx)
                self.known.discard(word_idx)
                session_results["unknown"] += 1
                self.history.append({"time": datetime.now().isoformat(), "word": word["en"], "result": "unknown"})
                idx += 1
            elif cmd == "q":
                break

            self.save_data()

        # Session summary
        self.clear_screen()
        self.show_header("📊 SESSION COMPLETE")
        print(f"  ✅ Known:   {session_results['known']}")
        print(f"  ❌ Unknown: {session_results['unknown']}")
        print(f"  📝 Total:   {session_results['known'] + session_results['unknown']}")
        print()
        input("  Press Enter to continue...")

    def add_word(self):
        self.clear_screen()
        self.show_header("➕ ADD NEW WORD")
        en = input("  English word: ").strip()
        if not en:
            return
        zh = input("  Chinese meaning: ").strip()
        if not zh:
            return
        ex = input("  Example sentence (optional): ").strip()

        self.words.append({"en": en, "zh": zh, "example": ex if ex else ""})
        self.save_data()
        print(f"\n  ✅ '{en}' added!")
        input("  Press Enter to continue...")

    def manage_words(self):
        while True:
            self.clear_screen()
            self.show_header("📋 MANAGE WORDS")
            for i, w in enumerate(self.words):
                prefix = ""
                if i in self.known:
                    prefix = "✅"
                elif i in self.unknown:
                    prefix = "❌"
                print(f"  {i+1:3d}. {prefix} {w['en']:20s} → {w['zh']}")
            print()
            print("  [n] Add new  [d #] Delete  [e #] Edit  [b] Back")
            cmd = input("  ▶  ").strip().lower()

            if cmd == "b":
                break
            elif cmd == "n":
                self.add_word()
            elif cmd.startswith("d "):
                try:
                    n = int(cmd[2:]) - 1
                    if 0 <= n < len(self.words):
                        removed = self.words.pop(n)
                        self.known.discard(n)
                        self.unknown.discard(n)
                        # Fix indices
                        self.known = {i if i < n else i - 1 for i in self.known}
                        self.unknown = {i if i < n else i - 1 for i in self.unknown}
                        self.save_data()
                        print(f"  🗑️  Deleted '{removed['en']}'")
                        input("  Press Enter...")
                except ValueError:
                    pass
            elif cmd.startswith("e "):
                try:
                    n = int(cmd[2:]) - 1
                    if 0 <= n < len(self.words):
                        w = self.words[n]
                        print(f"\n  Editing '{w['en']}' (leave blank to keep)")
                        en = input(f"  English [{w['en']}]: ").strip()
                        zh = input(f"  Chinese [{w['zh']}]: ").strip()
                        ex = input(f"  Example [{w['example']}]: ").strip()
                        if en:
                            w["en"] = en
                        if zh:
                            w["zh"] = zh
                        if ex:
                            w["example"] = ex
                        self.save_data()
                        print("  ✅ Updated!")
                        input("  Press Enter...")
                except ValueError:
                    pass

    def show_history(self):
        self.clear_screen()
        self.show_header("📜 HISTORY (last 50 entries)")
        recent = self.history[-50:]
        for h in reversed(recent):
            icon = "✅" if h["result"] == "known" else "❌"
            t = h["time"][:19].replace("T", " ")
            print(f"  {icon} {h['word']:20s} {t}")
        print()
        input("  Press Enter to continue...")

    def reset_progress(self):
        self.clear_screen()
        self.show_header("⚠️  RESET")
        confirm = input("  Reset all progress? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.known.clear()
            self.unknown.clear()
            self.history.clear()
            self.save_data()
            print("  ✅ Reset complete!")
        else:
            print("  ❌ Cancelled.")
        input("  Press Enter...")

if __name__ == "__main__":
    app = FlashcardApp()
    app.main_menu()
