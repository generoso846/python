from flask import Flask


app = Flask(__name__) 
@app route("/")
def curriculo():
return

'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Currículo — João Lucas Generoso Bruno</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', sans-serif;
      background: #f0f2f5;
      color: #1a1a2e;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      padding: 40px 16px;
    }

    .page {
      width: 100%;
      max-width: 860px;
      background: #ffffff;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 8px 40px rgba(0,0,0,0.12);
    }

    /* ── HEADER ── */
    .header {
      background: linear-gradient(135deg, #0f2b5b 0%, #1a4a8a 60%, #1e6fc4 100%);
      padding: 44px 48px 36px;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 36px;
    }

    .avatar {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background: rgba(255,255,255,0.15);
      border: 3px solid rgba(255,255,255,0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.6rem;
      font-weight: 700;
      color: #ffffff;
      flex-shrink: 0;
      letter-spacing: 1px;
    }

    .header-info h1 {
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      line-height: 1.2;
    }

    .header-info .role {
      font-size: 1rem;
      font-weight: 400;
      color: rgba(255,255,255,0.8);
      margin-top: 6px;
      letter-spacing: 0.3px;
    }

    .contact-row {
      display: flex;
      flex-wrap: wrap;
      gap: 18px;
      margin-top: 18px;
    }

    .contact-item {
      display: flex;
      align-items: center;
      gap: 7px;
      font-size: 0.85rem;
      color: rgba(255,255,255,0.9);
    }

    .contact-item svg {
      width: 15px;
      height: 15px;
      fill: rgba(255,255,255,0.75);
      flex-shrink: 0;
    }

    /* ── BODY ── */
    .body {
      display: grid;
      grid-template-columns: 1fr 280px;
      gap: 0;
    }

    /* ── MAIN COLUMN ── */
    .main {
      padding: 36px 40px;
      border-right: 1px solid #e8ecf0;
    }

    /* ── SIDEBAR ── */
    .sidebar {
      padding: 36px 28px;
      background: #f7f9fc;
    }

    /* ── SECTION ── */
    .section {
      margin-bottom: 32px;
    }

    .section:last-child {
      margin-bottom: 0;
    }

    .section-title {
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: #1a4a8a;
      border-bottom: 2px solid #1a4a8a;
      padding-bottom: 6px;
      margin-bottom: 18px;
    }

    /* ── OBJETIVO ── */
    .objetivo p {
      font-size: 0.9rem;
      line-height: 1.75;
      color: #3a3a4a;
    }

    /* ── EXPERIÊNCIA ── */
    .exp-item {
      margin-bottom: 22px;
      position: relative;
      padding-left: 16px;
    }

    .exp-item::before {
      content: '';
      position: absolute;
      left: 0;
      top: 6px;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #1a4a8a;
    }

    .exp-item:not(:last-child)::after {
      content: '';
      position: absolute;
      left: 3px;
      top: 14px;
      width: 1px;
      bottom: -16px;
      background: #cdd5e0;
    }

    .exp-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 8px;
      flex-wrap: wrap;
    }

    .exp-company {
      font-size: 0.95rem;
      font-weight: 700;
      color: #0f2b5b;
    }

    .exp-period {
      font-size: 0.75rem;
      font-weight: 500;
      color: #ffffff;
      background: #1a4a8a;
      padding: 2px 9px;
      border-radius: 20px;
      white-space: nowrap;
    }

    .exp-role {
      font-size: 0.82rem;
      color: #1e6fc4;
      font-weight: 600;
      margin-top: 3px;
    }

    .exp-desc {
      font-size: 0.84rem;
      color: #4a4a5a;
      line-height: 1.65;
      margin-top: 7px;
    }

    .exp-desc ul {
      padding-left: 16px;
      margin-top: 4px;
    }

    .exp-desc ul li {
      margin-bottom: 3px;
    }

    /* ── SIDEBAR SECTIONS ── */
    .skill-block {
      margin-bottom: 24px;
    }

    .skill-block:last-child {
      margin-bottom: 0;
    }

    /* ── LANGUAGE BAR ── */
    .lang-item {
      margin-bottom: 14px;
    }

    .lang-label {
      display: flex;
      justify-content: space-between;
      font-size: 0.83rem;
      font-weight: 600;
      color: #1a1a2e;
      margin-bottom: 5px;
    }

    .lang-level {
      font-weight: 400;
      color: #6b7280;
      font-size: 0.78rem;
    }

    .bar-track {
      height: 6px;
      background: #dde3ec;
      border-radius: 99px;
      overflow: hidden;
    }

    .bar-fill {
      height: 100%;
      border-radius: 99px;
      background: linear-gradient(90deg, #1a4a8a, #1e6fc4);
    }

    /* ── TECH TAGS ── */
    .tag-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .tag {
      font-size: 0.76rem;
      font-weight: 500;
      background: #e8eef7;
      color: #0f2b5b;
      padding: 4px 11px;
      border-radius: 20px;
      border: 1px solid #c6d4e8;
    }

    /* ── EDUCATION ── */
    .edu-item {
      margin-bottom: 16px;
    }

    .edu-course {
      font-size: 0.88rem;
      font-weight: 700;
      color: #0f2b5b;
    }

    .edu-school {
      font-size: 0.82rem;
      color: #1e6fc4;
      font-weight: 500;
      margin-top: 2px;
    }

    .edu-detail {
      font-size: 0.78rem;
      color: #6b7280;
      margin-top: 2px;
    }

    /* ── COMPETÊNCIAS ── */
    .comp-item {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      margin-bottom: 10px;
      font-size: 0.83rem;
      color: #3a3a4a;
      line-height: 1.5;
    }

    .comp-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #1a4a8a;
      margin-top: 5px;
      flex-shrink: 0;
    }

    /* ── PRINT ── */
    @media print {
      body { background: #fff; padding: 0; }
      .page { box-shadow: none; border-radius: 0; }
    }

    @media (max-width: 640px) {
      .body { grid-template-columns: 1fr; }
      .main { border-right: none; border-bottom: 1px solid #e8ecf0; }
      .header { flex-direction: column; align-items: flex-start; gap: 16px; padding: 28px 24px; }
      .main { padding: 24px; }
      .sidebar { padding: 24px; }
    }
  </style>
</head>
<body>
  <div class="page">

    <!-- HEADER -->
    <header class="header">
      <div class="avatar">JL</div>
      <div class="header-info">
        <h1>João Lucas Generoso Bruno</h1>
        <p class="role">Técnico em TI &amp; Segurança Eletrônica | Programador em Formação</p>
        <div class="contact-row">
          <span class="contact-item">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24 11.47 11.47 0 003.58.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.47 11.47 0 00.57 3.58 1 1 0 01-.24 1.01l-2.21 2.2z"/></svg>
            +55 (31) 99911-2008
          </span>
          <span class="contact-item">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
            joaojl2077@gmail.com
          </span>
          <span class="contact-item">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5A2.5 2.5 0 1112 6a2.5 2.5 0 010 5.5z"/></svg>
            Vila da Serra, Nova Lima — MG
          </span>
        </div>
      </div>
    </header>

    <!-- BODY -->
    <div class="body">

      <!-- MAIN -->
      <main class="main">

        <!-- OBJETIVO -->
        <section class="section objetivo">
          <h2 class="section-title">Objetivo Profissional</h2>
          <p>
            Busco uma oportunidade na área de <strong>Técnico em TI e/ou Programação</strong>, onde possa aplicar minha experiência prática em segurança eletrônica, infraestrutura de redes e suporte técnico, aliada à minha formação em andamento no curso de TI. Tenho perfil proativo, facilidade de aprendizado e sólida vivência em projetos de instalação e configuração de sistemas de segurança de alta complexidade.
          </p>
        </section>

        <!-- EXPERIÊNCIA -->
        <section class="section">
          <h2 class="section-title">Experiência Profissional</h2>

          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-company">Orbis Tecnologia de Segurança</span>
              <span class="exp-period">Atual</span>
            </div>
            <p class="exp-role">Técnico em Segurança Eletrônica</p>
            <div class="exp-desc">
              <ul>
                <li>Instalação e configuração de sistemas de CFTV com e sem inteligência artificial.</li>
                <li>Mapeamento de câmeras e integração com gravadores (DVR/NVR).</li>
                <li>Operação avançada do sistema <strong>iVMS-4200</strong> para monitoramento remoto.</li>
                <li>Passagem e organização de cabeamento estruturado em edificações residenciais e comerciais.</li>
                <li>Montagem completa de condomínios: câmeras, cancelas, leitores faciais e motores de portão.</li>
                <li>Configuração de câmeras com recursos de IA (reconhecimento facial, detecção de intrusão, análise de comportamento).</li>
              </ul>
            </div>
          </div>

          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-company">Sólides</span>
              <span class="exp-period">Anterior</span>
            </div>
            <p class="exp-role">Colaborador — Setor de Vendas / Suporte</p>
            <div class="exp-desc">
              <ul>
                <li>Atuação no setor de vendas com foco em atendimento consultivo ao cliente.</li>
                <li>Desenvolvimento de habilidades de comunicação, negociação e relacionamento com o público.</li>
                <li>Experiência com processos internos e ferramentas de gestão corporativa.</li>
              </ul>
            </div>
          </div>

        </section>

        <!-- PROJETOS / REALIZAÇÕES -->
        <section class="section">
          <h2 class="section-title">Projetos &amp; Realizações</h2>

          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-company">Montagem de Prédios Residenciais</span>
            </div>
            <div class="exp-desc">
              <p>Responsável pela montagem completa de sistemas de segurança em diversos empreendimentos residenciais, incluindo planejamento, instalação e comissionamento de câmeras de segurança, cancelas automatizadas, leitores faciais de acesso e motores para portões — garantindo integração total entre os sistemas.</p>
            </div>
          </div>

          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-company">Configuração de CFTV com Inteligência Artificial</span>
            </div>
            <div class="exp-desc">
              <p>Configuração e parametrização de câmeras IP com recursos de IA embarcada, incluindo detecção de faces, análise de comportamento e alertas inteligentes, com integração ao sistema iVMS-4200.</p>
            </div>
          </div>

        </section>

      </main>

      <!-- SIDEBAR -->
      <aside class="sidebar">

        <!-- FORMAÇÃO -->
        <section class="section">
          <h2 class="section-title">Formação</h2>
          <div class="edu-item">
            <p class="edu-course">Ensino Médio — Curso Técnico em TI</p>
            <p class="edu-school">COTEMIG</p>
            <p class="edu-detail">3º ano — Turma 3C1 | Em andamento</p>
          </div>
        </section>

        <!-- IDIOMAS -->
        <section class="section">
          <h2 class="section-title">Idiomas</h2>

          <div class="lang-item">
            <div class="lang-label">
              <span>Português</span>
              <span class="lang-level">Nativo</span>
            </div>
            <div class="bar-track"><div class="bar-fill" style="width:100%"></div></div>
          </div>

          <div class="lang-item">
            <div class="lang-label">
              <span>Inglês</span>
              <span class="lang-level">Avançado</span>
            </div>
            <div class="bar-track"><div class="bar-fill" style="width:85%"></div></div>
          </div>

          <div class="lang-item">
            <div class="lang-label">
              <span>Espanhol</span>
              <span class="lang-level">Intermediário</span>
            </div>
            <div class="bar-track"><div class="bar-fill" style="width:55%"></div></div>
          </div>
        </section>

        <!-- HABILIDADES TÉCNICAS -->
        <section class="section">
          <h2 class="section-title">Habilidades Técnicas</h2>
          <div class="tag-grid">
            <span class="tag">iVMS-4200</span>
            <span class="tag">CFTV / IP Cameras</span>
            <span class="tag">DVR / NVR</span>
            <span class="tag">Câmeras com IA</span>
            <span class="tag">Leitor Facial</span>
            <span class="tag">Cancelas</span>
            <span class="tag">Motores de Portão</span>
            <span class="tag">Cabeamento Estruturado</span>
            <span class="tag">Hardware Avançado</span>
            <span class="tag">Redes TCP/IP</span>
            <span class="tag">Suporte Técnico</span>
            <span class="tag">Windows / Linux</span>
          </div>
        </section>

        <!-- COMPETÊNCIAS -->
        <section class="section">
          <h2 class="section-title">Competências</h2>
          <div class="comp-item"><div class="comp-dot"></div><span>Raciocínio lógico e resolução de problemas</span></div>
          <div class="comp-item"><div class="comp-dot"></div><span>Trabalho em equipe e comunicação eficaz</span></div>
          <div class="comp-item"><div class="comp-dot"></div><span>Orientação a resultados e proatividade</span></div>
          <div class="comp-item"><div class="comp-dot"></div><span>Aprendizado rápido de novas tecnologias</span></div>
          <div class="comp-item"><div class="comp-dot"></div><span>Experiência sólida em atendimento ao cliente</span></div>
          <div class="comp-item"><div class="comp-dot"></div><span>Organização e atenção aos detalhes</span></div>
        </section>

      </aside>
    </div><!-- /body -->

  </div><!-- /page -->
</body>
</html>
'''
