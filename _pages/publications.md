---
permalink: /publications/
title: "Publications"
excerpt: "Research publications by Shenghui Li on efficient AI, low-rank adaptation, and federated learning."
---

<div class="section-heading"><h1>Publications</h1><a href="{{ site.author.googlescholar }}">Google Scholar <span aria-hidden="true">↗</span></a></div>
<p class="section-intro">A full list of the work featured on this site, from efficient foundation model adaptation to robust distributed learning.</p>

<h2>Recent &amp; selected research</h2>
<ol class="publication-list">
{% for paper in site.data.research %}
  <li><a href="{{ paper.paper }}">{{ paper.title }}</a><p class="publication-meta"><span class="publication-authors">{{ paper.authors }}</span> <span aria-hidden="true">·</span> <span class="publication-venue">{{ paper.venue }}</span>{% if paper.acceptance_rate %} · Acceptance rate: {{ paper.acceptance_rate }}{% endif %}</p></li>
{% endfor %}
</ol>

## Journal articles

- [An Experimental Study of Byzantine-Robust Aggregation Schemes in Federated Learning](https://ieeexplore.ieee.org/abstract/document/10018261), **Shenghui Li**, Edith C. H. Ngai, Thiemo Voigt, IEEE Transactions on Big Data (TBD), 2023
- [Byzantine-Robust Aggregation in Federated Learning Empowered Industrial IoT](https://ieeexplore.ieee.org/abstract/document/9614992), **Shenghui Li**, Edith C. H. Ngai, Thiemo Voigt, IEEE Transactions on Industrial Informatics (TII), 2023
- [Auto-weighted robust federated learning with corrupted data sources](https://dl.acm.org/doi/full/10.1145/3517821), **Shenghui Li**, Edith C. H. Ngai, Fanghua
  Ye, Thiemo Voigt, ACM Transactions on Intelligent Systems and Technology (TIST),
  2022
- [Makespan-minimized computation offloading for smart toys in edge-cloud computing](https://www.sciencedirect.com/science/article/pii/S1567422319300614), **Shenghui
  Li**, Wuhui Chen, Yufen Chen, Chuan Chen, Zibin Zheng, Electronic Commerce
  Research and Applications, 2019
- [Energy-efficient data routing in cooperative UAV swarms for medical assistance
  after a disaster](https://aip.scitation.org/doi/abs/10.1063/1.5092740), Yuanhao
  Yang, Xiaoyu Qiu, **Shenghui Li**, Junbo Wang, Wuhui Chen, Patrick CK Hung, Zibin
  Zheng, Chaos: An Interdisciplinary Journal of Nonlinear Science (CHAOS), 2019


## Other conference papers

- [Blades: A Unified Benchmark Suite for Byzantine Attacks and Defenses in Federated Learning](https://arxiv.org/abs/2206.05359), **Shenghui Li**, Edith C. H. Ngai, Fanghua Ye, Li Ju, Tianru Zhang, Thiemo Voigt, ACM/IEEE IoTDI, 2024

- [Enhancing Conversational Search: Large Language Model-Aided Informative Query Rewriting](https://arxiv.org/abs/2310.09716), Fanghua Ye, Meng Fang, **Shenghui Li**, Emine Yilmaz, The Conference on Empirical Methods in Natural
  Language Processing (EMNLP), 2023
- [MetaASSIST: Robust Dialogue State Tracking with Meta Learning](https://arxiv.org/abs/2210.12397), Fanghua Ye, Xi Wang, Jie Huang, **Shenghui Li**,
    Samuel Stern, and Emine Yilmaz, The Conference on Empirical Methods in Natural
  Language Processing (EMNLP), 2022
- [Slot self-attentive dialogue state tracking](https://dl.acm.org/doi/abs/10.1145/3442381.3449939),
  Fanghua Ye, Jarana Manotumruksa, Qiang Zhang, **Shenghui Li**,
  Emine Yilmaz, Proceedings of the Web Conference, 2021
- [Smart contract-based hierarchical auction mechanism for edge computing in
  blockchain-empowered IoT](https://ieeexplore.ieee.org/abstract/document/9217781/),
  Hui Lin, Zetao Yang, Zicong Hong, **Shenghui Li**, Wuhui Chen, IEEE 21st
  International Symposium on" A World of Wireless, Mobile and Multimedia Networks"
  (WoWMoM), 2020
- [Perishable Digital Goods Trading Mechanism for Blockchain-Based Vehicular Network](https://ieeexplore.ieee.org/abstract/document/9047309/), Rui Xi, Kang Liu, Shuo
  Liu, Wuhui Chen, **Shenghui Li**, IEEE Intl Conf on Parallel & Distributed
  Processing with Applications, Big Data & Cloud Computing, Sustainable Computing &
  Communications, Social Computing & Networking (ISPA/BDCloud/SocialCom/SustainCom),
  2019
- [Generative adversarial network based service recommendation in heterogeneous
  information networks](https://ieeexplore.ieee.org/abstract/document/8818434/),
  Fenfang Xie, **Shenghui Li**, Liang Chen, Yangjun Xu, Zibin Zheng, IEEE
  International Conference on Web Services (ICWS), 2019
- [Adaptive affinity learning for accurate community detection](https://ieeexplore.ieee.org/abstract/document/8594997/),
  Fanghua Ye, **Shenghui Li**, Zhiwei Lin, Chuan
  Chen, Zibin Zheng,  IEEE International Conference on Data Mining (ICDM), 2018
- [Latency-aware task assignment and scheduling in collaborative cloud robotic
  systems](https://ieeexplore.ieee.org/abstract/document/8457784/), **Shenghui Li**,
  Zhiheng Zheng, Wuhui Chen, Zibin Zheng, Junbo Wang, IEEE 11th International
  Conference on Cloud Computing (CLOUD), 2018
