---
permalink: /
title: ""
excerpt: "Shenghui Li — efficient foundation model adaptation, LoRA compression, and distributed learning systems."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="homepage">
<section id="about-me" class="about-section" aria-labelledby="about-title">
  <h1 id="about-title">About Me</h1>
  <p>I am a postdoctoral researcher in the Department of Electrical Engineering at Uppsala University, working with <a href="https://www.katalog.uu.se/profile/?id=N2-279">Prof. Thiemo Voigt</a>. I received my PhD from Uppsala University in January 2025, supervised by <a href="https://www.eee.hku.hk/people/echngai/">Prof. Edith C. H. Ngai</a>.</p>
  <p>I develop methods and systems that make foundation model adaptation more efficient under compute, memory, and communication constraints. My current work focuses on <strong>LoRA compression, multi-adapter serving, and federated adaptation</strong>, building on my earlier research in robust federated learning.</p>
  <div class="opportunity-note">
    <span class="opportunity-label">On the job market</span>
    <p>I’m currently on the job market, exploring opportunities in both industry and academia, with a focus on <strong>Efficient AI, LLM Post-Training, and Distributed RL</strong>. <a href="mailto:{{ site.author.email }}">Get in touch <span aria-hidden="true">↗</span></a></p>
  </div>
</section>

<section id="news" aria-labelledby="news-title">
  <h2 id="news-title">Recent News</h2>
  <ul class="news-list">
    <li><time datetime="2026-11">Nov 2026</time><span><a href="{{ '/fraq/' | relative_url }}">FraQ</a> accepted at <strong>EACL 2027</strong>.</span></li>
    <li><time datetime="2026-10">Oct 2026</time><span><a href="https://openreview.net/forum?id=CvmRAXEk8B">LoRA on a Budget</a> accepted at <strong>NeuralArtifacts@NeurIPS</strong>.</span></li>
    <li><time datetime="2025-08">Aug 2025</time><span>Our team won <strong>1st place</strong> at <a href="https://techarena-sweden.hackathon.com/">Huawei Sweden Tech Arena 2025</a>.</span></li>
  </ul>
  <details class="news-archive">
    <summary>Earlier news</summary>
    <ul class="news-list">
      <li><time datetime="2025-01">Jan 2025</time><span>Defended my PhD thesis, <a href="https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1914990">Robust Federated Learning: Defending Against Byzantine and Jailbreak Attacks</a>.</span></li>
      <li><time datetime="2024-01">Jan 2024</time><span><a href="https://arxiv.org/abs/2206.05359">Blades</a> accepted at <strong>IoTDI 2024</strong>.</span></li>
      <li><time datetime="2023-12">Dec 2023</time><span>Our team placed <strong>3rd</strong> at the <a href="https://www.agorize.com/en/challenges/huawei-sweden-hackathon-2023">Huawei Sweden Hackathon</a> for a cost-effective RAN computing solution.</span></li>
      <li><time datetime="2023-01">Jan 2023</time><span>Our experimental study of Byzantine-robust aggregation was accepted by <strong>IEEE Transactions on Big Data</strong>.</span></li>
    </ul>
  </details>
</section>

<section id="research" aria-labelledby="research-title">
  <div class="section-heading"><h2 id="research-title">Selected Research</h2><a href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">→</span></a></div>
  {% for paper in site.data.research %}{% include research-item.html %}{% endfor %}
</section>

<section id="open-source" aria-labelledby="open-source-title">
  <h2 id="open-source-title">Open Source</h2>
  <div class="project-list">
    <article class="project-item">
      <a class="project-image project-image--logo" href="https://github.com/lishenghui/loraforge"><img src="{{ '/images/research/loraforge-logo.png' | relative_url }}" width="1254" height="1254" alt="LoRAForge logo: a hammer striking a glowing anvil shaped like the letter F" loading="lazy"></a>
      <div><h3><a href="https://github.com/lishenghui/loraforge">LoRAForge</a></h3><p>Compress trained LoRA adapters and run them through a retained-rank-aware serving backend. Connects research methods to GPU execution.</p><div class="resource-links"><a href="https://github.com/lishenghui/loraforge">Code &amp; documentation <span aria-hidden="true">↗</span></a></div></div>
    </article>
    <article class="project-item">
      <a class="project-image project-image--logo" href="https://github.com/lishenghui/blades"><img src="{{ '/images/research/blades-logo.png' | relative_url }}" width="2000" height="2000" alt="Blades logo: a purple shield with silver blades and connected nodes" loading="lazy"></a>
      <div><h3><a href="https://github.com/lishenghui/blades">Blades</a></h3><p>Compare Byzantine attacks and defenses in one federated learning benchmark, with shared evaluation pipelines and reproducible experiments.</p><div class="resource-links"><a href="https://github.com/lishenghui/blades">Code &amp; documentation <span aria-hidden="true">↗</span></a></div></div>
    </article>
  </div>
</section>

<section id="experience" aria-labelledby="experience-title">
  <h2 id="experience-title">Experience &amp; Education</h2>
  <div class="timeline">
    <div class="timeline-item"><span class="timeline-date">Current</span><div><h3>Postdoctoral Researcher</h3><p>Department of Electrical Engineering, Uppsala University</p></div></div>
    <div class="timeline-item" id="education"><span class="timeline-date">2019 – 2025</span><div><h3>PhD · Uppsala University</h3><p>Department of Information Technology · Uppsala, Sweden</p></div></div>
    <div class="timeline-item"><span class="timeline-date">2017 – 2019</span><div><h3>Sun Yat-Sen University</h3><p>Guangzhou, China</p></div></div>
    <div class="timeline-item"><span class="timeline-date">2013 – 2017</span><div><h3>Xidian University</h3><p>Xi’an, China</p></div></div>
    <div class="timeline-item"><span class="timeline-date">Jul – Oct 2019</span><div><h3>Industry Internship · ByteDance</h3><p>Shanghai, China</p></div></div>
  </div>
</section>

<section id="teaching" class="secondary-section" aria-labelledby="teaching-title">
  <h2 id="teaching-title">Teaching</h2>
  <p><strong>Machine Learning for IoT</strong> — hands-on labs on gesture recognition and resource-constrained machine learning. <a href="{{ '/teaching/' | relative_url }}">Teaching &amp; course resources <span aria-hidden="true">→</span></a></p>
</section>

<section id="awards" class="secondary-section" aria-labelledby="awards-title">
  <h2 id="awards-title">Honors &amp; Awards</h2>
  <ul class="awards-list">
    <li><strong>1st place</strong> · Huawei Sweden Tech Arena <span>2025</span></li>
    <li><strong>3rd place</strong> · Huawei Sweden University Challenge <span>2023</span></li>
  </ul>
</section>
<footer class="homepage-footer">Shenghui Li · Uppsala University <a href="#about-me">Back to top ↑</a></footer>
</div>
