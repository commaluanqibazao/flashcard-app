#!/usr/bin/env python3
"""Flashcard - Terminal English Vocabulary Trainer
   Word list: IT Due Diligence & IT Integration (CET-6+)"""

import json
import random
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "flashcard_data.json")

DEFAULT_WORDS = [
    # ── IT Due Diligence Core ──
    {"en": "due diligence", "zh": "尽职调查", "example": "The IT due diligence revealed significant technical debt."},
    {"en": "acquisition", "zh": "收购；并购", "example": "The acquisition target had outdated infrastructure."},
    {"en": "divestiture", "zh": "资产剥离；拆分", "example": "The divestiture required separating the IT systems."},
    {"en": "disposition", "zh": "处置；配置", "example": "Asset disposition must comply with data privacy laws."},
    {"en": "depreciation", "zh": "折旧；贬值", "example": "IT asset depreciation affects the valuation model."},
    {"en": "amortization", "zh": "摊销；分期偿还", "example": "Software capitalization requires amortization schedules."},
    {"en": "liability", "zh": "负债；责任", "example": "Contingent IT liabilities can derail a deal."},
    {"en": "contingency", "zh": "或有事项；应急方案", "example": "A contingency plan for data migration is critical."},
    {"en": "indemnification", "zh": "赔偿；补偿", "example": "The contract includes indemnification for data breaches."},
    {"en": "escrow", "zh": "第三方托管", "example": "Source code escrow protects the buyer post-acquisition."},
    {"en": "warranty", "zh": "保证；担保", "example": "Software warranty clauses must cover latent defects."},
    {"en": "representation", "zh": "陈述；声明", "example": "The seller's representations about IT assets were misleading."},
    {"en": "covenant", "zh": "契约；承诺", "example": "Transition service agreements contain restrictive covenants."},
    {"en": "materiality", "zh": "重要性；实质性", "example": "Materiality thresholds define which IT issues must be disclosed."},
    {"en": "discrepancy", "zh": "差异；不符", "example": "A discrepancy in software license counts was found."},
    {"en": "remediation", "zh": "补救；整改", "example": "Security remediation plans are a deliverable in the SPA."},
    {"en": "mitigation", "zh": "缓解；减轻", "example": "Risk mitigation strategies include insurance and escrow."},
    {"en": "appraisal", "zh": "评估；估价", "example": "IT asset appraisal impacts the purchase price allocation."},
    {"en": "valuation", "zh": "估值；定价", "example": "Technology valuation often uses the income approach."},
    {"en": "assessment", "zh": "评估；评定", "example": "A cybersecurity assessment is mandatory pre-close."},

    # ── IT Integration Strategy ──
    {"en": "integration", "zh": "整合；集成", "example": "Post-merger IT integration is the most complex workstream."},
    {"en": "consolidation", "zh": "整合；合并", "example": "Data center consolidation reduces operational costs."},
    {"en": "synergy", "zh": "协同效应", "example": "IT synergy targets are often overestimated in M&A."},
    {"en": "harmonization", "zh": "协调；统一", "example": "Policy harmonization across entities is a quick win."},
    {"en": "rationalization", "zh": "合理化；优化", "example": "Application portfolio rationalization eliminates redundancy."},
    {"en": "standardization", "zh": "标准化", "example": "Standardization of the tech stack accelerates integration."},
    {"en": "orchestration", "zh": "编排；协调", "example": "Integration orchestration tools automate data workflows."},
    {"en": "assimilation", "zh": "同化；吸收", "example": "Cultural assimilation is often harder than technical integration."},
    {"en": "alignment", "zh": "对齐；协同", "example": "IT alignment with business strategy is a due diligence focus."},
    {"en": "convergence", "zh": "融合；趋同", "example": "The convergence of IT and OT systems creates new risks."},
    {"en": "divergence", "zh": "分歧；差异", "example": "Process divergence between legacy systems complicates data mapping."},
    {"en": "interoperability", "zh": "互操作性", "example": "Interoperability between ERP systems is a key integration challenge."},
    {"en": "portability", "zh": "可移植性", "example": "Cloud workload portability enables multi-cloud strategies."},
    {"en": "compatibility", "zh": "兼容性", "example": "Backward compatibility affects the upgrade timeline."},
    {"en": "scalability", "zh": "可扩展性", "example": "Scalability assessment determines if infrastructure can handle growth."},
    {"en": "elasticity", "zh": "弹性；伸缩性", "example": "Cloud elasticity allows dynamic resource allocation."},
    {"en": "redundancy", "zh": "冗余；备份", "example": "Geographic redundancy ensures business continuity."},
    {"en": "resilience", "zh": "韧性；恢复力", "example": "System resilience is measured by RTO and RPO metrics."},
    {"en": "robustness", "zh": "健壮性；鲁棒性", "example": "The architecture robustness was validated through stress testing."},
    {"en": "modularity", "zh": "模块化", "example": "Modularity simplifies the separation of divested systems."},

    # ── M&A Lifecycle & Process ──
    {"en": "mandate", "zh": "授权；委托", "example": "The IT team received a mandate to complete integration within 12 months."},
    {"en": "stakeholder", "zh": "利益相关者", "example": "Stakeholder buy-in is critical for integration success."},
    {"en": "governance", "zh": "治理；管理", "example": "A joint integration governance board oversees decision-making."},
    {"en": "oversight", "zh": "监督；监管", "example": "Program oversight ensures integration milestones are met."},
    {"en": "deliverable", "zh": "可交付成果", "example": "The Day 1 deliverable checklist includes 47 items."},
    {"en": "milestone", "zh": "里程碑", "example": "Integration milestones are tracked in the PMO dashboard."},
    {"en": "gate", "zh": "关卡；审批节点", "example": "Phase gates require sign-off before proceeding to the next stage."},
    {"en": "escalation", "zh": "升级；上报", "example": "Severity-1 incidents require immediate escalation to the steering committee."},
    {"en": "triage", "zh": "分类；分诊", "example": "Integration issues are triaged by the joint operations team."},
    {"en": "reconciliation", "zh": "对账；调节", "example": "License reconciliation reveals over-deployment gaps."},
    {"en": "migration", "zh": "迁移；转移", "example": "Data migration is the highest-risk integration workstream."},
    {"en": "transition", "zh": "过渡；转型", "example": "The transition service agreement defines support duration."},
    {"en": "transformation", "zh": "转型；变革", "example": "Digital transformation initiatives often accelerate post-merger."},
    {"en": "dispositioning", "zh": "处置；安排", "example": "Surplus hardware dispositioning must follow environmental regulations."},
    {"en": "segregation", "zh": "隔离；分离", "example": "System segregation is required for regulatory compliance."},
    {"en": "carve-out", "zh": "剥离；分拆", "example": "A carve-out requires building standalone infrastructure."},
    {"en": "day-one readiness", "zh": "首日就绪", "example": "Day-one readiness validates that critical systems are operational at close."},
    {"en": "cutover", "zh": "切换；转换", "example": "The cutover window is limited to 48 hours over the weekend."},
    {"en": "rollback", "zh": "回滚；撤销", "example": "A rollback plan must be tested before any production migration."},
    {"en": "runbook", "zh": "操作手册；流程文档", "example": "The integration runbook contains step-by-step procedures for Day 1."},

    # ── Enterprise Architecture & Systems ──
    {"en": "architecture", "zh": "架构；体系结构", "example": "Enterprise architecture establishes principles for system design."},
    {"en": "infrastructure", "zh": "基础设施", "example": "Infrastructure due diligence covers network, storage, and compute."},
    {"en": "ecosystem", "zh": "生态系统", "example": "The legacy ecosystem consists of over 200 interconnected applications."},
    {"en": "middleware", "zh": "中间件", "example": "Middleware abstraction layers simplify integration between disparate systems."},
    {"en": "legacy system", "zh": "遗留系统", "example": "Legacy system decommissioning is a major cost synergy driver."},
    {"en": "monolith", "zh": "单体架构", "example": "Monolith-to-microservices migration is a multi-year transformation."},
    {"en": "microservices", "zh": "微服务", "example": "Microservices architecture enables independent deployability."},
    {"en": "containerization", "zh": "容器化", "example": "Containerization improves workload portability across environments."},
    {"en": "orchestrator", "zh": "编排器", "example": "Kubernetes is the dominant container orchestrator in enterprise IT."},
    {"en": "virtualization", "zh": "虚拟化", "example": "Server virtualization consolidation improves hardware utilization."},
    {"en": "hypervisor", "zh": "虚拟机监控器", "example": "The hypervisor layer abstracts hardware from guest operating systems."},
    {"en": "bare-metal", "zh": "裸机；物理机", "example": "Bare-metal performance is required for latency-sensitive workloads."},
    {"en": "cluster", "zh": "集群", "example": "The cluster configuration ensures high availability for critical services."},
    {"en": "federation", "zh": "联邦；联合", "example": "Identity federation enables single sign-on across merged entities."},
    {"en": "mesh", "zh": "网状；网格", "example": "Service mesh provides observability and traffic management."},
    {"en": "topology", "zh": "拓扑；布局", "example": "Network topology diagrams are essential for infrastructure assessment."},
    {"en": "discovery", "zh": "发现；探测", "example": "Discovery tools inventory all connected assets in the environment."},
    {"en": "dependency", "zh": "依赖关系", "example": "Application dependency mapping reveals hidden integration points."},
    {"en": "catalogue", "zh": "目录；清单", "example": "The service catalogue documents all IT offerings and their owners."},
    {"en": "repository", "zh": "存储库；仓库", "example": "Source code repository migration is often underestimated."},

    # ── Cloud Computing ──
    {"en": "hybrid cloud", "zh": "混合云", "example": "Hybrid cloud strategies balance on-premise control with cloud agility."},
    {"en": "multi-cloud", "zh": "多云", "example": "Multi-cloud deployments avoid vendor lock-in but increase complexity."},
    {"en": "tenancy", "zh": "租用；租户", "example": "Multi-tenancy architecture serves multiple clients from shared infrastructure."},
    {"en": "elasticity", "zh": "弹性伸缩", "example": "Auto-scaling policies ensure elasticity during demand spikes."},
    {"en": "provisioning", "zh": "配置；部署", "example": "Automated provisioning reduces infrastructure setup time."},
    {"en": "orchestration", "zh": "自动编排", "example": "Cloud orchestration tools manage infrastructure as code."},
    {"en": "abstraction", "zh": "抽象化", "example": "Abstraction layers decouple applications from underlying infrastructure."},
    {"en": "instance", "zh": "实例", "example": "Reserved instances reduce cloud costs by up to 60%."},
    {"en": "sizing", "zh": "规格确定", "example": "Proper sizing optimizes cost without sacrificing performance."},
    {"en": "consumption", "zh": "消费；用量", "example": "Cloud consumption models shift CAPEX to OPEX."},
    {"en": "on-premise", "zh": "本地部署", "example": "On-premise to cloud migration is a core integration workstream."},
    {"en": "co-location", "zh": "托管；共置", "example": "Co-location facilities provide physical security and connectivity."},
    {"en": "edge computing", "zh": "边缘计算", "example": "Edge computing reduces latency for IoT workloads."},
    {"en": "serverless", "zh": "无服务器", "example": "Serverless architectures abstract infrastructure management entirely."},
    {"en": "region", "zh": "区域；地区", "example": "Data residency requirements dictate which cloud regions are permissible."},
    {"en": "availability zone", "zh": "可用区", "example": "Availability zones provide fault isolation within a region."},
    {"en": "disaster recovery", "zh": "灾难恢复", "example": "Disaster recovery planning must account for cross-region replication."},
    {"en": "service-level agreement", "zh": "服务水平协议", "example": "SLA commitments define uptime guarantees and penalty structures."},
    {"en": "capacity planning", "zh": "容量规划", "example": "Capacity planning ensures infrastructure meets future demand."},
    {"en": "chargeback", "zh": "成本分摊；回充", "example": "Chargeback models allocate cloud costs to business units."},

    # ── Data Management ──
    {"en": "governance", "zh": "数据治理", "example": "Data governance frameworks define ownership, quality, and lineage."},
    {"en": "stewardship", "zh": "管理职责", "example": "Data stewardship assigns accountability for data quality."},
    {"en": "lineage", "zh": "血缘；溯源", "example": "Data lineage tracking helps with regulatory compliance."},
    {"en": "provenance", "zh": "来源；出处", "example": "Provenance metadata records the origin and transformation of data."},
    {"en": "fidelity", "zh": "保真度；精确性", "example": "Data fidelity during migration must be validated through reconciliation."},
    {"en": "integrity", "zh": "完整性；一致性", "example": "Referential integrity constraints prevent orphaned records."},
    {"en": "deduplication", "zh": "去重", "example": "Data deduplication reduces storage footprint and migration volume."},
    {"en": "normalization", "zh": "归一化；规范化", "example": "Data normalization resolves format discrepancies across sources."},
    {"en": "canonical", "zh": "规范的；标准的", "example": "A canonical data model simplifies integration between systems."},
    {"en": "schema", "zh": "模式；架构", "example": "Schema mapping is the most time-consuming integration activity."},
    {"en": "extraction", "zh": "提取", "example": "ETL processes handle extraction from hundreds of source systems."},
    {"en": "transformation", "zh": "转换", "example": "Data transformation rules must be documented and tested."},
    {"en": "loading", "zh": "加载", "example": "Bulk loading performance impacts the migration timeline."},
    {"en": "warehouse", "zh": "数据仓库", "example": "Enterprise data warehouse consolidation is a major synergy initiative."},
    {"en": "lake", "zh": "数据湖", "example": "A data lake architecture accommodates structured and unstructured data."},
    {"en": "marshaling", "zh": "编排；序列化", "example": "Data marshaling converts objects for network transmission."},
    {"en": "synchronization", "zh": "同步", "example": "Real-time synchronization is required between merged CRM platforms."},
    {"en": "replication", "zh": "复制", "example": "Database replication ensures data availability during cutover."},
    {"en": "archival", "zh": "归档", "example": "Data archival policies balance retention requirements with storage costs."},
    {"en": "purge", "zh": "清除；销毁", "example": "Secure data purge processes are required before system decommissioning."},

    # ── Security & Compliance ──
    {"en": "encryption", "zh": "加密", "example": "End-to-end encryption protects data in transit and at rest."},
    {"en": "cipher", "zh": "密码；加密算法", "example": "Weak cipher suites must be deprecated during security hardening."},
    {"en": "authentication", "zh": "身份验证", "example": "Multi-factor authentication is a mandatory security control."},
    {"en": "authorization", "zh": "授权；权限", "example": "Role-based authorization restricts access to sensitive systems."},
    {"en": "entitlement", "zh": "权限；权利", "example": "Entitlement reviews ensure access is aligned with current roles."},
    {"en": "attestation", "zh": "认证；证明", "example": "SOC2 attestation is a common due diligence requirement."},
    {"en": "certification", "zh": "认证；证书", "example": "SSL certificate inventory is often overlooked in ITDD."},
    {"en": "penetration", "zh": "渗透", "example": "Penetration testing reveals exploitable vulnerabilities."},
    {"en": "vulnerability", "zh": "漏洞；脆弱性", "example": "Vulnerability management programs prioritize remediation based on CVSS scores."},
    {"en": "exploit", "zh": "利用；漏洞利用", "example": "Zero-day exploits pose significant risk to merged networks."},
    {"en": "breach", "zh": "违规；泄露", "example": "A historical data breach must be disclosed during due diligence."},
    {"en": "incident", "zh": "事件；安全事故", "example": "Incident response playbooks must be harmonized post-merger."},
    {"en": "forensic", "zh": "法医的；取证", "example": "Digital forensic analysis is required for breach investigation."},
    {"en": "audit trail", "zh": "审计轨迹", "example": "An immutable audit trail satisfies regulatory record-keeping requirements."},
    {"en": "segregation of duties", "zh": "职责分离", "example": "Segregation of duties prevents insider fraud in financial systems."},
    {"en": "privilege", "zh": "权限；特权", "example": "Least-privilege principles limit lateral movement in case of compromise."},
    {"en": "compliance", "zh": "合规；遵循", "example": "Regulatory compliance spans GDPR, SOX, HIPAA, and PCI-DSS."},
    {"en": "jurisdiction", "zh": "管辖范围；司法权", "example": "Data jurisdiction determines which legal frameworks apply."},
    {"en": "sovereignty", "zh": "主权；自主权", "example": "Data sovereignty laws restrict cross-border data transfers."},
    {"en": "sanction", "zh": "制裁；处罚", "example": "Non-compliance with export controls can result in severe sanctions."},

    # ── Networking & Infrastructure ──
    {"en": "latency", "zh": "延迟", "example": "Network latency between merged offices affects application performance."},
    {"en": "throughput", "zh": "吞吐量", "example": "Throughput capacity must be assessed for video conferencing workloads."},
    {"en": "subnet", "zh": "子网", "example": "Subnet conflicts between merging entities require IP re-addressing."},
    {"en": "gateway", "zh": "网关", "example": "API gateway consolidation simplifies the integration architecture."},
    {"en": "proxy", "zh": "代理服务器", "example": "Reverse proxy configuration must be updated during network integration."},
    {"en": "firewall", "zh": "防火墙", "example": "Firewall rule consolidation reduces the attack surface area."},
    {"en": "load balancer", "zh": "负载均衡器", "example": "Load balancer configuration ensures even traffic distribution."},
    {"en": "peering", "zh": "对等连接", "example": "Direct peering between cloud VPCs reduces data transfer costs."},
    {"en": "tunneling", "zh": "隧道技术", "example": "VPN tunneling provides encrypted connectivity during transitional phases."},
    {"en": "backbone", "zh": "骨干网", "example": "The network backbone must support double the combined traffic."},
    {"en": "segmentation", "zh": "分段；隔离", "example": "Network segmentation limits blast radius in security incidents."},
    {"en": "demilitarized zone", "zh": "隔离区(DMZ)", "example": "DMZ architecture exposes public-facing services while protecting internal networks."},
    {"en": "anycast", "zh": "任播", "example": "Anycast routing improves DNS resolution performance globally."},
    {"en": "multicast", "zh": "组播", "example": "Multicast traffic management is critical for financial trading systems."},
    {"en": "jitter", "zh": "抖动", "example": "Jitter buffers compensate for variable packet arrival times."},
    {"en": "bandwidth", "zh": "带宽", "example": "Bandwidth provisioning must account for data replication traffic."},
    {"en": "contention", "zh": "争用；竞争", "example": "Network contention affects application performance during peak usage."},
    {"en": "observability", "zh": "可观测性", "example": "Observability platforms consolidate logs, metrics, and traces."},
    {"en": "telemetry", "zh": "遥测", "example": "Infrastructure telemetry feeds the central monitoring system."},
    {"en": "saturation", "zh": "饱和", "example": "Port saturation indicates insufficient network capacity."},

    # ── Software & Systems Engineering ──
    {"en": "lifecycle", "zh": "生命周期", "example": "Software development lifecycle methodology affects delivery velocity."},
    {"en": "deployment", "zh": "部署", "example": "Continuous deployment pipelines accelerate time-to-market."},
    {"en": "provisioning", "zh": "资源调配", "example": "Infrastructure provisioning is fully automated via Terraform."},
    {"en": "configuration", "zh": "配置", "example": "Configuration drift between environments causes deployment failures."},
    {"en": "refactoring", "zh": "重构", "example": "Legacy code refactoring is necessary before system integration."},
    {"en": "deprecation", "zh": "弃用", "example": "API deprecation timelines must be communicated to all consumers."},
    {"en": "decommissioning", "zh": "退役；停用", "example": "System decommissioning includes secure data disposal."},
    {"en": "migration path", "zh": "迁移路径", "example": "A phased migration path minimizes business disruption."},
    {"en": "parallel run", "zh": "并行运行", "example": "A parallel run validates system behavior before the final cutover."},
    {"en": "fallback", "zh": "回退；备用", "example": "The fallback procedure restores the previous state within four hours."},
    {"en": "rollforward", "zh": "前滚", "example": "Transaction log rollforward recovers data to the point of failure."},
    {"en": "reconciliation", "zh": "对账", "example": "Financial reconciliation between legacy and new systems is mandatory."},
    {"en": "validation", "zh": "验证", "example": "Post-migration validation confirms data completeness."},
    {"en": "verification", "zh": "核实；检验", "example": "Independent verification ensures integration meets requirements."},
    {"en": "acceptance", "zh": "验收", "example": "User acceptance testing is the final gate before go-live."},
    {"en": "certification", "zh": "认证审查", "example": "Production readiness certification requires all test cases to pass."},
    {"en": "conformance", "zh": "符合性；一致性", "example": "Standards conformance ensures interoperability across the ecosystem."},
    {"en": "maturity", "zh": "成熟度", "example": "CMMI maturity level influences process reliability assessment."},
    {"en": "capability", "zh": "能力；功能", "example": "IT capability maturity is a key dimension of due diligence."},
    {"en": "roadmap", "zh": "路线图", "example": "The integration roadmap spans twelve quarters post-close."},

    # ── DevOps & CI/CD ──
    {"en": "continuous integration", "zh": "持续集成", "example": "Continuous integration detects merge conflicts early."},
    {"en": "continuous delivery", "zh": "持续交付", "example": "Continuous delivery automates the release pipeline."},
    {"en": "pipeline", "zh": "流水线", "example": "CI/CD pipeline consolidation accelerates software delivery."},
    {"en": "artifact", "zh": "构建产物", "example": "Artifact repository migration is often underestimated."},
    {"en": "registry", "zh": "注册表；仓库", "example": "Container image registries must be federated post-merger."},
    {"en": "blue-green", "zh": "蓝绿部署", "example": "Blue-green deployment minimizes downtime during releases."},
    {"en": "canary", "zh": "金丝雀发布", "example": "Canary releases limit blast radius of defective deployments."},
    {"en": "immutable", "zh": "不可变的", "example": "Immutable infrastructure eliminates configuration drift."},
    {"en": "idempotent", "zh": "幂等的", "example": "Idempotent deployment scripts ensure consistent results."},
    {"en": "idempotency", "zh": "幂等性", "example": "Idempotency is a fundamental principle of infrastructure automation."},
    {"en": "observability", "zh": "可观测性(运维)", "example": "Observability pillars are logs, metrics, and distributed traces."},
    {"en": "instrumentation", "zh": "探针；工具化", "example": "Application instrumentation provides granular performance data."},
    {"en": "tracing", "zh": "链路追踪", "example": "Distributed tracing identifies bottlenecks across microservices."},
    {"en": "profiling", "zh": "性能分析", "example": "CPU profiling reveals performance hotspots in the codebase."},
    {"en": "benchmarking", "zh": "基准测试", "example": "Performance benchmarking establishes baseline metrics for comparison."},
    {"en": "saturation", "zh": "饱和(性能)", "example": "Resource saturation thresholds trigger auto-scaling policies."},
    {"en": "latency", "zh": "响应延迟", "example": "P99 latency targets must be maintained during data migration."},
    {"en": "tail latency", "zh": "尾部延迟", "example": "Tail latency optimization is critical for real-time systems."},
    {"en": "chaos engineering", "zh": "混沌工程", "example": "Chaos engineering validates system resilience under failure conditions."},
    {"en": "site reliability", "zh": "站点可靠性", "example": "Site reliability engineering adopts software approaches to operations."},

    # ── Cybersecurity & Risk ──
    {"en": "cybersecurity", "zh": "网络安全", "example": "Cybersecurity due diligence assesses the target's security posture."},
    {"en": "threat", "zh": "威胁", "example": "Advanced persistent threats require continuous monitoring."},
    {"en": "vulnerability", "zh": "安全漏洞", "example": "Vulnerability scanning must cover all acquired assets."},
    {"en": "exploitability", "zh": "可利用性", "example": "Exploitability scores drive remediation prioritization."},
    {"en": "exfiltration", "zh": "数据泄露(外传)", "example": "Data exfiltration prevention requires network egress monitoring."},
    {"en": "ransomware", "zh": "勒索软件", "example": "Ransomware resilience is a key due diligence consideration."},
    {"en": "phishing", "zh": "钓鱼攻击", "example": "Phishing simulation results indicate security awareness levels."},
    {"en": "spoofing", "zh": "欺骗；伪造", "example": "Email spoofing protections include SPF, DKIM, and DMARC."},
    {"en": "impersonation", "zh": "冒充；仿冒", "example": "Executive impersonation attacks target finance departments."},
    {"en": "social engineering", "zh": "社会工程学", "example": "Social engineering tests reveal procedural vulnerabilities."},
    {"en": "reconnaissance", "zh": "侦察", "example": "Network reconnaissance is often the first phase of an attack."},
    {"en": "lateral movement", "zh": "横向移动", "example": "Network segmentation limits lateral movement post-breach."},
    {"en": "persistence", "zh": "持久化", "example": "Attackers establish persistence through scheduled tasks or backdoors."},
    {"en": "privilege escalation", "zh": "权限提升", "example": "Privilege escalation vulnerabilities must be patched urgently."},
    {"en": "hardening", "zh": "加固；强化", "example": "System hardening checklists are part of integration security activities."},
    {"en": "patching", "zh": "补丁管理", "example": "Patch management maturity indicates operational discipline."},
    {"en": "zero trust", "zh": "零信任", "example": "Zero trust architecture assumes breach and verifies every request."},
    {"en": "defense-in-depth", "zh": "纵深防御", "example": "Defense-in-depth strategies layer preventive, detective, and corrective controls."},
    {"en": "compensating control", "zh": "补偿性控制", "example": "Compensating controls mitigate risk when primary controls are infeasible."},
    {"en": "residual risk", "zh": "残余风险", "example": "Residual risk is accepted only when within the defined appetite."},

    # ── Regulatory & Legal ──
    {"en": "compliance", "zh": "法规遵从", "example": "SOX compliance requires IT general control documentation."},
    {"en": "regulatory", "zh": "监管的", "example": "Regulatory filings must disclose material IT risks."},
    {"en": "statutory", "zh": "法定的", "example": "Statutory data retention periods vary by jurisdiction."},
    {"en": "fiduciary", "zh": "信义；受托的", "example": "Directors have fiduciary duties to oversee cybersecurity risks."},
    {"en": "disclosure", "zh": "披露；公开", "example": "Material cybersecurity disclosures are required in SEC filings."},
    {"en": "promulgation", "zh": "颁布；发布", "example": "Policy promulgation ensures all employees are aware of new standards."},
    {"en": "adjudication", "zh": "裁决；判定", "example": "Dispute adjudication clauses define arbitration for IT service disagreements."},
    {"en": "arbitration", "zh": "仲裁", "example": "IT service disputes are subject to binding arbitration."},
    {"en": "litigation", "zh": "诉讼", "example": "IP litigation risks must be assessed during due diligence."},
    {"en": "indemnity", "zh": "赔偿(条款)", "example": "Data breach indemnity clauses are heavily negotiated in IT contracts."},
    {"en": "exposure", "zh": "风险敞口", "example": "IT risk exposure includes cybersecurity, compliance, and operational dimensions."},
    {"en": "provision", "zh": "条款；准备金", "example": "Contract provisions for software maintenance must be reviewed."},
    {"en": "stipulation", "zh": "规定；约定", "example": "Transition service agreements include stipulations on service levels."},
    {"en": "accrual", "zh": "应计；累积", "example": "IT project accruals affect the net working capital adjustment."},
    {"en": "depreciation", "zh": "折旧(财务)", "example": "Accelerated depreciation models apply to IT equipment less than three years old."},
    {"en": "capitalization", "zh": "资本化", "example": "Software development costs eligible for capitalization follow ASC 350-40."},
    {"en": "impairment", "zh": "减值", "example": "Goodwill impairment can result from overpaying for IT capabilities."},
    {"en": "contingent consideration", "zh": "或有对价", "example": "Earn-out structures link contingent consideration to IT integration milestones."},
    {"en": "earn-out", "zh": "盈利能力支付计划", "example": "IT integration delays can trigger earn-out disputes."},
    {"en": "escrow release", "zh": "第三方托管释放", "example": "Escrow release conditions are tied to IT integration completion certificates."},

    # ── IT Operations & Service Management ──
    {"en": "incident management", "zh": "事件管理", "example": "Incident management processes must be unified within 90 days."},
    {"en": "problem management", "zh": "问题管理", "example": "Root cause analysis is the core of problem management."},
    {"en": "change management", "zh": "变更管理", "example": "Change advisory board approval is required for production changes."},
    {"en": "release management", "zh": "发布管理", "example": "Release management coordinates deployment across multiple systems."},
    {"en": "configuration management", "zh": "配置管理", "example": "Configuration management database consolidation is a foundational activity."},
    {"en": "asset management", "zh": "资产管理", "example": "IT asset management tracks hardware and software throughout the lifecycle."},
    {"en": "capacity management", "zh": "容量管理", "example": "Capacity management ensures resources meet future demand."},
    {"en": "availability management", "zh": "可用性管理", "example": "Availability management targets 99.99% uptime for critical systems."},
    {"en": "continuity management", "zh": "连续性管理", "example": "Business continuity management includes IT disaster recovery plans."},
    {"en": "service catalog", "zh": "服务目录", "example": "The service catalog must be harmonized across merged entities."},
    {"en": "service desk", "zh": "服务台", "example": "Service desk consolidation reduces operational overhead."},
    {"en": "fulfillment", "zh": "履行；交付", "example": "Service request fulfillment automation improves efficiency."},
    {"en": "SLA breach", "zh": "服务协议违约", "example": "SLA breach penalties are calculated based on downtime duration."},
    {"en": "KPI", "zh": "关键绩效指标", "example": "IT KPIs track integration progress against the business case."},
    {"en": "dashboard", "zh": "仪表盘", "example": "The integration dashboard provides real-time status of all workstreams."},
    {"en": "playbook", "zh": "行动手册", "example": "The integration playbook documents standard operating procedures."},
    {"en": "RACI", "zh": "责任分配矩阵", "example": "RACI matrix clarifies decision rights for integration activities."},
    {"en": "service-level objective", "zh": "服务等级目标", "example": "SLOs define measurable targets for system reliability."},
    {"en": "error budget", "zh": "错误预算", "example": "Error budget policies balance reliability against feature velocity."},
    {"en": "post-mortem", "zh": "事后剖析", "example": "Post-mortem reports drive continuous improvement in IT operations."},

    # ── Strategy & Management Consulting ──
    {"en": "synergy capture", "zh": "协同效应实现", "example": "Synergy capture tracking ensures integration delivers projected value."},
    {"en": "value realization", "zh": "价值实现", "example": "Value realization milestones are tied to executive compensation."},
    {"en": "business case", "zh": "商业论证", "example": "The IT business case must demonstrate ROI within three years."},
    {"en": "target operating model", "zh": "目标运营模式", "example": "The target operating model defines the future-state IT organization."},
    {"en": "operating model", "zh": "运营模式", "example": "IT operating model design spans people, process, and technology."},
    {"en": "organizational design", "zh": "组织设计", "example": "Organizational design determines reporting lines and spans of control."},
    {"en": "span of control", "zh": "管理幅度", "example": "A lean IT organization typically has a span of control of 7 to 10."},
    {"en": "center of excellence", "zh": "卓越中心", "example": "A Cloud CoE establishes best practices and governance frameworks."},
    {"en": "shared services", "zh": "共享服务中心", "example": "IT shared services consolidation eliminates duplicate functions."},
    {"en": "insourcing", "zh": "内部化；内包", "example": "Insourcing previously outsourced IT functions may increase control."},
    {"en": "outsourcing", "zh": "外包", "example": "IT outsourcing contracts require due diligence on vendor stability."},
    {"en": "co-sourcing", "zh": "合作外包", "example": "Co-sourcing arrangements blend internal and external teams."},
    {"en": "offshoring", "zh": "离岸外包", "example": "Offshoring labor arbitrage must be balanced with communication overhead."},
    {"en": "nearshoring", "zh": "近岸外包", "example": "Nearshoring reduces time zone differences compared to traditional offshoring."},
    {"en": "subcontractor", "zh": "分包商", "example": "Subcontractor risk flows through the prime vendor relationship."},
    {"en": "prime vendor", "zh": "主供应商", "example": "Prime vendor consolidation simplifies procurement and reduces costs."},
    {"en": "retainer", "zh": "顾问聘用金", "example": "IT advisory retainers provide access to specialized expertise."},
    {"en": "statement of work", "zh": "工作说明书", "example": "SOW scope creep is a common source of integration cost overruns."},
    {"en": "workstream", "zh": "工作流；工作包", "example": "The integration program comprises twelve parallel workstreams."},
    {"en": "work package", "zh": "工作包", "example": "Each work package has defined deliverables, budget, and owner."},

    # ── Financial & Commercial IT Terms ──
    {"en": "capital expenditure", "zh": "资本支出(CAPEX)", "example": "IT CAPEX budgets cover hardware, software, and infrastructure."},
    {"en": "operational expenditure", "zh": "运营支出(OPEX)", "example": "Cloud migration shifts IT costs from CAPEX to OPEX."},
    {"en": "total cost of ownership", "zh": "总拥有成本", "example": "TCO analysis compares on-premise versus cloud deployment costs."},
    {"en": "return on investment", "zh": "投资回报率", "example": "IT integration ROI is measured against synergy targets."},
    {"en": "net present value", "zh": "净现值", "example": "NPV calculations discount projected IT synergy cash flows."},
    {"en": "internal rate of return", "zh": "内部收益率", "example": "IRR thresholds determine which integration projects are approved."},
    {"en": "payback period", "zh": "回收期", "example": "The integration investment has a targeted payback period of 18 months."},
    {"en": "run-rate", "zh": "年化运行率", "example": "IT run-rate cost analysis informs the synergy baseline."},
    {"en": "baseline", "zh": "基线；基准", "example": "IT cost baseline must be established before measuring synergies."},
    {"en": "benchmark", "zh": "基准参照", "example": "IT spending benchmarks compare cost against industry peers."},
    {"en": "cost avoidance", "zh": "成本规避", "example": "Consolidation-driven cost avoidance is softer than direct cost reduction."},
    {"en": "cost reduction", "zh": "成本削减", "example": "Headcount reduction is the largest IT cost reduction lever."},
    {"en": "overhead", "zh": "间接费用", "example": "IT overhead allocation methodologies impact business unit profitability."},
    {"en": "allocation", "zh": "分摊；分配", "example": "IT cost allocation models must be agreed upon early."},
    {"en": "procurement", "zh": "采购", "example": "IT procurement consolidation leverages vendor volume discounts."},
    {"en": "sourcing", "zh": "寻源；采购策略", "example": "Strategic sourcing evaluates vendor alternatives for major IT categories."},
    {"en": "negotiation", "zh": "谈判；协商", "example": "Vendor contract renegotiation achieves 15-20% cost savings."},
    {"en": "leverage", "zh": "杠杆；优势", "example": "Combined purchasing leverage improves vendor pricing terms."},
    {"en": "discount", "zh": "折扣；折让", "example": "Enterprise license agreement discounts depend on commitment volume."},
    {"en": "true-up", "zh": "调整；补足", "example": "Annual license true-up reconciles deployed versus purchased quantities."},

    # ── Advanced & Specialized ──
    {"en": "as-is", "zh": "现状(as-is)", "example": "The as-is assessment documents all current systems and processes."},
    {"en": "to-be", "zh": "目标状态(to-be)", "example": "The to-be architecture defines the target integration state."},
    {"en": "disparate", "zh": "不同的；异质的", "example": "Disparate legacy systems must be integrated into a unified platform."},
    {"en": "heterogeneous", "zh": "异构的", "example": "Heterogeneous environments increase integration complexity."},
    {"en": "homogeneous", "zh": "同构的", "example": "A homogeneous tech stack simplifies maintenance and reduces costs."},
    {"en": "bespoke", "zh": "定制的；专属的", "example": "Bespoke applications require specialized knowledge to maintain."},
    {"en": "off-the-shelf", "zh": "现成的；成品", "example": "Off-the-shelf software is preferred over custom development."},
    {"en": "greenfield", "zh": "全新建设；绿地", "example": "A greenfield implementation avoids legacy constraints."},
    {"en": "brownfield", "zh": "已有环境改造；棕地", "example": "Brownfield integration must coexist with existing systems."},
    {"en": "rip-and-replace", "zh": "完全替换", "example": "Rip-and-replace strategies carry higher risk than phased migration."},
    {"en": "lift-and-shift", "zh": "直接迁移(平移)", "example": "Lift-and-shift migration minimizes application changes."},
    {"en": "strangler pattern", "zh": "绞杀者模式", "example": "The strangler pattern incrementally replaces legacy functionality."},
    {"en": "big bang", "zh": "大爆炸式上线", "example": "Big bang cutover carries significant execution risk."},
    {"en": "phased rollout", "zh": "分阶段部署", "example": "A phased rollout reduces risk by limiting change scope."},
    {"en": "proof of concept", "zh": "概念验证", "example": "A proof of concept validates technical feasibility before full investment."},
    {"en": "minimum viable product", "zh": "最小可行产品", "example": "The MVP approach delivers value early and iterates based on feedback."},
    {"en": "technical debt", "zh": "技术债务", "example": "Technical debt assessment is a critical due diligence deliverable."},
    {"en": "technical debt ratio", "zh": "技术债务比率", "example": "A technical debt ratio above 20% indicates significant remediation needs."},
    {"en": "hairball", "zh": "错综复杂的集成", "example": "The application hairball makes system separation extremely difficult."},
    {"en": "spaghetti architecture", "zh": "意大利面式架构", "example": "Spaghetti architecture results from years of ad-hoc integrations."},
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
